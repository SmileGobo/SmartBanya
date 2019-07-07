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
        #основной рендер по данным
        elif role == QtCore.Qt.BackgroundRole:
            num = index.column()
            if num < len(self._data):
                val = self._data[num]
                #вычисляем маску относительно текущей
                MASK = 1 << index.row()
                return self.ON if MASK & val else self.OFF
            return self.OFF
    
    #def setData(self, index: Qt.QModelIndex, val: Qt.QVariant, role: int) -> bool:
    #    row = index.row()
    #    col - index.col()
    #    return True

    def addColumn(self, val: int):
        self._data.append(val)
        col = len(self._data) - 1
        left = self.createIndex(0, col)
        right = self.createIndex(7, col)
        self.dataChanged.emit(left, right)
    
        
class TestApp(QtWidgets.QMainWindow, ui.display.Ui_MainWindow):
    DefaultCellSize = 14
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно дл инициализации нашего дизайна
        self._table = Table()

       
        self._display.setModel(self._table)
        self.setCellSize(self.DefaultCellSize)
        self._run.clicked.connect(self._runHandler)

    def _runHandler(self):
        #тестовые данные?
        for col in (1, 2, 4, 8):
            self._table.addColumn(col)

    def setCellSize(self, value: int):
        def setSize(count, action):
            for index in range(0, count):
                action(index, value)
        
        setSize(self._table.columnCount(), self._display.setColumnWidth)
        setSize(self._table.rowCount(), self._display.setRowHeight)
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = TestApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()