from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLabel, QTableWidgetItem, QHeaderView, QVBoxLayout, QFrame, QSizePolicy, QLineEdit
from PyQt5.QtGui import QFont, QColor
from tbs import TableSetup
from PyQt5.QtCore import Qt

class ItemOrderForm(TableSetup):
    def __init__(self):
        TableSetup.__init__(self)
        self.tableWidgetRCDict = self.getTableWidgetRCDict() #{"cellName":('r','c')}
    
    def saveToDB(self):... #DB 저장하기 클릭시 호출
    def saveTableImage(self):... #파일로 저장하기 클릭시 호출
    def saveToElsx(self):... #엑셀로 저장하기 클릭시 호출
    def clearAll(self):... # 내용 지우기 클릭시 호출
    
    # form 좌표 호출
    def getTableWidgetRCDict(self):
        return {
            "mfgOrderNo1" :     (4,2),  # 제조지시 NO. 1
            "mfgOrderNo2" :     (4,3),  # 제조지시 NO. 2
            "mfgOrderNo3" :     (6,2),  # 제조지시 NO. 3
            "date" :            (4,7),  # 작성일
            "dueDate" :         (5,7),  # 출고예정일
            "productName1" :    (8,2),  # 제품명1
            "tab1Name" :        (9,2),  # 탭1
            "tab1Amount" :      (9,3),  # 탭1 수량
            "tab2Name" :        (10,2), # 탭2
            "tab2Amount" :      (10,3), # 탭2 수량
            "tab3Name" :        (11,2), # 탭3
            "tab3Amount" :      (11,3), # 탭3 수량
            "tab4Name" :        (12,2), # 탭4
            "tab4Amount" :      (12,3), # 탭4 수량         
            "image" :           (8,5),  # 이미지
            "seg1No" :          (15,4), # 세그먼트 NO.
            "seg1Amount" :      (15,6), # 세그먼트 수량
            "seg1Memo1" :       (15,8), # 세그먼트 비고1
            "seg1Memo2" :       (15,9), # 세그먼트 비고2       
            "seg2No" :          (17,4),  # 세그먼트 NO.          
            "seg2Amount" :      (17,6),  # 세그먼트 수량        
            "seg2Memo1" :       (17,8),  # 세그먼트 비고1        
            "seg2Memo2" :       (17,9),  # 세그먼트 비고2
            "shank1Name" :      (19,2),  # 샹크  
            "shank1Amount":     (19,6),  # 샹크 수량  
            "shank1Memo1" :     (19,8),  # 샹크 비고1
            "shank1Memo2" :     (19,9),  # 샹크 비고2
            "shank2Name" :      (20,2),  # 샹크  
            "shank2Amount":     (20,6),  # 샹크 수량  
            "shank2Memo1" :     (20,8),  # 샹크 비고1
            "shank2Memo2" :     (20,9),  # 샹크 비고2
            "shank3Name" :      (21,2),  # 샹크  
            "shank3Amount":     (21,6),  # 샹크 수량  
            "shank3Memo1" :     (21,8),  # 샹크 비고1
            "shank3Memo2" :     (21,9),  # 샹크 비고2
            "shank4Name" :      (22,2),  # 샹크  
            "shank4Amount":     (22,6),  # 샹크 수량  
            "shank4Memo1" :     (22,8),  # 샹크 비고1
            "shank4Memo2" :     (22,9),  # 샹크 비고2                        
            "others1Name" :     (23,2),  # 기타
            "others1Amount" :   (23,6),  # 기타 수량
            "others1Memo1" :    (23,8),  # 기타 비고1
            "others1Memo2" :    (23,9),  # 기타 비고2
            "others2Name" :     (24,2),  # 기타
            "others2Amount" :   (24,6),  # 기타 수량
            "others2Memo1" :    (24,8),  # 기타 비고1
            "others2Memo2" :    (24,9),  # 기타 비고2
            "others3Name" :     (25,2),  # 기타
            "others3Amount" :   (25,6),  # 기타 수량
            "others3Memo1" :    (25,8),  # 기타 비고1
            "others3Memo2" :    (25,9),  # 기타 비고2
            "others4Name" :     (26,2),  # 기타
            "others4Amount" :   (26,6),  # 기타 수량
            "others4Memo1" :    (26,8),  # 기타 비고1
            "others4Memo2" :    (26,9),  # 기타 비고2                        
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

    #테두리 그리기 정보
    def getBoxInfo(self):
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


    # ===========================================================================================

    # tableWidget에 form 그리기
    def setNewForm(self):
        self.tableWidget.clear()
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.initTable(39,10)
        for i in range(39):
            for j in range(10):
                t = QTableWidgetItem("")
                t.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i,j,t)

        def setCellNotEditable(item):
            item.setFlags(item.flags() & ~item.flags() | ~Qt.ItemIsEditable)

        def setCell(row,col,rowspan,colspan,text,cellType):
            item = QTableWidgetItem(str(text))

            if 'input' not in cellType:
                setCellNotEditable(item)
                item.setForeground(QColor(128,128,128))

            if 'black' in cellType:
                item.setForeground(QColor(0,0,0))
            elif 'red' in cellType:
                item.setForeground(QColor(255,0,0))

            if 'bold' in cellType:
                font = QFont("Arial", 12)
                font.setBold(True)
                item.setFont(font)                

            if 'title' in cellType:
                from PyQt5.QtGui import QFontDatabase
                HMKMRHD = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont("./font/HMKMRHD.TTF"))[0]
                font = QFont(HMKMRHD, 20)
                item.setFont(font)

            if 'center' in cellType:
                item.setTextAlignment(Qt.AlignCenter)
            elif 'right' in cellType:
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            elif 'left' in cellType:
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            if not (rowspan == 1 and colspan == 1):
                self.tableWidget.setSpan(row,col,rowspan,colspan)
            self.tableWidget.setItem(row,col, item)    
        # -------------------------------------------------------------------------------------------
        [self.tableWidget.setRowHeight(x, 10) for x in [3,7,13,27,34]] #작은 공백


        setCell(1,0,2,5,"공구 제조 지시서", 'title')
        # --------------------------
        setCell(4,0,3,2,"제조지시   NO.",'centerbold')
        setCell(4,5,1,2,"작성일",'centerbold')
        setCell(5,5,2,2,"출고예정일",'centerbold')
        setCell(8,0,1,2,"제품명",'centerbold') 
        setCell(9,0,4,2,"수량",'centerbold') 
        setCell(14,0,1,6,"구성품",'centerbold') 
        setCell(14,6,1,2,"수량",'centerbold') 
        setCell(14,8,1,2,"비고",'centerbold') 
        setCell(15,0,4,2,"세그멘트",'centerbold') 
        setCell(19,0,4,2,"샹크",'centerbold') 
        setCell(23,0,4,2,"기타",'centerbold') 
        setCell(28,0,2,2,"용접",'centerbold') 
        setCell(30,0,2,2,"드레싱",'centerbold') 
        setCell(32,0,2,2,"페인트",'centerbold') 
        setCell(35,0,4,2,"비고",'centerbold') 

        # # --------------------------
        setCell(9,4,1,1,"개",'left')
        setCell(10,4,1,1,"개",'left')
        setCell(11,4,1,1,"개",'left')
        setCell(12,4,1,1,"개",'left')
        setCell(15,7,2,1,"개",'left')
        setCell(17,7,2,1,"개",'left')
        setCell(18,7,1,1,"개",'left')
        setCell(19,7,1,1,"개",'left')
        setCell(20,7,1,1,"개",'left')
        setCell(21,7,1,1,"개",'left')
        setCell(22,7,1,1,"개",'left')
        setCell(23,7,1,1,"개",'left')
        setCell(24,7,1,1,"개",'left')
        setCell(25,7,1,1,"개",'left')
        setCell(26,7,1,1,"개",'left')
        setCell(15,2,1,2,"세그멘트 NO.",'left')
        setCell(16,2,1,2,"(세그 제조지시 NO.)",'left')
        setCell(17,2,1,2,"세그멘트 NO.",'left')
        setCell(18,2,1,2,"(세그 제조지시 NO.)",'left')
        # # --------------------------
        # setCell(6,7,1,1,"NET",'center')
        # # --------------------------
        setCell(9,3,1,1,"",'rightinput') 
        setCell(10,3,1,1,"",'rightinput') 
        setCell(11,3,1,1,"",'rightinput') 
        setCell(12,3,1,1,"",'rightinput') 
        setCell(16,4,1,1,"",'rightinput') 
        setCell(18,4,1,1,"",'rightinput') 
        setCell(15,6,2,1,"",'rightinput') 
        setCell(17,6,2,1,"",'rightinput') 
        setCell(19,6,1,1,"",'rightinput') 
        setCell(20,6,1,1,"",'rightinput') 
        setCell(21,6,1,1,"",'rightinput') 
        setCell(22,6,1,1,"",'rightinput') 
        setCell(23,6,1,1,"",'rightinput') 
        setCell(24,6,1,1,"",'rightinput') 
        setCell(25,6,1,1,"",'rightinput') 
        setCell(26,6,1,1,"",'rightinput') 
        # # --------------------------
        setCell(8,2,1,2,"",'leftinput')
        setCell(8,4,1,1,"",'leftinput')
        setCell(9,2,1,1,"",'leftinput')
        setCell(10,2,1,1,"",'leftinput')
        setCell(11,2,1,1,"",'leftinput')
        setCell(12,2,1,1,"",'leftinput')
        setCell(15,4,1,2,"",'leftinput')
        setCell(17,4,1,2,"",'leftinput')
        setCell(16,5,1,1,"",'leftinput')
        setCell(18,5,1,1,"",'leftinput')
        setCell(19,2,1,4,"",'leftinput')
        setCell(20,2,1,4,"",'leftinput')
        setCell(21,2,1,4,"",'leftinput')
        setCell(22,2,1,4,"",'leftinput')
        setCell(23,2,1,4,"",'leftinput')
        setCell(24,2,1,4,"",'leftinput')
        setCell(25,2,1,4,"",'leftinput')
        setCell(26,2,1,4,"",'leftinput')
        setCell(28,2,1,8,"",'leftinput')
        setCell(29,2,1,8,"",'leftinput')
        setCell(30,2,1,8,"",'leftinput')
        setCell(31,2,1,8,"",'leftinput')
        setCell(32,2,1,8,"",'leftinput')
        setCell(33,2,1,8,"",'leftinput')
        setCell(35,2,1,8,"",'leftinput')
        setCell(36,2,1,8,"",'leftinput')
        setCell(37,2,1,8,"",'leftinput')
        setCell(38,2,1,8,"",'leftinput')
        # # --------------------------
        setCell(4,2,2,1,"", 'centerinput')
        setCell(4,3,2,2,"", 'centerinput')
        setCell(4,7,1,3,"", 'centerinput')
        setCell(6,2,1,3,"", 'centerinput')
        setCell(5,7,2,3,"", 'centerinput')
        setCell(8,5,5,5,"", 'centerinput')
        # --------------------------
        setCell(0,6,3,1,"결\n\n재",'right')
        setCell(0,7,1,1,"담당",'center')
        setCell(0,8,1,1,"부서장",'center')
        setCell(0,9,1,1,"사장",'center')
        # --------------------------
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# ===========================================================================================

    def getButtonLayout(self):
        self.saveButton = QPushButton("DB에 저장하기")
        self.saveButton.clicked.connect(self.saveToDB)

        self.fileButton = QPushButton("파일로 저장하기")
        self.fileButton.clicked.connect(self.saveTableImage)

        self.xlsxButton = QPushButton("엑셀로 저장하기")
        self.xlsxButton.clicked.connect(self.saveToElsx)        

        self.clearButton = QPushButton("내용 지우기")
        self.clearButton.clicked.connect(self.clearAll)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(self.fileButton)
        buttonLayout.addWidget(self.xlsxButton)
        buttonLayout.addSpacing(80)
        buttonLayout.addWidget(self.clearButton)

        return buttonLayout
    