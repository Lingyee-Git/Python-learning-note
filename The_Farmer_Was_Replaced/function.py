# 这个文件专门存放函数

# 1.移动到目标坐标的函数
def my_move(x1, y1):
	while True:
		x, y = get_pos_x(), get_pos_y()
		if x1 != x or y1 != y:
			if x > x1:
				move(West)
			if x < x1:
				move(East)
			if y > y1:
				move(South)
			if y < y1:
				move(North)
		else:
			break