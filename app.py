from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap
import sys,os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QVBoxLayout, QHBoxLayout, QMainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    # Create a PyQt application
    app = QApplication(sys.argv)
    print(os.path.dirname(os.path.abspath(sys.argv[0])))
    # Create a QMainWindow (main window)
    main_window = QMainWindow()
    main_window.move(1300,0)
    main_window.setWindowTitle('hello')
    main_window.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))

    # Set the window properties (title and initial size)
    main_window.resize(700,900)  # (x, y, width, height)
    main_window.setWindowFlags(
                    QtCore.Qt.FramelessWindowHint 
                  | QtCore.Qt.WindowStaysOnTopHint)
    main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Create a central widget for the main window
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)

    # Create widgets (QLabel and QPushButton)
    label1 = QLabel()
    pix = QPixmap(resource_path("box2.png"))
    label1.setPixmap(pix);
    label2 = QLabel()
    movie = QMovie(resource_path('girl.gif'))
    label2.setMovie(movie)
    movie.start()
    label2.mousePressEvent = QApplication.quit
    

    # Create vertical and horizontal layouts
    vertical_layout = QVBoxLayout()
    

    # Add widgets to layouts
    vertical_layout.addWidget(label1)
    vertical_layout.addWidget(label2)
    

    # Set the layout for the central widget
    central_widget.setLayout(vertical_layout)

    # Show the window
    main_window.show()

    # Run the application's event loop
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    
    
    
