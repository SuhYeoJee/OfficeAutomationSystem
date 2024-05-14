from db_interface import DBInterface
from igzg.utils import getConfig
from pprint import pprint

class Model:
    def __init__(self):
        self.dbi = DBInterface(*getConfig(['username','password','database','port']))


    def make_and_insert_new_sps(self, rows_datas):
        def get_sp_raw_datas():
            sp_group_datas = {} # 전체 수주 정보
            sp_raw_datas = {'item_datas':[],'seg_datas':[],'bond_datas':[],} # 아이템, 세그먼트, 본드 정보

            for row_data in rows_datas:
                where = self.get_where_str('order_item_no',row_data)
                [item_order_data] = self.select_table_with_wheres('item_order',[where])

                where = f"`sys_id` = '{item_order_data['sys_item_id']}'"
                [item_data] = self.select_table_with_wheres('item',[where])

                where = f"`sys_id` = '{item_data['sys_seg1_id']}'"
                [seg1_data] = self.select_table_with_wheres('segment',[where])
                where = f"`sys_id` = '{seg1_data['sys_bond_id']}'"
                [bond1_data] = self.select_table_with_wheres('bond',[where])

                if item_data['sys_seg2_id']:
                    where = f"`sys_id` = '{item_data['sys_seg2_id']}'"
                    [seg2_data] = self.select_table_with_wheres('segment',[where]) 
                    where = f"`sys_id` = '{seg2_data['sys_bond_id']}'"
                    [bond2_data] = self.select_table_with_wheres('bond',[where])
                else:
                    seg2_data = {}
                    bond2_data = {}
                sp_raw_datas['item_datas'].append(item_data)
                sp_raw_datas['seg_datas'].append(seg1_data)
                sp_raw_datas['seg_datas'].append(seg2_data)
                sp_raw_datas['bond_datas'].append(bond1_data)
                sp_raw_datas['bond_datas'].append(bond2_data)
                # --------------------------
                group_name = item_data['group_name'] # 수주 정보를 그룹명으로 묶음
                if group_name not in sp_group_datas.keys():
                    sp_group_datas[group_name] = {'item_order_datas':[]}
                sp_group_datas[group_name]['item_order_datas'].append(item_order_data)
            return sp_group_datas,sp_raw_datas

        def get_sp_datas():
            def add_or_update(target_dict, key, cnt):
                target_dict[key] = target_dict.get(key, 0)+ cnt
            # -------------------------------------------------------------------------------------------
            sp_datas = {}
            for group_name, raw_data in sp_group_datas.items():
                sp_datas[group_name] = {'item':{}, 'seg': {},'bond':{}, 'data':{}}

                # --------------------------
                for item_order_data in raw_data['item_order_datas']: # 아이템 수량 합산 (세그먼트 수량 계산용)
                    item_name = item_order_data['item_name']
                    if item_name:
                        item_amount = int(item_order_data.get('item_amount', 0))
                        add_or_update(sp_datas[group_name]['item'],item_name,item_amount)
                # --------------------------
                for item_name, item_amount in sp_datas[group_name]['item'].items(): # 세그먼트 수량 계산
                    item_datas = sp_raw_datas['item_datas']
                    item_data = next((item for item in item_datas if item.get('name') == item_name), None)

                    seg1_no = item_data['seg1_no']
                    seg2_no = item_data['seg2_no']
                    if seg1_no:
                        seg1_amount = int(item_data['seg1_amount'])*item_amount
                        add_or_update(sp_datas[group_name]['seg'],seg1_no,seg1_amount)
                    if seg2_no:
                        seg2_amount = int(item_data['seg2_amount'])*item_amount
                        add_or_update(sp_datas[group_name]['seg'],seg2_no,seg2_amount)
                # --------------------------
                # 본드 데이터 정리(사용하는 분말 함량, 비율) 
                # 이게 본드에 순서도 있을걸요
                # 그럼 어쩌지
                # 순서는 내용 만들때 신경쓰고 일단 사용하는 녀석만 모은 딕셔너리 필요함
                # 본드명: {분말1:비율1, 분말2:비율2}
                
   
            return sp_datas
        
        def get_new_sps():
            new_sps = {}
            for group_name, group_data in sp_datas.items():
                new_sps[group_name] = []  # 사실 sp 는 그룹명으로 묶는거보다 ip번호로 묶는게 좋을텐데

                for (seg_no, seg_amout) in group_data['seg'].items():
                    new_sp = {}

                    for (k, val) in group_data['data']: # 기타 데이터 추가
                        new_sp[k] = val
                    # segment DB에서 가져오는 데이터
                    seg_data = next((d for d in sp_raw_datas['seg_datas'] if d.get('seg_no') == seg_no), None)
                    bond_data = next((d for d in sp_raw_datas['bond_datas'] if d.get('name') == seg_data['bond']), None)

                    from pprint import pprint
                    pprint(seg_data)
                    pprint(bond_data)
                    # -------------------------------------------------------------------------------------------
                    new_sp['seg_no1'] = seg_no
                    new_sp['product_name'] = seg_no
                    new_sp['amount_net'] = str(seg_amout)
                    new_sp['specification_l'] = seg_data['l']
                    new_sp['specification_t'] = seg_data['t']
                    new_sp['specification_w'] = seg_data['w']
                    new_sp['specification_v'] = seg_data['v']
                    new_sp['specification_model_text'] = seg_data['model_text']
                    new_sp['specification_model_img'] = seg_data['model_img']
                    new_sp['bond_select'] = seg_data['bond']
                    # new_sp['bond_abs_density'] = seg_data['v']
                    # new_sp['bond_hardness'] = seg_data['v']
                    new_sp['diamond_dia1_name'] = seg_data['d1']
                    new_sp['diamond_dia1_ratio'] = seg_data['d1_rate']
                    new_sp['diamond_dia2_name'] = seg_data['d2']
                    new_sp['diamond_dia2_ratio'] = seg_data['d2_rate']
                    new_sp['diamond_dia3_name'] = seg_data['d3']
                    new_sp['diamond_dia3_ratio'] = seg_data['d3_rate']
                    new_sp['diamond_concent1'] = seg_data['concent']
                    # new_sp['diamond_concent2'] = seg_data['v']
                    new_sp['sint_temp'] = bond_data['sint_temp']
                    new_sp['sint_time'] = bond_data['sint_time']
                    # new_sp['sint_test_theo_density'] = seg_data['v']
                    # new_sp['sint_test_benchmark'] = seg_data['v']
                    new_sp['forming_pressure'] = seg_data['forming_pressure']
                    new_sp['forming_height'] = seg_data['forming_height']
                    # new_sp['dosing_diamix'] = seg_data['v']
                    # new_sp['dosing_bond'] = seg_data['v']
                    new_sp['diamixing_bondmix_name'] = seg_data['bond']
                    # new_sp['diamixing_bondmix_amount'] = seg_data['v']
                    new_sp['diamixing_dia1_name'] = seg_data['d1']
                    # new_sp['diamixing_dia1_amount'] = seg_data['v']
                    new_sp['diamixing_dia2_name'] = seg_data['d2']
                    # new_sp['diamixing_dia2_amount'] = seg_data['v']
                    new_sp['diamixing_dia3_name'] = seg_data['d3']
                    # new_sp['diamixing_dia3_amount'] = seg_data['v']
                    # new_sp['diamixing_zinc_check'] = seg_data['v']
                    # new_sp['diamixing_zinc_amount'] = seg_data['v']
                    # new_sp['diamixing_paraffin_check'] = seg_data['v']
                    # new_sp['diamixing_paraffin_amount'] = seg_data['v']
                    new_sp['diamixing_mixing_time'] = bond_data['mixing_time']
                    new_sp['powdermixing_ballmill_time'] = bond_data['ballmill_time']
                    new_sp['powdermixing_bond_name'] = seg_data['bond']
                    # new_sp['powdermixing_bond_amount'] = seg_data['v']
                    new_sp['powdermixing_powder1_name'] = bond_data['v']
                    new_sp['powdermixing_powder1_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder1_amount'] = seg_data['v']
                    new_sp['powdermixing_powder2_name'] = seg_data['v']
                    new_sp['powdermixing_powder2_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder2_amount'] = seg_data['v']
                    new_sp['powdermixing_powder3_name'] = seg_data['v']
                    new_sp['powdermixing_powder3_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder3_amount'] = seg_data['v']
                    new_sp['powdermixing_powder4_name'] = seg_data['v']
                    new_sp['powdermixing_powder4_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder4_amount'] = seg_data['v']
                    new_sp['powdermixing_powder5_name'] = seg_data['v']
                    new_sp['powdermixing_powder5_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder5_amount'] = seg_data['v']
                    new_sp['powdermixing_powder6_name'] = seg_data['v']
                    new_sp['powdermixing_powder6_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder6_amount'] = seg_data['v']
                    new_sp['powdermixing_powder_total_ratio'] = seg_data['v']
                    new_sp['powdermixing_powder_total_amount'] = seg_data['v']     

                new_sps.append(new_sp)
            return new_sps
        # ===========================================================================================
        sp_group_datas,sp_raw_datas = get_sp_raw_datas()
        sp_datas = get_sp_datas()
        new_sps = get_new_sps()

        for new_sp in new_sps:
            new_sp = {x:new_sp[x] if new_sp[x] else 'NULL' for x in new_sp}
            self.insert_table('sp',new_sp)

        return new_sps


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
                    item_name = item_datas['name']
                    item_amount = ip_datas[group_name]['item'][item_name]
                    seg1_no = item_datas['seg1_no']
                    seg2_no = item_datas['seg2_no']
                    shank_name = item_datas['shank_name']
                    sub1_name = item_datas['sub1_name']
                    sub2_name = item_datas['sub2_name']
                    # ip_datas[group_name]['data']['auto_ip_no3'] = item_datas['recent_ip']
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

