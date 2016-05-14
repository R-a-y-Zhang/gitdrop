import dropbox as dbx

def mkdir(dst):
	dbx.files_create_folder(dst)
