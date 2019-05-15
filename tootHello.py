import sys
from mastodon import Mastodon

url = 'https://mstdn.jp/'
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

str = 'ンホ'
rep = 100

for num in range(rep):
    str += 'ォ'

for num in range(rep):
    str += 'ッ'

for num in range(rep):
    str += '！'

# mastodon.toot('はじめてのトゥート #Python練習')
# mastodon.toot(str)
print(str)

