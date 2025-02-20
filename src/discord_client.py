import json
from urllib.request import Request, urlopen


class DiscordClient:
    """
    Discordの操作を行うクラス。
    """

    def __init__(self, webhook_url: str):
        """
        初期化処理。

        Args:
            webhook_url (str): DiscordのWebhook URL。
        """
        self.webhook_url = webhook_url

    def send_message(self, message: str):
        """
        Discordにメッセージを送信する。

        Args:
            message (str): 送信するメッセージ。
        """
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
        }
        data = {"content": message}
        request = Request(
            self.webhook_url,
            data=json.dumps(data).encode(),
            headers=headers,
        )

        with urlopen(request) as res:
            assert res.getcode() == 204

    def send_family_card_amount(self, family_card_amount: str):
        """
        家族カードの引き落とし額をDiscordに送信する。

        Args:
            family_card_amount (str): 家族カードの引き落とし額。
        """
        self.send_message(
            f"三井住友カード家族カードの引き落とし額: {family_card_amount}"
        )
