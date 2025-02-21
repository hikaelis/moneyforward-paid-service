discordへのメッセージ送信方法は以下のURLとコードを参考にしてください。

@url <https://zenn.dev/karaage0703/articles/926f18ba04e093>
@url <https://discordpy.readthedocs.io/ja/latest/api.html>

```py
import json
from urllib.request import Request, urlopen


def post_discord(message: str, webhook_url: str):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    data = {"content": message}
    request = Request(
        webhook_url,
        data=json.dumps(data).encode(),
        headers=headers,
    )

    with urlopen(request) as res:
        assert res.getcode() == 204

if __name__ == "__main__":
    webhook_url = '<webhook url>'
    post_discord('Webhookテスト', webhook_url)
```
