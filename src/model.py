if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
# -------------------------------------------------------------------------------------------
from src.module.db_interface import DBInterface
from src.sp_model import SPModel
# --------------------------
from pprint import pprint
import json
# -------------------------------------------------------------------------------------------

class Model:
    def __init__(self):
        self.dbi = DBInterface()
        self.spm = SPModel()
        with open("./doc/DB_spec.json", 'r', encoding='utf-8') as file:
            self.db_spec = json.load(file)
    # ===========================================================================================
    # sp 생성, 삽입
    def make_and_insert_new_sps(self, rows_datas):
        def get_sp_raw_datas():
            sp_group_datas = {} # 전체 수주 정보
            sp_raw_datas = {'item_datas':[],'seg_datas':[],'bond_datas':[],'powder_datas':[]} # 아이템, 세그먼트, 본드, 분말 정보
            sp_raw_datas['powder_datas'] += self.select_table_all('powder')

            for row_data in rows_datas:
                where = self.get_where_str('order_item_no',row_data) # 전체 수주 정보
                [item_order_data] = self.select_table_with_wheres('item_order',[where])

                if item_order_data['sys_ip_id']: # ip_no 가져오기
                    where = f"`sys_id` = '{item_order_data['sys_ip_id']}'"
                    [ip_data] = self.select_table_with_wheres('ip',[where])
                    ip_no = ip_data.get('ip_no','')
                else:
                    ip_no = ''

                where = f"`sys_id` = '{item_order_data['sys_item_id']}'"
                [item_data] = self.select_table_with_wheres('item',[where])

                where = f"`sys_id` = '{item_data['sys_seg1_id']}'"
                [seg1_data] = self.select_table_with_wheres('segment',[where])
                where = f"`sys_id` = '{seg1_data['sys_bond_id']}'"
                [bond1_raw_data] = self.select_table_with_wheres('bond',[where])
                bond1_data = {k: v for k, v in bond1_raw_data.items() if v != ''}

                if item_data['sys_seg2_id']:
                    where = f"`sys_id` = '{item_data['sys_seg2_id']}'"
                    [seg2_data] = self.select_table_with_wheres('segment',[where]) 
                    where = f"`sys_id` = '{seg2_data['sys_bond_id']}'"
                    [bond2_raw_data] = self.select_table_with_wheres('bond',[where])
                    bond2_data = {k: v for k, v in bond2_raw_data.items() if v != ''}
                else:
                    seg2_data = {}
                    bond2_data = {}
                sp_raw_datas['item_datas'].append(item_data)
                sp_raw_datas['seg_datas'].append(seg1_data)
                sp_raw_datas['seg_datas'].append(seg2_data)
                sp_raw_datas['bond_datas'].append(bond1_data)
                sp_raw_datas['bond_datas'].append(bond2_data)
                # --------------------------
                if ip_no not in sp_group_datas.keys(): # 수주 정보를 ip_no로 묶음
                    sp_group_datas[ip_no] = {'item_order_datas':[]}
                sp_group_datas[ip_no]['item_order_datas'].append(item_order_data)
            return sp_group_datas,sp_raw_datas
        # ===========================================================================================
        sp_group_datas,sp_raw_datas = get_sp_raw_datas()
        sp_datas = self.get_sp_datas(sp_group_datas,sp_raw_datas)
        new_sps = self.get_new_sps(sp_datas,sp_raw_datas)

        for new_sp in new_sps:
            new_sp = {k:v if v else 'NULL' for k,v in new_sp.items() if v != ''} # 값 없는 항목 NULL 처리
            # 이거 지금 빈 문자열은 아예 항목을 제거하고 None값은 NULL 로 치환하는건데 검토 필요
            self.insert_table('sp',new_sp)

        return new_sps

    # ip 생성, 삽입
    def make_and_insert_new_ips(self, rows_datas):
        def get_ip_raw_datas():
            ip_group_datas = {} # 전체 수주 정보
            ip_raw_datas = {'item_datas':[]} # 아이템

            ip_group_datas = {}
            for row_data in rows_datas:
                # where = f"`order_item_no` = '{row_data['order_item_no']}'"
                where = self.get_where_str('order_item_no',row_data)
                [item_order_data] = self.select_table_with_wheres('item_order',[where])

                where = f"`sys_id` = '{item_order_data['sys_item_id']}'"
                [item_data] = self.select_table_with_wheres('item',[where])

                group_name = item_data['group_name']
                if group_name not in ip_group_datas.keys():
                    ip_group_datas[group_name] = {'item_order_datas':[]}
                ip_group_datas[group_name]['item_order_datas'].append(item_order_data)
                ip_raw_datas['item_datas'].append(item_data)
            return ip_group_datas, ip_raw_datas

        def get_ip_datas():
            def add_or_update(target_dict, key, cnt):
                target_dict[key] = target_dict.get(key, 0)+ cnt
            # -------------------------------------------------------------------------------------------
            ip_datas = {}
            for group_name, raw_data in ip_group_datas.items():
                ip_datas[group_name] = {'item':{}, 'seg': {}, 'shank': {}, 'sub': {}, 'data':{}}
                # --------------------------
                for item_order_datas in raw_data['item_order_datas']:
                    item_name = item_order_datas['item_name']
                    if item_name:
                        item_amount = int(item_order_datas.get('item_amount', 0))
                        add_or_update(ip_datas[group_name]['item'],item_name,item_amount) # 아이템 수량 합산
                    # --------------------------
                    ip_datas[group_name]['data']['due_date'] = item_order_datas['due_date']
                    ip_datas[group_name]['data']['shank_memo1'] = item_order_datas['engrave']
                # --------------------------
                for item_datas in ip_raw_datas['item_datas']:
                    item_name = item_datas['product_name']
                    item_amount = ip_datas[group_name]['item'][item_name]
                    seg1_no = item_datas['seg1_no']
                    seg2_no = item_datas['seg2_no']
                    shank_name = item_datas['shank_name']
                    sub1_name = item_datas['sub1_name']
                    sub2_name = item_datas['sub2_name']
                    ip_datas[group_name]['data']['shank_memo2'] = item_datas['mark']
                    ip_datas[group_name]['data']['welding1'] = item_datas['welding']
                    ip_datas[group_name]['data']['dressing1'] = item_datas['dressing']
                    ip_datas[group_name]['data']['paint1'] = item_datas['color']
                    if seg1_no:
                        seg1_amount = int(item_datas.get('seg1_amount', 0))*item_amount
                        add_or_update(ip_datas[group_name]['seg'],seg1_no,seg1_amount)
                    if seg2_no:
                        seg2_amount = int(item_datas.get('seg2_amount', 0))*item_amount
                        add_or_update(ip_datas[group_name]['seg'],seg2_no,seg2_amount)                        
                    if shank_name:
                        shank_amount = int(item_datas.get('shank_amount', 0))*item_amount
                        add_or_update(ip_datas[group_name]['shank'],shank_name,shank_amount)                             
                    if sub1_name:
                        sub1_amount = int(item_datas.get('sub1_amount', 0))*item_amount
                        add_or_update(ip_datas[group_name]['sub'],sub1_name,sub1_amount)                             
                    if sub2_name:
                        sub2_amount = int(item_datas.get('sub2_amount', 0))*item_amount
                        add_or_update(ip_datas[group_name]['sub'],sub2_name,sub2_amount)      
            return ip_datas
        
        def get_new_ips():
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

        ip_group_datas, ip_raw_datas = get_ip_raw_datas()
        ip_datas = get_ip_datas()
        new_ips = get_new_ips()

        for new_ip in new_ips:
            new_ip = {x:new_ip[x] if new_ip[x] else 'NULL' for x in new_ip}
            self.insert_table('ip',new_ip)

        return new_ips


    # [DB] ===========================================================================================
    def get_table_names(self)->list:
        tables = self.dbi.execute_query("SELECT name FROM sqlite_master WHERE type='table';")
        return self.data_to_list(tables)
    
    def get_table_cols(self, table_name)->list:
        columns = self.dbi.execute_query(f"PRAGMA table_info({table_name});")
        return self.data_to_list(columns,1)
    
    # [JSON] col 값을 json 옵션으로 필터링
    def get_table_cols_by_options(self,table_name,options=["except_sys"]):
        table_cols = self.get_table_cols(table_name)
        table_options = self.db_spec.get(table_name,{})

        if "except_sys" in options:
            table_cols = [x for x in table_cols if x not in table_options.get("sys",[])]
        if "except_auto" in options:
            table_cols = [x for x in table_cols if x not in table_options.get("auto",[])]
        if "except_insert" in options:
            table_cols = [x for x in table_cols if x not in table_options.get("except_insert",[])]
        
        result = {}
        for c in table_cols:
            kor_c = table_options['kor'].get(c,'')
            kor_c = kor_c if kor_c else c
            result[c] = kor_c
        
        return result
    
    # [select] -------------------------------------------------------------------------------------------
    def select_table_all(self, table_name)->list:
        rows = self.dbi.execute_query(f"SELECT * FROM {table_name};")
        cols = self.get_table_cols(table_name)
        return self.data_to_dict_list(rows,cols)

    def select_table_col_all(self,table_name,col):
        rows = self.dbi.execute_query(f"SELECT {col} FROM {table_name};")
        return self.data_to_list(rows)

    def select_table_like_keyword(self,table_name,table_col,keyword):
        keywords = ["'%"+k.strip().replace("'","\'")+"%'" for k in keyword.split(',')]
        table_cols = self.get_table_cols(table_name)
        if table_col == "all":
            table_col = ' || '.join([f"COALESCE(`{x}`, '')" for x in table_cols])
        else:
            table_col = f"`{table_col}`"
        where_str = ' AND '.join([ table_col + ' LIKE ' + k for k in keywords])
        query = f"SELECT * FROM {table_name} WHERE {where_str};"
        contents_raw = self.dbi.execute_query(query)
        return self.data_to_dict_list(contents_raw,table_cols)    

    def select_table_with_wheres(self,table_name,filter:list,and_or='and' ):
        table_cols = self.get_table_cols(table_name)
        where = f' {and_or} '.join(filter)
        contents_raw = self.dbi.execute_query(f"SELECT * FROM {table_name} WHERE {where};")
        return self.data_to_dict_list(contents_raw,table_cols)
    # [insert] -------------------------------------------------------------------------------------------
    def insert_table(self,table_name,insert_data:dict={}):
        cols = ', '.join('`' + k + '`' for k in insert_data.keys())
        values = (', '.join("'" + v + "'" for v in insert_data.values())).replace("'NULL'","NULL")
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({values});"
        return self.dbi.execute_query(query)    #cnt
    # [delete] -------------------------------------------------------------------------------------------
    def delete_table(self,table_name,delete_datas=[{}]):
        querys, wheres = [], []
        for data in delete_datas:
            where = self.get_where_str('sys_id',data)
            wheres.append(where)
            querys.append(f"DELETE FROM {table_name} WHERE {where}; ")
        for query in querys:
            self.dbi.execute_query(query)    
    # [update] -------------------------------------------------------------------------------------------
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
        table_contents = self.data_to_dict_list(contents_raw,table_cols)
        return table_contents
    
    # -------------------------------------------------------------------------------------------
    def get_where_str(self,col,data,operation = '='):
        if (data == None) or (data == {}):
            operation = 'IS' if operation == '=' else operation
            operation = 'IS NOT' if operation == '!=' else operation                
            where = f"""`{col}` {operation} NULL"""
        else:
            where = f"""`{col}` {operation} '{data[col]}'"""
        return where

    def data_to_dict_list(self,rows,cols)->list:
        return [{cols[idx]: value if value is not None else ''  for idx, value in enumerate(row)} for row in rows]
    
    def data_to_list(self, items, idx:int=0)->list:
        return [item[idx] for item in items]    
    # ===========================================================================================
if __name__ == "__main__":
    m = Model()
    # r = m.make_and_insert_new_sps(get_order_rows())

    # print(m.get_table_names())
    print(m.get_table_cols('sp'))
    # print(m.select_table_all('test'))
    # print(m.insert_table('test',{'name':'Sam'}))
    # print(m.select_table_all('test'))
    # print(m.update_table_with_return_wheres('test',[{'id': '4', 'name': 'SamSam'}]))
    # print(m.select_table_all('test'))
    # print(m.update_table_and_select_updated('test',[{'id': '4', 'name': 'SamSamSam'}]))
    # print(m.delete_table('test',[{'id': '4', 'name': 'Sam'}]))
    # print(m.select_table_all('test'))


