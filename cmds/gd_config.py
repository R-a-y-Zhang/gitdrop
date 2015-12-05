import dropbox as dbx

def config(cmds):
    config_file = open("user_options.config", "r")
    if cmds[0] == '--key':
        write_key(config_file, 'user_key', cmds)

    if cmds[0] == '--home':
        write_key(config_file, 'home', cmds)

    if cmds[0] == '--get-config':
        print(config_file.read())

    if cmds[0] == '--nkey':
        lines = list(config_file)
        api_key, api_secret = None, None
        for line in lines:
            if line.split(': ')[0] == 'api_key':
                api_key = line.split(': ')[1]
            if line.split(': ')[1] == 'api_secret':
                api_secret = line.split(': ')[1]
        auth_flow = dbx.DropboxOAuth2FlowNoRedirect(api_key, api_secret)

        authorize_url = auth_flow.start()
        print("1. Go to: " + authorize_url)
        print ("2. Click \"Allow\" (you might have to log in first).")
        print ("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ").strip()

        try:
            access_token, user_id = auth_flow.finish(auth_code)
        except:
            raise

        cmds.append(access_token)
        write_key(config_file, 'user_key', cmds)

    config_file.close()

def write_key(file, key, cmds):
    value = cmds[1]
    replaced = False;
    lines = list(file)
    for i in range(len(lines)):
        if key in lines[i]:
            lines[i] = '{}: {}\n'.format(key, value)
            replaced = True
    if replaced == False:
        lines.append('{}: {}\n'.format(key, value))
    file.close()
    file = open("user_options.config", 'w')
    for line in lines:
        file.write(line)
