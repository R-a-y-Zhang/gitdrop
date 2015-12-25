import os, random, struct
from Crypto.Cipher import AES
from hashlib import sha256 as sha256

def encrypt_file(key, input_, output_=None, chunksize=64*2048):
	if not output_:
		output_ = input_ + '.enc'
	
	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	encrypt = AES.new(key, AES.MODE_CBC, iv)
	filesize = os.path.getsize(input_)

	with open(input_, 'rb') as in_f:
		with open(output_, 'wb') as out_f:
			out_f.write(struct.pack('<Q', filesize))
			out_f.write(iv)

			while True:
				chunk = in_f.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - len(chunk) % 16)

				out_f.write(encrypt.encrypt(chunk))

def decrypt_file(key, input_, output_=None, chunksize=64*2048):
	if not output_:
		output_ = os.path.splitext(input_)[0]

	with open(input_, 'rb') as in_f:
		orig_size = struct.unpack('<Q', in_f.read(struct.calcsize('Q')))[0]
		iv = in_f.read(16)
		decrypt = AES.new(key, AES.MODE_CBC, iv)

		with open(output_, 'wb') as out_f:
			while True:
				chunk = in_f.read(chunksize)
				if len(chunk) == 0:
					break
				out_f.write(decrypt.decrypt(chunk))

			out_f.truncate(orig_size)

def enc_pass(pswd, sha=None, cnt=1000):
	if cnt == 0:
		return pswd
	if not sha:
		sha = sha256()
	pswd = pswd.encode('utf-8')
	pswd = sha.update(pswd).hexdigest()
	return enc_pass(pswd, sha, cnt - 1)
