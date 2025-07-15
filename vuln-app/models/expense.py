# expense.py
class Expense:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    @staticmethod
    def new_expense(id, amount):
        return Expense(id, amount)
