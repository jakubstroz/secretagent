from abc import ABC, abstractmethod

class Contact(ABC):
    def __init__(self, type, number, name, lastname) -> None:
        self.type = type
        self.number = number
        self.name = name
        self.lastname = lastname
        self.friends = []

    @abstractmethod
    def __str__(self) -> str:
        pass

class Soldier(Contact):
    def __init__(self, number, name, lastname) -> None:
        super().__init__('soldier', number, name, lastname)
    
    def __str__(self) -> str:
        info = str(self.number) + ' ' + self.name + ' ' + self.lastname + '\n'
        info += 'Znajomi:' + ' '.join(str(self.friends))
        return info
    

class Network():

    __persons = []
    __authorization = False
    __secretLogin = 'python'
    __secretPassword = 'project'


    def authorize(self):
        login = input('Podaj nazwę użytkownika: ')
        password = input('Podaj hasło: ')
        if login == self.__secretLogin and password == self.__secretPassword:
            print('poprawna autoryzacja')
            return True
        else:
            print('hasło lub/i login nieprawidłowy')
            return False


    def logged(func):
        def inside(self, *args, **kwargs):
            if self.__authorization == False:
                print('muisz być zalogowany')
                return
            else:
                print(f'wykonano funkcję {func.__name__}')
                return func(self, *args, **kwargs)
        return inside


    @logged
    def print(self, alist, *args):
        for i in alist:
            print(i)


    @logged
    def add_person(self, number):
        name = input("podaj imię: ")
        lastname = input("podaj nazwisko: ")
        new = Soldier(number, name, lastname)
        return new
    

    @logged
    def add_friend(self, persons):
        a = int(input('numer osoby 1: '))
        b = int(input('numer osoby 2: '))

        for x in persons:
            if x.number == a:
                x.friends += [b]
            if x.number == b:
                x.friends += [a]
        return persons
    

    def make(self):
        while True:
            print("""
            1 - wyświetl sieć kontaktów
            2 - dodaj osobę
            3 - dodaj powiązanie między kontaktami
            4 - zaloguj
            9 - zamknij \n
        """)
            x = int(input(': '))

            if x == 1:
                self.print(self.__persons)
            
            if x == 2:
                new = self.add_person(len(self.__persons)+1)
                if new != None: self.__persons.append(new)
            
            if x == 3:
                self.add_friend(self.__persons)
            
            if x == 4:
                if self.authorize():
                    self.__authorization = True
                else:
                    self.__authorization = False
            if x == 9:
                import sys
                sys.exit(0)

new = Network()
new.make()