class Type:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def amount_error(self):
        if self.amount <= 0:
            return 'The amount can not be negative or zero'

    def __str__(self):
        return f'Type: {self.type}, amount: {self.amount}.'