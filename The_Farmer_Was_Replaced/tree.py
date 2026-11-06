# 以下为单一种植收获树木的代码

# 第一版——根据是否横纵坐标均为奇数或偶数
def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

clear()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Tree:
				if can_harvest():
					harvest()
			x = get_pos_x()
			y = get_pos_y()
			a = is_even(x)
			b = is_even(y)
			if a and b:
				plant(Entities.Tree)
			elif not a and not b:
				plant(Entities.Tree)
			else:
				pass
			move(North)
		move(East)