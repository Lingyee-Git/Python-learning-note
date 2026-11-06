# 以下为单一种植收获干草的代码

# 第一版
clear()
while True:
	for i in range(get_world_size()):
		harvest()
		move(North)
	move(East)
