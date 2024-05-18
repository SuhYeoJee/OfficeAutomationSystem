if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")

from src.module.pyqt_imports import *
from src.module.window_builder import WindowBuilder
from src.module.table_plus_widget import TablePlusWidget

class SpViewTable(TablePlusWidget):
    def __init__(self)->None:
        self.border_data = self.get_border_data()
        self.form_data = self.get_form_data()
        self.pos_data = self.get_pos_data()
        self.sp_data = {v: k for k, v in self.pos_data.items()}
        super().__init__(self.border_data,self.form_data,self.pos_data)
        self.fill_form()
        self.fill_datas_position(self.sp_data)
        self.show()
    # -------------------------------------------------------------------------------------------
    # 테두리 그리기 정보
    def get_border_data(self)->list:
        return [
            [0,7,3,3,'bold'], [0,7,1,3,''], [0,8,3,1,''],
            [4,0,1,10,'bold'],[6,0,2,10,'bold'],[9,0,8,10,'bold'],[18,0,14,10,'bold'],[33,0,4,10,'bold'],
            [4,0,1,2,''],[9,0,2,2,''],[11,0,2,2,''], [13,0,4,2,''],
            [4,5,1,2,''],[9,2,2,3,''],[11,2,2,2,''], [13,2,4,5,''],
            [9,5,2,2,''],[11,4,1,3,''], [12,4,1,3,''],[9,7,8,3,''],
            [6,0,1,5,''],[7,0,1,5,''],[6,7,1,3,''],[7,7,1,3,''],[6,0,2,2,''],
            [18,0,2,2,''],[20,0,2,2,''],[22,0,2,2,''],[24,0,4,2,''],[28,0,4,2,''],[33,0,4,2,''],
            [18,2,1,5,''],[19,2,1,5,''],[20,2,1,5,''],[21,2,1,5,''],[22,2,2,5,''],
            [18,7,2,1,''],[18,8,2,1,''],[18,9,2,1,''],[20,7,2,3,''],[22,7,2,3,''],
            [24,2,1,5,''],[25,2,3,1,''],[25,3,1,4,''],[26,3,1,4,''],[27,3,1,4,''],
            [24,7,1,3,''],[25,7,1,3,''],[26,7,1,3,''],[27,7,1,3,''],[28,7,1,3,''],
            [28,2,1,5,''],[29,2,3,8,'']
        ]
    
    # 셀 병합 정보
    def get_form_data(self)->dict:
        return {
            'init_size' : (37,10),
            'slim_rows' : [3,5,8,17,32],
            'slim_cols' : [],
            'text_items' : {
                (1,0):[(2,5),"세그먼트 제조 지시서", ['title']],
                # --------------------------
                (4,0):[(1,2),"제조지시   NO.",['center','bold']],
                (4,5):[(1,2),"일         자",['center','bold']],
                (6,0):[(1,2),"세그먼트   NO.",['center','bold']],
                (7,0):[(1,2),"품         명",['center','bold']],
                (6,5):[(2,2),"수         량",['center','bold']],
                (9,0):[(2,2),"규         격",['center','bold']],
                (11,0):[(2,2),"본         드",['center','bold']],
                (13,0):[(4,2),"다이아몬드",['center','bold']],
                (18,0):[(2,2),"V\n소         결",['center','bold']],
                (18,7):[(2,1),"소   결\nTEST",['center','bold']],
                (20,0):[(2,2),"IV\n성         형",['center','bold']],
                (22,0):[(2,2),"III\n도         징",['center','bold']],
                (24,0):[(4,2),"II\n다  이  아\n믹      싱",['center','bold']],
                (28,0):[(4,2),"I\n분      말\n믹      싱",['center','bold']],
                (33,0):[(4,2),"기      타",['center','bold']],
                # --------------------------
                (6,9):[(1,1),"개",['left']],
                (7,9):[(1,1),"개",['left']],
                (10,6):[(1,1),"cc",['left']],
                (11,6):[(1,1),"g/cc",['left']],
                (12,6):[(1,1),"HRB",['left']],
                (15,6):[(1,1),"ct/cc",['left']],
                (18,6):[(1,1),"°C",['left']],
                (19,6):[(1,1),"min",['left']],
                (20,6):[(1,1),"bar",['left']],
                (21,6):[(1,1),"mm",['left']],
                (22,6):[(2,1),"g",['left']],
                (23,9):[(1,1),"g",['left']],
                (24,6):[(1,1),"g",['left']],
                (25,6):[(1,1),"g",['left']],
                (26,6):[(1,1),"g",['left']],
                (27,6):[(1,1),"g",['left']],
                (25,9):[(1,1),"g",['left']],
                (26,9):[(1,1),"g",['left']],
                (27,9):[(1,1),"시간",['left']],
                (28,9):[(1,1),"시간",['left']],
                # --------------------------
                (6,7):[(1,1),"NET",['center']],
                (7,7):[(1,1),"작업량",['center']],
                (9,2):[(1,1),"L",['center']],
                (9,3):[(1,1),"T",['center']],
                (9,4):[(1,1),"높이(W)",['center']],
                (9,5):[(1,2),"부피",['center']],
                (9,7):[(1,1),"[모형]",['center']],
                (11,4):[(1,1),"절대밀도",['center']],
                (12,4):[(1,1),"경      도",['center']],
                (13,3):[(1,2),"종류",['center']],
                (13,5):[(1,1),"비율",['center']],
                (13,6):[(1,1),"집중도",['center']],
                (14,2):[(1,1),"D1",['center']],
                (15,2):[(1,1),"D2",['center']],
                (16,2):[(1,1),"D3",['center']],
                (18,2):[(1,2),"온      도",['center']],
                (19,2):[(1,2),"시      간",['center']],
                (18,8):[(1,1),"이론밀도",['center']],
                (18,9):[(1,1),"기준(94%)",['center']],
                (20,2):[(1,2),"압      력",['center']],
                (24,2):[(1,1),"본드믹스",['center']],
                (25,2):[(3,1),"다이아\n몬드",['center']],
                (27,7):[(1,1),"믹   싱",['center']],
                (28,7):[(1,1),"볼   밀",['center']],
                (28,2):[(1,1),"본   드",['center']],
                (28,4):[(1,1),"작업량",['center']],
                (29,2):[(1,1),"분   말",['center']],
                (30,2):[(1,1),"구성비",['center']],
                (31,2):[(1,1),"혼합량",['center']],
                (29,9):[(1,1),"계",['center']],
                # --------------------------
                (7,2):[(1,3),"",['left','editable']], # 품명 통합
                (6,8):[(1,1),"",['right','editable']],
                (7,8):[(1,1),"",['right','editable']],
                (10,7):[(1,1),"",['right','editable']],
                (10,8):[(1,2),"",['right','editable']],
                (11,7):[(1,1),"",['right','editable']],
                (12,7):[(1,1),"",['right','editable']],
                (18,4):[(1,2),"",['right','editable']],
                (19,4):[(1,2),"",['right','editable']],
                (20,4):[(1,2),"",['right','editable']],
                (21,4):[(1,2),"",['right','editable']],
                (22,4):[(2,2),"",['right','editable']],
                (23,7):[(1,2),"",['right','editable']],
                (24,4):[(1,2),"",['right','editable']],
                (25,5):[(1,1),"",['right','editable']],
                (26,5):[(1,1),"",['right','editable']],
                (27,5):[(1,1),"",['right','editable']],
                (28,5):[(1,2),"",['right','editable']],
                # --------------------------
                (6,2):[(1,2),"",['left','editable']],
                (33,2):[(1,8),"",['left','editable']],
                (34,2):[(1,8),"",['left','editable']],
                (35,2):[(1,8),"",['left','editable']],
                (36,2):[(1,8),"",['left','editable']],
                # --------------------------
                (4,7):[(1,3),"", ['center','editable']],
                (11,7):[(6,3),"", ['center','editable']],
                (11,2):[(2,2),"", ['center','editable']],
                (14,3):[(1,2),"", ['center','editable']],
                (15,3):[(1,2),"", ['center','editable']],
                (16,3):[(1,2),"", ['center','editable']],
                (21,7):[(1,3),"", ['center','editable']],
                (25,3):[(1,2),"", ['center','editable']],
                (26,3):[(1,2),"", ['center','editable']],
                (27,3):[(1,2),"", ['center','editable']],
                # -------------------------------------------------------------------------------------------
                (0,6):[(3,1),"결\n\n재",['right']],
                # --------------------------
                (0,7):[(1,1),"담당",['center']],
                (0,8):[(1,1),"부서장",['center']],
                (0,9):[(1,1),"사장",['center']],
                (21,2):[(1,2),"성  형  높  이",['center','black','bold']],
                (20,7):[(1,3),"*부채꼴 충진 주의",['left']],
                (22,2):[(2,2),"다이아   믹스",['center','black','bold']],
                (22,7):[(1,3),"*다이아 없는 본드:",['left']],
                (24,7):[(1,3),"첨가제",['center']],
                # --------------------------
                (25,7):[(1,1),"ㅁ  징크", ['left']],
                (26,7):[(1,1),"ㅁ  파라핀", ['left']],
            },
        }

    # db col name 과 cell position 정보 매핑
    def get_pos_data(self)->dict:
        return {
            "auto_sp_no1"                   : (4,2),  # 제조지시 NO. 1
            "auto_sp_no2"                   : (4,3),  # 제조지시 NO. 2
            "auto_sp_no3"                   : (4,4),  # 제조지시 NO. 3
            "auto_date"                          : (4,7),  # 일자
            "seg_no1"                        : (6,2),  # 세그먼트 No. 1
            "seg_no2"                        : (6,4),  # 세그먼트 No. 2
            "product_name"                  : (7,2),  # 품명1
            "amount_net"                     : (6,8),  # 수량NET
            "amount_work"                    : (7,8),  # 수량작업량
            "specification_l"                : (10,2), # 규격L
            "specification_t"                : (10,3), # 규격T
            "specification_w"                : (10,4), # 규격높이(W)
            "specification_v"                : (10,5), # 부피
            "specification_model_text"        : (10,8), # 모형텍스트
            "specification_model_img"         : (11,7), # 모형이미지
            "bond_select"                    : (11,2), # 본드 본드선택
            "bond_abs_density"                : (11,5), # 본드 절대밀도
            "bond_hardness"                  : (12,5), # 본드 경도
            "diamond_dia1_name"                 : (14,3), # 다이아몬드 종류 D1
            "diamond_dia2_name"                 : (15,3), # 다이아몬드 종류 D2
            "diamond_dia3_name"                 : (16,3), # 다이아몬드 종류 D3
            "diamond_dia1_ratio"                : (14,5), # 다이아몬드 비율 D1
            "diamond_dia2_ratio"                : (15,5), # 다이아몬드 비율 D2
            "diamond_dia3_ratio"                : (16,5), # 다이아몬드 비율 D3
            "diamond_concent1"               : (14,6), # 다이아몬드 집중도1
            "diamond_concent2"               : (16,6), # 다이아몬드 집중도2
            "sint_temp"                      : (18,4), # 소결 온도
            "sint_time"                      : (19,4), # 소결 시간
            "sint_test_theo_density"           : (19,8), # 소결TEST 이론밀도
            "sint_test_benchmark"             : (19,9), # 소결TEST 기준94%
            "forming_pressure"               : (20,4), # 성형 압력
            "forming_height"                 : (21,4), # 성형 성형높이
            "dosing_diamix"                  : (22,4), # 도징 다이아믹스
            "dosing_bond"                    : (23,7), # 도징 다이아 없는 본드
            "diamixing_bondmix_name"             : (24,3), # 다이아믹싱 본드믹스1
            "diamixing_bondmix_amount"             : (24,4), # 다이아믹싱 본드믹스2
            "diamixing_dia1_name"               : (25,3), # 다이아믹싱 다이아몬드 종류 D1
            "diamixing_dia2_name"               : (26,3), # 다이아믹싱 다이아몬드 종류 D2
            "diamixing_dia3_name"               : (27,3), # 다이아믹싱 다이아몬드 종류 D3
            "diamixing_dia1_amount"             : (25,5), # 다이아믹싱 다이아몬드 무게 D1
            "diamixing_dia2_amount"             : (26,5), # 다이아믹싱 다이아몬드 무게 D2
            "diamixing_dia3_amount"             : (27,5), # 다이아믹싱 다이아몬드 무게 D3
            "diamixing_zinc_check"            : (25,7), # 다이아믹싱 징크체크
            "diamixing_paraffin_check"        : (26,7), # 다이아믹싱 파라핀체크
            "diamixing_zinc_amount"           : (25,8), # 다이아믹싱 징크무게
            "diamixing_paraffin_amount"       : (26,8), # 다이아믹싱 파라핀무게
            "diamixing_mixing_time"           : (27,8), # 다이아믹싱 믹싱시간
            "powdermixing_ballmill_time"      : (28,8), # 분말믹싱 볼밀시간
            "powdermixing_bond_name"              : (28,3), # 분말믹싱 본드
            "powdermixing_bond_amount"          : (28,5), # 분말믹싱 작업량
            "powdermixing_powder1_name"           : (29,3), # 분말믹싱 분말1
            "powdermixing_powder2_name"           : (29,4), # 분말믹싱 분말2
            "powdermixing_powder3_name"           : (29,5), # 분말믹싱 분말3
            "powdermixing_powder4_name"           : (29,6), # 분말믹싱 분말4
            "powdermixing_powder5_name"           : (29,7), # 분말믹싱 분말5
            "powdermixing_powder6_name"           : (29,8), # 분말믹싱 분말6
            "powdermixing_powder1_ratio"      : (30,3), # 분말믹싱 구성비1
            "powdermixing_powder2_ratio"      : (30,4), # 분말믹싱 구성비2
            "powdermixing_powder3_ratio"      : (30,5), # 분말믹싱 구성비3
            "powdermixing_powder4_ratio"      : (30,6), # 분말믹싱 구성비4
            "powdermixing_powder5_ratio"      : (30,7), # 분말믹싱 구성비5
            "powdermixing_powder6_ratio"      : (30,8), # 분말믹싱 구성비6
            "powdermixing_powder_total_ratio"  : (30,9), # 분말믹싱 구성비계
            "powdermixing_powder1_amount"     : (31,3), # 분말믹싱 혼합량1
            "powdermixing_powder2_amount"     : (31,4), # 분말믹싱 혼합량2
            "powdermixing_powder3_amount"     : (31,5), # 분말믹싱 혼합량3
            "powdermixing_powder4_amount"     : (31,6), # 분말믹싱 혼합량4
            "powdermixing_powder5_amount"     : (31,7), # 분말믹싱 혼합량5
            "powdermixing_powder6_amount"     : (31,8), # 분말믹싱 혼합량6
            "powdermixing_powder_total_amount" : (31,9), # 분말믹싱 혼합량계
            "memo1"                         : (33,2), # 기타1
            "memo2"                         : (34,2), # 기타2
            "memo3"                         : (35,2), # 기타3
            "memo4"                         : (36,2), # 기타4
        }    
    
    # -------------------------------------------------------------------------------------------
    def set_sp_data(self,datas)->None:
        self.sp_data = datas # {'auto_date': '2024-05-12',}
        result = {self.pos_data[key]: self.sp_data[key] for key in self.pos_data if key in self.sp_data}
        self.fill_datas_position(result)
        self.show()

