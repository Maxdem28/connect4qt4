# -*- coding: UTF-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from classi import *

class Main_window(QtGui.QMainWindow):
	grid_values = []
	width = width
	height = height
	winning_paths = []
	winning_limit = 4 ##the bot works only with 4 as winning_limit
	bottoni = []
	spostamenti = []
	giocatore = 1
	grid = ""
	pulsanti = QtGui.QVBoxLayout()
	pulsanti2 = QtGui.QHBoxLayout()	
	def __init__(self):

		self.grid = QtGui.QGridLayout()
		QtGui.QMainWindow.__init__(self)
	
		self.setWindowTitle('FORZA '+str(self.winning_limit))

		cwidget = QtGui.QWidget(self)

		for i in range(self.width):
			risultato = []
			for j in range(self.height):
				risultato.append("Vuoto")
			self.bottoni.append(QtGui.QPushButton("|\nV"))
			self.spostamenti.append(mover(i, self))
			self.bottoni[i].clicked.connect(self.spostamenti[i].sposta)
			self.grid_values.append(risultato)
		
			


		for i in range(self.width):		
			self.pulsanti2.addWidget(self.bottoni[i])	
			for j in range(self.height):
				self.grid.addWidget(QtGui.QLabel('Vuoto'), j, i)
		
		
		self.pulsanti.addLayout(self.pulsanti2)
		self.pulsanti.addLayout(self.grid)
		cwidget.setLayout(self.pulsanti)
		self.setCentralWidget(cwidget)

	def vittoriePossibili(self):
		for i in range(self.width-self.winning_limit+1):
			for j in range(self.height):
				result = []
				for k in range(self.winning_limit):
					result.append(self.grid_values[i+k][j])
				self.winning_paths.append(result)
		for i in range(self.width):
			for j in range(self.height-self.winning_limit+1):
				result = []
				for k in range(self.winning_limit):
					result.append(self.grid_values[i][j+k])
				self.winning_paths.append(result)
		for i in range(self.width-self.winning_limit+1):
			for j in range(self.height-self.winning_limit):
				result = []
				for k in range(self.winning_limit):
					result.append(self.grid_values[i+k][j+k])
				self.winning_paths.append(result)
		for i in range(self.winning_limit, self.width):
			for j in range(self.height-self.winning_limit+1):
				result = []
				for k in range(self.winning_limit):
					result.append(self.grid_values[i-k][j+k])
				self.winning_paths.append(result)

	def vittoria(self):
		#print(self.winning_paths)
		'''
		for i in range(self.width):
			for j in range(self.height):
				if self.grid_values[i][j] == 'Vuoto':
					print("\n"*5 + str(i) + " " + str(j))
					'''
		for i in self.winning_paths:
			#print(i)
			for j in range(self.winning_limit-1):
				#print(i[j], i[j+1])
				if (i[j] == i[j+1]) and (i[j]!= 'Vuoto'):
					#print("ok")
					if j == self.winning_limit -  2:
						return True
				else:
					break
		return False



	







app = QtGui.QApplication(sys.argv)
main = Main_window()
main.show()
sys.exit(app.exec_())





