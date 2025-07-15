class Expense:
    def __init__(self, id, amount):
        self.id = id  # Public attribute (CWE-522)
        self.amount = amount  # Public attribute (CWE-522)

    @staticmethod
    def new_expense(id, amount):
        return Expense(id, amount)  # No input validation (CWE-20)
