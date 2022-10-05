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

