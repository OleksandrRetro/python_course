class FileSizeConversion:
    """
    Function get file size in [Bytes] and convert it to [Kilobyte], [Megabyte], [Gigabyte]
    """

    def __verify_conversion(self, actual: str, expected: str) -> None:
        assert actual == expected, "Value {0} is not equals to {1}".format(actual, expected)

    def file_size(self, size_in_bytes: int, expected: str) -> None:
        match size_in_bytes:
            case size_in_bytes if size_in_bytes / (1024 * 1024 * 1024) >= 1:
                self.__verify_conversion("{:.1f}Gb".format(size_in_bytes / (1024 * 1024 * 1024)), expected)
            case size_in_bytes if size_in_bytes / (1024 * 1024) >= 1:
                self.__verify_conversion("{:.1f}Mb".format(size_in_bytes / (1024 * 1024)), expected)
            case size_in_bytes if size_in_bytes / 1024 >= 1:
                self.__verify_conversion("{:.1f}Kb".format(size_in_bytes / 1024), expected)
            case _:
                self.__verify_conversion("{:.1f}B".format(size_in_bytes), expected)


if __name__ == '__main__':
    instance: FileSizeConversion = FileSizeConversion()
    print("Application is started.")
    instance.file_size(19, "19.0B")
    instance.file_size(12345, "12.1Kb")
    instance.file_size(1101947, "1.1Mb")
    instance.file_size(572090, "558.7Kb")
    instance.file_size(999999999999, "931.3Gb")
    print("Application is finished correctly.")
