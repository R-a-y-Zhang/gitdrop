import dropbox, os, sys
from . import gd_utilities as gd_utils
def push(cmds):
    access_key = gd_utils.get_key('user_key')
    if access_key == None:
        print("User access key was not found, make sure it is properly configured")
        sys.exit(0)
    if os.path.exists('tracked_files.txt') == False:
        open('.tracked_files.txt', 'w').close()
    client = dropbox.client.DropboxClient(access_key)
    #basic outline
    #iterate thrrough the loaded doirectory
    #upload = os.listdir("/loaded")
    ld_folder, dst = None, None
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded')) == False:
        ld_folder = os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded'))
    else:
        ld_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded')

    upload = os.listdir(ld_folder)
    if len(upload) == 0:
        print("Nothing to upload")
        sys.exit('/')

    if len(cmds) == 0:
        dst = '/'
        print("No destination specified, defaulting to root \'/\'")
    else:
        dst = cmds[0]

    for file in upload:
        f = open(os.path.join(ld_folder, file),"rb")
        rep = client.put_file(dst + file, f)
        print (rep)
        #os.remove(file)
        f.close()
