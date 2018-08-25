import sys
from mastodon import Mastodon

url = 'https://mstdn.jp' # インスタンス
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

mastodon.status_post(
    'はじめての非公開トゥート #Python練習',
    visibility='private',
    sensitive=True,
    spoiler_text='おならぷーぷー'
)