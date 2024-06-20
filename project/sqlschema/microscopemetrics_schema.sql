

CREATE TABLE "ArgolightBCentersOfMass" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, points, lines, rectangles, ellipses, polygons, masks)
);

CREATE TABLE "ArgolightBDistanceKeyValues" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	"channel_A" INTEGER, 
	"channel_B" INTEGER, 
	mean_3d_dist FLOAT, 
	median_3d_dist FLOAT, 
	std_3d_dist FLOAT, 
	mad_3d_dist FLOAT, 
	mean_z_dist FLOAT, 
	median_z_dist FLOAT, 
	std_z_dist FLOAT, 
	mad_z_dist FLOAT, 
	PRIMARY KEY (name, description, data_reference, linked_references, "channel_A", "channel_B", mean_3d_dist, median_3d_dist, std_3d_dist, mad_3d_dist, mean_z_dist, median_z_dist, std_z_dist, mad_z_dist)
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
	PRIMARY KEY (argolight_b_image, bit_depth, saturation_threshold, spots_distance, sigma_z, sigma_y, sigma_x, lower_threshold_correction_factors, upper_threshold_correction_factors, remove_center_cross)
);

CREATE TABLE "ArgolightBIntensityKeyValues" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	channel_nr INTEGER, 
	nr_of_spots INTEGER, 
	intensity_max_spot FLOAT, 
	intensity_max_spot_roi INTEGER, 
	intensity_min_spot FLOAT, 
	intensity_min_spot_roi INTEGER, 
	mean_intensity FLOAT, 
	median_intensity FLOAT, 
	std_mean_intensity FLOAT, 
	mad_mean_intensity FLOAT, 
	min_max_intensity_ratio FLOAT, 
	PRIMARY KEY (name, description, data_reference, linked_references, channel_nr, nr_of_spots, intensity_max_spot, intensity_max_spot_roi, intensity_min_spot, intensity_min_spot_roi, mean_intensity, median_intensity, std_mean_intensity, mad_mean_intensity, min_max_intensity_ratio)
);

CREATE TABLE "ArgolightBOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	comment TEXT, 
	spots_labels_image TEXT, 
	spots_centers_of_mass TEXT, 
	intensity_key_values TEXT, 
	distance_key_values TEXT, 
	spots_properties TEXT, 
	spots_distances TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, validated, validation_datetime, comment, spots_labels_image, spots_centers_of_mass, intensity_key_values, distance_key_values, spots_properties, spots_distances)
);

CREATE TABLE "ArgolightEInput" (
	argolight_e_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	orientation_axis INTEGER NOT NULL, 
	measured_band FLOAT NOT NULL, 
	prominence_threshold FLOAT NOT NULL, 
	PRIMARY KEY (argolight_e_image, bit_depth, saturation_threshold, orientation_axis, measured_band, prominence_threshold)
);

CREATE TABLE "ArgolightEKeyValues" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	channel_nr INTEGER, 
	focus_slice INTEGER, 
	rayleigh_resolution_pixels FLOAT, 
	rayleigh_resolution_microns FLOAT, 
	"peak_position_A" FLOAT, 
	"peak_position_B" FLOAT, 
	"peak_height_A" FLOAT, 
	"peak_height_B" FLOAT, 
	"peak_prominence_A" FLOAT, 
	"peak_prominence_B" FLOAT, 
	PRIMARY KEY (name, description, data_reference, linked_references, channel_nr, focus_slice, rayleigh_resolution_pixels, rayleigh_resolution_microns, "peak_position_A", "peak_position_B", "peak_height_A", "peak_height_B", "peak_prominence_A", "peak_prominence_B")
);

CREATE TABLE "ArgolightEOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	comment TEXT, 
	peaks_rois TEXT, 
	key_measurements TEXT, 
	intensity_profiles TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, validated, validation_datetime, comment, peaks_rois, key_measurements, intensity_profiles)
);

CREATE TABLE "Channel" (
	name TEXT, 
	description TEXT, 
	excitation_wavelength_nm FLOAT, 
	emission_wavelength_nm FLOAT, 
	PRIMARY KEY (name, description, excitation_wavelength_nm, emission_wavelength_nm)
);

