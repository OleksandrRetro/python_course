from module_5.business import Engineer


class Alex(Engineer):

    def __init__(self, name, age):
        super().__init__(name, age)
        if self.__initialized: return
        self.__initialized = True

    def do_work(self):
        print("Do some work")

    __instance = None

    def __new__(cls, name, age):
        if cls.__instance is None:
            cls.__instance = super(Alex, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance
