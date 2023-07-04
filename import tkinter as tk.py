import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout

class ModelAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("執行模型分析")
        self.resize(400, 200)

        self.current_step = 1

        self.layout = QVBoxLayout()

        self.step_label = QLabel("步驟 1: 選擇文字檔案", self)
        self.layout.addWidget(self.step_label)

        self.choose_text_button = QPushButton("選擇文字檔案", self)
        self.choose_text_button.clicked.connect(self.choose_text_file)
        self.layout.addWidget(self.choose_text_button)

        self.next_button = QPushButton("下一步", self)
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.show_next_step)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)

    def choose_text_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "選擇文字檔案", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            self.text_file_path = file_path
            self.next_button.setEnabled(True)

    def show_next_step(self):
        self.layout.removeWidget(self.step_label)
        self.layout.removeWidget(self.choose_text_button)
        self.layout.removeWidget(self.next_button)

        if self.current_step == 1:
            self.current_step = 2
            self.step_label.setText("步驟 2: 選擇EXCEL檔案")
            self.choose_excel_button = QPushButton("選擇EXCEL檔案", self)
            self.choose_excel_button.clicked.connect(self.choose_excel_file)
            self.layout.addWidget(self.step_label)
            self.layout.addWidget(self.choose_excel_button)
        elif self.current_step == 2:
            self.current_step = 3
            self.step_label.setText("步驟 3: 進行分析")
            self.analyze_button = QPushButton("進行分析", self)
            self.analyze_button.clicked.connect(self.perform_analysis)
            self.layout.addWidget(self.step_label)
            self.layout.addWidget(self.analyze_button)

    def choose_excel_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "選擇EXCEL檔案", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            self.excel_file_path = file_path
            self.analyze_button.setEnabled(True)

    def perform_analysis(self):
        # 假设这里进行模型分析并生成result.xlsx
        result_file_path = os.path.join(os.path.dirname(self.excel_file_path), "result.xlsx")
        self.show_result(result_file_path)

    def show_result(self, file_path):
        self.layout.removeWidget(self.step_label)
        self.layout.removeWidget(self.choose_excel_button)
        self.layout.removeWidget(self.analyze_button)

        self.result_label = QLabel("分析成功，結果已存儲於以下檔案:", self)
        self.layout.addWidget(self.result_label)

        self.result_file_label = QLabel(file_path, self)
        self.layout.addWidget(self.result_file_label)

        # TODO: 在这里添加显示Excel内容和图片的代码

app = QApplication(sys.argv)
window = ModelAnalysisApp()
window.show()
sys.exit(app.exec_())
