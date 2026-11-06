# 以下为单一种植收获灌木的代码

# 第一版
clear()
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		move(North)
	move(East)