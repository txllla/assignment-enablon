import yaml


class ConfigUtil:
    @staticmethod
    def get_webdriver_config():
        with open("../webdriver_config.yaml", "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_logger_config():
        with open("../logger_config.yaml", "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_browser_config():
        with open("../browser_config.yaml", "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_test_data():
        with open("../tests/test_data.yaml", "r") as f:
            return yaml.safe_load(f)
