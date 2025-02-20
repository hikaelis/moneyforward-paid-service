import os

from dotenv import load_dotenv

load_dotenv()

LOGIN_PAGE_URL = os.environ.get("LOGIN_PAGE_URL")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
MITSUI_SUMITOMO_CARD_DETAIL_PAGE_XPATH = os.environ.get(
    "MITSUI_SUMITOMO_CARD_DETAIL_PAGE_XPath"
)
MITSUI_SUMITOMO_CARD_FAMILY_CARD_XPATH = os.environ.get(
    "MITSUI_SUMITOMO_CARD_FAMILY_CARD_XPath"
)
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

if not all(
    [
        LOGIN_PAGE_URL,
        EMAIL,
        PASSWORD,
        MITSUI_SUMITOMO_CARD_DETAIL_PAGE_XPATH,
        MITSUI_SUMITOMO_CARD_FAMILY_CARD_XPATH,
        DISCORD_WEBHOOK_URL,
    ]
):
    print("Environment variables are not set.")