CREATE TABLE "ChannelSeries" (
	channels TEXT NOT NULL, 
	PRIMARY KEY (channels)
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
	source_reference TEXT, 
	data_type TEXT NOT NULL, 
	"values" TEXT, 
	PRIMARY KEY (name, description, source_reference, data_type, "values")
);

CREATE TABLE "DataReference" (
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(17), 
	omero_object_id INTEGER, 
	PRIMARY KEY (data_uri, omero_host, omero_port, omero_object_type, omero_object_id)
);

CREATE TABLE "Ellipse" (
	name TEXT, 
	description TEXT, 
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
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, x, y, x_rad, y_rad)
);

CREATE TABLE "Experimenter" (
	name TEXT NOT NULL, 
	orcid TEXT NOT NULL, 
	PRIMARY KEY (orcid)
);

CREATE TABLE "FieldIlluminationInput" (
	field_illumination_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	PRIMARY KEY (field_illumination_image, bit_depth, saturation_threshold, corner_fraction, sigma)
);

CREATE TABLE "FieldIlluminationKeyMeasurements" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	table_data TEXT, 
	channel_name TEXT, 
	center_region_intensity_fraction FLOAT, 
	center_region_area_fraction FLOAT, 
	center_of_mass_y FLOAT, 
	center_of_mass_y_relative FLOAT, 
	center_of_mass_x FLOAT, 
	center_of_mass_x_relative FLOAT, 
	center_of_mass_distance_relative FLOAT, 
	center_geometric_y FLOAT, 
	center_geometric_y_relative FLOAT, 
	center_geometric_x FLOAT, 
	center_geometric_x_relative FLOAT, 
	center_geometric_distance_relative FLOAT, 
	center_fitted_y FLOAT, 
	center_fitted_y_relative FLOAT, 
	center_fitted_x FLOAT, 
	center_fitted_x_relative FLOAT, 
	center_fitted_distance_relative FLOAT, 
	max_intensity FLOAT, 
	max_intensity_pos_y FLOAT, 
	max_intensity_pos_y_relative FLOAT, 
	max_intensity_pos_x FLOAT, 
	max_intensity_pos_x_relative FLOAT, 
	max_intensity_distance_relative FLOAT, 
	top_left_intensity_mean FLOAT, 
	top_left_intensity_ratio FLOAT, 
	top_center_intensity_mean FLOAT, 
	top_center_intensity_ratio FLOAT, 
	top_right_intensity_mean FLOAT, 
	top_right_intensity_ratio FLOAT, 
	middle_left_intensity_mean FLOAT, 
	middle_left_intensity_ratio FLOAT, 
	middle_center_intensity_mean FLOAT, 
	middle_center_intensity_ratio FLOAT, 
	middle_right_intensity_mean FLOAT, 
	middle_right_intensity_ratio FLOAT, 
	bottom_left_intensity_mean FLOAT, 
	bottom_left_intensity_ratio FLOAT, 
	bottom_center_intensity_mean FLOAT, 
	bottom_center_intensity_ratio FLOAT, 
	bottom_right_intensity_mean FLOAT, 
	bottom_right_intensity_ratio FLOAT, 
	PRIMARY KEY (name, description, data_reference, linked_references, table_data, channel_name, center_region_intensity_fraction, center_region_area_fraction, center_of_mass_y, center_of_mass_y_relative, center_of_mass_x, center_of_mass_x_relative, center_of_mass_distance_relative, center_geometric_y, center_geometric_y_relative, center_geometric_x, center_geometric_x_relative, center_geometric_distance_relative, center_fitted_y, center_fitted_y_relative, center_fitted_x, center_fitted_x_relative, center_fitted_distance_relative, max_intensity, max_intensity_pos_y, max_intensity_pos_y_relative, max_intensity_pos_x, max_intensity_pos_x_relative, max_intensity_distance_relative, top_left_intensity_mean, top_left_intensity_ratio, top_center_intensity_mean, top_center_intensity_ratio, top_right_intensity_mean, top_right_intensity_ratio, middle_left_intensity_mean, middle_left_intensity_ratio, middle_center_intensity_mean, middle_center_intensity_ratio, middle_right_intensity_mean, middle_right_intensity_ratio, bottom_left_intensity_mean, bottom_left_intensity_ratio, bottom_center_intensity_mean, bottom_center_intensity_ratio, bottom_right_intensity_mean, bottom_right_intensity_ratio)
);

