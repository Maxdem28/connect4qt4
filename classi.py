import sys
from PyQt4 import QtGui, QtCore

class Column():
	height = 6
	boxes = []
	box_values = []
	vbox = QtGui.QVBoxLayout()

	def __init__(self, height):
		self.height = height
		for i in range(height):
			self.boxes.append(QtGui.QLabel('Vuoto'))
			self.box_values.append('Vuoto')
			self.vbox.addWidget(self.boxes[i])

	def set_box(self, x):
		for i in range(height):
			if self.box_values[i] == 'Vuoto':
				self.box_values[i] = x
				self.boxes[i] = QtGui.QLabel(x)

	def check_4_not_full(self):
		if self.box_values == ' ':
			return True
		return False


class mover():
	indice = 0
	main = "prova"

	def __init__(self, indice, m):
		self.indice = indice
		self.main = m
		
		
	def sposta(self, indice):
		if self.main.grid_values[self.indice][0] == "Vuoto":
			if self.main.giocatore == 1:
				disco = QtGui.QPushButton("")
				disco.setStyleSheet("background-color: red")
				turno = 1
				self.main.giocatore = 2
			elif self.main.giocatore == 2:
				disco = QtGui.QPushButton("")
				disco.setStyleSheet("background-color: yellow")
				turno = 2
				self.main.giocatore = 1		
			for i in range(self.main.height):
		
				if self.main.grid_values[self.indice][self.main.height-1-i]== "Vuoto":
					self.main.grid_values[self.indice][self.main.height-1-i] = turno
					#print(self.main.grid_values)
					a = disco
					self.main.grid.addWidget(disco, self.main.width-i, self.indice)
					self.main.vittoriePossibili()
					vitt = self.main.vittoria()
					if vitt:
						QtGui.QMessageBox.information(self.main, "Vittoria", "Partita finita")
					print("turno successivo")
					break
















