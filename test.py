from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

def area_func_button():
    print("im hear")
    app.exec()
    dlg.hide()
    area.show()

def read_text():
    if area.lineEdit.text() != "" & area.lineEdit_4.text() != "" & area.lineEdit_3.text() != "" & area.lineEdit_2.text() != "":
        top_left_x = area.lineEdit.text()
        top_left_y = area.lineEdit_3.text()
        top_right_x = area.lineEdit_4.text()
        top_right_y = area.lineEdit_2.text()
    else:
        area.lineEdit.setStyleSheet("color: red;")


dlg.PushButton_6.clicked.connect(area_func_button)
area = uic.loadUi("area_window.ui")
area.ok_button.clicked.connect(read_text)

dlg.show()
app.exec()








