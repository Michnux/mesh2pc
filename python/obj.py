import open3d as o3d
import numpy as np
import laspy
import alteia
import json
import subprocess

from mesh2pc import mesh2pc


def main():

	sdk = alteia.SDK(config_path='./config-connections.json')

	projects = sdk.projects.search(name = 'Delair_BIM')

	print(projects)

	project = projects[0]

	missions = sdk.missions.search(project=project.id)

	# print([mission.name for mission in missions])
	mission = missions[0]

	# help(sdk.datasets.search)

	datasets = sdk.datasets.search(filter={	'project': {'$eq':project.id},
											# 'mission': {'$eq':mission.id},
											'name': {'$eq':'Delair BIM'}
																	})
	# datasets = sdk.datasets.search(project=project.id)

	print([ds.name for ds in datasets])

	dataset = datasets[0]

	file_name = dataset.components[0]['filename']


	hsrs = dataset.horizontal_srs_wkt
	vsrs = dataset.vertical_srs_wkt
	offset = dataset.offset
	# print(offset, hsrs, vsrs)

	# help(sdk.datasets.download_component)

	for comp in dataset.components:
		obj = sdk.datasets.download_component(dataset=dataset.id, component=comp.get("name"), overwrite=True)

	# textured_mesh = o3d.io.read_triangle_mesh("./"+file_name)

	# pcd = textured_mesh.sample_points_uniformly(number_of_points=50000)
	# o3d.visualization.draw_geometries([pcd])

	# pipeline = [
	# 	{
	# 		"type": "readers.obj",
	# 		# "filename": "./"+file_name
	# 		"filename":"./untitled1.obj"
	# 	},
	# 	{
	# 		"type" : "writers.las",
	# 		"filename": "output.las",
	# 		"scale_x": 1.0e-5,
	# 		"scale_y": 1.0e-5,
	# 		"scale_z": 1.0e-5,
	# 		"offset_x": "auto",
	# 		"offset_y": "auto",
	# 		"offset_z": "auto",
	# 		# "count":500000
	# 	}
	# ]


	# with open('./pipeline.json', 'w') as outfile:
	# 	json.dump(pipeline, outfile)

	# subprocess.run('pdal pipeline ./pipeline.json', shell=True)


	input_path = "/home/python/"+file_name
	work_dir = '/home/python/'
	mesh2pc(input_path, work_dir, offset, hsrs, vsrs)


if __name__ == "__main__":

	main()