# マストドンにNSFWの画像つきのトゥートするやつ
# 参考サイト:https://takulog.info/exercise-python-for-mastodon-1-answer/

import sys
from mastodon import Mastodon

url = 'https://mstdn.jp' # インスタンス
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
imgfile1 = 'image/img2.jpg'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

img1 = mastodon.media_post(imgfile1)
img_files = [img1]

mastodon.status_post(
    status = '５回目のトゥート #Python練習',
    sensitive=True,
    media_ids = img_files
)