class SPViewer(QDialog):
    def __init__(self, parent=None, sp_data={}):
        super().__init__(parent)
        self.wb = WindowBuilder()
        self.widgets = {}
        self.sp_data = sp_data
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width() * 0.5), int(screen.height() * 0.78))

        self.setWindowTitle("SP Viewer")
        self.setLayout(self.get_sp_view_layout())
        self.get_sp_view_table().set_sp_data(self.sp_data)
        self.set_sp_view_layout()

    def get_sp_view_table(self)->SpViewTable:
        return self.widgets['sp_viewer_table']

    def get_sp_view_layout(self)->QHBoxLayout:
        sp_view_layout = QVBoxLayout()
        self.widgets['sp_viewer_table'] = SpViewTable()
        sp_view_layout.addWidget(self.widgets['sp_viewer_table'])
        # -------------------------------------------------------------------------------------------

        def get_worklaod_layout()->QHBoxLayout:
            workload_layout = self.wb.get_label_and_line_edit_layout("작업량",self.widgets, "workload")
            self.widgets['sp_viewer_workload_submit'] = self.wb.get_button("작업량 입력")
            workload_layout.addWidget(self.widgets['sp_viewer_workload_submit'])
            workload_layout.addStretch(1)
            return workload_layout

        def get_weight_layout()->QVBoxLayout:
            seg_weight_input1_layout = QVBoxLayout()
            seg_weight_input1_layout.addLayout(self.wb.get_label_and_line_edit_layout("체적",self.widgets,'weight_volume'))
            seg_weight_input1_layout.addLayout(self.wb.get_label_and_line_edit_layout("절대밀도",self.widgets,'weight_abs_density'))
            seg_weight_input2_layout = QVBoxLayout()
            seg_weight_input2_layout.addLayout(self.wb.get_label_and_line_edit_layout("상대밀도",self.widgets,'weight_rel_density'))
            seg_weight_input2_layout.addLayout(self.wb.get_label_and_line_edit_layout("LOSS",self.widgets,'weight_loss'))
            # --------------------------
            seg_weight_inputs_layout = QHBoxLayout()
            seg_weight_inputs_layout.addLayout(seg_weight_input1_layout)
            seg_weight_inputs_layout.addWidget(self.wb.get_vline_widget())
            seg_weight_inputs_layout.addLayout(seg_weight_input2_layout)
            # --------------------------
            seg_weight_layout = QVBoxLayout()
            seg_weight_layout.addLayout(seg_weight_inputs_layout)
            self.widgets['sp_viewer_weight_submit'] = self.wb.get_button("중량 계산")
            seg_weight_layout.addWidget(self.widgets['sp_viewer_weight_submit'])
            seg_weight_layout.addLayout(self.wb.get_label_and_line_edit_layout("중량",self.widgets,'weight_weight'))
            return seg_weight_layout
        
        def get_config_layout()->QVBoxLayout:
            seg_config0_layout = QHBoxLayout()
            seg_config0_layout.addWidget(self.wb.get_label(" "),5)        
            seg_config0_layout.addWidget(self.wb.get_label("체적"),5) 
            seg_config0_layout.addWidget(self.wb.get_label("체적비율"),7)
            seg_config0_layout.addWidget(self.wb.get_label("무게"),4)
            seg_config1_layout = QHBoxLayout()
            seg_config1_layout.addWidget(self.wb.get_label("다이아"))
            self.widgets['dia_volume'] = self.wb.get_line_edit_widget()
            seg_config1_layout.addWidget(self.widgets['dia_volume'])
            self.widgets['dia_volume_rate'] = self.wb.get_line_edit_widget()
            seg_config1_layout.addWidget(self.widgets['dia_volume_rate'])
            self.widgets['dia_weight'] = self.wb.get_line_edit_widget()
            seg_config1_layout.addWidget(self.widgets['dia_weight'])
            seg_config2_layout = QHBoxLayout()
            seg_config2_layout.addWidget(self.wb.get_label("본드"))
            self.widgets['bond_volume'] = self.wb.get_line_edit_widget()
            seg_config2_layout.addWidget(self.widgets['bond_volume'])
            self.widgets['bond_volume_rate'] = self.wb.get_line_edit_widget()
            seg_config2_layout.addWidget(self.widgets['bond_volume_rate'])
            self.widgets['bond_weight'] = self.wb.get_line_edit_widget()
            seg_config2_layout.addWidget(self.widgets['bond_weight'])
            seg_config3_layout = QHBoxLayout()
            seg_config3_layout.addWidget(self.wb.get_label("합계"))
            self.widgets['total_volume'] = self.wb.get_line_edit_widget()
            seg_config3_layout.addWidget(self.widgets['total_volume'])
            self.widgets['total_volume_rate'] = self.wb.get_line_edit_widget()
            seg_config3_layout.addWidget(self.widgets['total_volume_rate'])
            self.widgets['total_weight'] = self.wb.get_line_edit_widget()
            seg_config3_layout.addWidget(self.widgets['total_weight'])       

            seg_config4_layout = QHBoxLayout()
            seg_config4_layout.addWidget(self.wb.get_label("도징: 다이아믹스"))
            self.widgets['dosing_diamix'] = self.wb.get_line_edit_widget()
            seg_config4_layout.addWidget(self.widgets['dosing_diamix'])
            self.widgets['sp_viewer_diamix_submit'] = self.wb.get_button("작업량 계산")
            seg_config4_layout.addWidget(self.widgets['sp_viewer_diamix_submit'])

            seg_config_layout = QVBoxLayout()
            seg_config_layout.addLayout(seg_config0_layout)
            seg_config_layout.addLayout(seg_config1_layout)
            seg_config_layout.addLayout(seg_config2_layout)
            seg_config_layout.addLayout(seg_config3_layout)
            seg_config_layout.addWidget(self.wb.get_hline_widget())
            seg_config_layout.addLayout(seg_config4_layout)
            return seg_config_layout
        
        def get_density_layout()->QVBoxLayout:
            seg_density_input1_layout = QVBoxLayout()
            seg_density_input1_layout.addLayout(self.wb.get_label_and_line_edit_layout("이론밀도1",self.widgets,'density_theo_density1'))
            seg_density_input1_layout.addLayout(self.wb.get_label_and_line_edit_layout("이론밀도2",self.widgets,'density_theo_density2'))
            seg_density_input2_layout = QVBoxLayout()
            seg_density_input2_layout.addLayout(self.wb.get_label_and_line_edit_layout("최종밀도",self.widgets,'density_final_density'))
            seg_density_input2_layout.addLayout(self.wb.get_label_and_line_edit_layout("최종 상대밀도",self.widgets,'density_final_rel_density'))
            # --------------------------
            seg_density_inputs_layout = QHBoxLayout()
            seg_density_inputs_layout.addLayout(seg_density_input1_layout)
            seg_density_inputs_layout.addWidget(self.wb.get_vline_widget())
            seg_density_inputs_layout.addLayout(seg_density_input2_layout)
            # --------------------------
            seg_density_layout = QVBoxLayout()
            seg_density_layout.addWidget(QLabel("이론밀도 \n= 절대 밀도 * 본드 체적 비율 \n    + 다이아 밀도 * 다이아 체적 비율"))
            seg_density_layout.addWidget(self.wb.get_hline_widget())
            seg_density_layout.addLayout(seg_density_inputs_layout)
            return seg_density_layout
        
        def get_verification_layout()->QVBoxLayout:
            seg_verification_input1_layout = self.wb.get_label_and_line_edit_layout("본드 + 다이아 무게",self.widgets,'veri_weight')
            seg_verification_input2_layout = self.wb.get_label_and_line_edit_layout("믹스 * 수량",self.widgets,'veri_count')
            # --------------------------
            seg_verification_inputs_layout = QVBoxLayout()
            seg_verification_inputs_layout.addLayout(seg_verification_input1_layout)
            seg_verification_inputs_layout.addLayout(seg_verification_input2_layout)
            # --------------------------
            return seg_verification_inputs_layout
        
        # --------------------------
        side_button_layout = QVBoxLayout()
        self.widgets['sp_viewer_submit'] = self.wb.get_button("검수 완료")
        self.widgets['sp_viewer_image_export'] = self.wb.get_button("이미지 저장")
        self.widgets['sp_viewer_xlsx_export'] = self.wb.get_button("엑셀 저장")
        side_button_layout.addWidget(self.widgets['sp_viewer_submit'])
        side_button_layout.addWidget(self.widgets['sp_viewer_image_export'])
        side_button_layout.addWidget(self.widgets['sp_viewer_xlsx_export'])
        # -------------------------------------------------------------------------------------------
        side_layout = QVBoxLayout()
        side_layout.addWidget(QLabel("workload_layout"))
        side_layout.addLayout(self.wb.get_box_frame_layout(get_worklaod_layout()))
        side_layout.addStretch(1)
        side_layout.addWidget(QLabel("seg_weight_layout"))
        side_layout.addLayout(self.wb.get_box_frame_layout(get_weight_layout()))
        side_layout.addStretch(1)
        side_layout.addWidget(QLabel("seg_config_layout"))
        side_layout.addLayout(self.wb.get_box_frame_layout(get_config_layout()))        
        side_layout.addStretch(1)
        side_layout.addWidget(QLabel("seg_density_layout"))
        side_layout.addLayout(self.wb.get_box_frame_layout(get_density_layout()))      
        side_layout.addStretch(1)
        side_layout.addWidget(QLabel("seg_verification_layout"))
        side_layout.addLayout(self.wb.get_box_frame_layout(get_verification_layout()))                  
        side_layout.addStretch(5)
        side_layout.addLayout(side_button_layout)
        # --------------------------
        layout = QHBoxLayout()
        layout.addLayout(sp_view_layout,9)
        layout.addLayout(self.wb.get_box_frame_layout(side_layout),2)
        return layout
    
    def set_sp_view_layout(self, sp_data:dict={})->None:
        if not sp_data:
            sp_data = self.sp_data
        [self.widgets[key].setText(sp_data[key]) for key in self.widgets if key in sp_data]

    def get_sp_side_data(self)->dict:
        side_data = {key:self.widgets[key].text() for key in self.widgets if key in self.sp_data}
        self.sp_data.update(side_data)
        return side_data


    def set_sp_view_data(self,sp_data:dict={})->None:
        self.set_sp_view_layout(sp_data)
        self.get_sp_view_table().set_sp_data(sp_data)
# -------------------------------------------------------------------------------------------

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wb = WindowBuilder()
        self.setCentralWidget(self.wb.get_button("sp_view",self.open_sp_view))

    def open_sp_view(self):
        dialog = SPViewer(self,{'auto_date':"asdlfialwseijf"})
        dialog.show()
        from pprint import pprint
        pprint(dialog.get_sp_view_table().get_labeled_data())
        

# ===========================================================================================
def spv_test():
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec_()    

def spvt_test():
    app = QApplication([])
    i = SpViewTable()
    i.set_sp_data({'auto_date':"asdlfialwseijf"})
    app.exec_()

if __name__ == "__main__":
    spv_test()
