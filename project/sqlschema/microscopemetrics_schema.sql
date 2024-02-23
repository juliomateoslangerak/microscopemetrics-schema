

CREATE TABLE "ArgolightBCentersOfMass" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "ArgolightEKeyValues" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Channel" (
	name TEXT, 
	description TEXT, 
	excitation_wavelength_nm FLOAT, 
	emission_wavelength_nm FLOAT, 
	PRIMARY KEY (name, description, excitation_wavelength_nm, emission_wavelength_nm)
);

CREATE TABLE "ChannelSeries" (
	"values" TEXT NOT NULL, 
	PRIMARY KEY ("values")
);

CREATE TABLE "Color" (
	r INTEGER NOT NULL, 
	g INTEGER NOT NULL, 
	b INTEGER NOT NULL, 
	alpha INTEGER, 
	PRIMARY KEY (r, g, b, alpha)
);

CREATE TABLE "Column" (
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	"values" TEXT, 
	PRIMARY KEY (name, description, source_uri, "values")
);

CREATE TABLE "Ellipse" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	x_rad FLOAT NOT NULL, 
	y_rad FLOAT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Experimenter" (
	name TEXT NOT NULL, 
	orcid TEXT NOT NULL, 
	PRIMARY KEY (orcid)
);

CREATE TABLE "FieldIlluminationCentersFitted" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationCentersGeometric" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationCentersMaxIntensity" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationCentersOfMass" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationCornersIntensities" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	measurements_table TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationInput" (
	field_illumination_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	intensity_map_size INTEGER NOT NULL, 
	PRIMARY KEY (field_illumination_image, bit_depth, saturation_threshold, corner_fraction, sigma, intensity_map_size)
);

CREATE TABLE "FieldIlluminationKeyValues" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "FieldIlluminationProfilesIntensity" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	intensity_profiles_table TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Image2D" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Image5D" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	time_series TEXT, 
	channel_series TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "ImageAsNumpy" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	data TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "ImageMask" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Line" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	x1 FLOAT NOT NULL, 
	y1 FLOAT NOT NULL, 
	x2 FLOAT NOT NULL, 
	y2 FLOAT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "MetricsDatasetCollection" (
	datasets TEXT NOT NULL, 
	PRIMARY KEY (datasets)
);

CREATE TABLE "Microscope" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	type VARCHAR(10), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	comment TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Point" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y FLOAT NOT NULL, 
	x FLOAT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Polygon" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	is_open BOOLEAN NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Protocol" (
	name TEXT, 
	description TEXT, 
	version TEXT NOT NULL, 
	authors TEXT, 
	url TEXT NOT NULL, 
	PRIMARY KEY (url)
);

CREATE TABLE "PSFBeadsCenters" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "PSFBeadsInput" (
	psf_beads_images TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT, 
	min_lateral_distance_factor FLOAT NOT NULL, 
	sigma_z FLOAT NOT NULL, 
	sigma_y FLOAT NOT NULL, 
	sigma_x FLOAT NOT NULL, 
	snr_threshold FLOAT NOT NULL, 
	fitting_rss_threshold FLOAT NOT NULL, 
	intensity_robust_z_score_threshold FLOAT NOT NULL, 
	PRIMARY KEY (psf_beads_images, bit_depth, saturation_threshold, min_lateral_distance_factor, sigma_z, sigma_y, sigma_x, snr_threshold, fitting_rss_threshold, intensity_robust_z_score_threshold)
);

CREATE TABLE "PSFBeadsKeyValues" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Rectangle" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	w FLOAT NOT NULL, 
	h FLOAT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "Roi" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "TableAsPandasDF" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	df TEXT NOT NULL, 
	PRIMARY KEY (data_uri)
);

CREATE TABLE "TimeSeries" (
	"values" FLOAT NOT NULL, 
	PRIMARY KEY ("values")
);

CREATE TABLE "ArgolightBDataset" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (data_uri)
);

