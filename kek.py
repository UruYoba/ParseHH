import time
import Driver
from fake_useragent import UserAgent

user_agent = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
adres = "https://2ip.ru/"


if __name__ == "__main__":
    driver = Driver.get_browser()
    driver.maximize_window()
    driver.get(adres)
    time.sleep(5)