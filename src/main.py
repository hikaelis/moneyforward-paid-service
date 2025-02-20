from config import (
    DISCORD_WEBHOOK_URL,
    EMAIL,
    LOGIN_PAGE_URL,
    MITSUI_SUMITOMO_CARD_DETAIL_PAGE_XPATH,
    MITSUI_SUMITOMO_CARD_FAMILY_CARD_XPATH,
    PASSWORD,
)
from discord_client import DiscordClient
from moneyforward import MoneyForward


def main():
    """Retrieves information from MoneyForward and sends it to Discord.

    Returns:
        None
    """
    money_forward = MoneyForward(
        login_page_url=LOGIN_PAGE_URL,
        email=EMAIL,
        password=PASSWORD,
        mitsui_sumitomo_card_detail_page_xpath=MITSUI_SUMITOMO_CARD_DETAIL_PAGE_XPATH,
        mitsui_sumitomo_card_family_card_xpath=MITSUI_SUMITOMO_CARD_FAMILY_CARD_XPATH,
    )
    family_card_amount = money_forward.get_family_card_amount()

    discord_client = DiscordClient(DISCORD_WEBHOOK_URL)
    discord_client.send_family_card_amount(family_card_amount)


if __name__ == "__main__":
    main()
