if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")

from src.module.pyqt_imports import *
from src.module.window_builder import WindowBuilder
from src.module.table_plus_widget import TablePlusWidget

class IpViewTable(TablePlusWidget):
    def __init__(self)->None:
        self.border_data = self.get_border_data()
        self.form_data = self.get_form_data()
        self.pos_data = self.get_pos_data()
        self.ip_data = {v: k for k, v in self.pos_data.items()}
        super().__init__(self.border_data,self.form_data,self.pos_data)
        self.fill_form()
        self.fill_datas_position(self.ip_data)
        self.show()
    # -------------------------------------------------------------------------------------------
    # 테두리 그리기 정보
    def get_border_data(self)->list:
        return [
            [0,7,3,3,'bold'], [0,7,1,3,''], [0,8,3,1,''],
            [4,0,3,10,'bold'],[8,0,5,10,'bold'],[14,0,13,10,'bold'],[28,0,6,10,'bold'],[35,0,4,10,'bold'],
            [4,0,3,2,''],[8,0,1,5,''],[8,0,5,2,''], [15,0,4,2,''],[19,0,4,2,''],[23,0,4,2,''],
            [28,0,2,2,''],[30,0,2,2,''],[32,0,2,2,''],[35,0,4,2,''],
            [28,0,2,8,''],[30,0,2,8,''],[32,0,2,8,''],[35,0,4,8,''],
            [4,5,3,2,''],[5,5,2,5,''],[8,5,5,5,''],[14,0,1,6,''],[14,6,1,2,''],[14,8,1,2,''],
            [15,2,2,8,''],[15,6,2,2,''],[17,2,2,8,''],[17,6,2,2,''],
            [19,2,4,8,''],[19,6,4,2,''],[23,2,4,8,''],[23,6,4,2,''],
        ]
    
    # 셀 병합 정보
    def get_form_data(self)->dict:
        return {
            'init_size' : (39,10),
            'slim_rows' : [3,7,13,27,34],
            'slim_cols' : [],
            'text_items' : {
                (1,0):[(2,5),"공구 제조 지시서", ['title']],
                (4,0):[(3,2),"제조지시   NO.",['center','bold']],
                (4,5):[(1,2),"작성일",['center','bold']],
                (5,5):[(2,2),"출고예정일",['center','bold']],
                (8,0):[(1,2),"제품명",['center','bold']],
                (9,0):[(4,2),"수량",['center','bold']],
                (14,0):[(1,6),"구성품",['center','bold']],
                (14,6):[(1,2),"수량",['center','bold']],
                (14,8):[(1,2),"비고",['center','bold']],
                (15,0):[(4,2),"세그멘트",['center','bold']],
                (19,0):[(4,2),"샹크",['center','bold']],
                (23,0):[(4,2),"기타",['center','bold']],
                (28,0):[(2,2),"용접",['center','bold']],
                (30,0):[(2,2),"드레싱",['center','bold']],
                (32,0):[(2,2),"페인트",['center','bold']],
                (35,0):[(4,2),"비고",['center','bold']],

                # # --------------------------
                (9,4):[(1,1),"개",['left']],
                (10,4):[(1,1),"개",['left']],
                (11,4):[(1,1),"개",['left']],
                (12,4):[(1,1),"개",['left']],
                (15,7):[(2,1),"개",['left']],
                (17,7):[(2,1),"개",['left']],
                (18,7):[(1,1),"개",['left']],
                (19,7):[(1,1),"개",['left']],
                (20,7):[(1,1),"개",['left']],
                (21,7):[(1,1),"개",['left']],
                (22,7):[(1,1),"개",['left']],
                (23,7):[(1,1),"개",['left']],
                (24,7):[(1,1),"개",['left']],
                (25,7):[(1,1),"개",['left']],
                (26,7):[(1,1),"개",['left']],
                (15,2):[(1,2),"세그멘트 NO.",['left']],
                (16,2):[(1,2),"(세그 제조지시 NO.)",['left']],
                (17,2):[(1,2),"세그멘트 NO.",['left']],
                (18,2):[(1,2),"(세그 제조지시 NO.)",['left']],
                # # --------------------------
                # (6,7):[(1,1),"NET",'center'],
                # # --------------------------
                (9,3):[(1,1),"",['right','editable']],
                (10,3):[(1,1),"",['right','editable']],
                (11,3):[(1,1),"",['right','editable']],
                (12,3):[(1,1),"",['right','editable']],
                (16,4):[(1,1),"",['right','editable']],
                (18,4):[(1,1),"",['right','editable']],
                (15,6):[(2,1),"",['right','editable']],
                (17,6):[(2,1),"",['right','editable']],
                (19,6):[(1,1),"",['right','editable']],                
                (20,6):[(1,1),"",['right','editable']],
                (21,6):[(1,1),"",['right','editable']],
                (22,6):[(1,1),"",['right','editable']],
                (23,6):[(1,1),"",['right','editable']],
                (24,6):[(1,1),"",['right','editable']],
                (25,6):[(1,1),"",['right','editable']],
                (26,6):[(1,1),"",['right','editable']],
                # # --------------------------
                (8,2):[(1,2),"",['left','editable']],
                (8,4):[(1,1),"",['left','editable']],
                (9,2):[(1,1),"",['left','editable']],
                (10,2):[(1,1),"",['left','editable']],
                (11,2):[(1,1),"",['left','editable']],
                (12,2):[(1,1),"",['left','editable']],
                (15,4):[(1,2),"",['left','editable']],
                (17,4):[(1,2),"",['left','editable']],
                (16,5):[(1,1),"",['left','editable']],
                (18,5):[(1,1),"",['left','editable']],
                (19,2):[(1,4),"",['left','editable']],             
                (20,2):[(1,4),"",['left','editable']],
                (21,2):[(1,4),"",['left','editable']],
                (22,2):[(1,4),"",['left','editable']],
                (23,2):[(1,4),"",['left','editable']],
                (24,2):[(1,4),"",['left','editable']],
                (25,2):[(1,4),"",['left','editable']],
                (26,2):[(1,4),"",['left','editable']],
                (28,2):[(1,8),"",['left','editable']],
                (29,2):[(1,8),"",['left','editable']],
                (30,2):[(1,8),"",['left','editable']],
                (31,2):[(1,8),"",['left','editable']],
                (32,2):[(1,8),"",['left','editable']],
                (33,2):[(1,8),"",['left','editable']],
                (35,2):[(1,8),"",['left','editable']],
                (36,2):[(1,8),"",['left','editable']],
                (37,2):[(1,8),"",['left','editable']],
                (38,2):[(1,8),"",['left','editable']],
                # # --------------------------
                (4,2):[(2,1),"", ['center','editable']],
                (4,3):[(2,2),"", ['center','editable']],
                (4,7):[(1,3),"", ['center','editable']],
                (6,2):[(1,3),"", ['center','editable']],
                (5,7):[(2,3),"", ['center','editable']],
                (8,5):[(5,5),"", ['center','editable']],

                (15,8):[(2,1),"", ['center','editable']],
                (17,8):[(2,1),"", ['center','editable']],
                (15,9):[(2,1),"", ['center','editable']],
                (17,9):[(2,1),"", ['center','editable']],
                (19,8):[(4,1),"", ['center','editable']],
                (19,8):[(4,1),"", ['center','editable']],
                (19,9):[(4,1),"", ['center','editable']],   
                # --------------------------
                (0,6):[(3,1),"결\n\n재",['right']],
                (0,7):[(1,1),"담당",['center']],
                (0,8):[(1,1),"부서장",['center']],
                (0,9):[(1,1),"사장",['center']],
            },
        }

    # db col name 과 cell position 정보 매핑
    def get_pos_data(self)->dict:
        return {
            "auto_ip_no1" :     (4,2),  # 제조지시 NO. 1
            "auto_ip_no2" :     (4,3),  # 제조지시 NO. 2
            "auto_ip_no3" :     (6,2),  # 제조지시 NO. 3
            "auto_date" :            (4,7),  # 작성일
            "due_date" :         (5,7),  # 출고예정일
            # --------------------------                               
            "item_group_name" :    (8,2),  # 제품명1
            "item1_name" :        (9,2),  # 탭1
            "item1_amount" :      (9,3),  # 탭1 수량
            "item2_name" :        (10,2), # 탭2
            "item2_amount" :      (10,3), # 탭2 수량
            "item3_name" :        (11,2), # 탭3
            "item3_amount" :      (11,3), # 탭3 수량
            "item4_name" :        (12,2), # 탭4
            "item4_amount" :      (12,3), # 탭4 수량         
            "image" :           (8,5),   # 이미지
            # --------------------------                               
            "seg1_no" :          (15,4), # 세그먼트 NO.
            "seg1_sp_no" :      (16,4),  # 세그먼트 제조지시서
            "seg1_amount" :      (15,6), # 세그먼트 수량
            "seg1_memo1" :       (15,8), # 세그먼트 비고1
            "seg1_memo2" :       (15,9), # 세그먼트 비고2       
            "seg2_no" :          (17,4),  # 세그먼트 NO.          
            "seg2_sp_no" :      (18,4),  # 세그먼트 제조지시서
            "seg2_amount" :      (17,6),  # 세그먼트 수량        
            "seg2_memo1" :       (17,8),  # 세그먼트 비고1        
            "seg2_memo2" :       (17,9),  # 세그먼트 비고2
            # --------------------------                               
            "shank1_name" :      (19,2),  # 샹크  
            "shank1_amount":     (19,6),  # 샹크 수량  
            "shank2_name" :      (20,2),  # 샹크  
            "shank2_amount":     (20,6),  # 샹크 수량  
            "shank3_name" :      (21,2),  # 샹크  
            "shank3_amount":     (21,6),  # 샹크 수량  
            "shank4_name" :      (22,2),  # 샹크  
            "shank4_amount":     (22,6),  # 샹크 수량  
            "shank_memo1" :     (19,8),  # 샹크 비고1
            "shank_memo2" :     (19,9),  # 샹크 비고2
            # --------------------------                               
            "sub1_name" :     (23,2),  # 기타
            "sub1_amount" :   (23,6),  # 기타 수량
            "sub1_memo1" :    (23,8),  # 기타 비고1
            "sub1_memo2" :    (23,9),  # 기타 비고2
            "sub2_name" :     (24,2),  # 기타
            "sub2_amount" :   (24,6),  # 기타 수량
            "sub2_memo1" :    (24,8),  # 기타 비고1
            "sub2_memo2" :    (24,9),  # 기타 비고2
            "sub3_name" :     (25,2),  # 기타
            "sub3_amount" :   (25,6),  # 기타 수량
            "sub3_memo1" :    (25,8),  # 기타 비고1
            "sub3_memo2" :    (25,9),  # 기타 비고2
            "sub4_name" :     (26,2),  # 기타
            "sub4_amount" :   (26,6),  # 기타 수량
            "sub4_memo1" :    (26,8),  # 기타 비고1
            "sub4_memo2" :    (26,9),  # 기타 비고2       
            # --------------------------                 
            "welding1" :        (28,2),  # 용접1
            "welding2" :        (29,2),  # 용접2
            "dressing1" :       (30,2),  # 드레싱1
            "dressing2" :       (31,2),  # 드레싱2
            "paint1" :          (32,2),  # 페인트1
            "paint2" :          (33,2),  # 페인트2
            "memo1" :           (35,2),  # 비고1
            "memo2" :           (36,2),  # 비고2
            "memo3" :           (37,2),  # 비고3
            "memo4" :           (38,2),  # 비고4
        }    
    # -------------------------------------------------------------------------------------------
    def set_ip_data(self,datas)->None:
        self.ip_data = datas # {'auto_date': '2024-05-12',}
        result = {self.pos_data[key]: self.ip_data[key] for key in self.pos_data if key in self.ip_data}
        self.fill_datas_position(result)
        self.show()

