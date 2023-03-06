import json
import re

from csv import DictReader


class FileUtils(object):
    """
    Utility class to make operations with files.
    """
    __RESOURCES_DIR: str = "../resources/"

    @staticmethod
    def __read_file(file_path: str) -> str:
        with open(FileUtils.__RESOURCES_DIR + file_path) as f:
            contents = f.read()
        return contents

    def get_file_content_lower_without_special_chars(self, file_path: str) -> str:
        return re.sub('\\W+', '', self.__read_file(file_path).lower())

    @staticmethod
    def read_csv_file(file_path: str) -> list:
        with open(FileUtils.__RESOURCES_DIR + file_path, 'r') as f:
            return list(DictReader(f))

    @staticmethod
    def write_json_file(file_path: str, csv_list: list) -> None:
        with open(FileUtils.__RESOURCES_DIR + file_path, 'w') as f:
            f.write(json.dumps(csv_list, indent=2))
