from model import Model
from view import View
from PyQt5.QtWidgets import QApplication

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
        ...
        # --------------------------
        rows_datas = self.get_table_selected_rows_datas('paper_view_table')

        # ip_raw_datas = {
        #     'group_name':{
        #         'item_datas':[item_data], 
        #         'item_order_datas':[item_order_data]}}
        ip_raw_datas = {}
        for row_data in rows_datas:
            where = f"`order_item_no` = '{row_data['order_item_no']}'"
            [item_order_data] = self.model.select_table_with_wheres('item_order',[where])

            where = f"`sys_id` = '{item_order_data['sys_item_id']}'"
            [item_data] = self.model.select_table_with_wheres('item',[where])

            group_name = item_data['group_name']
            if group_name not in ip_raw_datas.keys():
                ip_raw_datas[group_name] = {'item_datas':[], 'item_order_datas':[]}
            ip_raw_datas[group_name]['item_datas'].append(item_data)
            ip_raw_datas[group_name]['item_order_datas'].append(item_order_data)

        def transform_data(ip_raw_datas):
            def add_or_update(target_dict, key, cnt):
                target_dict[key] = target_dict.get(key, 0)+ cnt
            # -------------------------------------------------------------------------------------------
            result = {}
            for group_name, raw_data in ip_raw_datas.items():
                result[group_name] = {'item':{}, 'seg': {}, 'shank': {}, 'sub': {}}
                # --------------------------
                for item_order_datas in raw_data['item_order_datas']:
                    item_name = item_order_datas['item_name']
                    if item_name:
                        item_amount = int(item_order_datas.get('item_amount', 0))
                        add_or_update(result[group_name]['item'],item_name,item_amount)
                # --------------------------
                for item_datas in raw_data['item_datas']:
                    item_name = item_datas['name']
                    item_amount = result[group_name]['item'][item_name]
                    seg1_no = item_datas['seg1_no']
                    seg2_no = item_datas['seg2_no']
                    shank_name = item_datas['shank_name']
                    sub1_name = item_datas['sub1_name']
                    sub2_name = item_datas['sub2_name']
                    if seg1_no:
                        seg1_amount = int(item_datas.get('seg1_amount', 0))*item_amount
                        add_or_update(result[group_name]['seg'],seg1_no,seg1_amount)
                    if seg2_no:
                        seg2_amount = int(item_datas.get('seg2_amount', 0))*item_amount
                        add_or_update(result[group_name]['seg'],seg2_no,seg2_amount)                        
                    if shank_name:
                        shank_amount = int(item_datas.get('shank_amount', 0))*item_amount
                        add_or_update(result[group_name]['shank'],shank_name,shank_amount)                             
                    if sub1_name:
                        sub1_amount = int(item_datas.get('sub1_amount', 0))*item_amount
                        add_or_update(result[group_name]['sub'],sub1_name,sub1_amount)                             
                    if sub2_name:
                        sub2_amount = int(item_datas.get('sub2_amount', 0))*item_amount
                        add_or_update(result[group_name]['sub'],sub2_name,sub2_amount)      
            return result

        # ===========================================================================================
        ip_datas = transform_data(ip_raw_datas)
        # {'TEST': {'item': {'TEST_ITEM': 1, 'TEST_ITEM2': 2},
        #         'seg': {'SQ0000': 4, 'SQ0001': 2, 'SQ9999': 1},
        #         'shank': {'3"DISC-CCW': 1, '3"DISC-CW': 2},
        #         'sub': {'PCD10': 2, 'PCD12': 1}}}
        from pprint import pprint
        pprint(ip_datas)


        # new_ip = {
        #     "ip_no" : '',
        #     "ip_no1" : '',
        #     "ip_no2" : '',
        #     "ip_no3" : '',
        #     "date" : '',
        #     "due_date" : '',
        #     "image" : '',
        #     "paint1" : '',
        #     "item_group_name" : '',
        #         "item1_name" : '',
        #         "item1_amount" : '',
        #         "item2_name" : '',
        #         "item2_amount" : '',
        #         "item3_name" : '',
        #         "item3_amount" : '',
        #         "item4_name" : '',
        #         "item4_amount" : '',
        #             "seg1_no" : '',
        #             "seg1_amount" : '',
        #             "seg2_no" : '',
        #             "seg2_amount" : '',
        #                 "shank1_name" : '',
        #                 "shank1_amount" : '',
        #                 "shank2_name" : '',
        #                 "shank2_amount" : '',
        #                 "shank3_name" : '',
        #                 "shank3_amount" : '',
        #                 "shank4_name" : '',
        #                 "shank4_amount" : '',
        #                     "sub1_name" : '',
        #                     "sub1_amount" : '',
        #                     "sub2_name" : '',
        #                     "sub2_amount" : '',
        #                     "sub3_name" : '',
        #                     "sub3_amount" : '',
        #                     "sub4_name" : '',
        #                     "sub4_amount" : '',
        # }

        # new_ip = {x:new_ip[x] if new_ip[x] else 'NULL' for x in new_ip}

        # self.model.insert_table('ip',new_ip)


    # [view] ===========================================================================================
    def view_button_mapping(self) -> None:
        self.db_view_button_mapping()
        # paper_view
        self.view.widgets['paper_view_open'].clicked.connect(self.set_paper_view_table_all_contents)
        self.view.widgets['paper_view_select_submit'].clicked.connect(self.t)
    
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
    def get_table_checked_rows(self, target_table:str = 'db_view_table') -> list:
        checked_rows = []
        for row in range(self.view.widgets[target_table].rowCount()):
            check_box = self.view.widgets[target_table].cellWidget(row, 0)
            if check_box and check_box.isChecked():
                checked_rows.append(row)
        else:
            if 0 in checked_rows: # 전체선택
                checked_rows = [row for row in range(self.view.widgets[target_table].rowCount())]
        return checked_rows

    def get_table_cell_text(self,row,col, target_table:str = 'db_view_table') -> str:
        cell_item = self.view.widgets[target_table].item(row, col)
        if cell_item: 
            return cell_item.text()
        else:
            return 'NULL'

    def get_table_row_data(self, row, target_table:str = 'db_view_table'):
        row_data = {}
        for col in range(1, self.view.widgets[target_table].columnCount()):
            cell_text = self.get_table_cell_text(row,col,target_table).strip()
            cell_text = cell_text if cell_text else 'NULL'
            row_data[self.get_table_cell_text(0,col,target_table).strip()] = cell_text
        return row_data

    def get_table_selected_rows_datas(self,target_table:str = 'db_view_table'):
        selected_rows = self.get_table_checked_rows(target_table)
        row_datas = []
        for row in selected_rows:
            row_datas.append(self.get_table_row_data(row,target_table))
        return row_datas

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
    def set_paper_view_table_all_contents(self) -> None:
        table_name = 'item_order'
        table_contents = self.model.select_table_with_wheres(table_name,["`sys_ip_id` is NULL"])
        self.view.show_table(table_contents,'paper_view_table')

# ===========================================================================================

if __name__ == "__main__":
    app = QApplication([])
    ctrl = Controller()
    ctrl.view.show()
    app.exec_()
