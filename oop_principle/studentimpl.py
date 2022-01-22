from student import Student


class StudentImpl(Student):

    # encapsulation -> private __ , protected _ , public
    # constructor
    def __init__(self, stuid, name, dept):
        self.__stuid = stuid
        self.__name = name
        self.__dept = dept

    def getstuid(self) -> str:
        return self.__stuid

    def setstuid(self, stuid):
        self.__stuid = stuid

    def getname(self) -> str:
        return self.__name

    def setname(self, name):
        self.__name = name

    def getdept(self):
        return self.__dept

    def setdept(self, dept):
        self.__dept = dept

    def __str__(self) -> str:
        return self.__stuid+" "+self.__name+" "+self.__dept
