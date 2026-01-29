import sys
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QFileDialog, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout)

class ChemicalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chemical Equipment Visualizer - Desktop')
        self.setGeometry(100, 100, 900, 600)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Header Section
        self.header = QLabel("Chemical Equipment Parameter Visualizer")
        self.header.setStyleSheet("font-size: 20px; font-weight: bold; color: #4e73df;")
        self.layout.addWidget(self.header)

        # Buttons
        self.btn_layout = QHBoxLayout()
        self.upload_btn = QPushButton("Upload CSV to Backend")
        self.upload_btn.clicked.connect(self.upload_csv)
        self.pdf_btn = QPushButton("Export PDF Report")
        self.pdf_btn.clicked.connect(self.download_pdf)
        
        self.btn_layout.addWidget(self.upload_btn)
        self.btn_layout.addWidget(self.pdf_btn)
        self.layout.addLayout(self.btn_layout)

        # Summary Labels
        self.stats_label = QLabel("Total Equipment: 0 | Avg Temp: 0°C | Max Pressure: 0 bar")
        self.layout.addWidget(self.stats_label)

        # Table for Data
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'rb') as f:
                try:
                    # Consuming the Django API
