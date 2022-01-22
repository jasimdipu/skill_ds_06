# semno, credit, percreditfees, waiver
# inheritance

from studentimpl import StudentImpl


class Administrator(StudentImpl):

    def __init__(self, stuid, name, dept, semno, credit, percreditfees, waiver=True):
        super().__init__(stuid, name, dept)
        self.__semno = semno
        self.__credit = credit
        self.__percreditfees = percreditfees
        self.__waiver = waiver
        self.__waiver_percent = 0.0
        self.__total_amount = credit*percreditfees
        self.__is_registered = False

    def first_installment(self):
        return (self.__total_amount*40)/100

    def registration(self, payment=0.0):
        if self.__is_registered == False:
            print(self.getstuid()+self.getname()+self.getdept())
            print("Your first installment: ", self.first_installment())
            if payment >= self.first_installment():
                return "You are registed successfully on sem "+str(self.__semno)

            elif payment == 0.0:
                payment = float(input("Please pay your first payment."))
                due_amount = self.__total_amount - payment
                self.__total_amount = due_amount
                print('first payment :', payment)
                print('your due amount:', self.__total_amount)
                self.__is_registered = True
                if payment >= self.first_installment():
                    return "You are registed successfully on sem "+str(self.__semno)
        else:
            return "You are already registered"
