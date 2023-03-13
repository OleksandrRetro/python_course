import re


class MultiplyNumbersWithRegex:
    """
    Create method to multiplies every number in given text on 2 and returns changed text.
    Use [re.sub] - https://docs.python.org/3/library/re.html#re.sub
    In parameter [repl] use [string] and [function]
    """

    __digit_regexp: str = r'\s[0-9]+\s'

    def __multiply_numbers(self, match_number, multiplier: int) -> str:
        num: int = int(match_number.group())
        return str(f" {num * multiplier} ")

    def change_text_with_function(self, text: str, multiplier: int = 2):
        return re.sub(self.__digit_regexp, lambda x: self.__multiply_numbers(x, multiplier), text)

    def change_text(self, text: str, multiplier: int = 2):
        return re.sub(self.__digit_regexp, lambda x: f" {(int(x.group()) * multiplier)} ", text)


if __name__ == '__main__':
    instance: MultiplyNumbersWithRegex = MultiplyNumbersWithRegex()
    given_text: str = "Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих " \
                      "футболистов средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 " \
                      "футбольных сборных"
    print(instance.change_text_with_function(given_text, 10))

    text_example: str = "I am 10 years old"
    print(instance.change_text(text_example))
    print(instance.change_text(text_example, 25))
