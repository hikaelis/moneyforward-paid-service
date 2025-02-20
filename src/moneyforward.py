from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MoneyForward:
    """
    マネーフォワードの操作を行うクラス。
    """

    def __init__(
        self,
        login_page_url,
        email,
        password,
        mitsui_sumitomo_card_detail_page_xpath,
        mitsui_sumitomo_card_family_card_xpath,
    ):
        """
        初期化処理。

        Args:
            login_page_url (str): ログインページのURL。
            email (str): ログインに使用するメールアドレス。
            password (str): ログインに使用するパスワード。
            mitsui_sumitomo_card_detail_page_xpath (str): 三井住友カードの詳細ページへのXPath。
            mitsui_sumitomo_card_family_card_xpath (str): 家族カードの金額のXPath。
        """
        self.login_page_url = login_page_url
        self.email = email
        self.password = password
        self.mitsui_sumitomo_card_detail_page_xpath = (
            mitsui_sumitomo_card_detail_page_xpath
        )
        self.mitsui_sumitomo_card_family_card_xpath = (
            mitsui_sumitomo_card_family_card_xpath
        )
        self.driver = self._setup_driver()

    def _setup_driver(self):
        """
        SeleniumのWebDriverをセットアップする。

        Returns:
            webdriver.Chrome: セットアップされたWebDriver。
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            return driver
        except Exception as e:
            print(f"Error setting up Chrome driver: {e}")
            return None

    def login(self):
        """
        マネーフォワードにログインする。
        """
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "sign_in_session_service_email").send_keys(
            self.email
        )
        self.driver.find_element(By.ID, "sign_in_session_service_password").send_keys(
            self.password
        )
        self.driver.find_element(By.NAME, "commit").click()

    def go_to_mitsui_sumitomo_card_detail_page(self):
        """
        三井住友カードの詳細ページに移動する。
        """
        mitsui_sumitomo_card_detail_page_element = self.driver.find_element(
            By.XPATH, self.mitsui_sumitomo_card_detail_page_xpath
        )
        mitsui_sumitomo_card_detail_page_element.click()

    def get_family_card_amount(self):
        """
        家族カードの金額を取得する。

        Returns:
            str: 家族カードの金額。
        """
        self.login()
        self.go_to_mitsui_sumitomo_card_detail_page()
        family_card_amount_element = self.driver.find_element(
            By.XPATH, self.mitsui_sumitomo_card_family_card_xpath
        )
        family_card_amount = family_card_amount_element.text
        self.driver.quit()
        return family_card_amount
