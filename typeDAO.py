import sqlite3
from type import Type
from transaction import Transaction


class TypeDAO:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def get_all_type(self):
        sql = '''
            SELECT *
            FROM Type
        '''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        types = []
        for row in rows:
            type1 = Type(type=row[0], amount=row[1])
            types.append(type1)
        return types


    def amount_by_type(self, t:Transaction):
        sql = '''
            UPDATE Type 
            SET amount = amount + ?
            WHERE type = ?
        '''
        if t.type == "Expense":
            self.cursor.execute(sql, (t.amount, t.type))
        elif t.type == "Income":
            self.cursor.execute(sql, (t.amount, t.type))
        self.conn.commit()
        return self.cursor.rowcount