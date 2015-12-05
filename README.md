# gitdrop
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
