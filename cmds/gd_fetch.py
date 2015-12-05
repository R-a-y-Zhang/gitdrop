import dropbox as dbx
from . import gd_utilities as gd_utils
import os, json, re, sys

def get_home():
    return gd_utils.get_key("home")

def get_access_key():
    return gd_utils.get_key("user_key")

def fetch(cmds):
    access_key = get_access_key()
    client = dbx.client.DropboxClient(access_key)
    isUrl, nolocal, nodrop, dst, inside = \
            False, False, False, get_home(), False
    dls_list = []

    # command parsing

    for i in xrange(len(cmds)):
        if cmds[i] == '--url':
            isUrl = True
        elif cmds[i] == '--dst':
            dst = cmds[-1]
        elif cmds[i] == '--nolocal':
            nolocal = True
        elif cmds[i] == '--nodrop':
            nodrop = True
        elif cmds[i] == '--all':
            all_contents = True
        elif cmds[i] == '--inside':
            inside = True
        else:
            if cmds[i-1] != '--dst':
                cmds[i] = cmds[i].replace('\'', '')
                dls_list.append(cmds[i])

    if nodrop == True and nolocal == True:
        nodrop, nolocal = False, True
    if isUrl == False:

        # works through the list of files given

        for dl in dls_list:
            dl = dl.strip() # strips off whitespace bc that'll fuck things up
            if dl[-1] == '/':
                dl = dl[:-1]
            isdir, directory, pattern = False, '/', ''
            if '/' in dl:
                isdir = True
                path = dl.split('/')
                pattern = path[-1]
                if len(path) > 1:
                    directory = path[:-2].join('/') # rejoins the directory
            else:
                pattern = dl

            try:
                folder_meta = client.metadata(directory)
                folder_json = json.loads(json.dumps(folder_meta['contents']))
                pattern = re.compile(pattern) # regex time
                for item in folder_json:
                    name = item['path'].replace(directory, '')
                    name = name.replace('/', '')
                    if pattern.match(name) != None:
                        if item['is_dir'] == True:
                            download_folder_contents(client, dl, dst)
                        if item['is_dir'] == False:
                            filename = item['path'].split('/')[-1] # gets filename
                            # not using os.path.join bc it messes up some things with unicode
                            output = open(dst + os.path.sep + filename, 'wb')
                            with client.get_file(item['path']) as f:
                                output.write(f.read())
                                f.close()
                            output.close()
                        if nodrop == True:
                            client.file_delete(item['path']) # if file can be deleted
            except:
                if input('Something went wrong, print error (y/n): ') == 'y':
                    raise


def download_folder_contents(client, folder, dst):
    folder_path = dst + os.path.sep + folder
    if os.path.isdir(folder_path) == False:
        os.mkdir(folder_path)
    folder_meta = client.metadata(folder)
    folder_json = json.loads(json.dumps(folder_meta['contents']))
    for item in folder_json:
        if item['is_dir'] == True:
            download_folder_contents(client, item['path'], folder_path)
        elif item['is_dir'] == False:
            filename = item['path'].split('/')[-1]
            output = open(folder_path + os.path.sep + filename, 'wb+')
            with client.get_file(item['path']) as f:
                output.write(f.read())
                f.close()
            output.close()
