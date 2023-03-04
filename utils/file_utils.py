import re


class FileUtils(object):
    """
    Utility class to make operations with files.
    """

    @staticmethod
    def __read_file(file_path: str) -> str:
        with open(file_path) as f:
            contents = f.read()
        return contents

    def get_file_content_lower_without_special_chars(self, file_path: str) -> str:
        return re.sub('\\W+', '', self.__read_file(file_path).lower())
