import random
import string


class RandomUtil:

    @staticmethod
    def get_random_alpha_string(length: int = 15) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))

    @staticmethod
    def get_random_numeric_string(length: int = 15) -> str:
        return ''.join(random.choices(string.digits, k=length))

    @staticmethod
    def get_random_alphanumeric_string(length: int = 15) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
