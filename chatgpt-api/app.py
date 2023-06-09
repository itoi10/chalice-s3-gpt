import openai
from chalice import Chalice, CORSConfig

app = Chalice(app_name="chatgpt-api")
cors_config = CORSConfig(allow_origin="*")


@app.route("/lengthy", methods=["POST"], cors=cors_config)
def lengthy():
    try:
        # リクエストからテキストを取得
        text = app.current_request.json_body.get("text")
        if not text:
            raise Exception("textがありません")

        messages = [
            {"role": "system", "content": "あなたは長文生成ツールです。「」の中のテキストを無駄に長い文章に変換してください。"},
            {"role": "user", "content": f"「{text}」"},
        ]

        # ChatGPTのAPIに送信
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # https://platform.openai.com/docs/models/gpt-3-5
            messages=messages,
            temperature=1,  # 0に近いほど決まった文章になる 0~2 デフォルト1
        )
        # レスポンスからメッセージを取得
        ai_message = response["choices"][0]["message"]["content"]
        # メッセージ一覧を返す
        return {"result": ai_message}

    except Exception as e:
        return {"error": f"{e}"}
