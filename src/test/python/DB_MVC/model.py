from db_interface import DBInterface
from igzg.utils import getConfig
from pprint import pprint


class SPModel:
    def __init__(self):
        ...

    def get_diamond_concent2(self,concent1:str)->str:
        return "{:.2f}%".format(float(concent1)/4.4*100)

    def get_sint_test_benchmark(self,density_theo_density1:str)->str:
        return "{:.2f}%".format(float(density_theo_density1)* 0.94)

    def get_weight_weight(self,sp_data:dict)->str:
        weight_volume = float(sp_data['weight_volume'])
        weight_abs_density = float(sp_data['weight_abs_density'])
        weight_rel_density = float(sp_data['weight_rel_density'])        
        weight_loss = float(sp_data['weight_loss'])
        # --------------------------
        weight = weight_volume * weight_abs_density * weight_rel_density * weight_loss
        return "{:.2f}".format(weight)
    
    def get_segment_config(self,sp_data:dict)->dict:
        weight_weight = float(sp_data['weight_weight'])
        specification_v = float(sp_data['specification_v'])
        diamond_concent1 = float(sp_data['diamond_concent1'])
        # --------------------------
        dia_weight = specification_v * diamond_concent1 * 0.2
        dia_volume = dia_weight /3.51
        dia_volume_rate = dia_volume / specification_v
        bond_volume = specification_v - dia_volume
        bond_volume_rate = bond_volume/ specification_v
        bond_weight= bond_volume_rate * weight_weight
        total_volume =  dia_volume  + bond_volume
        total_volume_rate = dia_volume_rate + bond_volume_rate
        total_weight = dia_weight + bond_weight
        # --------------------------
        result = {}
        result['dia_weight'] = dia_weight
        result['dia_volume'] = dia_volume
        result['dia_volume_rate'] = dia_volume_rate
        result['bond_volume'] = bond_volume
        result['bond_volume_rate'] = bond_volume_rate
        result['bond_weight'] = bond_weight
        result['total_volume'] = total_volume
        result['total_volume_rate'] = total_volume_rate
        result['total_weight'] = total_weight

        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_segment_density(self,sp_data:dict)->dict:
        weight_abs_density = float(sp_data['weight_abs_density'])
        bond_volume_rate = float(sp_data['bond_volume_rate'])
        dia_volume_rate = float(sp_data['dia_volume_rate'])
        total_weight = float(sp_data['total_weight'])
        specification_v = float(sp_data['specification_v'])
        diamond_concent1 = float(sp_data['diamond_concent1'])
        # --------------------------
        density_theo_density1 = weight_abs_density * bond_volume_rate + 3.51 * dia_volume_rate
        density_theo_density2 = weight_abs_density * bond_volume_rate + diamond_concent1 * 0.2
        density_final_density = total_weight / specification_v
        density_final_rel_density = density_final_density / density_theo_density1
        # --------------------------
        result = {}
        result['density_theo_density1'] = density_theo_density1
        result['density_theo_density2'] = density_theo_density2
        result['density_final_density'] = density_final_density
        result['density_final_rel_density'] = density_final_rel_density

        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_workload(self,sp_data:dict)->dict:
        dosing_diamix = float(sp_data['dosing_diamix'])
        dia_weight = float(sp_data['dia_weight'])
        workload = float(sp_data.get('amount_work',0)) # 최소 작업량입력한 경우
        workload = workload if workload else float(sp_data.get('amount_net',0))
        # --------------------------
        diamixing_bondmix_amount = workload * (dosing_diamix - dia_weight)
        powdermixing_bond_amount = ((diamixing_bondmix_amount + 4999) // 5000) * 5000 # 5000으로 나누어떨어지는 작업량
        powdermixing_bond_amount = powdermixing_bond_amount if powdermixing_bond_amount else 10000.0 # workload = 0 일때 기본 작업량
        amount_work = powdermixing_bond_amount // (dosing_diamix - dia_weight) # 최종 작업량
        diamixing_bondmix_amount = amount_work * (dosing_diamix - dia_weight) # 최종 본드량
        # --------------------------
        result = {}
        result['workload'] = workload
        result['powdermixing_bond_amount'] = powdermixing_bond_amount
        result['amount_work'] = amount_work
        result['diamixing_bondmix_amount'] = diamixing_bondmix_amount
        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_dia_amounts(self,sp_data:dict)->dict:
        # 다이아 무게
        dia_weight = float(sp_data['dia_weight'])
        amount_work = float(sp_data['amount_work'])
        diamond_dia1_ratio = float(sp_data['diamond_dia1_ratio'])
        diamond_dia2_ratio = float(sp_data['diamond_dia2_ratio'])
        diamond_dia3_ratio = float(sp_data['diamond_dia3_ratio'])
        # --------------------------
        def get_dia_amount(dia_ratio):
            from math import ceil
            return ceil(dia_weight * amount_work * dia_ratio/10)
        # --------------------------
        result = {}
        result['diamixing_dia1_amount'] = get_dia_amount(diamond_dia1_ratio)
        result['diamixing_dia2_amount'] = get_dia_amount(diamond_dia2_ratio)
        result['diamixing_dia3_amount'] = get_dia_amount(diamond_dia3_ratio)
        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_verification(self,sp_data:dict)->dict:
        diamixing_bondmix_amount = float(sp_data['diamixing_bondmix_amount'])
        diamixing_dia1_amount = float(sp_data['diamixing_dia1_amount'])
        diamixing_dia2_amount = float(sp_data['diamixing_dia2_amount'])
        diamixing_dia3_amount = float(sp_data['diamixing_dia3_amount'])
        dosing_diamix = float(sp_data['dosing_diamix'])
        amount_work = float(sp_data['amount_work'])
        # --------------------------
        veri_weight = diamixing_bondmix_amount + diamixing_dia1_amount + diamixing_dia2_amount + diamixing_dia3_amount
        veri_count = dosing_diamix * amount_work
        # --------------------------
        result = {}
        result['veri_weight'] = veri_weight
        result['veri_count'] = veri_count
        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_powder_amounts(self,sp_data:dict)->dict:
        powdermixing_bond_amount = float(sp_data['powdermixing_bond_amount'])
        powdermixing_powder_total_ratio = 0
        powdermixing_powder_total_amount = 0

        def get_powder_amount(ratio):
            return float(ratio) * powdermixing_bond_amount / 100

        result = {}
        for idx in range(1,7):
            ratio = float(sp_data.get(f'powdermixing_powder{idx}_ratio',0))
            if ratio:
                amount = get_powder_amount(ratio)
                result[f'powdermixing_powder{idx}_amount'] = amount
                powdermixing_powder_total_ratio += ratio
                powdermixing_powder_total_amount += amount
        else:
            result['powdermixing_powder_total_ratio'] = powdermixing_powder_total_ratio
            result['powdermixing_powder_total_amount'] = powdermixing_powder_total_amount
        return {k:"{:.2f}".format(v) for k,v in result.items()}

    def get_sp_datas(self,sp_group_datas,sp_raw_datas):
        def add_or_update(target_dict, key, cnt):
            target_dict[key] = target_dict.get(key, 0)+ cnt
        # -------------------------------------------------------------------------------------------
        sp_datas = {}
        for ip_no, raw_data in sp_group_datas.items():
            sp_datas[ip_no] = {'item':{}, 'seg': {},'bond':{}, 'data':{}}

            # --------------------------
            for item_order_data in raw_data['item_order_datas']: # 아이템 수량 합산 (세그먼트 수량 계산용)
                item_name = item_order_data['item_name']
                if item_name:
                    item_amount = int(item_order_data.get('item_amount', 0))
                    add_or_update(sp_datas[ip_no]['item'],item_name,item_amount)
            # --------------------------
            for item_name, item_amount in sp_datas[ip_no]['item'].items(): # 세그먼트 수량 계산
                item_datas = sp_raw_datas['item_datas']
                item_data = next((item for item in item_datas if item.get('name') == item_name), None)

                seg1_no = item_data['seg1_no']
                seg2_no = item_data['seg2_no']
                if seg1_no:
                    seg1_amount = int(item_data['seg1_amount'])*item_amount
                    add_or_update(sp_datas[ip_no]['seg'],seg1_no,seg1_amount)
                if seg2_no:
                    seg2_amount = int(item_data['seg2_amount'])*item_amount
                    add_or_update(sp_datas[ip_no]['seg'],seg2_no,seg2_amount)
        return sp_datas
    
    def get_new_sps(self,sp_datas,sp_raw_datas):
        new_sps = []
        for ip_no, group_data in sp_datas.items():
            for (seg_no, seg_amout) in group_data['seg'].items():
                new_sp = {}

                for (k, val) in group_data['data']: # 기타 데이터 추가
                    new_sp[k] = val
                # segment DB에서 가져오는 데이터
                seg_data = next((d for d in sp_raw_datas['seg_datas'] if d.get('seg_no') == seg_no), None)
                bond_data = next((d for d in sp_raw_datas['bond_datas'] if d.get('name') == seg_data['bond']), None)

                # -------------------------------------------------------------------------------------------
                # DB에서 채우기
                def get_new_sp_from_data():
                    new_sp['ip_no'] = ip_no
                    new_sp['seg_no1'] = seg_no
                    new_sp['product_name'] = seg_no
                    new_sp['amount_net'] = str(seg_amout)
                    new_sp['specification_l'] = seg_data['l']
                    new_sp['specification_t'] = seg_data['t']
                    new_sp['specification_w'] = seg_data['w']
                    new_sp['specification_v'] = seg_data['v']
                    new_sp['weight_volume'] = seg_data['v']
                    new_sp['specification_model_text'] = seg_data['model_text']
                    new_sp['specification_model_img'] = seg_data['model_img']
                    new_sp['bond_select'] = seg_data['bond']
                    new_sp['bond_abs_density'] = bond_data['abs_density']
                    new_sp['weight_abs_density'] = bond_data['abs_density']
                    new_sp['bond_hardness'] = bond_data['hardness_HRB']
                    new_sp['diamond_dia1_name'] = seg_data['d1']
                    new_sp['diamond_dia1_ratio'] = seg_data['d1_rate']
                    new_sp['diamond_dia2_name'] = seg_data['d2']
                    new_sp['diamond_dia2_ratio'] = seg_data['d2_rate']
                    new_sp['diamond_dia3_name'] = seg_data['d3']
                    new_sp['diamond_dia3_ratio'] = seg_data['d3_rate']
                    new_sp['diamond_concent1'] = seg_data['concent']
                    new_sp['sint_temp'] = bond_data['sint_temp']
                    new_sp['sint_time'] = bond_data.get('sint_time','')
                    new_sp['forming_pressure'] = seg_data['forming_pressure']
                    new_sp['forming_height'] = seg_data['forming_height']
                    new_sp['diamixing_bondmix_name'] = seg_data['bond']
                    new_sp['diamixing_dia1_name'] = seg_data['d1']
                    new_sp['diamixing_dia2_name'] = seg_data['d2']
                    new_sp['diamixing_dia3_name'] = seg_data['d3']
                    new_sp['diamixing_mixing_time'] = bond_data.get('mixing_time')
                    new_sp['powdermixing_ballmill_time'] = bond_data.get('ballmill_time')
                    new_sp['powdermixing_bond_name'] = seg_data['bond']

                    idx = 1
                    for x in [x['chemical_symbol'] for x in sp_raw_datas['powder_datas']]:
                        if bond_data.get(x,'') != '':
                            new_sp[f'powdermixing_powder{idx}_name'] = x
                            new_sp[f'powdermixing_powder{idx}_ratio'] = bond_data[x]
                            idx += 1
                get_new_sp_from_data()
                # -------------------------------------------------------------------------------------------
                # 고정값 채우기
                new_sp['weight_loss'] = '1.01'
                new_sp['weight_rel_density'] = '0.95'
                # -------------------------------------------------------------------------------------------
                # 계산값 채우기
                new_sp['diamond_concent2'] = self.get_diamond_concent2(new_sp['diamond_concent1'])
                new_sp['weight_weight'] = self.get_weight_weight(new_sp)
                new_sp.update(self.get_segment_config(new_sp)) # dia_weight, dia_volume, dia_volume_rate, bond_volume, bond_volume_rate, bond_weight, total_volume, total_volume_rate, total_weight
                new_sp.update(self.get_segment_density(new_sp)) # density_theo_density1, density_theo_density2, density_final_density, density_final_rel_density
                # -------------------------------------------------------------------------------------------
                # 계산값으로 채우기
                new_sp['dosing_diamix'] = new_sp['total_weight']
                new_sp['dosing_bond'] = new_sp['weight_weight']
                new_sp['sint_test_theo_density'] = new_sp['density_theo_density1']
                # -------------------------------------------------------------------------------------------
                # 계산값 채우기
                new_sp['sint_test_benchmark'] = self.get_sint_test_benchmark(new_sp['density_theo_density1'])
                new_sp.update(self.get_workload(new_sp)) # workload, powdermixing_bond_amount, amount_work, diamixing_bondmix_amount
                new_sp.update(self.get_dia_amounts(new_sp)) # diamixing_dia1~3_amount
                new_sp.update(self.get_powder_amounts(new_sp)) # powdermixing_powder1~6_amount, powdermixing_powder_total_ratio, powdermixing_powder_total_amount
                new_sp.update(self.get_verification(new_sp)) # veri_weight, veri_count

            new_sps.append(new_sp)
        return new_sps
    
    

# ===========================================================================================
class Model(SPModel):
    def __init__(self):
        self.dbi = DBInterface(*getConfig(['username','password','database','port']))

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
                    ip_no = ip_data.get('auto_ip_no','')
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
    'sys_ip_id': 'IP000000008',
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