def get_order_rows():
    return [{'bond_name': 'TEST',
    'color': 'TEST',
    'customer_name': 'coustomer1',
    'due_date': '235235',
    'engrave': 'TEST',
    'ip_no': 'NULL',
    'item_amount': '2',
    'item_group_name': 'TEST',
    'item_name': 'TEST_ITEM2',
    'order_customer_no': 'c1-1',
    'order_date': 'TEST',
    'order_item_no': '2',
    'order_no': '1',
    'seg_amount_net': 'TEST',
    'seg_amount_work': 'TEST',
    'seg_name': 'TEST',
    'seg_no': 'TEST',
    'shipping_date': 'TEST',
    'sp_no': 'NULL',
    'sys_bond_id': 'NULL',
    'sys_customer_id': 'NULL',
    'sys_description': 'NULL',
    'sys_id': 'IO000000002',
    'sys_ip_id': 'NULL',
    'sys_item_id': 'IT000000023',
    'sys_reg_date': '2024-05-07 11:46:48',
    'sys_seg_id': 'NULL',
    'sys_sp_id': 'NULL',
    'sys_update_date': '2024-05-13 19:19:15'}]    


if __name__ == "__main__":
    m = Model()
    r = m.make_and_insert_new_sps(get_order_rows())

    from pprint import pprint
    pprint(r)

