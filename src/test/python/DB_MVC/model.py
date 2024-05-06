from db_interface import DBInterface
from igzg.utils import getConfig
from pprint import pprint

class Model:
    def __init__(self):
        self.dbi = DBInterface(*getConfig(['username','password','database','port']))


    def make_ip(self):
        ...
    # [table_info] ===========================================================================================
    def get_table_names(self):
        tables_raw = self.dbi.execute_query("SHOW TABLES;")
        return self.fatchall_data_to_list(tables_raw)

    def get_table_cols(self, table_name):
        cols_raw = self.dbi.execute_query(f"SHOW COLUMNS FROM {table_name};")
        return self.fatchall_data_to_list(cols_raw)
    # [select] ===========================================================================================
    def select_table_all(self,table_name):
        table_cols = self.get_table_cols(table_name)
        contents_raw = self.dbi.execute_query(f"SELECT * FROM {table_name};")
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)

    def select_table_like_keyword(self,table_name,table_col,keyword):
        keywords = ["'%"+k.strip().replace("'","\'")+"%'" for k in keyword.split(',')]
        where_str = ' AND '.join([ '`'+ table_col + '` LIKE ' + k for k in keywords])
        query = f"SELECT * FROM {table_name} WHERE {where_str};"
        table_cols = self.get_table_cols(table_name)
        contents_raw = self.dbi.execute_query(query)
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)    

    def select_table_with_wheres(self,table_name,filter:list):
        table_cols = self.get_table_cols(table_name)
        where = ' and '.join(filter)
        contents_raw = self.dbi.execute_query(f"SELECT * FROM {table_name} WHERE {where};")
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)
    # [insert] ===========================================================================================
    def insert_table(self,table_name,insert_data:dict={}):
        cols = ', '.join('`' + k + '`' for k in insert_data.keys())
        values = (', '.join("'" + v + "'" for v in insert_data.values())).replace("'NULL'","NULL")
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({values});"
        self.dbi.execute_query(query)
    # [delete] ===========================================================================================
    def delete_table(self,table_name,delete_datas=[{}]):
        querys, wheres = [], []
        for data in delete_datas:
            where_str = f"""`sys_id` = '{data['sys_id']}'"""
            wheres.append(where_str)
            querys.append(f"DELETE FROM {table_name} WHERE {where_str}; ")
        for query in querys:
            self.dbi.execute_query(query)        
    # [update] ===========================================================================================
    def update_table_with_return_wheres(self,table_name,update_datas=[{}]):
        querys, wheres = [], []

        for data in update_datas:
            sets = [f"`{k.strip()}` = '{data[k].strip()}'".replace("'NULL'","NULL") for k in data]
            sets_str = ' , '.join(sets)
            where_str = f"""`sys_id` = '{data['sys_id']}'"""
            wheres.append(where_str)
            querys.append(f"UPDATE {table_name} SET {sets_str} WHERE {where_str}; ")
        for query in querys:
            self.dbi.execute_query(query)
        return wheres

    def update_table_and_select_updated(self,table_name,update_datas=[{}]):
        wheres = self.update_table_with_return_wheres(table_name,update_datas)
        query = f"SELECT * FROM {table_name} WHERE {' OR '.join(wheres)};"
        contents_raw = self.dbi.execute_query(query)
        # --------------------------
        table_cols = self.get_table_cols(table_name)
        table_contents = self.fatchall_data_to_dict_list(contents_raw,table_cols)
        return table_contents
    # [] ===========================================================================================
    def fatchall_data_to_list(self, data_raw):
        return [item[0] for item in data_raw]

    def fatchall_data_to_dict_list(self,data_raw,table_cols):
        return [{table_cols[i]: data[i] if data[i] is not None else '' for i in range(len(table_cols))} for data in data_raw]
# ===========================================================================================

if __name__ == "__main__":
    m = Model()
    print(m.get_table_names())