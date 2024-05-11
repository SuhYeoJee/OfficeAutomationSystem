from db_interface import DBInterface
from igzg.utils import getConfig
from pprint import pprint

class Model:
    def __init__(self):
        self.dbi = DBInterface(*getConfig(['username','password','database','port']))


    def make_and_insert_new_ips(self, rows_datas):
        def get_ip_raw_datas(rows_datas):
            ip_raw_datas = {}
            for row_data in rows_datas:
                # where = f"`order_item_no` = '{row_data['order_item_no']}'"
                where = self.get_where_str('order_item_no',row_data)
                [item_order_data] = self.select_table_with_wheres('item_order',[where])

                where = f"`sys_id` = '{item_order_data['sys_item_id']}'"
                [item_data] = self.select_table_with_wheres('item',[where])

                group_name = item_data['group_name']
                if group_name not in ip_raw_datas.keys():
                    ip_raw_datas[group_name] = {'item_datas':[], 'item_order_datas':[]}
                ip_raw_datas[group_name]['item_datas'].append(item_data)
                ip_raw_datas[group_name]['item_order_datas'].append(item_order_data)
            return ip_raw_datas

        def get_ip_datas(ip_raw_datas):
            def add_or_update(target_dict, key, cnt):
                target_dict[key] = target_dict.get(key, 0)+ cnt
            # -------------------------------------------------------------------------------------------
            result = {}
            for group_name, raw_data in ip_raw_datas.items():
                result[group_name] = {'item':{}, 'seg': {}, 'shank': {}, 'sub': {}, 'data':{}}
                # --------------------------
                for item_order_datas in raw_data['item_order_datas']:
                    item_name = item_order_datas['item_name']
                    if item_name:
                        item_amount = int(item_order_datas.get('item_amount', 0))
                        add_or_update(result[group_name]['item'],item_name,item_amount)
                    # --------------------------
                    result[group_name]['data']['due_date'] = item_order_datas['due_date']
                    result[group_name]['data']['shank_memo1'] = item_order_datas['engrave']
                # --------------------------
                for item_datas in raw_data['item_datas']:
                    item_name = item_datas['name']
                    item_amount = result[group_name]['item'][item_name]
                    seg1_no = item_datas['seg1_no']
                    seg2_no = item_datas['seg2_no']
                    shank_name = item_datas['shank_name']
                    sub1_name = item_datas['sub1_name']
                    sub2_name = item_datas['sub2_name']
                    result[group_name]['data']['auto_ip_no3'] = item_datas['recent_ip']
                    result[group_name]['data']['shank_memo2'] = item_datas['mark']
                    result[group_name]['data']['welding1'] = item_datas['welding']
                    result[group_name]['data']['dressing1'] = item_datas['dressing']
                    result[group_name]['data']['paint1'] = item_datas['color']
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
        
        def get_new_ips(ip_datas):
            new_ips = []
            for group_name, group_data in ip_datas.items():
                new_ip = {"item_group_name": group_name}
                
                for key, items in group_data.items():
                    if key == 'data':
                        for idx, (k, val) in enumerate(items.items(), start=1):
                            new_ip[k] = val
                    else:
                        for idx, (name, amount) in enumerate(items.items(), start=1):
                            new_ip[f"{key}{idx}_{'no' if key == 'seg' else 'name'}"] = name
                            new_ip[f"{key}{idx}_amount"] = str(amount)
                new_ips.append(new_ip)
            return new_ips
        # ===========================================================================================

        ip_raw_datas = get_ip_raw_datas(rows_datas)
        ip_datas = get_ip_datas(ip_raw_datas)
        new_ips = get_new_ips(ip_datas)

        for new_ip in new_ips:
            new_ip = {x:new_ip[x] if new_ip[x] else 'NULL' for x in new_ip}
            self.insert_table('ip',new_ip)


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

    def select_table_with_wheres(self,table_name,filter:list,and_or='and' ):
        table_cols = self.get_table_cols(table_name)
        where = f' {and_or} '.join(filter)
        contents_raw = self.dbi.execute_query(f"SELECT * FROM {table_name} WHERE {where};")
        return self.fatchall_data_to_dict_list(contents_raw,table_cols)
    
    def select_table_current_1mins(self,table_name):
        from datetime import datetime, timedelta
        now = datetime.now()
        one_minute_ago = now - timedelta(minutes=60)
        where = f"sys_update_date BETWEEN '{one_minute_ago}' AND '{now}'"        
        return self.select_table_with_wheres(table_name,[where])

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
            # where_str = f"""`sys_id` = '{data['sys_id']}'"""
            where = self.get_where_str('sys_id',data)

            wheres.append(where)
            querys.append(f"DELETE FROM {table_name} WHERE {where}; ")
        for query in querys:
            self.dbi.execute_query(query)        
    # [update] ===========================================================================================
    def update_table_with_return_wheres(self,table_name,update_datas=[{}]):
        querys, wheres = [], []

        for data in update_datas:
            sets = [f"`{k.strip()}` = '{data[k].strip()}'".replace("'NULL'","NULL") for k in data]
            sets_str = ' , '.join(sets)
            where = self.get_where_str('sys_id',data)
            wheres.append(where)
            querys.append(f"UPDATE {table_name} SET {sets_str} WHERE {where}; ")
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
    def get_where_str(self,col,data,operation = '='):
        if (data == None) or (data == {}):
            operation = 'IS' if operation == '=' else operation
            operation = 'IS NOT' if operation == '!=' else operation                
            where = f"""`{col}` {operation} NULL"""
        else:
            where = f"""`{col}` {operation} '{data[col]}'"""
        return where

    def fatchall_data_to_list(self, data_raw):
        return [item[0] for item in data_raw]

    def fatchall_data_to_dict_list(self,data_raw,table_cols):
        return [{table_cols[i]: data[i] if data[i] is not None else '' for i in range(len(table_cols))} for data in data_raw]
# ===========================================================================================

if __name__ == "__main__":
    m = Model()
    print(m.get_table_names())