# class View:
#     def show_data(self, data):
#         print("Data:", data)

#     def get_input(self):
#         return input("Enter data: ")

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, \
                            QWidget, QLabel, QFrame, QSizePolicy, QComboBox, QDesktopWidget, QLineEdit, \
                            QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class WindowBuilder():
    def __init__(self):
        ...

    def get_button(self,button_text:str = None, clicked_func = lambda: None, *args):
        button = QPushButton(button_text)
        button.clicked.connect(lambda: clicked_func(*args))
        return button
    
    def get_label(self,label_text:str):
        return QLabel(label_text)

    def get_box_frame_widget(self,layout):
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setLayout(layout)
        frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        return frame
    
    def get_box_frame_layout(self,layout):
        # 용례 : widget.setLayout(self.wb.get_box_frame_layout(layout))
        framed_layout = QHBoxLayout()
        framed_layout.addWidget(self.get_box_frame_widget(layout))
        return framed_layout

    def get_combo_box_widget(self, items, combo_func=lambda: None):
        combo_box = QComboBox()
        combo_box.addItems(items)
        combo_box.currentIndexChanged.connect(combo_func)
        # combo_box.setStyleSheet("QComboBox { text-align: center; }")
        return combo_box

    def get_line_edit_widget(self, size=100):
        lineEdit = QLineEdit()
        lineEdit.setFixedWidth(size) 
        return lineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wb = WindowBuilder()
        # --------------------------
        screen = QDesktopWidget().screenGeometry() # 화면 크기 조정
        self.resize(int(screen.width() * 0.5), int(screen.height() * 0.4))
        self.setWindowTitle("NOVA Office Automation System")
        # --------------------------
        self.widgets = {
            'main' : QWidget(),
            'order_view' : self.get_order_view_widget(),
            'work_view' : self.get_work_view_widget(),
            'make_paper' : self.get_make_paper_widget(),
            'db_view' : self.get_db_view_widget(),
        }
        self.setCentralWidget(self.widgets['main'])
        # --------------------------
        self.layouts = {
            'main' : QVBoxLayout(),
            'top_button' : self.get_top_button_layout()
        }
        self.widgets['main'].setLayout(self.layouts['main'])
        self.layouts['main'].addLayout(self.layouts['top_button'])
        self.layouts['main'].setAlignment(Qt.AlignTop)
        {self.layouts['main'].addWidget(self.widgets[x]) for x in ['order_view','work_view','make_paper','db_view']}
        # --------------------------
        self.show_this_widget('main')
    # ===========================================================================================

    def get_top_button_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.wb.get_button("수주 현황 보기", self.show_this_widget, 'order_view'))
        layout.addWidget(self.wb.get_button("작업 현황 보기", self.show_this_widget, 'work_view'))
        layout.addWidget(self.wb.get_button("작업지시서 생성", self.show_this_widget, 'make_paper'))
        layout.addWidget(self.wb.get_button("DB 관리", self.show_this_widget, 'db_view'))
        return layout
    
    def show_this_widget(self,widget):
        for k in self.widgets.keys():
            if k in ["main",widget]:
                self.widgets[k].show()
            else:
                self.widgets[k].hide()

    
    # 테이블 생성, 열/행 세팅
    def init_table(self,tableRowc,tableColc, table = None):
        if not table: table = self.table_widget
        table.setRowCount(tableRowc)
        table.setColumnCount(tableColc)
        table.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)        

    def show_table(self,dictList:list=[{}]):
        self.table_widget.clear()
        try:
            self.init_table(len(dictList)+1,len(dictList[0])+1)
        except IndexError:
            self.init_table(1,1)
            item = QTableWidgetItem(str('데이터가 없습니다.'))
            item.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setItem(0, 0, item)
        else:
            for row, d in enumerate(dictList):
                for col, (key, val) in enumerate(d.items(), start=1):
                    if row == 0: #colName
                        self.table_widget.setItem(0, col, QTableWidgetItem(str(key)))
                    self.table_widget.clearSpans()
                    self.table_widget.setItem(row + 1, col, QTableWidgetItem(str(val)))

    def get_db_view_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        # --------------------------

        top_layout = QHBoxLayout()

        table_select_layout = QHBoxLayout() # 테이블 선택 콤보박스, 확인버튼
        table_select_layout.setAlignment(Qt.AlignLeft)
        table_select_layout.addWidget(self.wb.get_combo_box_widget(['a','1','2342343','3']))
        table_select_layout.addWidget(self.wb.get_button("확인"))

        table_search_layout = QHBoxLayout() # 테이블 검색 컬럼 콤보박스, 검색어 입력창, 검색버튼
        table_search_layout.addWidget(self.wb.get_combo_box_widget(['date','seq']))
        table_search_layout.addWidget(self.wb.get_line_edit_widget(int(self.width()*0.4)))
        table_search_layout.addWidget(self.wb.get_button("검색"))

        table_control_layout = QHBoxLayout() # 데이터 입력, 수정, 삭제 버튼
        table_control_layout.addWidget(self.wb.get_button("입력"))
        table_control_layout.addWidget(self.wb.get_button("수정"))
        table_control_layout.addWidget(self.wb.get_button("삭제"))

        top_layout.addLayout(table_select_layout)
        top_layout.addStretch(2)
        top_layout.addLayout(table_search_layout)
        top_layout.addStretch(1)
        top_layout.addLayout(table_control_layout)

        # -------------------------------------------------------------------------------------------

        table_view_layout = QVBoxLayout()
        table_view_layout.addWidget(QLabel("table_view_layout"))
        self.table_widget = QTableWidget() # temp
        table_view_layout.addWidget(self.table_widget)
        
        layout.addLayout(top_layout)
        layout.addLayout(self.wb.get_box_frame_layout(table_view_layout))
        widget.setLayout(self.wb.get_box_frame_layout(layout))

        # -------------------------------------------------------------------------------------------
        self.show_table([{'name':'aaa','age':'12'},{'name':'bbb','age':'42'},{'name':'ccc','age':'23'}])

        return widget
    
    def get_temp_widget(self):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QLabel("temp_view"))
        widget.setLayout(self.wb.get_box_frame_layout(layout))
        return widget

    def get_work_view_widget(self): return self.get_temp_widget()
    def get_make_paper_widget(self): return self.get_temp_widget()
    def get_order_view_widget(self): return self.get_temp_widget()


# ===========================================================================================

def mainwindow_test():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    mainwindow_test()