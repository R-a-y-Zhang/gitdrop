import dropbox
from . import gd_utilities as gd_utils
access_key = gd_utils.get_key('user_key')

if access_key == None:
    print("User access key was not found, make sure it is properly configured")


def pull(args):
    client = dropbox.client.DropboxClient(access_key)
    if len(args)==0:
        #downloads everything
        print("downoading all files that are tracked")
        tracked_file = open("tracked_files.txt","r")

        for file in tracked_file.readlines():

            files_download_beforePaarseSecond = file.split(':')
            x = files_download_beforePaarseSecond[0]

            y = x.split("/")
            download_file = "/"+ y[len(y)-1]
            output_file = y[len(y)-1]
            print (download_file)
            with client.get_file(download_file) as fi:
                j = open(output_file,"a")
                j = open(output_file,"wb")
                j.write(fi.read())
                j.close()
