# 以下为单一种植收获胡萝卜的代码

# 第一版
clear()

# 第一次犁地并且种植
for j in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		plant(Entities.Carrot)
		move(North)
	move(East)

while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(North)	
	move(East)