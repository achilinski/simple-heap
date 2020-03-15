class Stos:

    def __init__(self, number_of_elements, exception_meassage):
        self.stos = []
        self.number = number_of_elements
        self.message = exception_meassage

    def __repr__(self):
        return str(self.stos)

    def add_elemnt(self, element):
        self.stack_overflow_alert()
        self.stos.append(element)

    def remove_elemnt(self):
        if self.is_it_empty():
            raise Exception(self.message)
        else:
            self.stos.pop(len(self.stos) - 1)

    def stack_overflow_alert(self):
        if len(self.stos) > self.number:
            raise Exception('za duzo ')

    def is_it_empty(self):
        return not self.stos

    def print_stos(self):
        print(self.stos)


def checker(str_to_check):
    stos = Stos(len(str_to_check), "nie zgdadza sie")
    for i in str_to_check:
        if i == '(':
            stos.add_elemnt(i)
        if i == ')':
            stos.remove_elemnt()

    if stos.is_it_empty():
        print('ok')
    else:
        print('nie')
