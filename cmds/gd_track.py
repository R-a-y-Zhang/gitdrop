import os, sys, shutil, path
from . import gd_utilities a gd_utils
	
def rewrite_file(data):
	log_file = gd_utils.get_key('files_log')
	with open(log_file, 'w') as f:
		for d in data:
			f.write(d)

def track_file(filepath):
	log_file = gd_utils.get_key('files_log')
	with open(log_file, 'a') as f:
		time_mod = os.path.getmtime(filepath)	
		size_mod = os.path.getsize(filepath)
		path_mod = os.path.abspath(filepath)
		f.write('{}-{}-{}-{}-{}\n'.format(path_mod, time_mod, time_mod, size_mod, size_mod))

def untrack_files(files_list):
	log_file = gd_utils.get_key('files_log')
	files = []
	with open(log_file) as f:
		files = f.readlines()
	
	updated_list = []
	for file in files:
		if file.split(' ')[0] not in files:
			updated_list.append(file)
	
	rewrite_file(updated_list)

def update_times():
	log_file = gd_utils.get_key('files_log')
	files = []
	with open(log_file) as f:
		files = f.readlines()
	
	for i in range(len(files)):
		f_data = f.split('-')
		time_mod = os.path.getmtime(files[i])
		size_mod = os.path.getsize(files[i])
		files[i] = '{}-{}-{}-{}-{}\n'.format(f_data[0], f_data[1], time_mod, f_data[3], size_mod)
	
	rewrite_file(files)

def update_push_times():
	log_file = gd_utils.get_key('files_log')
	files = []
	with open(log_file) as f:
		files = f.readlines()

	for i in range(len(files)):
		f_data = files[i]
		time_mod = os.path.getmtime(f_data[0])
		size_mod = os.path.getsize(f_data[0])
		files[i] = '{}-{}-{}-{}-{}\n'.format(f_data[0], time_mod, time_mod, size_mod, size_mod)
		
	rewrite_file(files)

def get_status():
	log_file = gd_utils.get_key('files_log')
	files = []
	with open(log_file) as f:
		files = f.readlines()
	
	out_lens = [0, 0, 0, 0, 0]
	fnames = []
	f_push_times = []
	f_update_times = []
	f_push_size = []
	f_update_size = []
	with file in files:
		f_data = file.split('-')
		fnames.append(f_data[0])
		f_push_times(time.ctime(f_data[1]))
		f_update_times(time.ctime(f_data[2]))
		f_push_size(f_data[3])
		f_update_size(f_data[4])
		for i in range(len(f_data)):
			if (len(f_data[i]) > out_lens[i]):
				out_lens[i] = len(f_data[i])

	str_output = '{0:%d}   {1:%d}   {2:%d}   {3:%d}   {4:%d}\n' % (out_lens[0], out_lens[1], out_lens[2], out_lens[3], out_lens[4])
	
	for i in range(len(fnames)):
		str_output.format(fnames[i], f_push_times[i], f_update_times[i], f_push_size[i], f_update_size[i])

