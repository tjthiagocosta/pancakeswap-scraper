from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import threading


from datetime import datetime
import time


def get_text(XPATH: str):
    return driver.find_element(By.XPATH, XPATH).text


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.get("https://pancakeswap.finance/position-managers?sortBy=earned&search=eth")

data = []


def scraper():
    while True:
        driver.refresh()
        time.sleep(15)
        apr = get_text(
            '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div')[:-1]
        now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        new_entry = [now, apr]
        data.append(new_entry)
        time.sleep(884)
        print("New data entry")


def data_saver():
    while True:
        # Git add
        subprocess.run(["git", "add", "."])

        # Git commit
        commit_message = "update data"
        subprocess.run(["git", "commit", "-m", commit_message])

        # Git push
        branch_name = "main"
        subprocess.run(["git", "push", "origin", branch_name])

        print("Data sent to Github")
        hour = 3600
        time.sleep(6*hour)


if __name__ == "__main__":
    # Create threads for each function
    scraper_thread = threading.Thread(target=scraper)
    data_saver_thread = threading.Thread(target=data_saver)

    # Start the threads
    scraper_thread.start()
    data_saver_thread.start()
