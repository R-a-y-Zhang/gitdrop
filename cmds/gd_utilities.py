def get_key(query):
    try:
        config_file = open("user_config.conf", "r")
        lines = config_file.readlines()
        config_file.close()
        for line in lines:
            line = line.split(":")
            if line[0] == query:
                return line[1].strip()
        return None
    except:
        return None

def write_key(key, value):
    try:
        config_file = open("user_config.conf", "r")
        lines = config_file.readlines()
        config_file.close()
        keys = [line.split(": ")[0] for line in lines]
        if key in keys:
            config_file[keys.index(key)] = "{}: {}".format(key, value)
        else:
            lines.append("{}: {}".format(key, value))

        config_file = open("user_config.conf", "w")
        for l in lines:
            config_file.write(l)
        config_file.close()
    except:
        return None

def get_conf():
    try:
        config_file = open("user_config.conf", "r")
        lines = config_file.readlines()
        config_file.close()
        return lines
    except:
        return None
