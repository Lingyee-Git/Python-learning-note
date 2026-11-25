# 以下为单一种植收获仙人掌的代码

# 冒泡排序

clear()

size = get_world_size()

while True:
	# 先种一排仙人掌
	for i in range(size):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		quick_print("第", get_pos_x()+1 , "棵仙人掌大小是", measure())
		move(East)
	
	# 开始排序
	for i in range(size - 1):
		for j in range(size - 1):
			move(East)
			s1 = measure()
			s2 = measure(West)
			if s1  < s2:
				swap(West)
		for j in range(size - 1):
			move(West)
		
	harvest()


# 冒泡排序2（每次排序后序列减一）

clear()

size = get_world_size()

while True:
	# 先种一排仙人掌
	for i in range(size):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		quick_print("第", get_pos_x()+1 , "棵仙人掌大小是", measure())
		move(East)
	
	turn = size
	
	# 开始排序
	for i in range(size - 1):
		for j in range(turn - 1):
			move(East)
			s1 = measure()
			s2 = measure(West)
			if s1  < s2:
				swap(West)
		for j in range(turn - 1):
			move(West)
		turn -= 1
	
	harvest()

# 选择排序

from function import *
clear()

while True:
	size = get_world_size()
	turn = []
	# 先种一排仙人掌
	for i in range(size):
		x = get_pos_x()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		turn.append([x, measure()])
		move(East)
		
	for i in range(size):
		a = 0
		for l in range(len(turn)):
			if turn[l][1] < turn[a][1]:
				a = l
		b = turn[a][0]
		my_move(b, 0)
		for s in range(i,b):
			swap(West)
			move(West)
		size -= 1
		turn.pop(a)
		for j in range(len(turn)):
			if turn[j][0] < b:
				turn[j][0] += 1
	
	my_move(0,0)
	harvest()