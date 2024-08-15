#!/usr/share/python

class Hello:
    _name = "Mulyo"

    def __init__(self, name=_name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def __repr__(self):
        return f'Hello {self.name}, happy pythoning!'


if __name__ == "__main__":

    hello = Hello()
    print(hello.__repr__())

    myName = input("Enter your name: ")
    hello.setName(myName)

    print(hello.__repr__())

    print(hello.getName())
