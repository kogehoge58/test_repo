import requests


# ジョーク生成関数
def create_joke():

	# エンドポイント
	url = "https://official-joke-api.appspot.com/jokes/random"

	# API呼び出し
	response = requests.get(url)

	# レスポンス返却
	return response.json()


# 翻訳関数
def translate(text):

	# DeepL APIのエンドポイント
	url = "https://api-free.deepl.com/v2/translate"

	# リクエストのパラメータ
	params = {
		"auth_key": "a497e307-2f42-46a2-9bbf-eab15014dfd5:fx",
		"text": text,
		"target_lang": "JA"
	}

	# POSTリクエストの送信
	response = requests.post(url, data=params)

	# レスポンス解析
	translated_text = response.json()["translations"][0]["text"]
	# レスポンス返却
	return translated_text


# メイン関数
def main():

	# ジョーク生成
	joke = create_joke()

	# 仕分け
	歌丸 = joke["setup"]
	円楽 = joke["punchline"]

	# 翻訳
	translated_歌丸 = translate(歌丸)
	translated_円楽 = translate(円楽)

	# 出力
	print("歌丸「" + translated_歌丸 + "」")
	print("円楽「" + translated_円楽 + "」")


main()