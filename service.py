from transactionsdao import TransactionsDAO
from category_amount_dao import CategoryAmountDAO
from typeDAO import TypeDAO


class TransactionService:
    def __init__(self):
        self.transactiondao = TransactionsDAO('transactions.sqlite')
        self.category_amountdao = CategoryAmountDAO("transactions.sqlite")
        self.typedao = TypeDAO("transactions.sqlite")

    def insert(self, transaction):
        id = self.transactiondao.insert(transaction)
        transaction.id = id

        return transaction

    def get_all(self):
        return self.transactiondao.get_all()

    def get_all_cat(self):
        return self.category_amountdao.get_all()

    def amount_is_correct(self):
        return self.transactiondao.amount_error()

    def amount_by_category(self, transaction):
        return self.category_amountdao.amount_by_category(transaction)

    def get_all_type(self):
        return self.typedao.get_all_type()

    def amount_by_type(self, transaction):
        return self.typedao.amount_by_type(transaction)
