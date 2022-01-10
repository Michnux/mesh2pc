import open3d as o3d
import numpy as np
import laspy
import subprocess
import os




def mesh2pc(input_path, work_dir, offsets, hsrs, vsrs):

	cmd = "xvfb-run CloudCompare -SILENT -C_EXPORT_FMT LAS -O "+input_path+" -SAMPLE_MESH POINTS 500000"

	subprocess.run(cmd, shell=True)

	files = os.listdir(work_dir)
	files = [f for f in files if 'SAMPLED_POINTS' in f]
	if len(files)==0:
		print('something went wrong')
	else:
		f = files[-1]

		las = laspy.read(f)

		print(las.header.scales)
		new_scale = 0.00001

		# print('las.z[0]', las.z[0])

		X = las.X*las.header.scales[0]
		Y = las.Y*las.header.scales[1]
		Z = las.Z*las.header.scales[2]

		# print(min(z), max(z))
		# print(z[0]/new_scale)

		las.X = X/new_scale
		las.Y = Y/new_scale
		las.Z = Z/new_scale
		# las.red = colors[:, 0]
		# las.green = colors[:, 1]
		# las.blue = colors[:, 2]
		las.header.offsets += np.array(offsets)
		las.header.scales = [new_scale]*3
		print(las.header.scales)

		las.write("output.las")




if __name__ == "__main__":


	input_path = '../work_dir/input.las'
	ref_path = '../work_dir/input.las'
	work_dir = '../work_dir/'
	mesh2pc(input_path, work_dir)