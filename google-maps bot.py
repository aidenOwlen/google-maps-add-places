# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapBot.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 420)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 281, 111))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(21, 38, 24, 16))
        self.label.setObjectName("label")
        self.PasswordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PasswordEdit.setGeometry(QtCore.QRect(73, 64, 181, 20))
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.EmailEdit = QtWidgets.QLineEdit(self.groupBox)
        self.EmailEdit.setGeometry(QtCore.QRect(73, 38, 181, 20))
        self.EmailEdit.setObjectName("EmailEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(21, 64, 46, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 281, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ImportEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.ImportEdit.setGeometry(QtCore.QRect(50, 30, 181, 20))
        self.ImportEdit.setReadOnly(True)
        self.ImportEdit.setObjectName("ImportEdit")
        self.ImportButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ImportButton.setGeometry(QtCore.QRect(80, 60, 111, 23))
        self.ImportButton.setObjectName("ImportButton")
        self.ImportButton.clicked.connect(self.openFile)

        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 230, 281, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SecondSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.SecondSpin.setGeometry(QtCore.QRect(80, 50, 111, 22))
        self.SecondSpin.setMaximum(1500)
        self.SecondSpin.setObjectName("SecondSpin")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.StartButton = QtWidgets.QPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(20, 350, 121, 41))
        self.StartButton.setObjectName("StartButton")
        self.StartButton.clicked.connect(self.start)
        self.StopButton = QtWidgets.QPushButton(Form)
        self.StopButton.setGeometry(QtCore.QRect(170, 350, 121, 41))
        self.StopButton.setObjectName("StopButton")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FiverrBot"))
        self.groupBox.setTitle(_translate("Form", "Login Info "))
        self.label.setText(_translate("Form", "Email"))
        self.label_2.setText(_translate("Form", "Password"))
        self.groupBox_2.setTitle(_translate("Form", "Import "))
        self.ImportButton.setText(_translate("Form", "Import File"))
        self.groupBox_3.setTitle(_translate("Form", "Options"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff1010;\">Pauses between each task in Seconds</span></p></body></html>"))
        self.StartButton.setText(_translate("Form", "Start"))
        self.StopButton.setText(_translate("Form", "Stop"))
    
    def start(self):
        password = self.PasswordEdit.text()
        email = self.EmailEdit.text()
        df = pandas.read_excel(self.ImportEdit.text(), sheetname='Sheet1')
        #print(self.ImportEdit.text()

        listAdr = ["Cahuenga Boulevard West, Los Angeles, CA, USA","Cahuenga Boulevard, Los Angeles, CA, USA","Cahuenga Boulevard West, Los Angeles, CA, USA","Cahuenga Park Trail, Los Angeles, CA, USA","Cahuenga Park Trail, Los Angeles, CA, USA"]
        categorie = "Tuning Automobile"
        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com/signin/v2/identifier?service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element_by_id("identifierId").send_keys(email)
        driver.find_element_by_id("identifierNext").click()

        wait = WebDriverWait(driver,20)
        try:
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.NAME, 'password')))
            driver.find_element_by_name("password").send_keys(password)
        except TimeoutException:
            pass
        time.sleep(5)
        #driver.find_element_by_name("password").send_keys("chtidibchto")
        driver.find_element_by_id("passwordNext").click()
        time.sleep(5)
        for i in df.index:
            name = df['Business Name'][i]
            phone = df['Business Phone'][i]
            #df['Business Category'][i]

            driver.get("https://www.google.com/maps")
            try:
                #wait.until(EC.visibility_of_element_located((By.ID, "searchbox")))
                #driver.find_element_by_class_name("searchbox-hamburger").click()
                time.sleep(10)
                driver.find_element_by_xpath("""//*[@id="omnibox-singlebox"]/div[1]/div[1]/button""").click()
            except TimeoutException:
                print("error asata")


            #driver.find_element_by_xpath("""//*[@id="omnibox-singlebox"]/div[1]/div[1]/button""").click()
            time.sleep(5)
            driver.find_element_by_xpath("""//*[@id="settings"]/div/div[2]/div/ul[4]/li[6]/button""").click()



            #driver.find_element_by_xpath("""//*[@id="settings"]/div/div[2]/div/ul[4]/li[6]/button""").click()

            try:
                time.sleep(4)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rap-text-input")))
                driver.find_element_by_xpath("""//*[@id="rap-card"]/div/div/div[2]/div[2]/div/div[5]""").click()
                k = driver.find_elements_by_class_name("rap-text-input")
            except TimeoutException:
                pass
            k[0].send_keys(name)
            time.sleep(2)
            k[1].send_keys(random.choice(listAdr))
            #driver.find_element_by_xpath("""//*[@id="rap-card"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/input""").send_keys(Keys.DOWN)
            #driver.find_element_by_xpath("""//*[@id="rap-card"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/input""").send_keys(Keys.ENTER)
            k[1].send_keys(Keys.TAB)
            time.sleep(2)
            k[1].send_keys(Keys.TAB)
            time.sleep(10)
            k[2].click()
            
            
            time.sleep(2)
            k[2].send_keys("Tuning A")
            time.sleep(2)
            try:
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.ID,":0")))
                k[2].send_keys(Keys.TAB)
            except TimeoutException:
                pass
            
            #driver.find_element_by_xpath("""//*[@id=":8k7"]""").click()
            time.sleep(3)
            #k[2].click()
            #k[2].send_keys(Keys.TAB)
            #time.sleep(2)
            #driver.find_element_by_xpath("""//*[@id="rap-card"]/div/div/div[2]/div[2]/div/div[5]""").click()
            k[3].send_keys(str(phone))
            time.sleep(2)
            driver.find_element_by_xpath("""//*[@id="rap-card"]/div/div/div[2]/div[3]/button""").click()
            time.sleep(2)
            driver.find_element_by_xpath("""//*[@id="modal-dialog-widget"]/div[2]/div/div[3]/div/div/div[3]/div[2]/button[3]""").click()
            time.sleep(4)
     #   .issue-card-submit-button.kd-button.kd-button-submit
    def openFile(self):

        fname = QtWidgets.QFileDialog.getOpenFileName()
        if fname[0]:
            f = open(fname[0], 'r')
            self.ImportEdit.setText(fname[0])  



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

