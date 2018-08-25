# 3. インスタンスへクライアント「Python_Exercise」を登録して、Client ID と Client Secret を取得してください。
# Client ID と Client Secret は Mastodon.pyモジュールを使えば、1つの関数で1つのファイルに格納してくれます。
# 以降の処理は全てこのファイルを使うので、非常に重要です。

from mastodon import Mastodon

url = 'https://mstdn.jp' # インスタンス
appname = 'Python_Exercise'
cid_file = 'Mastodon/client_id.txt'

Mastodon.create_app(
    appname,
    api_base_url=url,
    to_file = cid_file
)