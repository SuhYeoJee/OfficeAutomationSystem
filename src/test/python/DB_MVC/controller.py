from model import Model
from view import View
from PyQt5.QtWidgets import QApplication

if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
from src.module.table_plus_widget import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view_button_mapping()

    # [table] ===========================================================================================
    def db_view_do_table_update(self,table_name,update_datas=[{}]):
        table_contents = self.model.update_table_and_select_updated(table_name,update_datas)
        self.view.show_table(table_contents)

    def db_view_do_table_delete(self,table_name,delete_datas=[{}]):
        self.model.delete_table(table_name,delete_datas)
        self.set_db_view_table_all_contents()

    def db_view_do_table_insert(self,table_name,insert_data={}):
        self.model.insert_table(table_name,insert_data)
        self.set_db_view_table_all_contents()


    # [test] ===========================================================================================

    def t(self):
        print('t')
    

    def on_ip_no_cell_clicked(self, row, col):
        if col == self.get_table_col_index('ip_no','paper_view_table'):
            ip_no = self.get_table_by_name('paper_view_table').get_cell_text((row,col))
            ip_data = self.model.select_table_with_wheres('ip',[f"`auto_ip_no` = '{ip_no}'"])[0]
            self.view.get_ip_viewer(ip_data)
            self.view.dialogs['ip_viewer'].widgets["ip_viewer_submit"].clicked.connect(lambda: self.ip_viewer_update_ip(ip_data['sys_id']))
            self.view.dialogs['ip_viewer'].widgets["ip_viewer_image_export"].clicked.connect(self.t)
            self.view.dialogs['ip_viewer'].widgets["ip_viewer_xlsx_export"].clicked.connect(self.t)

    # [view] ===========================================================================================
    def view_button_mapping(self) -> None:
        self.view.widgets['paper_view_table'].cellClicked.connect(self.on_ip_no_cell_clicked) # ip 뷰어 연결

        self.db_view_button_mapping()
        # paper_view
        self.view.widgets['paper_view_open'].clicked.connect(self.set_paper_view_table_first_contents)
        self.view.widgets['paper_view_select_submit'].clicked.connect(self.do_ip_for_selected_item_order)
        self.view.widgets['paper_view_all_submit'].clicked.connect(self.do_ip_for_all_item_order)
    
    def db_view_button_mapping(self) -> None:
        self.view.widgets['db_view_open'].clicked.connect(self.set_db_view_table_name_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_col_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_all_contents)
        self.view.widgets["db_view_search_submit"].clicked.connect(self.set_db_view_table_search_contents)
        self.view.widgets["db_view_control_update"].clicked.connect(self.update_selected_rows)
        self.view.widgets["db_view_control_delete"].clicked.connect(self.delete_selected_rows)
        self.view.widgets["db_view_control_insert"].clicked.connect(self.update_and_show_insert_dialog)
        self.view.widgets["db_view_insert_submit"].clicked.connect(self.insert_dialog_data)

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

    def get_table_row_data(self, row, target_table:str = 'db_view_table'):
        return self.get_table_by_name(target_table).get_row_data(row)

    def get_table_col_index(self, col_name, target_table:str = 'db_view_table'):
        return self.get_table_by_name(target_table).get_col_index(col_name)

    def get_table_selected_rows_datas(self,target_table:str = 'db_view_table'):
        return self.get_table_by_name(target_table).get_selected_rows_datas()

    def get_table_all_rows_datas(self,target_table:str = 'db_view_table'):
        return self.get_table_by_name(target_table).get_all_rows_datas()

    # [view.db_view] -------------------------------------------------------------------------------------------
    def get_db_view_table_name(self) -> str:
        return self.view.widgets['db_view_table_names_combo_box'].currentText().strip()

    def get_db_view_search_col(self) -> str:
        return self.view.widgets['db_view_search_cols_combo_box'].currentText().strip()

    def get_db_view_search_keyword(self) -> str:
        return self.view.widgets['db_view_search_line_edit'].text().strip()
    
    #insert 다이얼로그에서 라벨 : 값 쌍으로 가져오기
    def get_insert_data_from_dialog(self) -> dict:
        insert_data = {}
        for k in self.view.dialog_widgets:
            line_edit_text = self.view.dialog_widgets[k].text().strip()
            insert_data[k] = line_edit_text if line_edit_text else 'NULL'
        return insert_data

    # -------------------------------------------------------------------------------------------

    def update_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_table_selected_rows_datas()
        self.db_view_do_table_update(table_name, rows_datas)

    def delete_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_table_selected_rows_datas()
        self.db_view_do_table_delete(table_name, rows_datas)

    def update_and_show_insert_dialog(self):
        table_name = self.get_db_view_table_name()
        table_cols = self.model.get_table_cols(table_name)
        self.view.get_db_view_insert_dialog(table_cols)
        self.view.show_db_view_insert_dialog()
        self.view.widgets["db_view_insert_submit"].clicked.connect(self.insert_dialog_data)

    def insert_dialog_data(self):
        table_name = self.get_db_view_table_name()
        self.view.dialogs['db_view_insert'].close()
        insert_data = self.get_insert_data_from_dialog()
        self.db_view_do_table_insert(table_name, insert_data)

    # --------------------------
    def set_db_view_table_name_combo_box(self) -> None:
        tables = self.model.get_table_names()
        self.view.change_combo_box('db_view_table_names_combo_box',tables)

    def set_db_view_table_col_combo_box(self) -> None:
        table_name = self.get_db_view_table_name()
        table_cols = self.model.get_table_cols(table_name)
        self.view.change_combo_box('db_view_search_cols_combo_box',table_cols)

    def set_db_view_table_all_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_contents = self.model.select_table_all(table_name)
        self.view.show_table(table_contents)

    def set_db_view_table_search_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_col = self.get_db_view_search_col()
        keyword = self.get_db_view_search_keyword()
        table_contents = self.model.select_table_like_keyword(table_name,table_col,keyword)
        self.view.show_table(table_contents)

    # [view.paper_view] -------------------------------------------------------------------------------------------
    def set_paper_view_table_first_contents(self) -> None:
        table_name = 'item_order'
        where_str = self.model.get_where_str('sys_ip_id',None)
        table_contents = self.model.select_table_with_wheres(table_name,[where_str])
        self.view.show_table(table_contents,'paper_view_table')

    def do_ip_for_selected_item_order(self):
        rows_datas = self.get_table_selected_rows_datas('paper_view_table')
        self.model.make_and_insert_new_ips(rows_datas)
        self.set_paper_view_table_new_ips()

    def do_ip_for_all_item_order(self):
        rows_datas = self.get_table_all_rows_datas('paper_view_table')
        self.model.make_and_insert_new_ips(rows_datas)
        self.set_paper_view_table_new_ips()

    def set_paper_view_table_new_ips(self):
        table_contents = self.model.select_table_current_1mins('item_order')
        self.view.show_table(table_contents,'paper_view_table')
        # self.view.widgets['paper_view_table'].cellClicked.connect(self.on_ip_no_cell_clicked) # ip 뷰어 연결

    def ip_viewer_update_ip(self,sys_id):
        ip_data = self.view.dialogs['ip_viewer'].widgets["ip_viewer_table"].get_labeled_data()
        ip_data['sys_id'] =  sys_id
        self.model.update_table_and_select_updated('ip',[ip_data])


# ===========================================================================================

if __name__ == "__main__":
    app = QApplication([])
    ctrl = Controller()
    ctrl.view.show()
    app.exec_()