CREATE TABLE "ArgolightBInput" (
	argolight_b_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	spots_distance FLOAT NOT NULL, 
	sigma_z FLOAT NOT NULL, 
	sigma_y FLOAT NOT NULL, 
	sigma_x FLOAT NOT NULL, 
	lower_threshold_correction_factors FLOAT, 
	upper_threshold_correction_factors FLOAT, 
	remove_center_cross BOOLEAN, 
	PRIMARY KEY (argolight_b_image, bit_depth, saturation_threshold, spots_distance, sigma_z, sigma_y, sigma_x, lower_threshold_correction_factors, upper_threshold_correction_factors, remove_center_cross), 
	FOREIGN KEY(argolight_b_image) REFERENCES "ImageAsNumpy" (data_uri)
);

CREATE TABLE "ArgolightBOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	comment TEXT, 
	spots_labels_image TEXT, 
	spots_centers_of_mass TEXT, 
	intensity_key_values TEXT, 
	distance_key_values TEXT, 
	spots_properties TEXT, 
	spots_distances TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, comment, spots_labels_image, spots_centers_of_mass, intensity_key_values, distance_key_values, spots_properties, spots_distances), 
	FOREIGN KEY(spots_labels_image) REFERENCES "ImageAsNumpy" (data_uri), 
	FOREIGN KEY(intensity_key_values) REFERENCES "ArgolightBIntensityKeyValues" (data_uri), 
	FOREIGN KEY(distance_key_values) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEDataset" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (data_uri)
);

CREATE TABLE "ArgolightEInput" (
	argolight_e_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	orientation_axis INTEGER NOT NULL, 
	measured_band FLOAT NOT NULL, 
	prominence_threshold FLOAT NOT NULL, 
	PRIMARY KEY (argolight_e_image, bit_depth, saturation_threshold, orientation_axis, measured_band, prominence_threshold), 
	FOREIGN KEY(argolight_e_image) REFERENCES "ImageAsNumpy" (data_uri)
);

CREATE TABLE "ArgolightEOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	comment TEXT, 
	peaks_rois TEXT, 
	key_measurements TEXT, 
	intensity_profiles TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, comment, peaks_rois, key_measurements, intensity_profiles), 
	FOREIGN KEY(key_measurements) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "Comment" (
	datetime DATETIME NOT NULL, 
	author TEXT, 
	comment_type VARCHAR(11) NOT NULL, 
	text TEXT NOT NULL, 
	PRIMARY KEY (datetime, author, comment_type, text), 
	FOREIGN KEY(author) REFERENCES "Experimenter" (orcid)
);

CREATE TABLE "FieldIlluminationDataset" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (data_uri)
);

CREATE TABLE "FieldIlluminationOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	comment TEXT, 
	key_values TEXT, 
	intensity_profiles TEXT, 
	intensity_map TEXT, 
	roi_profiles TEXT, 
	roi_corners TEXT, 
	roi_centers_of_mass TEXT, 
	roi_centers_geometric TEXT, 
	roi_centers_fitted TEXT, 
	roi_centers_max_intensity TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, comment, key_values, intensity_profiles, intensity_map, roi_profiles, roi_corners, roi_centers_of_mass, roi_centers_geometric, roi_centers_fitted, roi_centers_max_intensity), 
	FOREIGN KEY(key_values) REFERENCES "FieldIlluminationKeyValues" (data_uri), 
	FOREIGN KEY(roi_corners) REFERENCES "FieldIlluminationCornersIntensities" (data_uri)
);

CREATE TABLE "Mask" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y INTEGER NOT NULL, 
	x INTEGER NOT NULL, 
	mask TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(mask) REFERENCES "ImageMask" (data_uri)
);

CREATE TABLE "MetricsDataset" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (data_uri)
);

CREATE TABLE "PSFBeadsDataset" (
	name TEXT, 
	description TEXT, 
	data_uri TEXT NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (data_uri), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (data_uri)
);

