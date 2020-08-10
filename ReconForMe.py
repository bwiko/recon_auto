#!/usr/bin/env python3
from lib_s.recon import Ui_Recon
from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import re 
import time 
import threading


class Main(QtWidgets.QWidget,Ui_Recon) : 
	# :DN:->domain name  :FN:->file name 
	path = "/media/bl0x41cko/b6e9e652-b822-4754-aa85-1fc74a54d597/recon_test"
	command_auto = {"assetfinder:1":"$HOME/go/bin/assetfinder :DN: > "+path+"/:FN:/:FN:_asset",
	"subfinder:1":"subfinder -d ':DN:' -o '"+path+"/:FN:/:FN:_SF'",
	"sublist3r:1":"sublist3r -d ':DN:' -o '"+path+"/:FN:/:FN:_SL'",
	"amass:1":"amass enum -norecursive -noalts -d ':DN:' -o '"+path+"/:FN:/:FN:_amass'",
	"waybackmachine:1":"$HOME/go/bin/waybackurls :DN: > "+path+"/:FN:/:FN:_way",
	"filter:2":"cat "+path+"/:FN:/:FN:_asset "+path+"/:FN:/:FN:_amass "+path+"/:FN:/:FN:_SF "+path+"/:FN:/:FN:_SL | sort -u > "+path+"/:FN:/:FN:_subd",
	"httprobe:2":"cat "+path+"/:FN:/:FN:_subd | $HOME/go/bin/httprobe > "+path+"/:FN:/HTTP_S_domain_:FN:"
	} #name:command  not just put %DOMAIN%
	attack_start=False
	list_itam = []
	proprity = []
	counter = 0
	def __init__(self,parent=None):
			QtWidgets.QWidget.__init__(self,parent=parent)
			self.setupUi(self)
			# os.system('export GOPATH=$HOME/go')
			# os.system('export PATH=$PATH:$GOPATH/bin')
			self.lineEdit.setText(os.popen('xclip -o').read())
			self.aff_list_of_job()
			self.attack.clicked.connect(self.start_threada_command)
			self.Close.clicked.connect(self.closer)

	def filter(self,domain): 
		#regex ->[a-zA-Z]+\.[a-zA-Z]+
		com = re.compile('[a-zA-Z]+\.[a-zA-Z]+')
		if com.match(domain) == None : 
			return False 
		return True 
	
	def closer(self): 

		self.close()
	def start_threada_command(self):
	 	self.attack.setEnabled(False)
	 	self.Close.setEnabled(False)
	 	P1 = threading.Thread(target=self.start_comand)
	 	P1.start()
	def start_comand(self): 
		self.attack_start = True 
		domain = self.lineEdit.text()
		if self.filter(domain):
			file_name = domain.split(".")[0] 
			os.system("mkdir -p "+self.path+"/"+file_name+" 2>/dev/null")
			i=0 
			for job in self.command_auto :
				self.counter = i
				command = self.command_auto[job]	
				command = command.replace(":DN:",domain).replace(":FN:",file_name)
				os.system(command)
				#time.sleep(1)
				#threading.Thread(target=self.refresh).start()
				brush = QtGui.QBrush(QtGui.QColor(14,137,43)) #308dc7
				brush.setStyle(QtCore.Qt.SolidPattern)
				self.list_itam[i].setBackground(0, brush)
		
				i+=1
				#self.refresh()
			
			QtWidgets.QMessageBox.about(self, "Tip", "All of the command was executed successfully !!")#the tool finish
		else : 
			self.attack.setEnabled(True)	
			QtWidgets.QMessageBox.about(self, "Tip", "Nice Try bitch !!")#it's a joke bitch hhh
		#self.attack.setEnabled(False)
		self.Close.setEnabled(True)	
	
	def aff_list_of_job(self): 
		for job in self.command_auto : 
			item_0 = QtWidgets.QTreeWidgetItem()
			job = job.split(":")
			name_comand = job[0]
			item_0.setText(0,name_comand)
			brush = QtGui.QBrush(QtGui.QColor(48,141,199)) #308dc7
			brush.setStyle(QtCore.Qt.SolidPattern)
			item_0.setBackground(0, brush)
			brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
			brush.setStyle(QtCore.Qt.NoBrush)
			item_0.setForeground(0, brush)
			self.treeWidget.addTopLevelItem(item_0)
			self.list_itam.append(item_0)
			self.proprity.append(job[1])
			
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = Main()
	#ui = Ui_MainWindow()
	#ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())


import icon_rc
