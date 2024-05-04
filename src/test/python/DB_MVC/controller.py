from model import Model
from view import View
from PyQt5.QtWidgets import QApplication
# Controller
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

    # [view] ===========================================================================================
    def view_button_mapping(self) -> None:
        # db_view
        self.view.widgets['db_view_open'].clicked.connect(self.set_db_view_table_name_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_col_combo_box)
        self.view.widgets["db_view_table_names_submit"].clicked.connect(self.set_db_view_table_contents)


    # [view.db_view] -------------------------------------------------------------------------------------------
    def get_db_view_table_name(self) -> str:
        return self.view.get_combo_box_item('db_view_table_names_combo_box')

    def get_db_view_table_col(self) -> str:
        return self.view.get_combo_box_item('db_view_search_cols_combo_box')

    def set_db_view_table_name_combo_box(self) -> None:
        tables = self.get_table_names()
        self.view.change_combo_box('db_view_table_names_combo_box',tables)

    def set_db_view_table_col_combo_box(self) -> None:
        table_name = self.get_db_view_table_name()
        table_cols = self.get_table_cols(table_name)
        self.view.change_combo_box('db_view_search_cols_combo_box',table_cols)

    def set_db_view_table_contents(self) -> None:
        table_name = self.get_db_view_table_name()
        table_contents = self.get_table_contents(table_name)
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