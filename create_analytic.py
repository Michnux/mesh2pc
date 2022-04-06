import alteia



sdk = alteia.SDK(config_path='./config-connections-setec.json')


analytic = sdk.analytics.search(name="seteccapture/mesh2pc_setec")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="seteccapture/mesh2pc_setec",
	version="1.0.0",
	display_name="mesh2pc",
	description="Generates a Point Cloud from a Mesh file",
	docker_image="registry-1.docker.io/michaeldelagarde/mesh2pc_setec:latest",
	company="61386c9dd215430006a73e57",
	instance_type='small',
	volume_size=20,
	inputs=[{
		"name": "input_obj",
		"display_name": "input_obj",
		"description": ".obj of other mesh file",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "mesh"}},
				"required": ["type"]
			},
		},
		"required": True
	},
	],
	parameters=[{
		"name": "n_points",
		"display_name": "Number of points",
		"description": "Number of points of point cloud (default: 500.000)",
		"required": False,
		"scheme": {
			"type": "string"#, "pattern": "^[0-9]$"
		}
	 },
	],
	deliverables=[
	# {
	# 	"name": "outputtif",
	# 	"display_name": "outputtif",
	# 	"description": "outputtif",
	# 	"scheme": {
	# 		"type": "string", "pattern": "^[0-9a-f]{24}$"
	# 	},
	# 	"source": {
	# 		"service": "data-manager",
	# 		"resource": "dataset",
	# 		"scheme": {
	# 			"type": "object",
	# 			"properties": {"type": {"const": "raster"}},
	# 			"required": ["type"]
	# 		},
	# 	},
	# 	"required": False
	# }
	],
	groups=["UTILS"])