def __int__(self):
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *

    class Mysignal(QObject):
        signal1 = pyqtSignal()

        def run(self):
            self.signal1.emit()

    class Mywindow(QMainWindow):
        def __int__(self):
            super().__init__()

            mysignal = Mysignal()
            mysignal.signal1.connect(self.signal_emitted)
            mysignal.run()

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()