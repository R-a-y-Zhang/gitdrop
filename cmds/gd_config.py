import dropbox as dbx
from . import gd_utilities as gd_utils
def config(cmds):
    if cmds[0] == '--key':
        gd_utils.write_key(config_file, 'user_key', cmds)

    if cmds[0] == '--home':
        gd_utils.write_key(config_file, 'home', cmds)

    if cmds[0] == '--get-config':
        print(gd_utils.get_conf())

    if cmds[0] == '--nkey':
        api_key, api_secret = gd_utils.get_key('api_key'), gd_utils.get_key('api_secret')
        print(api_key + " " + api_secret)

        auth_flow = dbx.DropboxOAuth2FlowNoRedirect(api_key, api_secret)

        authorize_url = auth_flow.start()
        print("1. Go to: " + authorize_url)
        print ("2. Click \"Allow\" (you might have to log in first).")
        print ("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ")

        try:
            access_token, user_id = auth_flow.finish(auth_code)
        except:
            raise

        gd_utils.write_key("user_key", access_token)
