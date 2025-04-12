class CategoryAmount:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def amount_error(self):
        if self.amount <= 0:
            return 'The amount can not be negative or zero'

    def __str__(self):
        return (f'Category: {self.category}\n'
                f'Amount: {self.amount}')