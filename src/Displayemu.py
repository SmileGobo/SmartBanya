import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, Qt, QtCore
import ui.display  # Это наш конвертированный файл дизайна

class Table(Qt.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._data = []
        pass

    DISPLAY_WIDTH = 40
    DISPLAY_HEIGHT = 8

    def rowCount(self, index =  Qt.QModelIndex()):
        return self.DISPLAY_HEIGHT
    
    def columnCount(self, index = Qt.QModelIndex()):
        return self.DISPLAY_WIDTH
    
    ON  = Qt.QColor(255, 0, 0)
    OFF = Qt.QColor(0, 0, 0)

    def data(self, index: Qt.QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            return None

        elif role == QtCore.Qt.SizeHintRole:
            return Qt.QSize(0, 0)
        elif role == QtCore.Qt.BackgroundRole:
            num = index.column()
            if num < len(self._data):
                val = self._data[num]
                MASK = 1 << index.row()
                return self.ON if MASK & val else self.OFF
            return self.OFF

    def addColumn(self, val: int):
        self._data.append(val)
        
class TestApp(QtWidgets.QMainWindow, ui.display.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно дл инициализации нашего дизайна
        self._table = Table()

        cols = (1, 2, 4, 8)
        for col in cols:
            self._table.addColumn(col)

        def setSize(count, action):
            SIZE = 25
            for index in range(0, count):
                action(index, SIZE)
        
        self._display.setModel(self._table)
        setSize(self._table.columnCount(), self._display.setColumnWidth)
        setSize(self._table.rowCount(), self._display.setRowHeight)

    def run(self):
        pass
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = TestApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()