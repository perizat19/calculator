class Transaction():

    def __init__(self, id, date, amount, type, category):
        self.id = id
        self.date = date
        self.amount = amount
        self.type = type
        self.category = category

    def set_id(self, id):
        self.id = id

    def amount_error(self):
        if self.amount <= 0:
            return 'The amount can not be negative or zero'

    def __str__(self):
        return (f'ID: {self.id}\n'
                f'Date: {self.date}\n'
                f'Transaction amount: {self.amount}\n'
                f'Transaction type: {self.type}'
                f'Category: {self.category}')
