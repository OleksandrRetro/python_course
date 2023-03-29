from module_9.singleton_alex import Alex


def test_singleton():
    a1 = Alex("Igor", 13)
    a2 = Alex("Igor", 13)

    if id(a1) == id(a2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
