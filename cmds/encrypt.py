from simplecrypt import encrypt,decrypt as crypt
import simplecrypt
import hashlib
import sys
#
pass = ""
def encrypt_f(args,password):
    password = 'mynameisckrillexandahow'

    rey = hashlib.sha256(password).digest()
    for i in range (10000):

        rey = hashlib.sha256(rey).hexdigest()
    with open(args[1], 'rb') as fo:
        plaintext = fo.read()

    enc = encrypt(rey, plaintext)
    with open(args[1], 'wb') as fo:
        fo.write(enc)
        fo.close()
def decrypt_f(args,password):
    cyper = open(args[1],'rb').read()
    rey = hashlib.sha256(password).digest()
    for i in range (10000):
        rey = hashlib.sha256(rey).hexdigest()
    l = simplecrypt.decrypt(rey,cyper)
    x = open(args[1],'wb')
    x.write(l)
#encrypt_f(sys.argv)
decrypt_f(sys.argv,'mynameisckrillexandahow')


def set_pass(args):
    pass = args[1]

    

def getPass():
    if pass == "":
        print("Please Set A password")
    else:
        return pass
