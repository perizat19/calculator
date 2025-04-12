import sqlite3
from category_amount import CategoryAmount
from transaction import Transaction


class CategoryAmountDAO:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def get_all(self):
        sql = '''
                    SELECT *
                    FROM AmountByCategory
                '''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        amounts_cat = []
        for row in rows:
            cat_amount = CategoryAmount(category=row[0], amount=row[1])
            amounts_cat.append(cat_amount)
        return amounts_cat

    def amount_by_category(self, t:Transaction):
        sql = '''
            UPDATE AmountByCategory 
            SET amount = amount + ?
            WHERE category = ?
        '''
        if t.category == "Food":
            self.cursor.execute(sql, (t.amount, t.category))
        elif t.category == "Transport":
            self.cursor.execute(sql, (t.amount, t.category))
        elif t.category == "Housing":
            self.cursor.execute(sql, (t.amount, t.category))
        elif t.category == "Health Care":
            self.cursor.execute(sql, (t.amount, t.category))
        elif t.category == "Entertainment":
            self.cursor.execute(sql, (t.amount, t.category))
        else:
            self.cursor.execute(sql, (t.amount, t.category))
        self.conn.commit()
        return self.cursor.rowcount
