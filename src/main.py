import sys, math
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QSplitter,
QAction, QTextEdit, QToolBar, QDockWidget, QVBoxLayout, QHBoxLayout, QAction, QFrame,
QLabel, QLineEdit, QGridLayout, QTableWidget, QHeaderView, QTableView, QTableWidgetItem)

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.initializeUI()

    def initializeUI(self):

        self.setFixedSize(900,600)
        self.setWindowTitle("Hemodynamics Calculator")
        self.parametersWindow()
        self.show()

    def parametersWindow(self):

        weight_lbl = QLabel("Weight [kg]")
        self.weight_entry = QLineEdit()
        self.weight_entry.setMaximumWidth(200)

        height_lbl = QLabel("Height [cm]")
        self.height_entry = QLineEdit()
        self.height_entry.setMaximumWidth(200)

        hb_lbl = QLabel("Hb [g/dL]")
        self.hb_entry = QLineEdit()
        self.hb_entry.setMaximumWidth(200)

        ao_sat_lbl = QLabel("Aorta Sat")
        self.ao_sat_entry = QLineEdit()
        self.ao_sat_entry.setMaximumWidth(200)

        aosp_lbl = QLabel("AO Sys Pressure")
        self.aosp_entry = QLineEdit()
        self.aosp_entry.setMaximumWidth(200)

        aodp_lbl = QLabel("AO Dias Pressure")
        self.aodp_entry = QLineEdit()
        self.aodp_entry.setMaximumWidth(200)

        aomp_lbl = QLabel("AO Mean Pressure")
        self.aomp_entry = QLineEdit()
        self.aomp_entry.setMaximumWidth(200)

        pa_sat_lbl = QLabel("PA Sat")
        self.pa_sat_entry = QLineEdit()
        self.pa_sat_entry.setMaximumWidth(200)

        pasp_lbl = QLabel("PA Sys Pressure")
        self.pasp_entry = QLineEdit()
        self.pasp_entry.setMaximumWidth(200)

        padp_lbl = QLabel("PA Dias Pressure")
        self.padp_entry = QLineEdit()
        self.padp_entry.setMaximumWidth(200)

        pamp_lbl = QLabel("PA Mean Pressure")
        self.pamp_entry = QLineEdit()
        self.pamp_entry.setMaximumWidth(200)

        pcwp_lbl = QLabel("PA Wedge Pressure")
        self.pcwp_entry = QLineEdit()
        self.pcwp_entry.setMaximumWidth(200)

        rap_lbl = QLabel("RA Mean Pressure")
        self.rap_entry = QLineEdit()
        self.rap_entry.setMaximumWidth(200)

        ivc_sat_lbl = QLabel("IVC Sat")
        self.ivc_sat_entry = QLineEdit()
        self.ivc_sat_entry.setMaximumWidth(200)

        svc_sat_lbl = QLabel("SVC Sat")
        self.svc_sat_entry = QLineEdit()
        self.svc_sat_entry.setMaximumWidth(200)

        pv_sat_lbl = QLabel("PV Sat")
        self.pv_sat_entry = QLineEdit()
        self.pv_sat_entry.setMaximumWidth(200)
 
        self.apply_btn = QPushButton("Apply")
        self.apply_btn.setEnabled(True)
        self.apply_btn.clicked.connect(self.calculatorEngine)

        mid_panel_v_box = QVBoxLayout()
        mid_panel_v_box.setAlignment(Qt.AlignTop)

        side_panel_v_box = QVBoxLayout()
        side_panel_v_box.setAlignment(Qt.AlignTop)

        calc_panel_v_box = QVBoxLayout()
        calc_panel_v_box.setAlignment(Qt.AlignTop)
        
        side_panel_v_box.addWidget(weight_lbl)
        side_panel_v_box.addWidget(self.weight_entry)
        side_panel_v_box.addSpacing(2)

        side_panel_v_box.addWidget(height_lbl)
        side_panel_v_box.addWidget(self.height_entry)
        side_panel_v_box.addSpacing(2)

        side_panel_v_box.addWidget(hb_lbl)
        side_panel_v_box.addWidget(self.hb_entry)
        side_panel_v_box.addSpacing(2)

        side_panel_v_box.addWidget(ao_sat_lbl)
        side_panel_v_box.addWidget(self.ao_sat_entry)
        side_panel_v_box.addSpacing(2)
        
        side_panel_v_box.addWidget(pa_sat_lbl)
        side_panel_v_box.addWidget(self.pa_sat_entry)
        side_panel_v_box.addSpacing(2)
        
        side_panel_v_box.addWidget(svc_sat_lbl)
        side_panel_v_box.addWidget(self.svc_sat_entry)
        side_panel_v_box.addSpacing(2)

        side_panel_v_box.addWidget(ivc_sat_lbl)
        side_panel_v_box.addWidget(self.ivc_sat_entry)
        side_panel_v_box.addSpacing(2)

        side_panel_v_box.addWidget(pv_sat_lbl)
        side_panel_v_box.addWidget(self.pv_sat_entry)

        mid_panel_v_box.addWidget(aosp_lbl)
        mid_panel_v_box.addWidget(self.aosp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(aodp_lbl)
        mid_panel_v_box.addWidget(self.aodp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(aomp_lbl)
        mid_panel_v_box.addWidget(self.aomp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(pasp_lbl)
        mid_panel_v_box.addWidget(self.pasp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(padp_lbl)
        mid_panel_v_box.addWidget(self.padp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(pamp_lbl)
        mid_panel_v_box.addWidget(self.pamp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(pcwp_lbl)
        mid_panel_v_box.addWidget(self.pcwp_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addWidget(rap_lbl)
        mid_panel_v_box.addWidget(self.rap_entry)
        mid_panel_v_box.addSpacing(2)

        mid_panel_v_box.addSpacing(160)
        mid_panel_v_box.addWidget(self.apply_btn)

        calc_lbl = QLabel("Calculations")
        calc_lbl.setFont(QFont("calibri", 15, QFont.Bold))

        self.co_calc = QLabel("Cardiac Output:  ")
        self.ci_calc = QLabel("Cardiac Index:  ")
        self.svr_calc = QLabel("SVR:  ")
        self.pvr_calc = QLabel("PVR:  ")
        self.tpg_calc = QLabel("TPR:  ")
        self.dpg_calc = QLabel("DPG:  ")

        calc_panel_v_box.addWidget(calc_lbl)
        calc_panel_v_box.addSpacing(2)

        self.calc_tbl = QTableWidget()
        self.calc_tbl.setRowCount(9)

        self.calc_tbl.setColumnCount(2)

        self.calc_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.calc_tbl.verticalHeader().setVisible(False)
        self.calc_tbl.horizontalHeader().setVisible(False)

        self.calc_tbl.setEditTriggers(QTableView.NoEditTriggers)
        
        self.calc_tbl.setItem(0,0, QTableWidgetItem("Cardiac Output (L/min)"))
        self.calc_tbl.setItem(1,0, QTableWidgetItem("Cardiac Index (L/min/m2)"))
        self.calc_tbl.setItem(2,0, QTableWidgetItem("SVR (Dynes.sec.cm-5)"))
        self.calc_tbl.setItem(3,0, QTableWidgetItem("SVR (Wood)"))

        self.calc_tbl.setItem(4,0, QTableWidgetItem("PVR (Dynes.sec.cm-5)"))
        self.calc_tbl.setItem(5,0, QTableWidgetItem("PVR (Wood)"))

        self.calc_tbl.setItem(6,0, QTableWidgetItem("TPG (mmHg)"))
        self.calc_tbl.setItem(7,0, QTableWidgetItem("DPG (mmHg)"))
                
        self.calc_tbl.setItem(8,0, QTableWidgetItem("Qp/Qs"))

        calc_panel_v_box.addWidget(self.calc_tbl)

        side_panel_frame = QFrame()
        side_panel_frame.setMaximumWidth(200)
        side_panel_frame.setFrameStyle(QFrame.WinPanel)
        side_panel_frame.setLayout(side_panel_v_box)

        mid_panel_frame = QFrame()
        mid_panel_frame.setMaximumWidth(200)
        mid_panel_frame.setFrameStyle(QFrame.WinPanel)
        mid_panel_frame.setLayout(mid_panel_v_box)

        calc_panel_frame = QFrame()
        calc_panel_frame.setMinimumWidth(200)
        calc_panel_frame.setFrameStyle(QFrame.WinPanel)
        calc_panel_frame.setLayout(calc_panel_v_box)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(side_panel_frame)
        main_h_box.addWidget(mid_panel_frame)
        main_h_box.addWidget(calc_panel_frame)

        container = QWidget()
        container.setLayout(main_h_box)
        self.setCentralWidget(container)

    def calculatorEngine(self):

        self.ivc_sat_val = int(self.ivc_sat_entry.text())/100
        self.svc_sat_val = int(self.svc_sat_entry.text())/100
        self.ao_sat_val = int(self.ao_sat_entry.text())/100
        self.pa_sat_val = int(self.pa_sat_entry.text())/100
        self.pv_sat_val = int(self.pv_sat_entry.text())/100
        self.hb_val = int(self.hb_entry.text())
        self.mv_sat_val = ((3*self.svc_sat_val) + self.ivc_sat_val)/4
        self.weight_val = int(self.weight_entry.text())
        self.height_val = int(self.height_entry.text())
        
        self.aosp_val = int(self.aosp_entry.text())
        self.aodp_val = int(self.aodp_entry.text())

        if self.aomp_entry.text():
            self.aomp_val = int(self.aomp_entry.text()) 
        else:
            self.aomp_val = (self.aosp_val + (2*self.aodp_val))/3
        
        self.pasp_val = int(self.pasp_entry.text())
        self.padp_val = int(self.padp_entry.text())
        
        if self.pamp_entry.text():
            self.pamp_val = int(self.pamp_entry.text()) 
        else:
            self.pamp_val = (self.pasp_val + (2*self.padp_val))/3

        self.pcwp_val = int(self.pcwp_entry.text())
        self.rap_val = int(self.rap_entry.text())
        self.ao_o2_cont = self.hb_val * 1.34 * self.ao_sat_val
        self.mv_o2_cont = self.hb_val * 1.34 * self.mv_sat_val
        self.bsa_val = math.sqrt((self.height_val * self.weight_val)/3600) 
        self.o2_cons_val = (3 * self.weight_val)
        self.co_val = self.o2_cons_val /((self.ao_o2_cont - self.mv_o2_cont)*10)
        self.ci_val = self.co_val/self.bsa_val
        self.svr_val_wood = (self.aomp_val - self.rap_val)/self.co_val
        self.pvr_val_wood = (self.pamp_val - self.pcwp_val)/self.co_val
        self.svr_val = self.svr_val_wood * 80
        self.pvr_val = self.pvr_val_wood * 80
        self.tpg_val = self.pamp_val - self.pcwp_val
        self.dpg_val = self.padp_val - self.pcwp_val
        self.pv_o2_cont = self.hb_val * 1.34 * self.pv_sat_val
        self.pa_o2_cont = self.hb_val * 1.34 * self.pa_sat_val
        self.qp_val = self.o2_cons_val / ((self.pv_o2_cont - self.pa_o2_cont)*10)

        self.calc_tbl.setItem(0,1, QTableWidgetItem(str(round(self.co_val,2))))
        self.calc_tbl.setItem(1,1, QTableWidgetItem(str(round(self.ci_val,2))))
        self.calc_tbl.setItem(2,1, QTableWidgetItem(str(round(self.svr_val,2))))
        self.calc_tbl.setItem(3,1, QTableWidgetItem(str(round(self.svr_val_wood,2))))
        self.calc_tbl.setItem(4,1, QTableWidgetItem(str(round(self.pvr_val,2))))
        self.calc_tbl.setItem(5,1, QTableWidgetItem(str(round(self.pvr_val_wood,2))))
        self.calc_tbl.setItem(6,1, QTableWidgetItem(str(round(self.tpg_val,2))))
        self.calc_tbl.setItem(7,1, QTableWidgetItem(str(round(self.dpg_val,2))))
        self.calc_tbl.setItem(8,1, QTableWidgetItem(str(round(self.qp_val/self.co_val,2))))

