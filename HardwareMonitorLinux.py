import sys
import psutil
import platform
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                            QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QFont
import subprocess

class HardwareMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hardware Monitor - Linux")
        self.setMinimumSize(800, 600)
        
        # Arc theme colors
        self.colors = {
            'background': QColor(47, 52, 63),
            'foreground': QColor(211, 218, 227),
            'accent': QColor(82, 148, 226),
            'tab_active': QColor(56, 60, 74),
            'tab_inactive': QColor(47, 52, 63)
        }
        
        # Setup fonts
        self.header_font = QFont("Ubuntu", 10, QFont.Weight.Bold)
        self.content_font = QFont("Ubuntu", 9)
        
        self.setup_ui()
        self.setup_timers()
        
    def setup_ui(self):
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {self.colors['background'].name()};
                color: {self.colors['foreground'].name()};
            }}
            QTabWidget::pane {{
                border: 1px solid {self.colors['accent'].name()};
                background-color: {self.colors['background'].name()};
            }}
            QTabBar::tab {{
                background-color: {self.colors['tab_inactive'].name()};
                color: {self.colors['foreground'].name()};
                padding: 8px 20px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }}
            QTabBar::tab:selected {{
                background-color: {self.colors['tab_active'].name()};
            }}
            QTableWidget {{
                background-color: {self.colors['background'].name()};
                color: {self.colors['foreground'].name()};
                gridline-color: {self.colors['accent'].name()};
            }}
            QHeaderView::section {{
                background-color: {self.colors['tab_active'].name()};
                color: {self.colors['foreground'].name()};
                padding: 5px;
            }}
        """)
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Create tabs
        self.cpu_tab = self.create_info_tab()
        self.ram_tab = self.create_info_tab()
        self.gpu_tab = self.create_info_tab()
        self.system_tab = self.create_info_tab()
        
        # Add tabs with custom colors
        self.tabs.addTab(self.cpu_tab, "CPU")
        self.tabs.addTab(self.ram_tab, "RAM")
        self.tabs.addTab(self.gpu_tab, "GPU")
        self.tabs.addTab(self.system_tab, "System")
        
        # Initial update
        self.update_all_info()
    
    def create_info_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        table = QTableWidget()
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Information", "Value"])
        table.horizontalHeader().setStretchLastSection(True)
        table.setAlternatingRowColors(True)
        
        layout.addWidget(table)
        tab.setLayout(layout)
        return tab
    
    def setup_timers(self):
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_all_info)
        self.update_timer.start(3000)  # Update every 3 seconds
    
    def update_all_info(self):
        self.update_cpu_info()
        self.update_ram_info()
        self.update_gpu_info()
        self.update_system_info()
    
    def update_cpu_info(self):
        table = self.cpu_tab.layout().itemAt(0).widget()
        table.setRowCount(0)
        
        # CPU Information
        cpu_info = {
            "CPU Model": platform.processor(),
            "Physical Cores": psutil.cpu_count(logical=False),
            "Logical Cores": psutil.cpu_count(),
            "Current Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
            "CPU Usage": f"{psutil.cpu_percent()}%",
        }
        
        self.add_info_to_table(table, "== CPU Information ==", "")
        for key, value in cpu_info.items():
            self.add_info_to_table(table, key, str(value))
            
        # CPU Temperature (if available)
        try:
            temperatures = psutil.sensors_temperatures()
            if 'coretemp' in temperatures:
                self.add_info_to_table(table, "== CPU Temperatures ==", "")
                for entry in temperatures['coretemp']:
                    self.add_info_to_table(table, entry.label, f"{entry.current}°C")
        except:
            pass
    
    def update_ram_info(self):
        table = self.ram_tab.layout().itemAt(0).widget()
        table.setRowCount(0)
        
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        ram_info = {
            "Total Memory": f"{memory.total / (1024**3):.2f} GB",
            "Available Memory": f"{memory.available / (1024**3):.2f} GB",
            "Used Memory": f"{memory.used / (1024**3):.2f} GB",
            "Memory Percentage": f"{memory.percent}%",
            "Swap Total": f"{swap.total / (1024**3):.2f} GB",
            "Swap Used": f"{swap.used / (1024**3):.2f} GB",
            "Swap Free": f"{swap.free / (1024**3):.2f} GB",
        }
        
        self.add_info_to_table(table, "== Memory Information ==", "")
        for key, value in ram_info.items():
            self.add_info_to_table(table, key, str(value))
    
    def update_gpu_info(self):
        table = self.gpu_tab.layout().itemAt(0).widget()
        table.setRowCount(0)
        
        # Try to get GPU information using nvidia-smi if available
        try:
            gpu_info = subprocess.check_output(['nvidia-smi', '--query-gpu=name,temperature.gpu,memory.total,memory.used,memory.free,utilization.gpu', '--format=csv,noheader']).decode()
            gpu_data = gpu_info.strip().split(',')
            
            self.add_info_to_table(table, "== NVIDIA GPU Information ==", "")
            self.add_info_to_table(table, "GPU Model", gpu_data[0])
            self.add_info_to_table(table, "Temperature", f"{gpu_data[1].strip()}°C")
            self.add_info_to_table(table, "Total Memory", gpu_data[2].strip())
            self.add_info_to_table(table, "Used Memory", gpu_data[3].strip())
            self.add_info_to_table(table, "Free Memory", gpu_data[4].strip())
            self.add_info_to_table(table, "GPU Utilization", gpu_data[5].strip())
        except:
            # Fallback to basic display information
            try:
                display_info = subprocess.check_output(['xrandr']).decode()
                self.add_info_to_table(table, "== Display Information ==", "")
                for line in display_info.split('\n'):
                    if ' connected ' in line:
                        self.add_info_to_table(table, "Display", line.split()[0])
                        self.add_info_to_table(table, "Resolution", line.split()[2])
            except:
                self.add_info_to_table(table, "GPU Information", "Not available")
    
    def update_system_info(self):
        table = self.system_tab.layout().itemAt(0).widget()
        table.setRowCount(0)
        
        system_info = {
            "OS": platform.system(),
            "Distribution": platform.freedesktop_os_release()['PRETTY_NAME'] if hasattr(platform, 'freedesktop_os_release') else platform.linux_distribution()[0],
            "Kernel Version": platform.release(),
            "Architecture": platform.machine(),
            "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        self.add_info_to_table(table, "== System Information ==", "")
        for key, value in system_info.items():
            self.add_info_to_table(table, key, str(value))
    
    def add_info_to_table(self, table, label, value):
        row = table.rowCount()
        table.insertRow(row)
        
        label_item = QTableWidgetItem(label)
        value_item = QTableWidgetItem(value)
        
        if label.startswith("=="):
            label_item.setFont(self.header_font)
            label_item.setForeground(self.colors['accent'])
        else:
            label_item.setFont(self.content_font)
            value_item.setFont(self.content_font)
        
        table.setItem(row, 0, label_item)
        table.setItem(row, 1, value_item)

def main():
    app = QApplication(sys.argv)
    window = HardwareMonitor()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
