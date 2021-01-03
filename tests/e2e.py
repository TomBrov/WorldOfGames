from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def test_score_service():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    chrome_driver = os.path.join("./chromedriver")
    driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

    driver.get("http://127.0.0.1:5000")
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