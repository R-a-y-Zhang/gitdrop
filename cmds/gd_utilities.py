def get_key(query):
    try:
        config_file = open("user_options.config", "r")
        lines = config_file.readlines()
        config_file.close()
        for line in lines:
            line = line.split(":")
            if line[0] == query:
                return line[1].strip()
        return None
    except:
        return None
