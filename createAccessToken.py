from mastodon import Mastodon
import json

f = open("Mastodon/config.json",'r')
json_data = json.load(f) #JSON形式で読み込む

url = 'https://mstdn.jp'
username = 'doraiso'
email = json_data[username]['email']
password = json_data[username]['password']
cid_file = 'Mastodon/client_id.txt'
token_file = 'Mastodon/access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    api_base_url=url,
)
mastodon.log_in(
    username = email,
    password = password,
    to_file = token_file
)