CREATE TABLE "FieldIlluminationOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	comment TEXT, 
	key_measurements TEXT, 
	intensity_profiles TEXT, 
	roi_profiles TEXT, 
	roi_corners TEXT, 
	roi_centers_of_mass TEXT, 
	roi_centers_geometric TEXT, 
	roi_centers_fitted TEXT, 
	roi_centers_max_intensity TEXT, 
	roi_center_region TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, validated, validation_datetime, comment, key_measurements, intensity_profiles, roi_profiles, roi_corners, roi_centers_of_mass, roi_centers_geometric, roi_centers_fitted, roi_centers_max_intensity, roi_center_region)
);

CREATE TABLE "HarmonizedMetricsDatasetCollection" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	datasets TEXT, 
	dataset_class TEXT NOT NULL, 
	PRIMARY KEY (name, description, data_reference, linked_references, datasets, dataset_class)
);

CREATE TABLE "Image" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
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
	acquisition_datetime DATETIME, 
	source_images TEXT, 
	array_data TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, voxel_size_x_micron, voxel_size_y_micron, voxel_size_z_micron, shape_x, shape_y, shape_z, shape_c, shape_t, time_series, channel_series, acquisition_datetime, source_images, array_data)
);

CREATE TABLE "ImageMask" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
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
	acquisition_datetime DATETIME, 
	source_images TEXT, 
	array_data TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, voxel_size_x_micron, voxel_size_y_micron, voxel_size_z_micron, shape_x, shape_y, shape_z, shape_c, shape_t, time_series, channel_series, acquisition_datetime, source_images, array_data)
);

CREATE TABLE "Line" (
	name TEXT, 
	description TEXT, 
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
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, x1, y1, x2, y2)
);

CREATE TABLE "Mask" (
	name TEXT, 
	description TEXT, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y INTEGER NOT NULL, 
	x INTEGER NOT NULL, 
	mask TEXT, 
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, y, x, mask)
);

CREATE TABLE "MetricsDatasetCollection" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	datasets TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, datasets)
);

CREATE TABLE "Microscope" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	type VARCHAR(10), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	comments TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, type, manufacturer, model, serial_number, comments)
);

CREATE TABLE "MicroscopeCollection" (
	microscopes TEXT NOT NULL, 
	PRIMARY KEY (microscopes)
);

CREATE TABLE "Point" (
	name TEXT, 
	description TEXT, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y FLOAT NOT NULL, 
	x FLOAT NOT NULL, 
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, y, x)
);

CREATE TABLE "Polygon" (
	name TEXT, 
	description TEXT, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	vertexes TEXT NOT NULL, 
	is_open BOOLEAN NOT NULL, 
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, vertexes, is_open)
);

CREATE TABLE "Protocol" (
	name TEXT, 
	description TEXT, 
	version TEXT NOT NULL, 
	authors TEXT, 
	url TEXT NOT NULL, 
	PRIMARY KEY (url)
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
	fitting_r2_threshold FLOAT NOT NULL, 
	intensity_robust_z_score_threshold FLOAT NOT NULL, 
	PRIMARY KEY (psf_beads_images, bit_depth, saturation_threshold, min_lateral_distance_factor, sigma_z, sigma_y, sigma_x, snr_threshold, fitting_r2_threshold, intensity_robust_z_score_threshold)
);

