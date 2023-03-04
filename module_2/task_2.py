class MinMaxValue(object):
    """
    Given list -> [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    Convert all elements to [int] type
    Print [min] and [max] values
    """

    @staticmethod
    def convert_to_int(actual_list: list) -> list:
        result_list: list = []
        for index in range(len(actual_list)):
            try:
                result_list.append(int(actual_list[index]))
            except ValueError:
                print(f"ValueError while converting element ->  {actual_list[index]}")
            except TypeError:
                print(f"TypeError while converting element ->  {actual_list[index]}")
        return result_list

    @staticmethod
    def print_min_max_values(actual_list: list) -> None:
        print(f"Min value -> {min(actual_list)}")
        print(f"Max value -> {max(actual_list)}")


if __name__ == '__main__':
    values_list: list = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    print(f"Given list -> {values_list}")
    converted_list: list = MinMaxValue.convert_to_int(values_list)
    print(f"Converted list elements to int() -> {converted_list}")
    MinMaxValue.print_min_max_values(converted_list)
