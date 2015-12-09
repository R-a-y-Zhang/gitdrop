from cmds import gd_config, gd_list, gd_move, gd_copy, gd_mkdir, gd_track, \
                    gd_push, gd_fetch, gd_share, gd_delete, gd_pull
import sys

if (len(sys.argv) == 1):
    sys.argv.append('help')
direct = sys.argv[1]
if direct == 'config':
    gd_config.config(sys.argv[2:])

elif direct == 'list':
    gd_list.list(sys.argv[2:])

elif direct == 'move':
    gd_move.move(sys.argv[2:])

elif direct == 'copy':
    gd_copy.copy(sys.argv[2:])

elif direct == 'mkdir':
    gd_mkdir.mkdir(sys.argv[2:])

elif direct == 'track':
    gd_track.track(sys.argv[2:])

elif direct == 'status':
    gd_track.status(sys.argv[2:])

elif direct == 'load':
    gd_track.load(sys.argv[2:])

elif direct == 'push':
    gd_push.push(sys.argv[2:])

elif direct == 'fetch':
    gd_fetch.fetch(sys.argv[2:])

elif direct == 'share':
    gd_share.share(sys.argv[2:])

elif direct == 'del' or direct == 'delete':
    gd_delete.delete(sys.argv[2:])
elif direct=="pull":
    gd_pull.pull(sys.argv[2:])

elif direct == 'help':
    print("""
    If this is your first time, please use the command 'python gitdrop.py config --nkey'
    [] - required
    () - optional
    config [option] [value] - configures gitdrop
        --key : configures user access key. This is required in order for gitdrop
            to access dropbox files
        --home : sets home directory, or where gitdrop will download files to with
            'fetch'. Can be overriden in 'fetch'

    list (options) [path] - lists files in a given destination
        --verbose : lists last modified, file size, and if it is a directory in
            addition to the file name
        --v : same as '-verbose'
        --tree (r) : lists the files in a tree. If 'r' is blank, gitdrop will step
            through every folder. If 'r' is specified, gitdrop will step through
            and stop at the level specified

    move (options) --src [src] --dst [dst] - moves files/folders from 'src' on dropbox to 'dst' on dropbox
        nofolder : move only files
        nofile : move only folders
        --src : folders and files from this directory and move it to directories under '--dst'
                    if moving from multiple sources to multiple directories (folder 'a' to folder 'c'
                    and folder 'b' to folder 'd') place src and dst in order (i.e. 'move --src a b --dst c d')
                    if moving from multiple sources to one directory (folders 'a' 'b' and 'c' to 'd')
                    just write the dst once (i.e. 'move --src a b c --dst d')

    copy (options) [src] [dst] - copies files/folders from 'src' on dropbox to 'dst' on dropbox
        --nofolder : copy only files
        --nofile : copy only folders

    track (options) [paths] - tracks folders or files specified
        --u : untracks the folders or files specified

    status (option) - displays status of tracked files
        --loaded : displays status of loaded files only

    load [paths] - loads files to be ready for push.


    status - shows any changes to folders and files that have been tracked. This
        includes additions, deletions, and modifications

    push (option) (dst) - uploads loaded files to dropbox. If 'dst' is unspecified then will upload to
            root folder ('/').
        --force : upload all tracked files, regardless if loaded
        --f : see '--force'

    fetch (options) (--url) [path] (--dst) - downloads the specified files to location dst. If dst
            not specified, will download automatically to 'home' specified in
            the configuration
        --url [urls] (options): downloads files from specified urls to both dropbox and local filesystem
        --nolocal : download only to dropbox and not locally
        --all : download all of contents from dropbox
        --nodrop : download only to local filesystem and not to dropbox
        --dst : specifies the destination of the files

    share [paths] - gets a shareable url for the files specified

    del [path] - deletes files on dropbox within the specified path
    """)

else:
    print("Does not recognize command: %s" % (direct))
    print("Does not recognize command, type 'help' for list of commands")