CREATE TABLE "PSFBeadsOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	comment TEXT, 
	bead_crops TEXT, 
	analyzed_bead_centers TEXT, 
	discarded_bead_centers_lateral_edge TEXT, 
	discarded_bead_centers_self_proximity TEXT, 
	considered_bead_centers_axial_edge TEXT, 
	considered_bead_centers_intensity_outlier TEXT, 
	considered_bead_centers_z_fit_quality TEXT, 
	considered_bead_centers_y_fit_quality TEXT, 
	considered_bead_centers_x_fit_quality TEXT, 
	key_values TEXT, 
	bead_properties TEXT, 
	bead_z_profiles TEXT, 
	bead_y_profiles TEXT, 
	bead_x_profiles TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, comment, bead_crops, analyzed_bead_centers, discarded_bead_centers_lateral_edge, discarded_bead_centers_self_proximity, considered_bead_centers_axial_edge, considered_bead_centers_intensity_outlier, considered_bead_centers_z_fit_quality, considered_bead_centers_y_fit_quality, considered_bead_centers_x_fit_quality, key_values, bead_properties, bead_z_profiles, bead_y_profiles, bead_x_profiles), 
	FOREIGN KEY(key_values) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "Sample" (
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	protocol TEXT NOT NULL, 
	PRIMARY KEY (name, description, type, protocol), 
	FOREIGN KEY(protocol) REFERENCES "Protocol" (url)
);

CREATE TABLE "Vertex" (
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	"Polygon_data_uri" TEXT, 
	PRIMARY KEY (x, y, "Polygon_data_uri"), 
	FOREIGN KEY("Polygon_data_uri") REFERENCES "Polygon" (data_uri)
);

