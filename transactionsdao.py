import sqlite3
from transaction import Transaction
from category_amount import CategoryAmount
from type import Type


class TransactionsDAO:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def get_all(self):
        sql = '''
            SELECT *
            FROM transactions_all
        '''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        transactions = []

        for row in rows:
            transaction = Transaction(id=row[0], date=row[1], amount=row[2], type=row[3], category=row[4])
            transactions.append(transaction)

        return transactions

    def get_by_id(self, id):
        sql = '''
            SELECT *
            FROM transactions_all
            WHERE id = ?
        '''
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()

        if row:
            transaction = Transaction(id=row[0], date=row[1], amount=row[2], type=row[3], category=row[4])
        else:
            transaction = None

        return transaction

    def insert(self, t:Transaction):
        sql = '''
            INSERT INTO transactions_all (date, amount, type, category)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (t.date, t.amount, t.type, t.category))
        self.conn.commit()

        return self.cursor.lastrowid

    def update(self, t:Transaction):
        sql = '''
            UPDATE transactions_all
            SET date = ?, amount = ?, type = ?, category = ?
            WHERE id = ?
        '''
        self.cursor.execute(sql, (t.date, t.amount, t.type, t.category))
        self.conn.commit()

        return self.cursor.rowcount

    def delete(self, id):
        sql = '''
            DELETE FROM transactions_all 
            WHERE id = ?
        '''
        self.cursor.execute(sql, (id,))
        self.conn.commit()

        return self.cursor.rowcount

    def amount_error(self, t:Transaction):
        if t.amount <= 0:
            return 'Amount cannot be negative or zero.'

