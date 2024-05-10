if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
from src.module.pyqt_imports import *
from src.module.exceptions import *

class TablePlusWidget(QTableWidget):
    def __init__(self, border_data=[], \
                 form_data={'init_size' : (1,1), 'slim_rows' : [],'slim_cols' : [],'text_items' : [],}):
        super().__init__()
        self.border_data = border_data
        self.form_data = form_data

    # 열/행 세팅
    def init_table(self,row,col):
        self.setRowCount(row)
        self.setColumnCount(col)
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
    
        [self.setItem(r, c, QTableWidgetItem()) for r in range(row) for c in range(col)] # 빈 아이템 채우기 (테두리 표시)

    # 내용 채우기
    def fill_table_data_sequence(self,dict_list:list=[{}],use_check_box:bool=True,use_table_header:bool=True):
        self.clear()
        try:
            if len(dict_list[0]) == 0:
                raise NoTableDataError
            row = len(dict_list)+1 if use_table_header else len(dict_list) # row+1(표머리)
            col = len(dict_list[0])+1 if use_check_box else len(dict_list[0]) # col+1(체크박스)
            self.init_table(row,col)
        except NoTableDataError:
            self.init_table(1,1)
            self.setItem(0, 0, QTableWidgetItem(str('데이터가 없습니다.')))
        else: #표 내용 작성
            if use_check_box:
                self.setCellWidget(0, 0, self.set_and_get_table_checkbox(None)) #전체 체크박스
            for row, d in enumerate(dict_list):
                if use_check_box:
                    self.setCellWidget(row+1, 0, self.set_and_get_table_checkbox(None)) #행 체크박스
                for col, (key, val) in enumerate(d.items()):
                    col_idx = col+1 if use_check_box else col
                    row_idx = row+1 if use_table_header else row
                    if use_table_header:
                        self.setItem(0, col_idx, QTableWidgetItem(str(key))) #표머리
                    self.setItem(row_idx, col_idx, QTableWidgetItem(str(val))) #값
        finally:
            self.resizeColumnsToContents()

    def fill_table_data_position(self,data_position):...
    # -------------------------------------------------------------------------------------------
    # 표 형식 채우기
    def fill_table_form(self):
        self.verticalHeader().setMinimumSectionSize(10)
        self.init_table(*self.form_data['init_size'])
        self.set_slim_rows(self.form_data['slim_rows'])
        self.set_slim_cols(self.form_data['slim_cols'])
        # -------------------------------------------------------------------------------------------
        for f in self.form_data['text_items']:
            pos,span,text,item_option = f
            self.setSpan(*pos,*span)
            self.set_and_get_table_text_item(pos,text,item_option)

    # [table util] ===========================================================================================
    def set_slim_rows(self,rows,height=10)->None:
        [self.setRowHeight(r, height) for r in rows]

    def set_slim_cols(self,col,width=10)->None:
        [self.setColumnWidth(c, width) for c in col]

    # -------------------------------------------------------------------------------------------

    def set_and_get_table_text_item(self,pos,text,item_option=[])->QTableWidgetItem:
        item = QTableWidgetItem(str(text))

        if 'editable' not in item_option: # 수정불가 회색으로 표시
            item.setFlags(item.flags() & ~item.flags() | ~Qt.ItemIsEditable)
            item.setForeground(QColor(128,128,128))
        # --------------------------
        if 'black' in item_option:
            item.setForeground(QColor(0,0,0))
        elif 'red' in item_option:
            item.setForeground(QColor(255,0,0))                    
        # --------------------------
        if 'bold' in item_option:
            font = QFont("Arial", 12)
            font.setBold(True)
            item.setFont(font)
        # --------------------------
        # if 'title' in item_option:
        #     from PyQt5.QtGui import QFontDatabase
        #     HMKMRHD = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont("./font/HMKMRHD.TTF"))[0]
        #     font = QFont(HMKMRHD, 20)
        #     item.setFont(font)
        # --------------------------
        if 'center' in item_option:
            item.setTextAlignment(Qt.AlignCenter)
        elif 'right' in item_option:
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        elif 'left' in item_option:
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # --------------------------
        if pos: 
            self.setItem(*pos,item)
        return item

    def set_and_get_table_btn_item(self,pos,text,func)->QPushButton:
        button = QPushButton(str(text))
        button.clicked.connect(func)
        if pos: 
            self.setCellWidget(*pos, button)
        return button

    def set_and_get_table_checkbox(self, pos, default:bool=False)->QCheckBox:
        checkbox = QCheckBox()
        checkbox.setStyleSheet("QCheckBox::indicator { width: 30px; height: 30px; }")
        checkbox.setChecked(default)
        if pos: 
            self.setCellWidget(*pos, checkbox)
        return checkbox
        
    def set_and_get_table_combobox(self,pos,items,comblFunc=lambda: None)->QComboBox:
        combobox = QComboBox()
        combobox.addItems(items)
        combobox.currentIndexChanged.connect(comblFunc)
        combobox.setStyleSheet("QComboBox { text-align: center; }")
        if pos: 
            self.setCellWidget(*pos, combobox)
        return combobox

    # -------------------------------------------------------------------------------------------
    def get_item(self,pos):
        return self.cellWidget(*pos)
    
    def get_table_text(self,pos)->str:
        item = self.get_item(pos)
        if item is None: 
            return ''
        else:
            return item.text()

    # -------------------------------------------------------------------------------------------
    def change_table_text_item(self, pos, text)->None:
        item = self.get_item(pos)
        if item is None: 
            self.set_and_get_table_text_item(pos,text)
        else:
            item.setText(text)

    # -------------------------------------------------------------------------------------------
    # 특정 셀의 체크박스 체크여부 반환
    def is_checkbox_checked(self, pos):
        if self.isCheckBox(*pos):
            checkbox = self.get_item(pos)
            isinstance(checkbox, QCheckBox)
            return checkbox.isChecked()
        else:
            return None

    # [draw border] ===========================================================================================
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())

        for i in self.border_data:
            row, col, rowspan, colspan, border = i

            color = Qt.red if 'red' in border else Qt.black
            width = 3 if 'bbold' in border else 2 if 'bold' in border else 1
                
            painter.setPen(QPen(color, width, Qt.SolidLine))

            rect = self.visualItemRect(self.item(row,col))
            for i in range(row,row+rowspan):
                for j in range(col,col+colspan):
                    if (i, j) != (row,col):
                        rect = rect.united(self.visualItemRect(self.item(i, j)))

            painter.drawRect(rect)
        painter.end()

