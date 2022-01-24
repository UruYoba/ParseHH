from selenium import webdriver
from os import path
from fake_useragent import UserAgent


def get_browser():
    abs_path = path.dirname(__file__)
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")

    driver_path = path.join("ChromeDriver", "chromedriver.exe")
    return webdriver.Chrome(
        executable_path=path.join(abs_path, driver_path),
        options=options
    )


if __name__ == "__main__":
    url = "https://www.google.com/"
    driver = get_browser()
    driver.get(url)
