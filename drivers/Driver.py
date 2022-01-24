import os.path
import time
from ChromeDriver import Chrome

url = "https://lipetsk.hh.ru/"
# driver = Chrome.configure()
# driver.get(url)
# time.sleep(5)
# driver.close()
# driver.quit()

if __name__ == "__main__":
    driver = Chrome.configure()
    print()
    print(os.path.abspath(__file__))
    driver.get(url)

