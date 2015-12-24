from simplecrypt import encrypt,decrypt as crypt
import simplecrypt
import hashlib
import sys
import os
#
pass = ""
def encrypt_f(args):

    password = args[0]

    rey = hashlib.sha256(password).digest()
    for i in range (10000):

        rey = hashlib.sha256(rey).hexdigest()
    with open(args[1], 'rb') as fo:
        plaintext = fo.read()

    enc = encrypt(rey, plaintext)
    with open(args[1], 'wb') as fo:
        fo.write(enc)
        fo.close()
def decrypt_f(args):
    password = args[0]
    cyper = open(args[1],'rb').read()
    rey = hashlib.sha256(password).digest()
    for i in range (10000):
        rey = hashlib.sha256(rey).hexdigest()
    l = simplecrypt.decrypt(rey,cyper)
    x = open(args[1],'wb')
    x.write(l)
#encrypt_f(sys.argv[1:])
decrypt_f(sys.argv[1:])




def getPass():
    if pass == "":
        print("Please Set A password")
    else:
        return pass

def help():
    print("Usage encrypt('key',filename)")
    print("if its a directory u can encrypt all all files within those direcories with -r arg, or s specfic directory with -r [directories]")

def recursiveHelper(args):
    if os.isdir(args[0]):
        for file os.walk(args[0]):
            if os.isdir(file):
                return os.walk(file) + recursiveHelper(file)
            else:
                return file
