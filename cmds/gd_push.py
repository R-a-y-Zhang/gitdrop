import dropbox, os
from . import gd_utilities as gd_util
access_key = gd_util.get_key('user_key')
if access_key == None:
    print("User access key was not found, make sure it is properly configured")
client = dropbox.client.DropboxClient(access_key)
#basic outline
#iterate thrrough the loaded doirectory
#upload = os.listdir("/loaded")
upload = os.listdir(os.path.dirname(os.path.abspath(__file__)))
for file in upload:
    f = open(file)
    rep = client.put_file(j)
    f.close()
