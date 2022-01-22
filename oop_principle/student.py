from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def getstuid(self):
        pass

    @abstractmethod
    def setstuid(self, stuid):
        pass

    @abstractmethod
    def getname(self):
        pass

    @abstractmethod
    def setname(self, name):
        pass

    @abstractmethod
    def getdept(self):
        pass

    @abstractmethod
    def setdept(self, dept):
        pass
