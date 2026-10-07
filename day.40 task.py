'''
class CentralBank:
    """Base class"""
    cash = 10000000
    def __init__(self):
        self.branch_name = "Central Bank Main Branch"
        self.__secret_cash = 2000000
    @classmethod
    def available_cash(cls):
        print(f'Available Cash with {cls.__name__} is {cls.cash}')
    def branch_details(self):
        print(f'Branch Name is {self.branch_name}')
    def secret_cash(self):
        print(f'Secret Cash is {self.__secret_cash}')
class AxisBank(CentralBank):
    """Derived class-1"""
    cash = 5000000
    def axis_cash(self):
        print(f'Axis Bank Cash is {self.cash}')
        print(f'Total Cash is {self.cash + CentralBank.cash}')
class ICICIBank(CentralBank):
    """Derived class-2"""
    cash = 7000000
    def icici_cash(self):
        print(f'ICICI Bank Cash is {self.cash}')
        print(f'Total Cash is {self.cash + CentralBank.cash}')
u1 = AxisBank()
print(u1.cash)
u1.available_cash()
u1.branch_details()
u1.secret_cash()
u1.axis_cash()
u2 = ICICIBank()
print(u2.cash)
u2.available_cash()
u2.branch_details()
u2.secret_cash()
u2.icici_cash()
'''
Task2: Real scenario for multiple inheritance
class Developer:
    """Developer features"""
    def write_code(self):
        print("Developer can write code")
class Designer:
    """Designer features"""
    def design_ui(self):
        print("Designer can design UI")
class TechLead(Developer, Designer):
    """TechLead inherits from Developer and Designer"""
    def manage_team(self):
        print("TechLead can manage the team")
u1 = TechLead()
u1.write_code()
u1.design_ui()
u1.manage_team()
