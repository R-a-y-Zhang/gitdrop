from simplecrypt import encrypt,decrypt as crypt
import simplecrypt
import hashlib
import sys
import os
import shutil

#
listOfFiles = []
def main(args):



def encrypt_f(args,password):
    password = password
    rey = hashlib.sha256(password).digest()
    for i in range (10000):
        rey = hashlib.sha256(rey).hexdigest()
    with open(args[0], 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(rey, plaintext)
    with open(args[0], 'wb') as fo:
        fo.write(enc)
        fo.close()
def decrypt_f(args,password):
    password =  password
    cyper = open(args[0],'rb').read()
    rey = hashlib.sha256(password).digest()
    for i in range (10000):
        rey = hashlib.sha256(rey).hexdigest()
    l = simplecrypt.decrypt(rey,cyper)
    x = open(args[0],'wb')
    x.write(l)
#encrypt_f(sys.argv[1:])
#decrypt_f(sys.argv[1:])

def help():
    print("Usage encrypt('key',filename)")
    print("if its a directory u can encrypt all all files within those direcories with -r arg, or s specfic directory with -r [directories]")
def recursiveHelper(args):
    if os.path.isdir(args[0]):
        for root,dirs,files in os.walk(args[0]):
            for file in files:
                filepath = os.path.join(root,file)
                listOfFiles.append(filepath)
        print(listOfFiles)
        return listOfFiles
recursiveHelper("../cmds")
