class Multiples:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 100000000.
    """

    def print_sum(self, range_below: int) -> None:
        result: int = 0
        for item in range(1, range_below):
            if not item % 3:
                result += item
            elif not item % 5:
                result += item
        print(f"Result -> {result}")


if __name__ == '__main__':
    instance: Multiples = Multiples()
    print("Given rule.")
    instance.print_sum(10)
    print("\nTask:")
    instance.print_sum(100000001)
