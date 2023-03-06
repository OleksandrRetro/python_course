class ListFiltering(object):
    """
    Given list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    Create function to filter only [int] values.
    Using for, list comprehensions, filter() + lambda
    """

    @staticmethod
    def filter_list_using_for(input_list: list) -> list:
        result_list: list = []
        for item in input_list:
            if isinstance(item, int):
                result_list.append(item)
        return result_list

    @staticmethod
    def filter_list_using_list_comprehensions(input_list: list) -> list:
        result_list: list = [item for item in input_list if isinstance(item, int)]
        return result_list

    @staticmethod
    def filter_list_using_filter_lambda(input_list: list) -> list:
        result_list: list = list(filter(lambda e: isinstance(e, int), input_list))
        return result_list


if __name__ == '__main__':
    given_list: list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    print(ListFiltering.filter_list_using_for(given_list))
    print(ListFiltering.filter_list_using_list_comprehensions(given_list))
    print(ListFiltering.filter_list_using_filter_lambda(given_list))

    assert ListFiltering.filter_list_using_for([1, 2, 'a', 'b']) == [1, 2]
    assert ListFiltering.filter_list_using_list_comprehensions([1, 'a', 'b', 0, 15]), [1, 0, 15]
    assert ListFiltering.filter_list_using_filter_lambda([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123]
