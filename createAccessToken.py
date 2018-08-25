# https://takulog.info/exercise-python-for-mastodon-1-answer/
# 4. インスタンスからアクセストークンを取得して、ファイル「access_token.txt」に保存してください。
# 今回はパスワード方式で登録します。実運用では推奨されていません。
# また、前問1-3で取得したClient IDおよびClient Secretを保存したファイルを利用します。
# 同じく、以降の処理は全てここでのファイルを使うので、非常に重要です。
# なお、EMAIL@EXAMPLE.COM および PASSWORD もアカウントの正確なものと読み替えてください。
# ※この方法が褒められたものでは無いとは思いますが。。。


from mastodon import Mastodon
import json

f = open("Mastodon/config.json",'r') # ここにメールアドレスとかパスワードぶっこんでる
json_data = json.load(f) # JSON形式で読み込む

url = 'https://mstdn.jp' # インスタンス
username = 'doraiso' # これぼく

email = json_data[username]['email'] # JSONからメールアドレス読むの
password = json_data[username]['password'] # JSONからパスワード読むの

cid_file = 'Mastodon/client_id.txt' # クライアントIDというやつ
token_file = 'Mastodon/access_token.txt' # ここにアクセストークンを入れるの

mastodon = Mastodon(
    client_id=cid_file,
    api_base_url=url,
)
mastodon.log_in(
    username = email,
    password = password,
    to_file = token_file
)