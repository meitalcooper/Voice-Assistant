import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Infoweb:
    """
    Class to handle web information retrieval using Selenium WebDriver.
    """
    def __init__(self):
        # Initialize Chrome WebDriver with the specified path to the ChromeDriver
        chrome_service = Service(executable_path='C:\\Users\\meital\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def get_info(self, query):
        """
        Fetches information from Wikipedia based on the user query.
        """
        try:
            self.query = query
            self.driver.get("https://www.wikipedia.org/")
            search_box = self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
            search_box.send_keys(query)
            search_box.submit()
            time.sleep(10)  # Short delay to allow page to load results
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()


class Music():
    """
    Class to play music or videos from YouTube using Selenium WebDriver.
    """
    def __init__(self):
        chrome_service = Service(executable_path='C:\\Users\\meital\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def get_music(self, query):
        """
        Plays a YouTube video based on the user query.
        """
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
        video.click()
        time.sleep(10)









