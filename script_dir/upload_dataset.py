import alteia



def upload_dataset(file_path, project_id, mission_id, script_dir, hsrs, vsrs):

	url = os.getenv("ALTEIA_PLATEFORM_URL")
		client_id = os.getenv("ALTEIA_CLIENT_ID")
		client_secret = os.getenv("ALTEIA_CLIENT_SECRET")
		if not url or not client_id or not client_secret:
			logger.error('Plateform URL, client id or client secret not set')
			return

	sdk = SDK(
		url=url,
		client_id=client_id,
		client_secret=client_secret,
		connection={'disable_ssl_certificate': True},
	)


	new_dataset = sdk.datasets.create_pcl_dataset(	name='sampled point cloud',
														project=project_id,
														mission=mission_id,
														categories=[],
														horizontal_srs_wkt = hsrs,
														vertical_srs_wkt = vsrs)

	sdk.datasets.upload_file(dataset=new_dataset.id,
							 component='pcl',
							 file_path=file_path)


if __name__ == "__main__":

	upload_dataset('../work_dir/max.tif', '61c1d5a73e614e00085c6a01', '61c4aeffd730570008b5e7c9', './')