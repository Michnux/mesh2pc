import laspy
import subprocess
import os
import shutil



def mesh2pc(input_path, work_dir, n_points, hsrs, vsrs):

	#get the CC dir
	cc_dir=input_path
	c=cc_dir[-1]
	while c!='/':
		c = cc_dir[-1]
		cc_dir = cc_dir[:-1]
	cc_dir+='/'

	#convert to .ply if format is .glb
	if input_path[-4:]=='.glb':
		import trimesh
		mesh = trimesh.load_mesh(input_path)
		input_path = input_path[:-4]+'.ply'
		mesh.export(input_path)


	#run CC
	cmd = "xvfb-run CloudCompare -SILENT -C_EXPORT_FMT LAS -O "+input_path+" -SAMPLE_MESH POINTS "+str(n_points)
	subprocess.run(cmd, shell=True)

	#convert to las
	files = os.listdir(cc_dir)
	files = [f for f in files if 'SAMPLED_POINTS' in f]

	if len(files)==0:
		print('something went wrong')
	else:
		f = files[-1]
		shutil.copyfile(cc_dir+f, work_dir+"output.las")

	# 	las = laspy.read(cc_dir+f)

	# 	print(las.header.scales)
	# 	new_scale = 0.00001

	# 	# print('las.z[0]', las.z[0])

	# 	X = las.X*las.header.scales[0]
	# 	Y = las.Y*las.header.scales[1]
	# 	Z = las.Z*las.header.scales[2]

	# 	# print(min(z), max(z))
	# 	# print(z[0]/new_scale)

	# 	las.X = X/new_scale
	# 	las.Y = Y/new_scale
	# 	las.Z = Z/new_scale
	# 	# las.red = colors[:, 0]
	# 	# las.green = colors[:, 1]
	# 	# las.blue = colors[:, 2]
	# 	las.header.offsets += offsets
	# 	las.header.scales = [new_scale]*3
	# 	print(las.header.scales)

		# las.write(work_dir+"output.las")




if __name__ == "__main__":


	input_path = '../work_dir/input.las'
	ref_path = '../work_dir/input.las'
	work_dir = '../work_dir/'
	mesh2pc(input_path, work_dir)