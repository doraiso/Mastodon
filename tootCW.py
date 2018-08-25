# マストドンにCWを付けたトゥートするやつ
# 参考サイト:https://takulog.info/exercise-python-for-mastodon-1-answer/
import sys
from mastodon import Mastodon

url = 'https://mstdn.jp/'
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
miso = ''

for num in range(50):
    miso += 'みそみそ～'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

mastodon.status_post(
    miso,
    spoiler_text='４回目のトゥート #Python練習'
)