if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
# -------------------------------------------------------------------------------------------
from src.module.table_plus_widget import *
from src.model import Model
from src.view import View
# --------------------------
from PyQt5.QtWidgets import QApplication
# -------------------------------------------------------------------------------------------

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view_button_mapping()
    # --------------------------
    # sp_viewer_image_export
    # ip_viewer_image_export
    # ip_viewer_xlsx_export
    def t(self):print('t')
    
    # [mapping] ===========================================================================================
    def view_button_mapping(self) -> None:
        self.db_view_button_mapping()
        self.paper_view_button_mapping()
        self.work_view_button_mapping()
    # -------------------------------------------------------------------------------------------
    def work_view_button_mapping(self) -> None:
        #테이블 클릭 매핑
        self.view.widgets['work_view_table'].cellClicked.connect(lambda row, col: self.on_ip_no_cell_clicked(row, col, "work_view_table"))
        self.view.widgets['work_view_table'].cellClicked.connect(lambda row, col: self.on_sp_no_cell_cliced(row, col, "work_view_table"))
        #테이블 내용 세팅
        self.view.widgets['work_view_open'].clicked.connect(self.set_work_view_table_contents)
    # --------------------------
    def paper_view_button_mapping(self) -> None:
        #테이블 클릭 매핑
        self.view.widgets['paper_view_table'].cellClicked.connect(lambda row, col: self.on_ip_no_cell_clicked(row, col, "paper_view_table"))
        self.view.widgets['paper_view_table'].cellClicked.connect(lambda row, col: self.on_sp_no_cell_cliced(row, col, "paper_view_table"))
        #테이블 내용 세팅
        self.view.widgets['paper_view_open'].clicked.connect(self.set_paper_view_table_new_ips)
        #상단 버튼 매핑
        self.view.widgets['paper_view_ip_select_submit'].clicked.connect(self.do_ip_for_selected_item_order)
        self.view.widgets['paper_view_ip_all_submit'].clicked.connect(self.do_ip_for_all_item_order)
        self.view.widgets['paper_view_sp_select_submit'].clicked.connect(self.do_sp_for_selected_item_order)
        self.view.widgets['paper_view_sp_all_submit'].clicked.connect(self.do_sp_for_all_item_order)
    # --------------------------
    def db_view_button_mapping(self) -> None:
        #테이블 내용 세팅
        self.view.widgets['db_view_open'].clicked.connect(self.set_db_view_table_name_combo_box)
        #상단 버튼 매핑
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_col_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_all_contents)
        self.view.widgets["db_view_search_submit"].clicked.connect(self.set_db_view_table_search_contents)
        self.view.widgets["db_view_control_update"].clicked.connect(self.update_selected_rows)
        self.view.widgets["db_view_control_delete"].clicked.connect(self.delete_selected_rows)
        self.view.widgets["db_view_control_insert"].clicked.connect(self.update_and_show_insert_dialog)
        # self.view.widgets["db_view_insert_submit"].clicked.connect(self.insert_dialog_data)
    # [mapping func] ===========================================================================================
    # ip no 셀 클릭시 뷰어호출, 버튼매핑
    def on_ip_no_cell_clicked(self, row, col, table_name):
        if col in [self.get_table_col_index(x,table_name) for x in ['ip_no','IP']]:
            ip_no = self.get_table_by_name(table_name).get_cell_text((row,col))
            try:
                ip_data = self.model.select_table_with_wheres('ip',[f"`ip_no` = '{ip_no}'"])[0]
            except IndexError:
                ... #해당 ip 없음
            else:
                self.view.get_ip_viewer(ip_data)
                # --------------------------
                self.view.dialogs['ip_viewer'].widgets["submit"].clicked.connect(lambda: self.ip_viewer_update_ip(ip_data['sys_id']))
                self.view.dialogs['ip_viewer'].widgets["image_export"].clicked.connect(self.t)
                self.view.dialogs['ip_viewer'].widgets["xlsx_export"].clicked.connect(self.t)                
    # --------------------------
    # ip뷰어 수정내용 저장
    def ip_viewer_update_ip(self,sys_id): 
        ip_data = self.view.dialogs['ip_viewer'].widgets["ptable"].get_labeled_data()
        ip_data['sys_id'] =  sys_id
        self.model.update_table_and_select_updated('ip',[ip_data])

    # [sp 매핑] -------------------------------------------------------------------------------------------
    # sp no 셀 클릭시 뷰어호출, 버튼매핑
    def on_sp_no_cell_cliced(self,row,col,table_name):
        if col in [self.get_table_col_index(x,table_name) for x in ['sp_no','SP']]:
            sp_no = self.get_table_by_name(table_name).get_cell_text((row,col))
            try:
                sp_data = self.model.select_table_with_wheres('sp',[f"`sp_no` = '{sp_no}'"])[0]
            except IndexError:
                ... #해당 sp 없음
            else:                
                self.view.get_sp_viewer(sp_data)
                # --------------------------
                self.view.dialogs['sp_viewer'].widgets["submit"].clicked.connect(lambda: self.sp_viewer_update_sp(sp_data['sys_id']))
                self.view.dialogs['sp_viewer'].widgets["image_export"].clicked.connect(self.t)        
                self.view.dialogs['sp_viewer'].widgets["sp_viewer_workload_submit"].clicked.connect(self.sp_viewer_do_workload_update)
                self.view.dialogs['sp_viewer'].widgets["sp_viewer_weight_submit"].clicked.connect(self.sp_viewer_do_weight_update)
                self.view.dialogs['sp_viewer'].widgets["sp_viewer_diamix_submit"].clicked.connect(self.sp_viewer_do_dosing_diamix_update)
    
    # --------------------------
    # sp 작업량 갱신
    def sp_viewer_do_workload_update(self):
        sp_data = self.sp_viewer_get_sp_data() #현재 입력값 가져오기
        asp_data = self.model.spm.sp_viewer_workload_update(sp_data)
        self.view.dialogs['sp_viewer'].set_sp_view_data(asp_data) # sp view 갱신
    # --------------------------
    # sp 분말무게 갱신
    def sp_viewer_do_weight_update(self):
        sp_data = self.sp_viewer_get_sp_data() #현재 입력값 가져오기
        asp_data = self.model.spm.sp_viewer_weight_update(sp_data)
        self.view.dialogs['sp_viewer'].set_sp_view_data(asp_data) # sp view 갱신
    # --------------------------
    # sp 다이아믹스 갱신
    def sp_viewer_do_dosing_diamix_update(self):
        sp_data = self.sp_viewer_get_sp_data() #현재 입력값 가져오기
        asp_data = self.model.spm.sp_viewer_dosing_diamix_update(sp_data)
        self.view.dialogs['sp_viewer'].set_sp_view_data(asp_data) # sp view 갱신
    # --------------------------
    # sp뷰어 내용 전부 가져오기
    def sp_viewer_get_sp_data(self)->dict:
        sp_data = self.view.dialogs['sp_viewer'].widgets["ptable"].get_labeled_data()
        side_data = self.view.dialogs['sp_viewer'].get_sp_side_data(sp_data) # 사이드 레이아웃 가져오기
        sp_data.update(side_data)
        return sp_data
    # --------------------------
    # sp뷰어 수정내용 저장
    def sp_viewer_update_sp(self,sys_id): 
        sp_data = self.sp_viewer_get_sp_data()
        sp_data['sys_id'] =  sys_id
        self.model.update_table_and_select_updated('sp',[sp_data])
    # [ip/sp 생성함수 호출] -------------------------------------------------------------------------------------------
    def do_ip_for_selected_item_order(self):
        rows_datas = self.get_table_selected_rows_datas('paper_view_table')
        self.do_ip(rows_datas)

    def do_ip_for_all_item_order(self):
        rows_datas = self.get_table_all_rows_datas('paper_view_table')
        self.do_ip(rows_datas)

    def do_ip(self,rows_datas):
        self.model.make_and_insert_new_ips(rows_datas)
        self.set_paper_view_table_new_ips()
    # --------------------------
    def do_sp_for_selected_item_order(self):
        rows_datas = self.get_table_selected_rows_datas('paper_view_table')
        self.do_sp(rows_datas)
        
    def do_sp_for_all_item_order(self):
        rows_datas = self.get_table_all_rows_datas('paper_view_table')
        self.do_sp(rows_datas)

    def do_sp(self,rows_datas):
        self.model.make_and_insert_new_sps(rows_datas)
        self.set_work_view_table_contents() # 작업현황으로 이동
        self.view.show_this_view('work_view')
    
    # [테이블 세팅] -------------------------------------------------------------------------------------------
    # work view 테이블 세팅
    def set_work_view_table_contents(self):
        table_name = 'item_order'
        where_str = self.model.get_where_str('shipping_date',None) #납기일 이전 조건 추가 필요
        table_contents = self.model.select_table_with_wheres(table_name,[where_str])
        translated_table_contents = self.translate_eng_to_kor(table_name,table_contents)
        self.view.show_table(translated_table_contents,'work_view_table')        
    # --------------------------
    # paper view 테이블 세팅
    def set_paper_view_table_new_ips(self) -> None:
        table_name = 'item_order'
        where_str = self.model.get_where_str('sys_sp_id',None)
        table_contents = self.model.select_table_with_wheres(table_name,[where_str])
        translated_table_contents = self.translate_eng_to_kor(table_name,table_contents)
        self.view.show_table(translated_table_contents,'paper_view_table')
    # --------------------------
    # DB view 상단 테이블 선택 세팅
    def set_db_view_table_name_combo_box(self) -> None:
        tables = self.model.get_table_names()
        self.view.change_combo_box('db_view_table_names_combo_box',tables)

    # DB view 상단 속성 선택 세팅
    def set_db_view_table_col_combo_box(self) -> None:
        table_name = self.get_db_view_table_name()
        table_cols = self.model.get_table_cols(table_name)
        table_cols.insert(0,"all")
        self.view.change_combo_box('db_view_search_cols_combo_box',table_cols)

    # DB view 테이블 세팅 (전체)
    def set_db_view_table_all_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_contents = self.model.select_table_all(table_name)
        translated_table_contents = self.translate_eng_to_kor(table_name,table_contents)
        self.view.show_table(translated_table_contents)

    # DB view 테이블 세팅 (검색결과)
    def set_db_view_table_search_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_col = self.get_db_view_search_col()
        if table_col == "all":
            #여기에서 처리
            ...
        keyword = self.get_db_view_search_keyword()
        table_contents = self.model.select_table_like_keyword(table_name,table_col,keyword)
        translated_table_contents = self.translate_eng_to_kor(table_name,table_contents)
        self.view.show_table(translated_table_contents)

    # [위젯 값 읽기] -------------------------------------------------------------------------------------------
    # db view에서 선택중인 테이블 가져오기
    def get_db_view_table_name(self) -> str:
        return self.view.widgets['db_view_table_names_combo_box'].currentText().strip()

    # db view에서 선택중인 속성명 가져오기
    def get_db_view_search_col(self) -> str:
        return self.view.widgets['db_view_search_cols_combo_box'].currentText().strip()

    # db view에서 입력된 검색어 가져오기
    def get_db_view_search_keyword(self) -> str:
        return self.view.widgets['db_view_search_line_edit'].text().strip()

    # [view_table] ===========================================================================================
    def get_table_by_name(self,target_table:str) -> TablePlusWidget:
        return self.view.widgets[target_table]

    def get_table_checked_rows(self, target_table:str = 'db_view_table') -> list:
        return self.get_table_by_name(target_table).get_checked_rows()

    def get_table_all_rows(self, target_table:str = 'db_view_table') -> list:
        return self.get_table_by_name(target_table).get_all_rows()

    def get_table_cell_text(self,row,col, target_table:str = 'db_view_table') -> str:
        cell_item = self.get_table_by_name(target_table).get_cell_text((row,col))
        return cell_item if cell_item else 'NULL'

    def get_table_row_data(self, row, target_table:str = 'db_view_table')->dict:
        return self.get_table_by_name(target_table).get_row_data(row)

    def get_table_col_index(self, col_name, target_table:str = 'db_view_table')->int:
        return self.get_table_by_name(target_table).get_col_index(col_name)

    def get_table_selected_rows_datas(self,target_table:str = 'db_view_table')->list:
        return self.get_table_by_name(target_table).get_selected_rows_datas()

    def get_table_all_rows_datas(self,target_table:str = 'db_view_table')->list:
        return self.get_table_by_name(target_table).get_all_rows_datas()

    # [db_view DB 수정] ===========================================================================================
    # 선택항목 갱신
    def update_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_table_selected_rows_datas()
        translated_table_contents = self.translate_kor_to_eng(table_name,rows_datas)
        table_contents = self.model.update_table_and_select_updated(table_name,translated_table_contents)
        translated_table_contents = self.translate_eng_to_kor(table_name,table_contents)
        self.view.show_table(translated_table_contents)

    # 선택항목 삭제
    def delete_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_table_selected_rows_datas()
        translated_table_contents = self.translate_kor_to_eng(table_name,rows_datas)
        self.model.delete_table(table_name,translated_table_contents)
        self.set_db_view_table_all_contents()

    # 새 항목 입력
    def insert_dialog_data(self, table_name, dialog_table_cols):
        self.view.dialogs['db_view_insert'].close()      
        insert_data = self.get_insert_data_from_dialog()
        insert_data = self.translate_kor_to_eng_cols(dialog_table_cols,insert_data)
        self.model.insert_table(table_name,insert_data)
        self.set_db_view_table_all_contents()
    # [db_view 입력 대화창] ===========================================================================================
    # 입력창에서 라벨 : 값 쌍으로 가져오기
    def get_insert_data_from_dialog(self) -> dict:
        insert_data = {}
        for k in self.view.dialog_widgets:
            line_edit_text = self.view.dialog_widgets[k].text().strip()
            insert_data[k] = line_edit_text if line_edit_text else 'NULL'
        return insert_data

    # 입력창 생성
    def update_and_show_insert_dialog(self):
        table_name = self.get_db_view_table_name()
        # db에서 속성 읽기
        dialog_table_cols = self.model.get_table_cols_by_options(table_name,['except_sys','except_auto','except_insert'])
        # json에서 속성 값 도메인 읽기
        domain_raw_datas = self.model.db_spec.get(table_name,{}).get("domain",{})

        # 속성 도메인 처리
        def get_domains_from_dict(domain_data):
            table_name, col = next(iter(domain_data.items()), (None, None))
            domains = self.model.select_table_col_all(table_name,col)
            return list(set(domains))
        
        domain_datas = {}
        for k,v in domain_raw_datas.items():
            if isinstance(v,dict):
                domain_datas[k] = get_domains_from_dict(v)
            else:
                domain_datas[k] = v
        # --------------------------
        self.view.get_db_view_insert_dialog(table_name, dialog_table_cols,domain_datas)
        self.view.show_db_view_insert_dialog()
        self.view.widgets["db_view_insert_submit"].clicked.connect(lambda : self.insert_dialog_data(table_name, dialog_table_cols))


    def translate_eng_to_kor(self, table_name,table_contents):
        dialog_table_cols = self.model.get_table_cols_by_options(table_name,['except_sys'])
        translated_table_contents = [self.translate_eng_to_kor_cols(dialog_table_cols,x) for x in table_contents]
        return translated_table_contents

    def translate_kor_to_eng(self, table_name,table_contents):
        dialog_table_cols = self.model.get_table_cols_by_options(table_name,['except_sys'])
        translated_table_contents = [self.translate_kor_to_eng_cols(dialog_table_cols,x) for x in table_contents]
        return translated_table_contents

    # 입력항목 속성명 번역 {영:한},{한:값} -> {영:값}
    def translate_kor_to_eng_cols(self,cols,datas)->dict:
        result = {}
        for k, v in datas.items():
            eng = next((eng.strip() for eng, kor in cols.items() if kor == k), None)
            key = eng if eng else k
            result[key] = v
        return result

    # 입력항목 속성명 번역 {영:한},{영:값} -> {한:값}
    def translate_eng_to_kor_cols(self,cols,datas)->dict:
        result = {}
        for k, v in datas.items():
            kor = next((kor.strip() for eng, kor in cols.items() if eng == k), None)
            key = kor if kor else k
            result[key] = v
        return result

# ===========================================================================================
def main():
    app = QApplication([])
    app.setStyleSheet('*{font-family: Arial;font-size: 12pt;}')
    ctrl = Controller()
    ctrl.view.show()
    app.exec_()


if __name__ == "__main__":
    main()