CREATE TABLE "ArgolightBCentersOfMass_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBCentersOfMass" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_channel_A" (
	backref_id TEXT, 
	"channel_A" INTEGER, 
	PRIMARY KEY (backref_id, "channel_A"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_channel_B" (
	backref_id TEXT, 
	"channel_B" INTEGER, 
	PRIMARY KEY (backref_id, "channel_B"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_mean_3d_dist" (
	backref_id TEXT, 
	mean_3d_dist FLOAT, 
	PRIMARY KEY (backref_id, mean_3d_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_median_3d_dist" (
	backref_id TEXT, 
	median_3d_dist FLOAT, 
	PRIMARY KEY (backref_id, median_3d_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_std_3d_dist" (
	backref_id TEXT, 
	std_3d_dist FLOAT, 
	PRIMARY KEY (backref_id, std_3d_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_mad_3d_dist" (
	backref_id TEXT, 
	mad_3d_dist FLOAT, 
	PRIMARY KEY (backref_id, mad_3d_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_mean_z_dist" (
	backref_id TEXT, 
	mean_z_dist FLOAT, 
	PRIMARY KEY (backref_id, mean_z_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_median_z_dist" (
	backref_id TEXT, 
	median_z_dist FLOAT, 
	PRIMARY KEY (backref_id, median_z_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_std_z_dist" (
	backref_id TEXT, 
	std_z_dist FLOAT, 
	PRIMARY KEY (backref_id, std_z_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBDistanceKeyValues_mad_z_dist" (
	backref_id TEXT, 
	mad_z_dist FLOAT, 
	PRIMARY KEY (backref_id, mad_z_dist), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBDistanceKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_channel_nr" (
	backref_id TEXT, 
	channel_nr INTEGER, 
	PRIMARY KEY (backref_id, channel_nr), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_nr_of_spots" (
	backref_id TEXT, 
	nr_of_spots INTEGER, 
	PRIMARY KEY (backref_id, nr_of_spots), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_intensity_max_spot" (
	backref_id TEXT, 
	intensity_max_spot FLOAT, 
	PRIMARY KEY (backref_id, intensity_max_spot), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_intensity_max_spot_roi" (
	backref_id TEXT, 
	intensity_max_spot_roi INTEGER, 
	PRIMARY KEY (backref_id, intensity_max_spot_roi), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_intensity_min_spot" (
	backref_id TEXT, 
	intensity_min_spot FLOAT, 
	PRIMARY KEY (backref_id, intensity_min_spot), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_intensity_min_spot_roi" (
	backref_id TEXT, 
	intensity_min_spot_roi INTEGER, 
	PRIMARY KEY (backref_id, intensity_min_spot_roi), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_mean_intensity" (
	backref_id TEXT, 
	mean_intensity FLOAT, 
	PRIMARY KEY (backref_id, mean_intensity), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_median_intensity" (
	backref_id TEXT, 
	median_intensity FLOAT, 
	PRIMARY KEY (backref_id, median_intensity), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_std_mean_intensity" (
	backref_id TEXT, 
	std_mean_intensity FLOAT, 
	PRIMARY KEY (backref_id, std_mean_intensity), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_mad_mean_intensity" (
	backref_id TEXT, 
	mad_mean_intensity FLOAT, 
	PRIMARY KEY (backref_id, mad_mean_intensity), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightBIntensityKeyValues_min_max_intensity_ratio" (
	backref_id TEXT, 
	min_max_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, min_max_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightBIntensityKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_channel_nr" (
	backref_id TEXT, 
	channel_nr INTEGER, 
	PRIMARY KEY (backref_id, channel_nr), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_focus_slice" (
	backref_id TEXT, 
	focus_slice INTEGER, 
	PRIMARY KEY (backref_id, focus_slice), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_rayleigh_resolution_pixels" (
	backref_id TEXT, 
	rayleigh_resolution_pixels FLOAT, 
	PRIMARY KEY (backref_id, rayleigh_resolution_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_rayleigh_resolution_microns" (
	backref_id TEXT, 
	rayleigh_resolution_microns FLOAT, 
	PRIMARY KEY (backref_id, rayleigh_resolution_microns), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_position_A" (
	backref_id TEXT, 
	"peak_position_A" FLOAT, 
	PRIMARY KEY (backref_id, "peak_position_A"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_position_B" (
	backref_id TEXT, 
	"peak_position_B" FLOAT, 
	PRIMARY KEY (backref_id, "peak_position_B"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_height_A" (
	backref_id TEXT, 
	"peak_height_A" FLOAT, 
	PRIMARY KEY (backref_id, "peak_height_A"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_height_B" (
	backref_id TEXT, 
	"peak_height_B" FLOAT, 
	PRIMARY KEY (backref_id, "peak_height_B"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_prominence_A" (
	backref_id TEXT, 
	"peak_prominence_A" FLOAT, 
	PRIMARY KEY (backref_id, "peak_prominence_A"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "ArgolightEKeyValues_peak_prominence_B" (
	backref_id TEXT, 
	"peak_prominence_B" FLOAT, 
	PRIMARY KEY (backref_id, "peak_prominence_B"), 
	FOREIGN KEY(backref_id) REFERENCES "ArgolightEKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationCentersFitted_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationCentersFitted" (data_uri)
);

CREATE TABLE "FieldIlluminationCentersGeometric_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationCentersGeometric" (data_uri)
);

CREATE TABLE "FieldIlluminationCentersMaxIntensity_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationCentersMaxIntensity" (data_uri)
);

CREATE TABLE "FieldIlluminationCentersOfMass_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationCentersOfMass" (data_uri)
);

CREATE TABLE "FieldIlluminationCornersIntensities_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationCornersIntensities" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_channel_nr" (
	backref_id TEXT, 
	channel_nr INTEGER, 
	PRIMARY KEY (backref_id, channel_nr), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_region_intensity_fraction" (
	backref_id TEXT, 
	center_region_intensity_fraction FLOAT, 
	PRIMARY KEY (backref_id, center_region_intensity_fraction), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_region_area_fraction" (
	backref_id TEXT, 
	center_region_area_fraction FLOAT, 
	PRIMARY KEY (backref_id, center_region_area_fraction), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_y" (
	backref_id TEXT, 
	center_of_mass_y FLOAT, 
	PRIMARY KEY (backref_id, center_of_mass_y), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_y_relative" (
	backref_id TEXT, 
	center_of_mass_y_relative FLOAT, 
	PRIMARY KEY (backref_id, center_of_mass_y_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_x" (
	backref_id TEXT, 
	center_of_mass_x FLOAT, 
	PRIMARY KEY (backref_id, center_of_mass_x), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_x_relative" (
	backref_id TEXT, 
	center_of_mass_x_relative FLOAT, 
	PRIMARY KEY (backref_id, center_of_mass_x_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_distance_relative" (
	backref_id TEXT, 
	center_of_mass_distance_relative FLOAT, 
	PRIMARY KEY (backref_id, center_of_mass_distance_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_geometric_y" (
	backref_id TEXT, 
	center_geometric_y FLOAT, 
	PRIMARY KEY (backref_id, center_geometric_y), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_geometric_y_relative" (
	backref_id TEXT, 
	center_geometric_y_relative FLOAT, 
	PRIMARY KEY (backref_id, center_geometric_y_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_geometric_x" (
	backref_id TEXT, 
	center_geometric_x FLOAT, 
	PRIMARY KEY (backref_id, center_geometric_x), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_geometric_x_relative" (
	backref_id TEXT, 
	center_geometric_x_relative FLOAT, 
	PRIMARY KEY (backref_id, center_geometric_x_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_geometric_distance_relative" (
	backref_id TEXT, 
	center_geometric_distance_relative FLOAT, 
	PRIMARY KEY (backref_id, center_geometric_distance_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_fitted_y" (
	backref_id TEXT, 
	center_fitted_y FLOAT, 
	PRIMARY KEY (backref_id, center_fitted_y), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_fitted_y_relative" (
	backref_id TEXT, 
	center_fitted_y_relative FLOAT, 
	PRIMARY KEY (backref_id, center_fitted_y_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_fitted_x" (
	backref_id TEXT, 
	center_fitted_x FLOAT, 
	PRIMARY KEY (backref_id, center_fitted_x), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_fitted_x_relative" (
	backref_id TEXT, 
	center_fitted_x_relative FLOAT, 
	PRIMARY KEY (backref_id, center_fitted_x_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_center_fitted_distance_relative" (
	backref_id TEXT, 
	center_fitted_distance_relative FLOAT, 
	PRIMARY KEY (backref_id, center_fitted_distance_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity" (
	backref_id TEXT, 
	max_intensity FLOAT, 
	PRIMARY KEY (backref_id, max_intensity), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_y" (
	backref_id TEXT, 
	max_intensity_pos_y FLOAT, 
	PRIMARY KEY (backref_id, max_intensity_pos_y), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_y_relative" (
	backref_id TEXT, 
	max_intensity_pos_y_relative FLOAT, 
	PRIMARY KEY (backref_id, max_intensity_pos_y_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_x" (
	backref_id TEXT, 
	max_intensity_pos_x FLOAT, 
	PRIMARY KEY (backref_id, max_intensity_pos_x), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_x_relative" (
	backref_id TEXT, 
	max_intensity_pos_x_relative FLOAT, 
	PRIMARY KEY (backref_id, max_intensity_pos_x_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_max_intensity_distance_relative" (
	backref_id TEXT, 
	max_intensity_distance_relative FLOAT, 
	PRIMARY KEY (backref_id, max_intensity_distance_relative), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_left_intensity_mean" (
	backref_id TEXT, 
	top_left_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, top_left_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_left_intensity_ratio" (
	backref_id TEXT, 
	top_left_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, top_left_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_center_intensity_mean" (
	backref_id TEXT, 
	top_center_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, top_center_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_center_intensity_ratio" (
	backref_id TEXT, 
	top_center_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, top_center_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_right_intensity_mean" (
	backref_id TEXT, 
	top_right_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, top_right_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_top_right_intensity_ratio" (
	backref_id TEXT, 
	top_right_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, top_right_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_left_intensity_mean" (
	backref_id TEXT, 
	middle_left_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, middle_left_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_left_intensity_ratio" (
	backref_id TEXT, 
	middle_left_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, middle_left_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_center_intensity_mean" (
	backref_id TEXT, 
	middle_center_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, middle_center_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_center_intensity_ratio" (
	backref_id TEXT, 
	middle_center_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, middle_center_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_right_intensity_mean" (
	backref_id TEXT, 
	middle_right_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, middle_right_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_middle_right_intensity_ratio" (
	backref_id TEXT, 
	middle_right_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, middle_right_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_left_intensity_mean" (
	backref_id TEXT, 
	bottom_left_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, bottom_left_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_left_intensity_ratio" (
	backref_id TEXT, 
	bottom_left_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, bottom_left_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_center_intensity_mean" (
	backref_id TEXT, 
	bottom_center_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, bottom_center_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_center_intensity_ratio" (
	backref_id TEXT, 
	bottom_center_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, bottom_center_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_right_intensity_mean" (
	backref_id TEXT, 
	bottom_right_intensity_mean FLOAT, 
	PRIMARY KEY (backref_id, bottom_right_intensity_mean), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationKeyValues_bottom_right_intensity_ratio" (
	backref_id TEXT, 
	bottom_right_intensity_ratio FLOAT, 
	PRIMARY KEY (backref_id, bottom_right_intensity_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationKeyValues" (data_uri)
);

CREATE TABLE "FieldIlluminationProfilesIntensity_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "FieldIlluminationProfilesIntensity" (data_uri)
);

CREATE TABLE "Image2D_source_image_uri" (
	backref_id TEXT, 
	source_image_uri TEXT, 
	PRIMARY KEY (backref_id, source_image_uri), 
	FOREIGN KEY(backref_id) REFERENCES "Image2D" (data_uri)
);

CREATE TABLE "Image2D_data" (
	backref_id TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "Image2D" (data_uri)
);

CREATE TABLE "Image5D_source_image_uri" (
	backref_id TEXT, 
	source_image_uri TEXT, 
	PRIMARY KEY (backref_id, source_image_uri), 
	FOREIGN KEY(backref_id) REFERENCES "Image5D" (data_uri)
);

CREATE TABLE "Image5D_data" (
	backref_id TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "Image5D" (data_uri)
);

CREATE TABLE "ImageAsNumpy_source_image_uri" (
	backref_id TEXT, 
	source_image_uri TEXT, 
	PRIMARY KEY (backref_id, source_image_uri), 
	FOREIGN KEY(backref_id) REFERENCES "ImageAsNumpy" (data_uri)
);

CREATE TABLE "ImageMask_source_image_uri" (
	backref_id TEXT, 
	source_image_uri TEXT, 
	PRIMARY KEY (backref_id, source_image_uri), 
	FOREIGN KEY(backref_id) REFERENCES "ImageMask" (data_uri)
);

CREATE TABLE "ImageMask_data" (
	backref_id TEXT, 
	data BOOLEAN NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "ImageMask" (data_uri)
);

CREATE TABLE "PSFBeadsCenters_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsCenters" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_channel_nr" (
	backref_id TEXT, 
	channel_nr INTEGER, 
	PRIMARY KEY (backref_id, channel_nr), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_analyzed" (
	backref_id TEXT, 
	nr_of_beads_analyzed INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_analyzed), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_discarded_lateral_edge" (
	backref_id TEXT, 
	nr_of_beads_discarded_lateral_edge INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_discarded_lateral_edge), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_discarded_self_proximity" (
	backref_id TEXT, 
	nr_of_beads_discarded_self_proximity INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_discarded_self_proximity), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_axial_edge" (
	backref_id TEXT, 
	nr_of_beads_considered_axial_edge INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_considered_axial_edge), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_intensity_outlier" (
	backref_id TEXT, 
	nr_of_beads_considered_intensity_outlier INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_considered_intensity_outlier), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_z_fit" (
	backref_id TEXT, 
	nr_of_beads_considered_bad_z_fit INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_considered_bad_z_fit), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_y_fit" (
	backref_id TEXT, 
	nr_of_beads_considered_bad_y_fit INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_considered_bad_y_fit), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_x_fit" (
	backref_id TEXT, 
	nr_of_beads_considered_bad_x_fit INTEGER, 
	PRIMARY KEY (backref_id, nr_of_beads_considered_bad_x_fit), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_mean" (
	backref_id TEXT, 
	fit_rss_z_mean FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_z_mean), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_median" (
	backref_id TEXT, 
	fit_rss_z_median FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_z_median), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_std" (
	backref_id TEXT, 
	fit_rss_z_std FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_z_std), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_mean" (
	backref_id TEXT, 
	fit_rss_y_mean FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_y_mean), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_median" (
	backref_id TEXT, 
	fit_rss_y_median FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_y_median), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_std" (
	backref_id TEXT, 
	fit_rss_y_std FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_y_std), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_mean" (
	backref_id TEXT, 
	fit_rss_x_mean FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_x_mean), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_median" (
	backref_id TEXT, 
	fit_rss_x_median FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_x_median), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_std" (
	backref_id TEXT, 
	fit_rss_x_std FLOAT, 
	PRIMARY KEY (backref_id, fit_rss_x_std), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_z_pixels" (
	backref_id TEXT, 
	resolution_mean_fwhm_z_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_z_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_z_pixels" (
	backref_id TEXT, 
	resolution_median_fwhm_z_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_z_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_z_pixels" (
	backref_id TEXT, 
	resolution_std_fwhm_z_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_z_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_y_pixels" (
	backref_id TEXT, 
	resolution_mean_fwhm_y_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_y_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_y_pixels" (
	backref_id TEXT, 
	resolution_median_fwhm_y_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_y_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_y_pixels" (
	backref_id TEXT, 
	resolution_std_fwhm_y_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_y_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_x_pixels" (
	backref_id TEXT, 
	resolution_mean_fwhm_x_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_x_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_x_pixels" (
	backref_id TEXT, 
	resolution_median_fwhm_x_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_x_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_x_pixels" (
	backref_id TEXT, 
	resolution_std_fwhm_x_pixels FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_x_pixels), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_z_microns" (
	backref_id TEXT, 
	resolution_mean_fwhm_z_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_z_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_z_microns" (
	backref_id TEXT, 
	resolution_median_fwhm_z_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_z_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_z_microns" (
	backref_id TEXT, 
	resolution_std_fwhm_z_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_z_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_y_microns" (
	backref_id TEXT, 
	resolution_mean_fwhm_y_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_y_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_y_microns" (
	backref_id TEXT, 
	resolution_median_fwhm_y_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_y_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_y_microns" (
	backref_id TEXT, 
	resolution_std_fwhm_y_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_y_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_x_microns" (
	backref_id TEXT, 
	resolution_mean_fwhm_x_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_x_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_x_microns" (
	backref_id TEXT, 
	resolution_median_fwhm_x_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_x_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_x_microns" (
	backref_id TEXT, 
	resolution_std_fwhm_x_microns FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_x_microns), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_lateral_asymmetry_ratio" (
	backref_id TEXT, 
	resolution_mean_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY (backref_id, resolution_mean_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_lateral_asymmetry_ratio" (
	backref_id TEXT, 
	resolution_median_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY (backref_id, resolution_median_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_lateral_asymmetry_ratio" (
	backref_id TEXT, 
	resolution_std_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY (backref_id, resolution_std_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY(backref_id) REFERENCES "PSFBeadsKeyValues" (data_uri)
);

CREATE TABLE "Roi_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "Roi" (data_uri)
);