CREATE TABLE "PSFBeadsKeyMeasurements" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	table_data TEXT, 
	channel_nr INTEGER, 
	considered_valid_count INTEGER, 
	considered_self_proximity_count INTEGER, 
	considered_lateral_edge_count INTEGER, 
	considered_axial_edge_count INTEGER, 
	considered_intensity_outlier_count INTEGER, 
	considered_bad_fit_z_count INTEGER, 
	considered_bad_fit_y_count INTEGER, 
	considered_bad_fit_x_count INTEGER, 
	intensity_integrated_mean FLOAT, 
	intensity_integrated_median FLOAT, 
	intensity_integrated_std FLOAT, 
	intensity_max_mean FLOAT, 
	intensity_max_median FLOAT, 
	intensity_max_std FLOAT, 
	intensity_min_mean FLOAT, 
	intensity_min_median FLOAT, 
	intensity_min_std FLOAT, 
	intensity_std_mean FLOAT, 
	intensity_std_median FLOAT, 
	intensity_std_std FLOAT, 
	fit_r2_z_mean FLOAT, 
	fit_r2_z_median FLOAT, 
	fit_r2_z_std FLOAT, 
	fit_r2_y_mean FLOAT, 
	fit_r2_y_median FLOAT, 
	fit_r2_y_std FLOAT, 
	fit_r2_x_mean FLOAT, 
	fit_r2_x_median FLOAT, 
	fit_r2_x_std FLOAT, 
	fwhm_pixel_z_mean FLOAT, 
	fwhm_pixel_z_median FLOAT, 
	fwhm_pixel_z_std FLOAT, 
	fwhm_pixel_y_mean FLOAT, 
	fwhm_pixel_y_median FLOAT, 
	fwhm_pixel_y_std FLOAT, 
	fwhm_pixel_x_mean FLOAT, 
	fwhm_pixel_x_median FLOAT, 
	fwhm_pixel_x_std FLOAT, 
	fwhm_micron_z_mean FLOAT, 
	fwhm_micron_z_median FLOAT, 
	fwhm_micron_z_std FLOAT, 
	fwhm_micron_y_mean FLOAT, 
	fwhm_micron_y_median FLOAT, 
	fwhm_micron_y_std FLOAT, 
	fwhm_micron_x_mean FLOAT, 
	fwhm_micron_x_median FLOAT, 
	fwhm_micron_x_std FLOAT, 
	fwhm_lateral_asymmetry_ratio_mean FLOAT, 
	fwhm_lateral_asymmetry_ratio_median FLOAT, 
	fwhm_lateral_asymmetry_ratio_std FLOAT, 
	average_bead_fit_r2_z FLOAT, 
	average_bead_fit_r2_y FLOAT, 
	average_bead_fit_r2_x FLOAT, 
	average_bead_fwhm_pixel_z FLOAT, 
	average_bead_fwhm_pixel_y FLOAT, 
	average_bead_fwhm_pixel_x FLOAT, 
	average_bead_fwhm_micron_z FLOAT, 
	average_bead_fwhm_micron_y FLOAT, 
	average_bead_fwhm_micron_x FLOAT, 
	average_bead_fwhm_lateral_asymmetry_ratio FLOAT, 
	average_bead_intensity_integrated FLOAT, 
	average_bead_intensity_max FLOAT, 
	average_bead_intensity_min FLOAT, 
	average_bead_intensity_std FLOAT, 
	PRIMARY KEY (name, description, data_reference, linked_references, table_data, channel_nr, considered_valid_count, considered_self_proximity_count, considered_lateral_edge_count, considered_axial_edge_count, considered_intensity_outlier_count, considered_bad_fit_z_count, considered_bad_fit_y_count, considered_bad_fit_x_count, intensity_integrated_mean, intensity_integrated_median, intensity_integrated_std, intensity_max_mean, intensity_max_median, intensity_max_std, intensity_min_mean, intensity_min_median, intensity_min_std, intensity_std_mean, intensity_std_median, intensity_std_std, fit_r2_z_mean, fit_r2_z_median, fit_r2_z_std, fit_r2_y_mean, fit_r2_y_median, fit_r2_y_std, fit_r2_x_mean, fit_r2_x_median, fit_r2_x_std, fwhm_pixel_z_mean, fwhm_pixel_z_median, fwhm_pixel_z_std, fwhm_pixel_y_mean, fwhm_pixel_y_median, fwhm_pixel_y_std, fwhm_pixel_x_mean, fwhm_pixel_x_median, fwhm_pixel_x_std, fwhm_micron_z_mean, fwhm_micron_z_median, fwhm_micron_z_std, fwhm_micron_y_mean, fwhm_micron_y_median, fwhm_micron_y_std, fwhm_micron_x_mean, fwhm_micron_x_median, fwhm_micron_x_std, fwhm_lateral_asymmetry_ratio_mean, fwhm_lateral_asymmetry_ratio_median, fwhm_lateral_asymmetry_ratio_std, average_bead_fit_r2_z, average_bead_fit_r2_y, average_bead_fit_r2_x, average_bead_fwhm_pixel_z, average_bead_fwhm_pixel_y, average_bead_fwhm_pixel_x, average_bead_fwhm_micron_z, average_bead_fwhm_micron_y, average_bead_fwhm_micron_x, average_bead_fwhm_lateral_asymmetry_ratio, average_bead_intensity_integrated, average_bead_intensity_max, average_bead_intensity_min, average_bead_intensity_std)
);

