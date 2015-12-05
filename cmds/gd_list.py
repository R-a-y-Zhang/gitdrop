import sys, codecs
import dropbox as dbx
import json
from . import gd_utilities as gd_utils

def list(cmds):
    access_key = gd_utils.get_key("user_key")
    if len(cmds) < 1:
        print("Argument list insufficient")
        sys.exit(0)

    # command parsing

    paths_start = 0
    verbose = False
    tree, depth = False, -1
    if cmds[0] == '--verbose' or cmds[0] == '--v':
        paths_start += 1
        verbose = True

    if cmds[0] == '--tree':
        tree = True
        paths_start += 1
        try:
            depth = int(cmds[1])
            paths_start += 1
        except:
            pass

    # where it all begins
    folder_paths = cmds[paths_start:]
    if access_key == None:
        print("Unable to fetch access key or there is no configuration file")
        print("Please reconfigure your options")

    else:
        if folder_paths[0] == '--a' or folder_paths[0] == '--all':
            folder_paths = ['/'] # default folder path '/'
        client = dbx.client.DropboxClient(access_key)
        meta = None
        for folder_path in folder_paths:
            print()
            try:
                meta = client.metadata(folder_path) # pulls metadata on the folder
            except:
                print("Cannot find directory \"%s\"" % (folder_path))
            if meta != None:
                files_json = json.dumps(meta['contents'], indent=4)
                files_json = json.loads(files_json)
                print("Folder: %s" % (folder_path))
                if verbose == False and tree == False: # non-verbose printing
                    for file_json in files_json:
                        print(file_json["path"].replace(folder_path, '', 1))
                if verbose == True: # verbose printing
                    print("%-35s %-10s %-10s %-50s" % ("last modified", "file size", "read only", "filename"))
                    for file_json in files_json:
                        print("%-35s %-10s %-10s %-50s" % \
                        (file_json["modified"], file_json["size"], file_json["read_only"], file_json["path"].replace(folder_path, '', 1)))
                elif tree == True:
                    outputFile(client, folder_path, 0, depth)

# oh-mighty tree-printing

def outputFile(client, filepath, indentation, depth):
    if depth == 0:
        pass

    else:
        if depth <= -1:
            depth = -1
        meta = client.metadata(filepath)
        files_json = json.dumps(meta['contents'], indent=4)
        files_json = json.loads(files_json)
        for file_json in files_json:
            if file_json['is_dir'] == True:
                foldername = file_json['path'].replace(filepath, '')
                print('\t' * indentation, foldername.replace('/', ''))
                outputFile(client, file_json['path'], indentation + 1, depth - 1)

            elif file_json['is_dir'] == False:
                filename = file_json['path'].replace(filepath, '')
                print('\t' * indentation, filename.replace('/', ''))
        print()
