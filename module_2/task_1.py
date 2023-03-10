class FizzBuzz:
    """
    Print integers from 1 to 100
    If (integer % 3 and integer % 5) -> print "FizzBuzz"
    If integer % 3 -> print "Fizz"
    If integer % 5 -> "Buzz"
    """

    def variant_1(self) -> None:
        for item in range(1, 101):
            if not item % 3 and not item % 5:
                print(f"{item} % 3 and {item} % 5 - > FizzBuzz")
            elif not item % 3:
                print(f"{item} % 3 -> Fizz")
            elif not item % 5:
                print(f"{item} % 5 -> Buzz")
            else:
                print(f"{item} is not a FizzBuzz value")

    def variant_2(self) -> None:
        for item in range(1, 101):
            match item:
                case item if (not item % 3 and not item % 5):
                    print(f"{item} % 3 and {item} % 5 - > FizzBuzz")
                case item if not item % 3:
                    print(f"{item} % 3 -> Fizz")
                case item if not item % 5:
                    print(f"{item} % 5 -> Buzz")
                case _:
                    print(f"{item} is not a FizzBuzz value")


if __name__ == '__main__':
    instance: FizzBuzz = FizzBuzz()
    # Using IF
    print("VARIANT_1 STARTED")
    instance.variant_1()
    print("VARIANT_1 FINISHED")

    # Using Match
    print("\nVARIANT_2 STARTED")
    instance.variant_2()
    print("VARIANT_2 FINISHED")
