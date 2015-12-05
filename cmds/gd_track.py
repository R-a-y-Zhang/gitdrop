import os, datetime, sys, shutil

def track(args):
    untrack = False
    if args[0] == '--u':
        untrack = True
    tracker_file = open('tracked_files.txt', 'r')
    status = tracker_file.readlines()
    tracker_file.close()
    files_tracked, modifications = [line.split(": ")[0] for line in status], \
                                    [line.split(": ")[1] for line in status]

    fs_list = args[1:]
    for f in fs_list:
        abs_path = check_in_dir(f)

        if os.path.exists(abs_path) == False: # if file does not exist
            print("File: %s not found" % (abs_path))
            continue

        mod_date = datetime.datetime.fromtimestamp(os.stat(abs_path).st_mtime)
        time_str = "{}-{}-{} {}:{}:{}".format(mod_date.day, \
            mod_date.month, mod_date.year, mod_date.hour, mod_date.minute, mod_date.second)

        if abs_path not in files_tracked: # if not already tracked, track it
            status.append("{}: {}".format(abs_path, time_str))
        if abs_path in files_tracked: # if is tracked, update time
            target = "{}: {}".format(abs_path, time_str)
            status[files_tracked.index(abs_path)] = target

    tracker_file = open('tracked_files.txt', 'w')
    for s in status:
        tracker_file.write("%s\n" % (s))

    tracker_file.close()

def status(args):
    if args[0] == '--loaded':
        pass

    else:
        fs_list = args
        tracker_file = open('tracked_files.txt', 'r')
        status = tracker_file.readlines()
        tracker_file.close()
        files_tracked, mod_times = [line.split(": ")[0] for line in status], \
                                    [line.split(": ")[0] for line in status]
        for f in fs_list:
            abs_path = check_in_dir(f)

            if os.path.exists(abs_path) == False:
                print("File: %s not found" % (abs_path))
                continue

            if abs_path not in files_tracked:
                print("File: %s not tracked" % (abs_path))

            elif abs_path in files_tracked:
                ltm = datetime.datetime.fromtimestamp(os.stat(abs_path).st_mtime)
                formatted_time = "{}-{}-{} {}:{}:{}".format(ltm.day, ltm.month,\
                ltm.year, ltm.hour, ltm.minute, ltm.second)
                if ltm == mod_times[files_tracked.index(abs_path)]:
                    print("File %s: No change since last loaded" % (abs_path))

                if ltm == modtimes[files_tracked.index(abs_path)]:
                    print("File %s: Changed since last loaded" % (abs_path))
        output = open('tracked_files.txt', 'w')
        for s in status:
            output.write('%s\n', (s))

        output.close()

def load(args):
    tracker_file = open('tracked_files.txt', 'r')
    status = tracker_file.readlines()
    tracker_file.close()
    files_tracked, modifications = [line.split(": ")[0] for line in status], \
                                    [line.split(": ")[1] for line in status]
    if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded')) == False:
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded'))

    for f in args:
        abs_path = check_in_dir(f)
        if os.path.exists(abs_path) == False:
            print("File: %s not found" % (abs_path))
            continue

        src = abs_path
        dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loaded')
        shutil.copy(src, dst)
        if src not in files_tracked:
            ltm = datetime.datetime.fromtimestamp(os.stat(abs_path).st_mtime)
            formatted_time = "{}-{}-{} {}:{}:{}".format(ltm.day, ltm.month, \
                ltm.year, ltm.hour, ltm.minute, ltm.second)
            status.append("{}: {}".format(src, formatted_time))
        if src in files_tracked:
            status[files_tracked.index(src)] = "{}: {}".format(src, formatted_time)

def check_in_dir(f):
    if os.path.exists(os.path.join(os.get(cwd(), f))) == True:
        return os.path.join(os.getcwd(), f)
    return f
