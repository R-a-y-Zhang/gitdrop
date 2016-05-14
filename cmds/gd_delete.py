import dropbox as dbx

def delete(src):
	dbx.files_permanently_delete(src)
