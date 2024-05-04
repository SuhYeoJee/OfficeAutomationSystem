from model import Model
from view import View
from PyQt5.QtWidgets import QApplication

PK = 'sys_id'

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view_button_mapping()

    # [model.dbi] ===========================================================================================
    def get_table_names(self):
        tables_raw = self.model.dbi.execute_query("SHOW TABLES;")
        return self.fatchall_data_to_list(tables_raw)

    def get_table_cols(self, table_name):
        cols_raw = self.model.dbi.execute_query(f"SHOW COLUMNS FROM {table_name};")
        return self.fatchall_data_to_list(cols_raw)

    def get_table_contents(self,table_name):
        table_cols = self.get_table_cols(table_name)
        contents_raw = self.model.dbi.execute_query(f"SELECT * FROM {table_name};")
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)

    def get_table_search(self,table_name,table_col,keyword):
        keywords = ["'%"+k.strip().replace("'","\'")+"%'" for k in keyword.split(',')]
        where_str = ' AND '.join([ '`'+ table_col + '` LIKE ' + k for k in keywords])
        query = f"SELECT * FROM {table_name} WHERE {where_str};"
        table_cols = self.get_table_cols(table_name)
        contents_raw = self.model.dbi.execute_query(query)
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)
    
    # -------------------------------------------------------------------------------------------

    def do_table_update(self,table_name,update_datas):
        querys, wheres = [], []

        for data in update_datas:
            sets = [f"`{k.strip()}` = '{data[k].strip()}'".replace("'NULL'","NULL") for k in data]
            sets_str = ' , '.join(sets)
            where_str = f"""{PK} = '{data[PK]}'"""
            wheres.append(where_str)
            querys.append(f"UPDATE {table_name} SET {sets_str} WHERE {where_str}; ")
        for query in querys:
            self.model.dbi.execute_query(query)

        # 수정된 항목만 표시하기
        query = f"SELECT * FROM {table_name} WHERE {' OR '.join(wheres)};"
        table_cols = self.get_table_cols(table_name)
        contents_raw = self.model.dbi.execute_query(query)
        table_contents = self.fatchall_data_to_dict_list(contents_raw,table_cols)
        self.view.show_table(table_contents)

    def do_table_delete(self,table_name,update_datas):
        querys, wheres = [], []

        for data in update_datas:
            where_str = f"""{PK} = '{data[PK]}'"""
            wheres.append(where_str)
            querys.append(f"DELETE FROM {table_name} WHERE {where_str}; ")
        for query in querys:
            self.model.dbi.execute_query(query)        
        self.model.dbi.execute_query(query)
        self.set_db_view_table_all_contents()

    def do_table_insert(self,table_name,insert_data:dict):
        cols = ', '.join('`' + k + '`' for k in insert_data.keys())
        values = (', '.join("'" + v + "'" for v in insert_data.values())).replace("'NULL'","NULL")
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({values});"
        self.model.dbi.execute_query(query)
        self.set_db_view_table_all_contents()


    # [view] ===========================================================================================
    def view_button_mapping(self) -> None:
        # db_view
        self.view.widgets['db_view_open'].clicked.connect(self.set_db_view_table_name_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_col_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_all_contents)
        self.view.widgets["db_view_search_submit"].clicked.connect(self.set_db_view_table_search_contents)
        self.view.widgets["db_view_control_update"].clicked.connect(self.update_selected_rows)
        self.view.widgets["db_view_control_delete"].clicked.connect(self.delete_selected_rows)
        self.view.widgets["db_view_control_insert"].clicked.connect(self.update_and_show_insert_dialog)
        self.view.widgets["db_view_insert_submit"].clicked.connect(self.insert_insert_dialog_data)

    # [view.db_view] -------------------------------------------------------------------------------------------
    def get_db_view_table_name(self) -> str:
        return self.view.widgets['db_view_table_names_combo_box'].currentText().strip()

    def get_db_view_search_col(self) -> str:
        return self.view.widgets['db_view_search_cols_combo_box'].currentText().strip()

    def get_db_view_search_keyword(self) -> str:
        return self.view.widgets['db_view_search_line_edit'].text().strip()
    
    def get_db_view_checked_rows(self) -> list:
        checked_rows = []
        for row in range(self.view.widgets['table'].rowCount()):
            check_box = self.view.widgets['table'].cellWidget(row, 0)
            if check_box and check_box.isChecked():
                checked_rows.append(row)
        else:
            if 0 in checked_rows: # 전체선택
                checked_rows = [row for row in range(self.view.widgets['table'].rowCount())]
        return checked_rows
    
    def get_table_cell_text(self,row,col) -> str:
        cell_item = self.view.widgets['table'].item(row, col)
        if cell_item: 
            return cell_item.text()
        else:
            return 'NULL'

    def get_db_view_row_data(self, row):
        row_data = {}
        for col in range(1, self.view.widgets['table'].columnCount()):
            row_data[self.get_table_cell_text(0,col)] = self.get_table_cell_text(row,col)
        return row_data

    def get_db_view_selected_rows_datas(self):
        selected_rows = self.get_db_view_checked_rows()
        row_datas = []
        for row in selected_rows:
            row_datas.append(self.get_db_view_row_data(row))
        return row_datas

    #insert 다이얼로그에서 라벨 : 값 쌍으로 가져오기
    def get_insert_data_from_dialog(self) -> dict:
        insert_data = {}
        for k in self.view.dialog_widgets:
            value = self.view.dialog_widgets[k].text().strip()
            insert_data[k] = value if value else 'NULL'
        return insert_data

    # -------------------------------------------------------------------------------------------

    def update_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_db_view_selected_rows_datas()
        self.do_table_update(table_name, rows_datas)

    def delete_selected_rows(self):
        table_name = self.get_db_view_table_name()
        rows_datas = self.get_db_view_selected_rows_datas()
        self.do_table_delete(table_name, rows_datas)

    def update_and_show_insert_dialog(self):
        table_name = self.get_db_view_table_name()
        table_cols = self.get_table_cols(table_name)
        self.view.get_db_view_insert_dialog(table_cols)
        self.view.show_db_view_insert_dialog()
        self.view.widgets["db_view_insert_submit"].clicked.connect(self.insert_insert_dialog_data)

    def insert_insert_dialog_data(self):
        table_name = self.get_db_view_table_name()
        self.view.dialogs['db_view_insert'].close()
        insert_data = self.get_insert_data_from_dialog()
        self.do_table_insert(table_name, insert_data)

    # --------------------------
    def set_db_view_table_name_combo_box(self) -> None:
        tables = self.get_table_names()
        self.view.change_combo_box('db_view_table_names_combo_box',tables)

    def set_db_view_table_col_combo_box(self) -> None:
        table_name = self.get_db_view_table_name()
        table_cols = self.get_table_cols(table_name)
        self.view.change_combo_box('db_view_search_cols_combo_box',table_cols)

    def set_db_view_table_all_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_contents = self.get_table_contents(table_name)
        self.view.show_table(table_contents)

    def set_db_view_table_search_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_col = self.get_db_view_search_col()
        keyword = self.get_db_view_search_keyword()
        table_contents = self.get_table_search(table_name,table_col,keyword)
        self.view.show_table(table_contents)

    # ===========================================================================================

    def fatchall_data_to_list(self, data_raw):
        return [item[0] for item in data_raw]
    
    def fatchall_data_to_dict_list(self,data_raw,table_cols):
        return [{table_cols[i]: data[i] if data[i] is not None else '' for i in range(len(table_cols))} for data in data_raw]

# ===========================================================================================

if __name__ == "__main__":
    app = QApplication([])
    ctrl = Controller()
    ctrl.view.show()
    app.exec_()