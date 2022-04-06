# import trimesh

# mesh = trimesh.load_mesh('output_voies.glb')

# mesh.export('output_voies.ply')



input_path = '/home/ble/ble/dfdfd.glb'

print(input_path[-4:])

if input_path[-4:]=='.glb':

	input_path = input_path[:-4]+'.ply'


print(input_path)