# 以下为单一种植收获南瓜的代码

# 第一版
clear()

#第一次耕地种南瓜
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)

while True:
	# 定义一个布尔类型变量，记录南瓜好坏
	all_good = True
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			# 单格行为
			plant(Entities.Pumpkin)
			if not can_harvest():
				all_good = False
			move(North)
		move(East)
	
	# 直到全部是好
	if all_good:
		harvest()


# 第二版
# 使用列表简化遍历程序

from function import *

clear()

#第一次耕地种南瓜
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)

# 定义一个空列表
list1 = []

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			# 单格行为
			# 记录坏南瓜位置
			if not can_harvest():
				x, y = get_pos_x(), get_pos_y()
				list1.append((x,y))
			# 记录完毕再播种
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	
	# 只拜访修复坏南瓜
	while list1:	# 当list1为空时，等价于while False即不循环
		for i in list1[:]:
			# 取出坏南瓜坐标
			x, y = i[0], i[1]
			# 前往该坐标
			my_move(x,y)
			if can_harvest():
				list1.remove((x,y))
			else:
				plant(Entities.Pumpkin)
	
	harvest()
	my_move(0,0)