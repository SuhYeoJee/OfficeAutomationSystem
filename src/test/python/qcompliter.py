import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QLineEdit, QCompleter, QVBoxLayout, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    # QTableWidget 생성
    table_widget = QTableWidget(5, 2)
    
    # QCompleter를 사용할 QLineEdit 생성
    line_edit = QLineEdit()
    completer_list = ['apple','apple2','apple3', 'banana', 'cherry', 'grape', 'orange']
    completer = QCompleter(completer_list)
    line_edit.setCompleter(completer)

    # QLineEdit을 QTableWidget의 셀에 삽입
    table_widget.setCellWidget(0, 0, line_edit)

    window_layout = QVBoxLayout()
    window_layout.addWidget(table_widget)
    window.setLayout(window_layout)

    window.show()
    sys.exit(app.exec_())
