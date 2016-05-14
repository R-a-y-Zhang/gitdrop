import dropbox as dbx

def copy(src,dst):
	dbx.copy_files(src,dst)