# ===========================================================================================

def main():
    def get_border_data():
        return [
            [0,7,3,3,'bold'], [0,7,1,3,''], [0,8,3,1,''],
            [4,0,3,10,'bold'],[8,0,5,10,'bold'],[14,0,13,10,'bold'],[28,0,6,10,'bold'],[35,0,4,10,'bold'],
            [4,0,3,2,''],[8,0,1,5,''],[8,0,5,2,''], [15,0,4,2,''],[19,0,4,2,''],[23,0,4,2,''],
            [28,0,2,2,''],[30,0,2,2,''],[32,0,2,2,''],[35,0,4,2,''],
            [28,0,2,8,''],[30,0,2,8,''],[32,0,2,8,''],[35,0,4,8,''],
            [4,5,3,2,''],[5,5,2,5,''],[8,5,5,5,''],[14,0,1,6,''],[14,6,1,2,''],[14,8,1,2,''],
            [15,2,2,8,''],[15,6,2,2,''],[17,2,2,8,''],[17,6,2,2,''],
            [19,2,4,8,''],[19,6,4,2,''],[23,2,4,8,''],[23,6,4,2,''],
        ]
    def get_form_data():
        return {
            'init_size' : (39,10),
            'slim_rows' : [3,7,13,27,34],
            'slim_cols' : [],
            'text_items' : [
                [(1,0),(2,5),"공구 제조 지시서", 'title'],
                [(4,0),(3,2),"제조지시   NO.",'centerbold'],
                [(4,5),(1,2),"작성일",'centerbold'],
                [(5,5),(2,2),"출고예정일",'centerbold'],
                [(8,0),(1,2),"제품명",'centerbold'],
            ],
        }

    app = QApplication([])

    table_widget = TablePlusWidget(get_border_data(),get_form_data())
    table_widget.fill_table_form()
    table_widget.show()
    app.exec_()

if __name__ == "__main__":
    main()
