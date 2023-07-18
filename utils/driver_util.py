from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_util import ConfigUtil


class DriverUtil:
    __instance = None

    @staticmethod
    def get_instance():
        if DriverUtil.__instance is None:
            chrome_options = Options()
            arguments = ConfigUtil.get_browser_config()["browser-options"]
            for arg in arguments:
                chrome_options.add_argument(arg)
            DriverUtil.__instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                                     options=chrome_options)
        return DriverUtil.__instance

    @staticmethod
    def quit_and_reset():
        DriverUtil.__instance.quit()
        DriverUtil.__instance = None
