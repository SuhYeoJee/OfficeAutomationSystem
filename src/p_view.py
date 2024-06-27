if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
# -------------------------------------------------------------------------------------------
from src.module.pyqt_imports import *
from src.module.window_builder import WindowBuilder
from src.module.table_plus_widget import TablePlusWidget
from src.data.p_table import pTableForm as TF
# ===========================================================================================


class pTable(TablePlusWidget):
    def __init__(self,is_sp:bool=True)->None:
        if is_sp:   #sp 테이블 생성
            super().__init__(TF.SP_BORDER,TF.SP_FORM,TF.SP_POS)
            self.pos_data = TF.SP_POS
        else:       # ip 테이블 생성
            super().__init__(TF.IP_BORDER,TF.IP_FORM,TF.IP_POS)
            self.pos_data = TF.IP_POS
        self.ptable_data = {v: k for k, v in self.pos_data.items()} # 초깃값
        # -------------------------------------------------------------------------------------------
        self.fill_form()
        self.fill_datas_position(self.ptable_data)
        self.show()
    # ===========================================================================================
    def set_ptable_data(self,datas)->None:
        self.ptable_data = datas
        result = {self.pos_data[key]: self.ptable_data[key] for key in self.pos_data if key in self.ptable_data}
        self.fill_datas_position(result)
        self.show()

class pView(QDialog):
    def __init__(self, parent=None, ptable_data={}, is_sp:bool=True):
        super().__init__(parent)
        self.wb = WindowBuilder()
        self.widgets = {}
        self.ptable_data = ptable_data
        screen = QDesktopWidget().screenGeometry()
        if is_sp:   #sp 뷰어 생성
            self.setWindowTitle("SP Viewer")
            self.resize(int(screen.width() * 0.5), int(screen.height() * 0.78))
            self.setLayout(self.get_sp_view_layout())
        else:       #ip 뷰어 생성
            self.setWindowTitle("IP Viewer")
            self.resize(int(screen.width() * 0.4), int(screen.height() * 0.78))
            self.setLayout(self.get_ip_view_layout())
        self.widgets['ptable'].set_ptable_data(ptable_data) # 값 입력
        if is_sp:
            self.set_sp_view_layout(ptable_data)

    # ===========================================================================================
    def get_ip_view_layout(self)->QHBoxLayout:
        ip_view_layout = QVBoxLayout()
        self.widgets['ptable'] = pTable(False)
        ip_view_layout.addWidget(self.widgets['ptable'])

        side_button_layout = QVBoxLayout()
        self.widgets['submit'] = self.wb.get_button("검수 완료")
        self.widgets['image_export'] = self.wb.get_button("이미지 저장")
        self.widgets['xlsx_export'] = self.wb.get_button("엑셀 저장")
        side_button_layout.addWidget(QLabel("This is a sub dialog")) #temp
        side_button_layout.addWidget(self.widgets['submit'])
        side_button_layout.addWidget(self.widgets['image_export'])
        side_button_layout.addWidget(self.widgets['xlsx_export'])

        layout = QHBoxLayout()
        layout.addLayout(ip_view_layout)
        layout.addLayout(self.wb.get_box_frame_layout(side_button_layout))
        return layout
    # ===========================================================================================
    def get_sp_view_layout(self)->QHBoxLayout:
        sp_view_layout = QVBoxLayout()
        self.widgets['ptable'] = pTable()
        sp_view_layout.addWidget(self.widgets['ptable'])
        # -------------------------------------------------------------------------------------------
        # 사이드 레이아웃
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
        self.widgets['submit'] = self.wb.get_button("검수 완료")
        self.widgets['image_export'] = self.wb.get_button("이미지 저장")
        self.widgets['xlsx_export'] = self.wb.get_button("엑셀 저장")
        side_button_layout.addWidget(self.widgets['submit'])
        side_button_layout.addWidget(self.widgets['image_export'])
        side_button_layout.addWidget(self.widgets['xlsx_export'])
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
    
    # 사이드 레이아웃 값 지정
    def set_sp_view_layout(self, sp_data:dict={})->None:
        if not sp_data:
            sp_data = self.sp_data
        [self.widgets[key].setText(sp_data[key]) for key in self.widgets if key in sp_data]

    # sp 사이드, 표 값 지정
    def set_sp_view_data(self,sp_data:dict={})->None:
        self.set_sp_view_layout(sp_data)
        self.widgets['pTable'].set_sp_data(sp_data)

    # 사이드 레이아웃 읽기
    def get_sp_side_data(self)->dict:
        side_data = {key:self.widgets[key].text() for key in self.widgets if key in self.sp_data}
        self.sp_data.update(side_data)
        return side_data
    # ===========================================================================================
    
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setCentralWidget(WindowBuilder().get_button("ip_view",self.open_ip_view))
        self.setCentralWidget(WindowBuilder().get_button("sp_view",self.open_sp_view))

    def open_ip_view(self):
        dialog = pView(self,{'creation_date':"작성일 값 지정"},is_sp=False)
        dialog.show()

    def open_sp_view(self):
        dialog = pView(self,{'creation_date':"작성일 값 지정",'veri_count':'수량 값'},is_sp=True)
        dialog.show()        
        
if __name__ == "__main__":
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec_()
