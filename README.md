## Description of the Analytic:

Generates a sampled Point Cloud (.las), from a mesh file (.obj or other formats)


## Inputs:

The mesh file (.obj, .glb)


## Parameters:

Number of points (Default: 500 000)


## Outputs:

A sampled Point Cloud (.las)


## Analytics creation

create_analytic.py allows to create the analytics without using the CLI
This requires credentials to be added to the project dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

Credentials to access the docker registry used still have to be created from the CLI


## Fix-me:

* The scripts generates a raster (output.las) as a final result.
A dataset is created and the output.las component uplaoded from the docker using the SDK (cf. uplaod_dataset.py file)
This requires credentials to be added to the script_dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

this is a quick-fix as the transfert of the generated results (as described in the outputs.json file) doesn't seem to work properly


* The file type for input selection of the analytics is 'mesh'
However, in the GUI Selector only glb files show up. .obj files do not.
Quick-fix: add a parameter corresponding to the .obj file and fetch it from the docker using the SDK
