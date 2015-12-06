import dropbox
import os
key = open("user_key","r")
data = key.read()
client = dropbox.client.DropboxClient(data)
#basic outline
#iterate thrrough the loaded doirectory
upload = os.listdir("/loaded")
for file in upload:
    j = open(file)
    rep = client.put_file(j)
