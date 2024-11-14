import random
import string


class PasswordGen:
    def __init__(self, length: int = 8, numbers: bool = True):
        self.length = length
        self.numbers = numbers

    def gen(self):
        password = ""
        if self.numbers:
            for i in range(self.length):
                letter_or_num = random.randint(0, 1)
                if letter_or_num:
                    password += f"{random.choice(string.ascii_letters)}"
                else:
                    password += f"{random.choice(string.digits)}"

            return password
        else:
            for i in range(self.length):
                password += f"{random.choice(string.ascii_letters)}"

            return password