CREATE TABLE "PSFBeadsOutput" (
	processing_application TEXT NOT NULL, 
	processing_version TEXT NOT NULL, 
	processing_entity TEXT, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	warnings TEXT, 
	errors TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	comment TEXT, 
	analyzed_bead_centers TEXT, 
	considered_bead_centers_lateral_edge TEXT, 
	considered_bead_centers_self_proximity TEXT, 
	considered_bead_centers_axial_edge TEXT, 
	considered_bead_centers_intensity_outlier TEXT, 
	considered_bead_centers_z_fit_quality TEXT, 
	considered_bead_centers_y_fit_quality TEXT, 
	considered_bead_centers_x_fit_quality TEXT, 
	key_measurements TEXT, 
	bead_properties TEXT, 
	bead_profiles_z TEXT, 
	bead_profiles_y TEXT, 
	bead_profiles_x TEXT, 
	average_bead TEXT, 
	PRIMARY KEY (processing_application, processing_version, processing_entity, processing_datetime, processing_log, warnings, errors, validated, validation_datetime, comment, analyzed_bead_centers, considered_bead_centers_lateral_edge, considered_bead_centers_self_proximity, considered_bead_centers_axial_edge, considered_bead_centers_intensity_outlier, considered_bead_centers_z_fit_quality, considered_bead_centers_y_fit_quality, considered_bead_centers_x_fit_quality, key_measurements, bead_properties, bead_profiles_z, bead_profiles_y, bead_profiles_x, average_bead)
);

CREATE TABLE "Rectangle" (
	name TEXT, 
	description TEXT, 
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
	PRIMARY KEY (name, description, z, c, t, fill_color, stroke_color, stroke_width, x, y, w, h)
);

CREATE TABLE "Roi" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	points TEXT, 
	lines TEXT, 
	rectangles TEXT, 
	ellipses TEXT, 
	polygons TEXT, 
	masks TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, points, lines, rectangles, ellipses, polygons, masks)
);

CREATE TABLE "TimeSeries" (
	"values" FLOAT NOT NULL, 
	PRIMARY KEY ("values")
);

CREATE TABLE "Vertex" (
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	PRIMARY KEY (x, y)
);

CREATE TABLE "ArgolightBDataset" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, microscope, sample, experimenter, acquisition_datetime, processed, input, output), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid)
);

CREATE TABLE "ArgolightEDataset" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, microscope, sample, experimenter, acquisition_datetime, processed, input, output), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid)
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
	data_reference TEXT, 
	linked_references TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, microscope, sample, experimenter, acquisition_datetime, processed, input, output), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid)
);

CREATE TABLE "MetricsDataset" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, microscope, sample, experimenter, acquisition_datetime, processed, input, output), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid)
);

CREATE TABLE "PSFBeadsDataset" (
	name TEXT, 
	description TEXT, 
	data_reference TEXT, 
	linked_references TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (name, description, data_reference, linked_references, microscope, sample, experimenter, acquisition_datetime, processed, input, output), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid)
);

CREATE TABLE "Sample" (
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	protocol TEXT NOT NULL, 
	PRIMARY KEY (name, description, type, protocol), 
	FOREIGN KEY(protocol) REFERENCES "Protocol" (url)
);
