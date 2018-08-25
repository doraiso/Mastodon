from mastodon import Mastodon

url = 'https://mstdn.jp'
appname = 'Python_Exercise'
cid_file = 'Mastodon/client_id.txt'

Mastodon.create_app(
    appname,
    api_base_url=url,
    to_file = cid_file
)