class IPViewer(QDialog):
    def __init__(self, parent=None, ip_data={}):
        super().__init__(parent)
        self.wb = WindowBuilder()
        self.widgets = {}
        self.ip_data = ip_data
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width() * 0.4), int(screen.height() * 0.78))

        self.setWindowTitle("IP Viewer")
        self.setLayout(self.get_ip_view_layout())
        self.get_ip_view_table().set_ip_data(self.ip_data)

    def get_ip_view_table(self)->IpViewTable:
        return self.widgets['ip_viewer_table']

    def get_ip_view_layout(self)->QHBoxLayout:
        ip_view_layout = QVBoxLayout()
        self.widgets['ip_viewer_table'] = IpViewTable()
        ip_view_layout.addWidget(self.widgets['ip_viewer_table'])

        side_button_layout = QVBoxLayout()
        self.widgets['ip_viewer_submit'] = self.wb.get_button("검수 완료")
        self.widgets['ip_viewer_image_export'] = self.wb.get_button("이미지 저장")
        self.widgets['ip_viewer_xlsx_export'] = self.wb.get_button("엑셀 저장")
        side_button_layout.addWidget(QLabel("This is a sub dialog"))
        side_button_layout.addWidget(self.widgets['ip_viewer_submit'])
        side_button_layout.addWidget(self.widgets['ip_viewer_image_export'])
        side_button_layout.addWidget(self.widgets['ip_viewer_xlsx_export'])

        layout = QHBoxLayout()
        layout.addLayout(ip_view_layout)
        layout.addLayout(self.wb.get_box_frame_layout(side_button_layout))
        return layout
        
# -------------------------------------------------------------------------------------------

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wb = WindowBuilder()
        self.setCentralWidget(self.wb.get_button("ip_view",self.open_ip_view))

    def open_ip_view(self):
        dialog = IPViewer(self)
        dialog.show()
        from pprint import pprint
        pprint(dialog.get_ip_view_table().get_labeled_data())
        

# ===========================================================================================
def ipv_test():
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec_()    

def ipvt_test():
    app = QApplication([])
    i = IpViewTable()
    i.set_ip_data({(0,0):"asdlfialwseijf"})
    app.exec_()

if __name__ == "__main__":
    ipv_test()
