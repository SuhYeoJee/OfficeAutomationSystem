if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
# -------------------------------------------------------------------------------------------
from src.module.pyqt_imports import *
from src.module.table_plus_widget import TablePlusWidget
from src.module.window_builder import WindowBuilder
# -------------------------------------------------------------------------------------------
from src.p_view import pView
# ===========================================================================================

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wb = WindowBuilder()
        self.widgets = {}
        self.layouts = {}
        self.dialogs = {}
        # --------------------------
        screen = QDesktopWidget().screenGeometry() # 화면 크기 조정
        self.resize(int(screen.width() * 0.5), int(screen.height() * 0.4))
        self.setWindowTitle("NOVA Office Automation System")
        # --------------------------
        self.widgets['main'] = QWidget()
        self.widgets['db_view'] = self.get_db_view_widget()
        self.widgets['order_view'] = self.get_order_view_widget()
        self.widgets['work_view'] = self.get_work_view_widget()
        self.widgets['paper_view'] = self.get_paper_view_widget()
        self.setCentralWidget(self.widgets['main'])
        # --------------------------
        self.layouts['main'] = QVBoxLayout()
        self.layouts['top_button'] = self.get_top_button_layout()
        # --------------------------
        self.widgets['main'].setLayout(self.layouts['main'])
        self.layouts['main'].addLayout(self.layouts['top_button'])
        self.layouts['main'].setAlignment(Qt.AlignTop)
        {self.layouts['main'].addWidget(self.widgets[x]) for x in ['order_view','work_view','paper_view','db_view']}
        # --------------------------
        self.show_this_view('main')
    # [레이아웃 구성] ===========================================================================================
    # 상단 버튼바 레이아웃
    def get_top_button_layout(self):
        def on_button_clicked(button): # 버튼클릭시 색상 강조
            [self.widgets[x].setStyleSheet("") for x in ['order_view_open','db_view_open','paper_view_open','work_view_open']]
            self.widgets[button].setStyleSheet("background-color: darkGray;")

        layout = QHBoxLayout()
        self.widgets['order_view_open'] = self.wb.get_button("수주 현황 보기", self.show_this_view, 'order_view')
        self.widgets['work_view_open'] = self.wb.get_button("작업 현황 보기", self.show_this_view, 'work_view')
        self.widgets['paper_view_open'] = self.wb.get_button("작업지시서 생성", self.show_this_view, 'paper_view')
        self.widgets['db_view_open'] = self.wb.get_button("DB 관리", self.show_this_view, 'db_view')

        self.widgets['order_view_open'].clicked.connect(lambda: on_button_clicked('order_view_open'))
        self.widgets['work_view_open'].clicked.connect(lambda: on_button_clicked('work_view_open'))
        self.widgets['paper_view_open'].clicked.connect(lambda: on_button_clicked('paper_view_open'))
        self.widgets['db_view_open'].clicked.connect(lambda: on_button_clicked('db_view_open'))

        [layout.addWidget(self.widgets[x]) for x in ['order_view_open','work_view_open','paper_view_open','db_view_open']]
        return layout
    # [각 뷰 상단 구성 > get_table_view_widget 호출] -------------------------------------------------------------------------------------------
    def get_order_view_widget(self): 
        top_button_layout = QHBoxLayout()
        top_button_layout.setAlignment(Qt.AlignLeft)
        self.widgets['order_view_submit'] = self.wb.get_button("확인") #temp
        top_button_layout.addWidget(self.widgets['order_view_submit'] )                
        return self.get_table_view_widget('order_view',top_button_layout)
    # --------------------------
    def get_work_view_widget(self): 
        top_button_layout = QHBoxLayout()
        top_button_layout.setAlignment(Qt.AlignLeft)
        self.widgets['work_view_ip_select_submit'] = self.wb.get_button("출고일 등록") #temp
        top_button_layout.addWidget(self.widgets['work_view_ip_select_submit'] )        
        return self.get_table_view_widget('work_view',top_button_layout)
    # --------------------------
    def get_paper_view_widget(self): 
        top_button_layout = QHBoxLayout()
        top_button_layout.setAlignment(Qt.AlignLeft)
        self.widgets['paper_view_ip_select_submit'] = self.wb.get_button("IP 선택 생성")
        self.widgets['paper_view_ip_all_submit'] = self.wb.get_button("IP 전체 생성")
        self.widgets['paper_view_sp_select_submit'] = self.wb.get_button("SP 선택 생성")
        self.widgets['paper_view_sp_all_submit'] = self.wb.get_button("SP 전체 생성")
        top_button_layout.addWidget(self.widgets['paper_view_ip_select_submit'] )
        top_button_layout.addWidget(self.widgets['paper_view_ip_all_submit'] )
        top_button_layout.addWidget(self.widgets['paper_view_sp_select_submit'] )
        top_button_layout.addWidget(self.widgets['paper_view_sp_all_submit'] )
        return self.get_table_view_widget('paper_view',top_button_layout)
    # --------------------------
    def get_db_view_widget(self): 
        table_select_layout = QHBoxLayout() # 테이블 선택 콤보박스, 확인버튼
        table_select_layout.setAlignment(Qt.AlignLeft)
        self.widgets["db_view_table_names_combo_box"] = self.wb.get_combo_box_widget([])
        self.widgets["db_view_table_names_submit"] = self.wb.get_button("확인")
        table_select_layout.addWidget(self.widgets["db_view_table_names_combo_box"])
        table_select_layout.addWidget(self.widgets["db_view_table_names_submit"])
        self.layouts['db_view_table_select'] = table_select_layout
        # --------------------------
        table_search_layout = QHBoxLayout() # 테이블 검색 컬럼 콤보박스, 검색어 입력창, 검색버튼
        self.widgets["db_view_search_cols_combo_box"] = self.wb.get_combo_box_widget([])
        self.widgets["db_view_search_line_edit"] = self.wb.get_line_edit_widget(int(self.width()*0.4))
        self.widgets["db_view_search_submit"] = self.wb.get_button("검색")
        table_search_layout.addWidget(self.widgets["db_view_search_cols_combo_box"])
        table_search_layout.addWidget(self.widgets["db_view_search_line_edit"])
        table_search_layout.addWidget(self.widgets["db_view_search_submit"])
        self.layouts['db_view_table_search'] = table_search_layout
        # --------------------------
        table_control_layout = QHBoxLayout() # 데이터 입력, 수정, 삭제 버튼
        self.widgets["db_view_control_insert"] = self.wb.get_button("입력")
        self.widgets["db_view_control_update"] = self.wb.get_button("수정")
        self.widgets["db_view_control_delete"] = self.wb.get_button("삭제")
        table_control_layout.addWidget(self.widgets["db_view_control_insert"])
        table_control_layout.addWidget(self.widgets["db_view_control_update"])
        table_control_layout.addWidget(self.widgets["db_view_control_delete"])
        self.layouts['db_view_table_control'] = table_control_layout
        # --------------------------
        # self.get_db_view_insert_dialog()
        # --------------------------
        top_button_layout = QHBoxLayout()
        top_button_layout.addLayout(self.layouts['db_view_table_select'])
        top_button_layout.addStretch(2)
        top_button_layout.addLayout(self.layouts['db_view_table_search'])
        top_button_layout.addStretch(1)
        top_button_layout.addLayout(self.layouts['db_view_table_control'])
        self.layouts['db_view_table_top'] = top_button_layout

        return self.get_table_view_widget('db_view',top_button_layout)
    # -------------------------------------------------------------------------------------------
    def get_table_view_widget(self,view_name:str, top_button_layout:QHBoxLayout):
        top_layout = QHBoxLayout()
        top_layout.addStretch(2)
        top_layout.addLayout(top_button_layout)
        # --------------------------
        self.layouts[f'{view_name}_table_view'] = QVBoxLayout()
        self.widgets[f'{view_name}_table'] = TablePlusWidget()
        self.layouts[f'{view_name}_table_view'].addWidget(self.widgets[f'{view_name}_table'])
        self.show_table(target_table=f'{view_name}_table')
        # --------------------------
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(self.layouts[f'{view_name}_table_view'])
        # --------------------------        
        widget = QWidget()
        widget.setLayout(self.wb.get_box_frame_layout(layout))
        # --------------------------
        return widget
    # ===========================================================================================
    # 페이지 전환
    def show_this_view(self,widget):
        for k in ["order_view",'work_view','paper_view','db_view']:
            self.widgets[k].hide()
        else:
            self.widgets[widget].show()
    # ===========================================================================================
    # db뷰 입력 대화창
    def get_db_view_insert_dialog(self, table_name:str='', table_cols:dict = {}, domain_datas:dict = {}):
        if table_name == '':
            print('특수 입력 대화창')
        # -------------------------------------------------------------------------------------------
        # else: #일반 입력 대화창
        # 오른쪽, 왼쪽 분할
        first_half_layout,second_half_layout = QVBoxLayout(),QVBoxLayout()
        eng_table_cols = list(table_cols.keys())
        mid_idx = (len(eng_table_cols) + 1) // 2
        first_half, second_half = eng_table_cols[:mid_idx], eng_table_cols[mid_idx:]

        self.dialog_widgets = {}

        for eng_col in first_half: # 한글화
            kor_col = table_cols[eng_col]
            domains = domain_datas.get(eng_col,[])
            first_half_layout.addLayout(self.wb.get_label_and_line_edit_layout(kor_col,self.dialog_widgets,eng_col,domains))
        for eng_col in second_half:
            kor_col = table_cols[eng_col]
            domains = domain_datas.get(eng_col,[])
            second_half_layout.addLayout(self.wb.get_label_and_line_edit_layout(kor_col,self.dialog_widgets,eng_col,domains))
        # --------------------------
        input_layout = QHBoxLayout()
        input_layout.addLayout(first_half_layout)
        input_layout.addWidget(self.wb.get_vline_widget())
        input_layout.addLayout(second_half_layout)
        # --------------------------
        layout = QVBoxLayout()
        layout.addLayout(self.wb.get_box_frame_layout(input_layout))
        self.widgets['db_view_insert_submit'] = self.wb.get_button('저장')
        layout.addWidget(self.widgets['db_view_insert_submit'])
        # --------------------------
        dialog = QDialog(self)
        dialog.setWindowTitle(f'[{table_name}] 새 항목 입력')
        dialog.setLayout(layout)
        self.dialogs["db_view_insert"] = dialog

    # [ctrl 호출] ===========================================================================================
    # db뷰 입력 대화창
    def show_db_view_insert_dialog(self):
        self.dialogs["db_view_insert"].show()

    def get_ip_viewer(self,ip_data):
        dialog = pView(self,ptable_data=ip_data,is_sp=False)
        dialog.show()
        self.dialogs["ip_viewer"] = dialog

    def get_sp_viewer(self,sp_data):
        dialog = pView(self,ptable_data=sp_data,is_sp=True)
        dialog.show()
        self.dialogs["sp_viewer"] = dialog

    # [테이블] ===========================================================================================
    # 테이블 생성, 열/행 세팅
    def init_table(self,tableRowc,tableColc,target_table:str = 'db_view_table'):
        table = self.widgets[target_table]
        table.setRowCount(tableRowc)
        table.setColumnCount(tableColc)
        table.setEditTriggers(QAbstractItemView.DoubleClicked)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
    # -------------------------------------------------------------------------------------------
    # 테이블 내용 갱신
    def show_table(self,dictList:list=[{}], target_table:str = 'db_view_table',no_sys_cols:bool=True):
        self.widgets[target_table].clear()
        try:
            
            self.init_table(len(dictList)+1,len(dictList[0])+1,target_table) # 추가row(표머리), 추가col(체크박스)
        except IndexError:
            self.init_table(1,1,target_table)
            item = QTableWidgetItem(str('데이터가 없습니다.'))
            item.setTextAlignment(Qt.AlignCenter)
            self.widgets[target_table].setItem(0, 0, item)
        else: #표 내용 작성
            self.widgets[target_table].setCellWidget(0, 0, QCheckBox())                
            for row, d in enumerate(dictList):
                self.widgets[target_table].setCellWidget(row+1, 0, QCheckBox())                
                for col, (key, val) in enumerate(d.items(), start=1):
                    
                    if row == 0: #colName
                        self.widgets[target_table].setItem(0, col, QTableWidgetItem(str(key)))
                        if no_sys_cols and 'sys_' in key:
                            self.widgets[target_table].setColumnHidden(col,True)
                        else:
                            self.widgets[target_table].setColumnHidden(col,False)
                    self.widgets[target_table].clearSpans()
                    self.widgets[target_table].setItem(row + 1, col, QTableWidgetItem(str(val)))
        self.widgets[target_table].resizeColumnsToContents()
    # -------------------------------------------------------------------------------------------
    # 테이블 체크박스 반영
    def change_combo_box(self,target_combo_box,new_items):
        self.widgets[target_combo_box].clear()
        self.widgets[target_combo_box].addItems(new_items)
    # ===========================================================================================



if __name__ == "__main__":
    app = QApplication([])
    window = View()
    window.show()
    app.exec_()
