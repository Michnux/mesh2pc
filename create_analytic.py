import alteia



sdk = alteia.SDK(config_path='./config-connections.json')


analytic = sdk.analytics.search(name="alteiademo/mesh2pc")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="alteiademo/mesh2pc",
	version="1.0.0",
	display_name="mesh2pc",
	description="Generates a Point Cloud from a Mesh file",
	docker_image="registry-1.docker.io/michaeldelagarde/mesh2pc:latest",
	company="5c1a2567b3c575583e8a650d",
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
	{
		"name": "output",
		"display_name": "output",
		"description": "output",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "pcl"}},
				"required": ["type"]
			},
		},
		"required": True
	}
	],
	groups=["Tuto"])