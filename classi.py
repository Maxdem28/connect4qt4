import sys
from PyQt4 import QtGui, QtCore

width = 6
height = 7
freeSpots = width*height
difficulty = 5
moveIndex = 0
'''
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
'''
def maxi(alpha, beta, depth, actualGrid):
	global moveIndex
	if (depth == 0):
		return evaluate(actualGrid)
	for m in range(width):
		for h in range(height-1, -1, -1):
			if (h+1<height and actualGrid[m][h+1]=='Vuoto'):
				break
			if actualGrid[m][h] == 'Vuoto':
				actualGrid[m][h] = 2
				score = mini(alpha, beta, depth - 1, actualGrid)
				if score >= beta:
					actualGrid[m][h] = 'Vuoto'
					return beta
				if score > alpha:
					alpha = score
					if depth == difficulty:
						moveIndex = m
				actualGrid[m][h] = 'Vuoto'
	return alpha
			
def mini(alpha, beta, depth, actualGrid):
	if (depth == 0):
		return evaluate(actualGrid)
	for m in range(width):
		for h in range(height-1, -1, -1):
			if (h+1<height and actualGrid[m][h+1]=='Vuoto'):
				break
			if actualGrid[m][h] == 'Vuoto':
				actualGrid[m][h] = 1
				score = maxi(alpha, beta, depth - 1, actualGrid)
				if score <= alpha:
					actualGrid[m][h] = 'Vuoto'
					return alpha
				if score < beta:
					beta = score
				actualGrid[m][h] = 'Vuoto'
	return beta


def evaluate(grid):
    value = 0
    for i in range(width):
        for j in range(height):
            if grid[i][j]==2:
                for k in range(1,4):
                    if j+k < height:
                        if grid[i][j+k] != 2:
                            value+=k
                            break       
                        elif k == 3:
                            value += 450
                            break
                    else:
                        break
        
                for k in range(1,4):
                    if i+k < width:
                        if grid[i+k][j] != 2:
                            value+=k
                            break       
                        elif k == 3:
                            value += 450
                            break
                    else:
                        break
                for k in range(1,4):
                    if j+k < height and i+k < width:
                        if grid[i+k][j+k] != 2:
                            value+=k
                            break       
                        elif k == 3:
                            value += 450
                            break
                    else:
                        break
                for k in range(1,4):
                    if i+k < width and j-k > 0:
                        if grid[i+k][j-k] != 2:
                            value+=k
                            break       
                        elif k == 3:
                            value += 450
                            break
                    else:
                        break

            if grid[i][j]==1:
                for k in range(1,4):
                    if j+k < height:
                        if grid[i][j+k] != 1:
                            value-=k
                            break       
                        elif k == 3:
                            value -= 500
                            break
                    else:
                        break
        
                for k in range(1,4):
                    if i+k < width:
                        if grid[i+k][j] != 1:
                            value-=k
                            break       
                        elif k == 3:
                            value -= 500
                            break
                    else:
                        break
                for k in range(1,4):
                    if j+k < height and i+k < width:
                        if grid[i+k][j+k] != 1:
                            value-=k
                            break       
                        elif k == 3:
                            value -= 500
                            break
                    else:
                        break
                for k in range(1,4):
                    if i+k < width and j-k > 0:
                        if grid[i+k][j-k] != 1:
                            value-=k
                            break       
                        elif k == 3:
                            value -= 500
                            break
                    else:
                        break
    return value


def calculate(grid):
	global freeSpots
	global difficulty
	if difficulty > freeSpots:
		difficulty = freeSpots
	cacca = maxi(-100000, 100000, difficulty, grid)
	freeSpots -= 1


class mover():
	indice = 0
	main = "prova"

	def __init__(self, indice, m):
		self.indice = indice
		self.main = m
		
		
	def sposta(self):
		global moveIndex
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
					self.main.grid.addWidget(disco, self.main.width-i, self.indice)
					self.main.vittoriePossibili()
					vitt = self.main.vittoria()
					if vitt:
						QtGui.QMessageBox.information(self.main, "Vittoria", "Partita finita. Vince " + str(turno))
						exit()
					#print("turno successivo")
					if (self.main.giocatore == 2):
						calculate(self.main.grid_values) #cosa ritorna minimax
						#print(moveIndex)
						self.main.spostamenti[moveIndex].sposta()
					break