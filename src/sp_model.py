
# SP 계산식
class SPModel:
    # [계산식] ===========================================================================================
    # 집중도 계산
    def get_diamond_concent2(self,concent1:str)->str:
        return "{:.2f}%".format(float(concent1)/4.4*100)

    # 소결 기준94
    def get_sint_test_benchmark(self,density_theo_density1:str)->str:
        return "{:.2f}%".format(float(density_theo_density1)* 0.94)

    # 중량 계산
    def get_weight_weight(self,sp_data:dict)->str:
        weight_volume = float(sp_data['weight_volume'])
        weight_abs_density = float(sp_data['weight_abs_density'])
        weight_rel_density = float(sp_data['weight_rel_density'])        
        weight_loss = float(sp_data['weight_loss'])
        # --------------------------
        weight = weight_volume * weight_abs_density * weight_rel_density * weight_loss
        return "{:.2f}".format(weight)
    
    # seg_config_layout 계산
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

    # seg_density_layout 계산
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

    # 작업량 계산
    def get_workload(self,sp_data:dict)->dict:
        dosing_diamix = float(sp_data['dosing_diamix'])
        dia_weight = float(sp_data['dia_weight'])
        workload = float(sp_data.get('workload',0)) # 최소 작업량입력한 경우
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

    # 다이아믹싱 무게 계산
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

    # seg_verification_layout 계산
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

    # 분말 혼합량 계산
    def get_powder_amounts(self,sp_data:dict)->dict:
        powdermixing_bond_amount = float(sp_data['powdermixing_bond_amount'])
        powdermixing_powder_total_ratio = 0
        powdermixing_powder_total_amount = 0

        def get_powder_amount(ratio):
            return float(ratio) * powdermixing_bond_amount / 100

        result = {}
        sp_data = {k: v for k, v in sp_data.items() if v != ''}
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

    # [sp 생성] ===========================================================================================
    # sp 표시값 정리
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
                item_data = next((item for item in item_datas if item.get('product_name') == item_name), None)

                seg1_no = item_data['seg1_no']
                seg2_no = item_data['seg2_no']
                if seg1_no:
                    seg1_amount = int(item_data['seg1_amount'])*item_amount
                    add_or_update(sp_datas[ip_no]['seg'],seg1_no,seg1_amount)
                if seg2_no:
                    seg2_amount = int(item_data['seg2_amount'])*item_amount
                    add_or_update(sp_datas[ip_no]['seg'],seg2_no,seg2_amount)
        return sp_datas
    
    # sp 전체 계산값 생성
    def get_new_sps(self,sp_datas,sp_raw_datas):
        new_sps = []
        for ip_no, group_data in sp_datas.items():
            for (seg_no, seg_amout) in group_data['seg'].items():
                new_sp = {}

                for (k, val) in group_data['data']: # 기타 데이터 추가
                    new_sp[k] = val
                # segment DB에서 가져오는 데이터
                seg_data = next((d for d in sp_raw_datas['seg_datas'] if d.get('seg_no') == seg_no), None)
                bond_data = next((d for d in sp_raw_datas['bond_datas'] if d.get('product_name') == seg_data['bond_name']), None)

                # -------------------------------------------------------------------------------------------
                # DB에서 채우기
                def get_new_sp_from_data():
                    new_sp['ip_no'] = ip_no
                    new_sp['seg_no'] = seg_no
                    new_sp['product_name'] = seg_no
                    new_sp['amount_net'] = str(seg_amout)
                    new_sp['specification_l'] = seg_data['specification_l']
                    new_sp['specification_t'] = seg_data['specification_t']
                    new_sp['specification_w'] = seg_data['specification_w']
                    new_sp['specification_v'] = seg_data['specification_v']
                    new_sp['weight_volume'] = seg_data['specification_v']
                    new_sp['specification_model_text'] = seg_data['model_text']
                    new_sp['specification_model_img'] = seg_data['model_img']
                    new_sp['bond_select'] = seg_data['bond_name']
                    new_sp['bond_abs_density'] = bond_data['density']
                    new_sp['weight_abs_density'] = bond_data['density']
                    new_sp['bond_hardness'] = bond_data['hardness_HRB']
                    new_sp['diamond_dia1_name'] = seg_data['dia1']
                    new_sp['diamond_dia1_ratio'] = seg_data['dia1_ratio']
                    new_sp['diamond_dia2_name'] = seg_data['dia2']
                    new_sp['diamond_dia2_ratio'] = seg_data['dia2_ratio']
                    new_sp['diamond_dia3_name'] = seg_data['dia3']
                    new_sp['diamond_dia3_ratio'] = seg_data['dia3_ratio']
                    new_sp['diamond_concent1'] = seg_data['concent']
                    new_sp['sint_temp'] = bond_data['sint_temp']
                    new_sp['sint_time'] = bond_data.get('sint_time','')
                    new_sp['forming_pressure'] = seg_data['forming_pressure']
                    new_sp['forming_height'] = seg_data['forming_height']
                    new_sp['diamixing_bondmix_name'] = seg_data['bond_name']
                    new_sp['diamixing_dia1_name'] = seg_data['dia1']
                    new_sp['diamixing_dia2_name'] = seg_data['dia2']
                    new_sp['diamixing_dia3_name'] = seg_data['dia3']
                    new_sp['diamixing_mixing_time'] = bond_data.get('mixing_time')
                    new_sp['powdermixing_ballmill_time'] = bond_data.get('ballmill_time')
                    new_sp['powdermixing_bond_name'] = seg_data['bond_name']

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
    
    # [갱신] ===========================================================================================
    # 중량 갱신
    def sp_viewer_weight_update(self,sp_data):
        sp_data.update(self.get_workload(sp_data))
        sp_data.update({'weight_weight':self.get_weight_weight(sp_data)})
        sp_data.update(self.get_segment_config(sp_data))
        sp_data.update(self.get_segment_density(sp_data))
        sp_data.update(self.get_workload(sp_data))
        sp_data.update(self.get_dia_amounts(sp_data))
        sp_data.update(self.get_verification(sp_data))
        sp_data.update(self.get_powder_amounts(sp_data))
        return sp_data

    # 작업량 갱신
    def sp_viewer_workload_update(self,sp_data)->dict:
        sp_data.update(self.get_workload(sp_data))
        sp_data.update(self.get_dia_amounts(sp_data))
        sp_data.update(self.get_verification(sp_data))
        sp_data.update(self.get_powder_amounts(sp_data))
        return sp_data

    # 다이아 갱신
    def sp_viewer_dosing_diamix_update(self,sp_data):
        return self.sp_viewer_workload_update(sp_data)
