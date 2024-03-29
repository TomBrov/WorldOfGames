from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from redis import Redis
import os


def test_score_service():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    chrome_driver = os.path.join("./chromedriver")
    driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

    redis = Redis(password='wog123', decode_responses=True)
    redis.set('user', 8)
    redis.close()

    driver.get("http://0.0.0.0:8777")
    score = int(driver.find_element_by_id("score").get_attribute("innerText"))
    if 1 < score < 1000:
        x = True
    else:
        x = False
    driver.close()
    return x


if __name__ == '__main__':
    if test_score_service():
        exit(0)
    else:
        exit(1)