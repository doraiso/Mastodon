import random
from mastodon import Mastodon

url = 'https://mstdn.jp/'
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

strinit = 'ンホ'
strnho = ['ォ','ッ','！']
repnum = 100

def nho(strinput):
    str = ''
    rep = random.randint(1,repnum)
    for num in range(rep):
        str += strinput
    return str

def appendnho():
    str = ''
    for num in strnho:
        str += nho(num)
    return str

nho = strinit + appendnho()

print(nho)

mastodon.status_post(
    nho,
    spoiler_text='ンホォ #Python練習'
)