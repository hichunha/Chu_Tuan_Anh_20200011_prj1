from csv import reader
from settings import tile_size
from os import walk
import pygame

#Nhập các hình ảnh bên trong của 1 thư mục duy nhất
#Thư mục nhập cơ bản
def import_folder(path):
	surface_list = []
	# Nếu chỉ chạy information thì sẽ ra 3 thư mục là đường dẫn, tệp con và hình ảnh
	# Do chỉ cần hình ảnh nên sẽ cho là _ đối với đường dẫn và thư mục con
	# for information in walk(path):
	#     print(information)
	for _,__,image_files in walk(path):
		for image in image_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def import_csv_layout(path):
	terrain_map = []
	with open(path) as map:
		level = reader(map,delimiter = ',')
		for row in level:
			terrain_map.append(list(row))
		return terrain_map

def import_cut_graphics(path):
	surface = pygame.image.load(path).convert_alpha()
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)

	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size,tile_size),flags = pygame.SRCALPHA)
			new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
			cut_tiles.append(new_surf)

	return cut_tiles
