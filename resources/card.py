
class credit_card(object):
    def __init__(self, name, sec_code, code):
        credit = 0
        self.name = name
        self.sec_code = sec_code
        self.code = code
        self.credit = float(credit)

    def add_credi(self, credit):
        self.credit += float(credit)

    def remove_credi(self, credit):
        self.credit -= float(credit)
        
    def print_credit(self):
        return self.credit

    


