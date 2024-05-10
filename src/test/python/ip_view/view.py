if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")

from src.module.pyqt_imports import *
from src.module.window_builder import WindowBuilder

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wb = WindowBuilder()
        self.setCentralWidget(self.wb.get_button("ip_view",self.open_ip_view))

    def open_ip_view(self):
        dialog = IPViewer(self,{"col1":"val1","col2":"val2","col3":"val3",})
        dialog.show()

class IPViewer(QDialog):
    def __init__(self, parent=None, ip_data={}):
        super().__init__(parent)
        print(ip_data)
        self.wb = WindowBuilder()

        self.setWindowTitle("IP Viewer")
        self.setLayout(self.get_ip_view_layout())

    def get_ip_view_layout(self):
        ip_view_layout = QVBoxLayout()
        ip_view_layout.addWidget(QLabel("This is a sub dialog"))



        layout = self.wb.get_box_frame_layout(ip_view_layout)
        return layout
        
if __name__ == "__main__":
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec_()    

