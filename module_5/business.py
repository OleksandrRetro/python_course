import abc
from abc import ABC


class Company(object):
    """ Represents a company """

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee):
        if isinstance(employee, Engineer) or isinstance(employee, Manager):
            if employee.company is not None:
                employee.company = None

    def dismiss_employee(self, employee):
        if employee.is_employed():
            print(f"Employee {employee.name} dismissed.")
            employee.company = None
        else:
            print(f"Employee {employee.name} is not a company member.")

    def notify_im_leaving(self, employee):
        print(f"Employee {employee.name} leaving the company {employee.company}.")
        employee.company = None

    def do_tasks(self, employee):
        if employee.is_employed() and isinstance(employee, Engineer):
            self.__money -= 10
            employee.put_money_into_my_wallet(10)
        return 10

    def write_reports(self, employee):
        if employee.is_employed() and isinstance(employee, Manager):
            self.__money -= 12
            employee.put_money_into_my_wallet(12)
        return 12

    def make_a_party(self):
        if not self.is_bankrupt:
            for employee in self.employees:
                employee.bonus_to_salary(employee.company, 5)
        print(self.is_bankrupt)

    def show_money(self):
        print(f"Company money = {self.__money}")

    def go_bankrupt(self):
        self.__money = 0
        self.employees.clear()

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name


class Person(object):
    """ Represents any person """

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        if self.company != company:
            self.company = company

    def become_unemployed(self):
        self.company = None

    def notify_dismissed(self):
        self.company = None

    def bonus_to_salary(self, company, reward=5):
        if self.company == company:
            self.__money += 5

    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    def put_money_into_my_wallet(self, amount):
        self.__money += amount

    def show_money(self):
        print(self.__money)

    @abc.abstractmethod
    def do_work(self):
        print("Do some work")

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'


class Engineer(Employee, ABC):

    def __init__(self, name, age):
        super().__init__(name, age)


class Manager(Employee, ABC):

    def __init__(self, name, age):
        super().__init__(name, age)


def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()

    # add second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()
