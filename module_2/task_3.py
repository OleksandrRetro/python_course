from utils.file_utils import FileUtils


class LettersCount(object):
    """
    Read text from file [/resources/module_2/letters_count.txt]
    Print the most frequent letter in the text
    Print how much times [Python] in text
    """

    @staticmethod
    def print_most_frequent_letter(text: str) -> None:
        counted_chars: dict = {}
        for char in text:
            if char in counted_chars:
                counted_chars[char] += 1
            else:
                counted_chars[char] = 1
        most_frequent: int = max(counted_chars.values())
        print("Most frequent letter is -> [{0}] with frequency -> [{1}] times."
              .format(list(counted_chars.keys())[list(counted_chars.values()).index(most_frequent)], most_frequent))


if __name__ == '__main__':
    file_path: str = "module_2/letters_count.txt"
    file_content: str = FileUtils().get_file_content_lower_without_special_chars(file_path)
    LettersCount.print_most_frequent_letter(file_content)
    string_pattern: str = "Python"
    print(f"Frequency of [{string_pattern}], is -> [{file_content.count(string_pattern.lower())}]")
