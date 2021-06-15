import numpy as np
import random


def add_value(grid):
	pass
def sort_grid (grid):
	''' make element sortering in matrix 'grid'. in each column and row element move up in case of above possition is 0(zero)'''
	for k in range(3):
		for i in range(4):
			for j in range(3):
				if grid[j][i] == 0:
					grid[j][i] = grid[j+1][i]
					grid[j+1][i] = 0
				else: continue
			
	return grid

def sum_up(grid):
	'''sum up equal values from down to up or moves not equal values from down to up
	make corect ordering of value'''
	sort_grid(grid)
	for i in range(4):
		if grid[0][i] == grid[1][i]:
			check_1_2(grid,i)
		elif grid[2][i] == grid[3][i]:
			check_3_4(grid,i)
		elif grid[1][i] == grid[2][i]:
			check_2_3(grid,i)
	sort_grid(grid)
	return grid

def check_1_2 (grid,i):
	'''sum elements first and second values in appropriate colomn'''
	grid[0][i] += grid[1][i]
	grid[1][i] = 0
	return grid

def check_2_3 (grid,i):
	'''sum elements second and third values in appropriate colomn'''
	grid[1][i] += grid[2][i]
	grid[2][i] = 0
	return grid

def check_3_4 (grid,i):
	'''sum elements third and forth values in appropriate colomn'''
	grid[2][i] += grid[3][i]
	grid[3][i] = 0
	return grid



def sum_down (grid):
	'''sum up equal values from up to down or moves not equal values from up to down
	make corect ordering of value'''
	grid = sum_up(np.rot90(grid,2))
	grid = np.rot90(grid,-2)
	return grid


def sum_left(grid):
	'''sum up equal values from right to left or moves not equal values from right to left
	make corect ordering of value'''
	grid = sum_up(np.rot90(grid,-1))
	grid = np.rot90(grid,1)
	return grid


def sum_right (grid):
	'''sum up equal values from left to right or moves not equal values from left to right
	make corect ordering of value'''
	grid = sum_up(np.rot90(grid,1))
	grid = np.rot90(grid,-1)
	return grid


def grid_cell_color(cell_value):
	'''this function return grid cell color depends from value in cells'''
	colors = {
		0:(227,217,198),	#ral 1013
		2:(221,196,154),	#ral 1014
		4:(210,170,109),	#ral 1002
		8:(235,156,82),		#ral 1034
		16:(249,154,28),	#ral 1033
		32:(218,110,0),		#ral 2000
		64:(255,77,6),		#ral 2005
		128:(255,178,0),	#ral 2007
		256:(213,101,77),	#ral 2012
		512:(191,57,34),	#ral 2002
		1024:(167,41,32),	#ral 3000
		2048:(255,45,33)	#ral 3024
	}
	return colors[cell_value]

def grid_score (grid):
	'''this function find the maximum value in the grid and return it like the actual maximum result for current game'''
	score = np.max(grid)
	return score

def grid_new_value(grid):
	'''this function add new value into a random cell with value '0' or empty cell after each cycle of values summing'''
	values_list = [2,4]
	new_value = random.choice(values_list)
	grid = grid.astype(int)
	zero_coordinates = []
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				zero_coordinates.append((i,j))
			else: continue

	coordinate_choice = random.choice(zero_coordinates)	#randomly choice cell with velue '0' for further new_value inserion insted of '0'
	grid[coordinate_choice[0]][coordinate_choice[1]] = new_value
	grid = grid.astype(int)
	return grid


def is_empty_cell(grid):
	'''this function check is there cell with value = 0 in whole matrix'''
	grid = grid.astype(int)
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				status = "GO"
				return status
			else:
				status = "STOP"
	return status
