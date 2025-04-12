import os
from datetime import datetime

from PyQt6 import uic
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelection
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableView, QTabWidget, QComboBox
from transaction import Transaction
from service import TransactionService


class MainWindow(QMainWindow):

    mainTabs: QTabWidget
    typeTab: QTabWidget
    expenseLineEdit: QLineEdit
    categoryComboBox: QComboBox
    addExpButton: QPushButton
    incomeLineEdit: QLineEdit
    incomeComboBox: QComboBox
    addIncButton: QPushButton
    typeTableView: QTableView
    historyTableView: QTableView
    categoryTableView: QTableView
    actionClear: QPushButton
    actionRefresh_2: QPushButton

    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "exp_track_design.ui")
        uic.loadUi(ui_path, self)

        self.transactionservice = TransactionService()

        self.tablemodel = TransactionTableModel(self.transactionservice.get_all())
        self.historyTableView.setModel(self.tablemodel)

        self.tablemodel_cat = AmountByCatTableModel(self.transactionservice.get_all_cat())
        self.categoryTableView.setModel(self.tablemodel_cat)

        self.tablemodel_type = TypeTableModel(self.transactionservice.get_all_type())
        self.typeTableView.setModel(self.tablemodel_type)

        self.addExpButton.clicked.connect(self.on_click_exp_add)
        self.addIncButton.clicked.connect(self.on_click_inc_add)

        self.actionClear.triggered.connect(self.on_click_clear)
        self.actionRefresh_2.triggered.connect(self.on_click_refresh)

        self.historyTableView.selectionModel().selectionChanged.connect(self.on_table_clicked)
        self.categoryTableView.selectionModel().selectionChanged.connect(self.on_table_clicked)

    def on_table_clicked(self, selected: QItemSelection, deselected: QItemSelection):
        selected_indexes = selected.indexes()

        if selected_indexes:
            selected_index = selected_indexes[0]

            row = selected_index.row()
            selected_transaction:Transaction = self.tablemodel.transactions[row]

            self.expenseLineEdit.setText(selected_transaction.amount)
            self.categoryComboBox.setCurrentText(selected_transaction.category)

            print(f"Selected Transaction: {selected_transaction}")

    def on_click_exp_add(self):
        amount = self.expenseLineEdit.text()
        date = str(datetime.now())
        type1 = 'Expense'
        category = self.categoryComboBox.currentText()

        transaction = Transaction(id=None, date=date, amount=amount, type=type1, category=category)
        transaction = self.transactionservice.insert(transaction)
        self.tablemodel.addTransaction(transaction)
        self.tablemodel_type = self.transactionservice.amount_by_type(transaction)
        self.tablemodel_cat = self.transactionservice.amount_by_category(transaction)

    def on_click_inc_add(self):
        amount = self.incomeLineEdit.text()
        date = str(datetime.now())
        type1 = 'Income'
        category = self.incomeComboBox.currentText()

        transaction = Transaction(id=None, date=date, amount=amount, type=type1, category=category)
        transaction = self.transactionservice.insert(transaction)
        self.tablemodel.addTransaction(transaction)
        self.tablemodel_cat = self.transactionservice.amount_by_category(transaction)
        self.tablemodel_type = self.transactionservice.amount_by_type(transaction)

    def on_click_clear(self):
        self.expenseLineEdit.clear()
        self.incomeLineEdit.clear()

    def on_click_refresh(self):
        pass


class TransactionTableModel(QAbstractTableModel):
    def __init__(self, transactions=None):
        super().__init__()
        self.transactions = transactions or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.transactions)

    def columnCount(self, parent=QModelIndex()):
        return 5

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            transaction = self.transactions[index.row()]
            if index.column() == 0:
                return transaction.id
            elif index.column() == 1:
                return transaction.date
            elif index.column() == 2:
                return transaction.amount
            elif index.column() == 3:
                return transaction.type
            elif index.column() == 4:
                return transaction.category
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['ID', 'Date', 'Amount', 'Type', 'Category']
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None

    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        row = len(self.transactions)
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()
        self.layoutChanged.emit()


class AmountByCatTableModel(QAbstractTableModel):
    def __init__(self, amounts_cat=None):
        super().__init__()
        self.amounts_cat = amounts_cat or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.amounts_cat)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            category_amount = self.amounts_cat[index.row()]
            if index.column() == 0:
                return category_amount.category
            elif index.column() == 1:
                return category_amount.amount

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['Category', 'Amount']
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None

    def addAmountCat(self, category_amount):
        self.amounts_cat.append(category_amount)
        row = len(self.amounts_cat)
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()
        self.layoutChanged.emit()


class TypeTableModel(QAbstractTableModel):
    def __init__(self, types=None):
        super().__init__()
        self.types = types or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.types)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            type_amount = self.types[index.row()]
            if index.column() == 0:
                return type_amount.type
            elif index.column() == 1:
                return type_amount.amount

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['Type', 'Amount']
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None

    def addAmountType(self, category_amount):
        self.types.append(category_amount)
        row = len(self.types)
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()
        self.layoutChanged.emit()





