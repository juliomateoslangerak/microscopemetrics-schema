

CREATE TABLE "ArgolightBDistanceKeyValues" (
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
	PRIMARY KEY ("channel_A", "channel_B", mean_3d_dist, median_3d_dist, std_3d_dist, mad_3d_dist, mean_z_dist, median_z_dist, std_z_dist, mad_z_dist)
);

CREATE TABLE "ArgolightBIntensityKeyValues" (
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
	PRIMARY KEY (channel_nr, nr_of_spots, intensity_max_spot, intensity_max_spot_roi, intensity_min_spot, intensity_min_spot_roi, mean_intensity, median_intensity, std_mean_intensity, mad_mean_intensity, min_max_intensity_ratio)
);

CREATE TABLE "ArgolightEKeyValues" (
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
	PRIMARY KEY (channel_nr, focus_slice, rayleigh_resolution_pixels, rayleigh_resolution_microns, "peak_position_A", "peak_position_B", "peak_height_A", "peak_height_B", "peak_prominence_A", "peak_prominence_B")
);

CREATE TABLE "ArgolightEOutput" (
	peaks_rois TEXT, 
	key_measurements TEXT, 
	intensity_profiles TEXT, 
	PRIMARY KEY (peaks_rois, key_measurements, intensity_profiles)
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
	name TEXT NOT NULL, 
	source_uri TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "Comment" (
	datetime DATETIME NOT NULL, 
	comment_type VARCHAR(11), 
	text TEXT NOT NULL, 
	PRIMARY KEY (datetime, comment_type, text)
);

CREATE TABLE "Ellipse" (
	label TEXT NOT NULL, 
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
	PRIMARY KEY (label)
);

CREATE TABLE "Experimenter" (
	name TEXT NOT NULL, 
	orcid TEXT NOT NULL, 
	PRIMARY KEY (orcid)
);

CREATE TABLE "FieldIlluminationKeyValues" (
	channel_nr INTEGER, 
	center_region_intensity_fraction FLOAT, 
	center_region_area_fraction FLOAT, 
	centroid_weighted_y FLOAT, 
	centroid_weighted_y_relative FLOAT, 
	centroid_weighted_x FLOAT, 
	centroid_weighted_x_relative FLOAT, 
	centroid_weighted_distance_relative FLOAT, 
	centroid_y FLOAT, 
	centroid_y_relative FLOAT, 
	centroid_x FLOAT, 
	centroid_x_relative FLOAT, 
	centroid_distance_relative FLOAT, 
	centroid_fitted_y FLOAT, 
	centroid_fitted_y_relative FLOAT, 
	centroid_fitted_x FLOAT, 
	centroid_fitted_x_relative FLOAT, 
	centroid_fitted_distance_relative FLOAT, 
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
	PRIMARY KEY (channel_nr, center_region_intensity_fraction, center_region_area_fraction, centroid_weighted_y, centroid_weighted_y_relative, centroid_weighted_x, centroid_weighted_x_relative, centroid_weighted_distance_relative, centroid_y, centroid_y_relative, centroid_x, centroid_x_relative, centroid_distance_relative, centroid_fitted_y, centroid_fitted_y_relative, centroid_fitted_x, centroid_fitted_x_relative, centroid_fitted_distance_relative, max_intensity, max_intensity_pos_y, max_intensity_pos_y_relative, max_intensity_pos_x, max_intensity_pos_x_relative, max_intensity_distance_relative, top_left_intensity_mean, top_left_intensity_ratio, top_center_intensity_mean, top_center_intensity_ratio, top_right_intensity_mean, top_right_intensity_ratio, middle_left_intensity_mean, middle_left_intensity_ratio, middle_center_intensity_mean, middle_center_intensity_ratio, middle_right_intensity_mean, middle_right_intensity_ratio, bottom_left_intensity_mean, bottom_left_intensity_ratio, bottom_center_intensity_mean, bottom_center_intensity_ratio, bottom_right_intensity_mean, bottom_right_intensity_ratio)
);

CREATE TABLE "Image2D" (
	name TEXT, 
	description TEXT, 
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	PRIMARY KEY (image_url)
);

CREATE TABLE "Image5D" (
	name TEXT, 
	description TEXT, 
	image_url TEXT NOT NULL, 
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
	PRIMARY KEY (image_url)
);

CREATE TABLE "ImageAsNumpy" (
	name TEXT, 
	description TEXT, 
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	data TEXT, 
	PRIMARY KEY (image_url)
);

CREATE TABLE "ImageMask" (
	name TEXT, 
	description TEXT, 
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	PRIMARY KEY (image_url)
);

CREATE TABLE "Microscope" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	type VARCHAR(10), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	url TEXT, 
	comment TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Point" (
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y FLOAT NOT NULL, 
	x FLOAT NOT NULL, 
	PRIMARY KEY (label)
);

CREATE TABLE "Polygon" (
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	is_open BOOLEAN NOT NULL, 
	PRIMARY KEY (label)
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
	fitting_rss_threshold FLOAT NOT NULL, 
	intensity_zscore_threshold FLOAT NOT NULL, 
	PRIMARY KEY (psf_beads_images, bit_depth, saturation_threshold, min_lateral_distance_factor, sigma_z, sigma_y, sigma_x, snr_threshold, fitting_rss_threshold, intensity_zscore_threshold)
);

CREATE TABLE "PSFBeadsKeyMeasurements" (
	channel_nr INTEGER, 
	nr_of_beads_analyzed INTEGER, 
	nr_of_beads_discarded_lateral_edge INTEGER, 
	nr_of_beads_discarded_self_proximity INTEGER, 
	nr_of_beads_considered_axial_edge INTEGER, 
	nr_of_beads_considered_intensity_outlier INTEGER, 
	nr_of_beads_considered_bad_z_fit INTEGER, 
	nr_of_beads_considered_bad_y_fit INTEGER, 
	nr_of_beads_considered_bad_x_fit INTEGER, 
	fit_rss_z_mean FLOAT, 
	fit_rss_z_median FLOAT, 
	fit_rss_z_std FLOAT, 
	fit_rss_y_mean FLOAT, 
	fit_rss_y_median FLOAT, 
	fit_rss_y_std FLOAT, 
	fit_rss_x_mean FLOAT, 
	fit_rss_x_median FLOAT, 
	fit_rss_x_std FLOAT, 
	resolution_mean_fwhm_z_pixels FLOAT, 
	resolution_median_fwhm_z_pixels FLOAT, 
	resolution_std_fwhm_z_pixels FLOAT, 
	resolution_mean_fwhm_y_pixels FLOAT, 
	resolution_median_fwhm_y_pixels FLOAT, 
	resolution_std_fwhm_y_pixels FLOAT, 
	resolution_mean_fwhm_x_pixels FLOAT, 
	resolution_median_fwhm_x_pixels FLOAT, 
	resolution_std_fwhm_x_pixels FLOAT, 
	resolution_mean_fwhm_z_microns FLOAT, 
	resolution_median_fwhm_z_microns FLOAT, 
	resolution_std_fwhm_z_microns FLOAT, 
	resolution_mean_fwhm_y_microns FLOAT, 
	resolution_median_fwhm_y_microns FLOAT, 
	resolution_std_fwhm_y_microns FLOAT, 
	resolution_mean_fwhm_x_microns FLOAT, 
	resolution_median_fwhm_x_microns FLOAT, 
	resolution_std_fwhm_x_microns FLOAT, 
	resolution_mean_fwhm_lateral_asymmetry_ratio FLOAT, 
	resolution_median_fwhm_lateral_asymmetry_ratio FLOAT, 
	resolution_std_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY (channel_nr, nr_of_beads_analyzed, nr_of_beads_discarded_lateral_edge, nr_of_beads_discarded_self_proximity, nr_of_beads_considered_axial_edge, nr_of_beads_considered_intensity_outlier, nr_of_beads_considered_bad_z_fit, nr_of_beads_considered_bad_y_fit, nr_of_beads_considered_bad_x_fit, fit_rss_z_mean, fit_rss_z_median, fit_rss_z_std, fit_rss_y_mean, fit_rss_y_median, fit_rss_y_std, fit_rss_x_mean, fit_rss_x_median, fit_rss_x_std, resolution_mean_fwhm_z_pixels, resolution_median_fwhm_z_pixels, resolution_std_fwhm_z_pixels, resolution_mean_fwhm_y_pixels, resolution_median_fwhm_y_pixels, resolution_std_fwhm_y_pixels, resolution_mean_fwhm_x_pixels, resolution_median_fwhm_x_pixels, resolution_std_fwhm_x_pixels, resolution_mean_fwhm_z_microns, resolution_median_fwhm_z_microns, resolution_std_fwhm_z_microns, resolution_mean_fwhm_y_microns, resolution_median_fwhm_y_microns, resolution_std_fwhm_y_microns, resolution_mean_fwhm_x_microns, resolution_median_fwhm_x_microns, resolution_std_fwhm_x_microns, resolution_mean_fwhm_lateral_asymmetry_ratio, resolution_median_fwhm_lateral_asymmetry_ratio, resolution_std_fwhm_lateral_asymmetry_ratio)
);

CREATE TABLE "PSFBeadsOutput" (
	bead_crops TEXT, 
	analyzed_bead_centroids TEXT, 
	discarded_bead_centroids_lateral_edge TEXT, 
	discarded_bead_centroids_self_proximity TEXT, 
	considered_bead_centroids_axial_edge TEXT, 
	considered_bead_centroids_intensity_outlier TEXT, 
	considered_bead_centroids_fit_quality TEXT, 
	key_values TEXT, 
	bead_properties TEXT, 
	bead_z_profiles TEXT, 
	bead_y_profiles TEXT, 
	bead_x_profiles TEXT, 
	PRIMARY KEY (bead_crops, analyzed_bead_centroids, discarded_bead_centroids_lateral_edge, discarded_bead_centroids_self_proximity, considered_bead_centroids_axial_edge, considered_bead_centroids_intensity_outlier, considered_bead_centroids_fit_quality, key_values, bead_properties, bead_z_profiles, bead_y_profiles, bead_x_profiles)
);

CREATE TABLE "Roi" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);

CREATE TABLE "RoiGeometricCenters" (
	label TEXT NOT NULL, 
	description TEXT, 
	shapes TEXT, 
	PRIMARY KEY (label)
);

CREATE TABLE "RoiMassCenters" (
	label TEXT NOT NULL, 
	description TEXT, 
	shapes TEXT, 
	PRIMARY KEY (label)
);

CREATE TABLE "RoiMeasurements" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);

CREATE TABLE "RoiProfiles" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);

CREATE TABLE "TableAsPandasDF" (
	name TEXT, 
	description TEXT, 
	table_url TEXT, 
	df TEXT NOT NULL, 
	PRIMARY KEY (name, description, table_url, df)
);

CREATE TABLE "TimeSeries" (
	"values" FLOAT NOT NULL, 
	PRIMARY KEY ("values")
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
	FOREIGN KEY(argolight_b_image) REFERENCES "ImageAsNumpy" (image_url)
);

CREATE TABLE "ArgolightBOutput" (
	spots_labels_image TEXT, 
	spots_centroids TEXT, 
	intensity_key_values TEXT, 
	distance_key_values TEXT, 
	spots_properties TEXT, 
	spots_distances TEXT, 
	PRIMARY KEY (spots_labels_image, spots_centroids, intensity_key_values, distance_key_values, spots_properties, spots_distances), 
	FOREIGN KEY(spots_labels_image) REFERENCES "ImageAsNumpy" (image_url)
);

CREATE TABLE "ArgolightEInput" (
	argolight_e_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	orientation_axis INTEGER NOT NULL, 
	measured_band FLOAT NOT NULL, 
	prominence_threshold FLOAT NOT NULL, 
	PRIMARY KEY (argolight_e_image, bit_depth, saturation_threshold, orientation_axis, measured_band, prominence_threshold), 
	FOREIGN KEY(argolight_e_image) REFERENCES "ImageAsNumpy" (image_url)
);

CREATE TABLE "FieldIlluminationInput" (
	field_illumination_image TEXT NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	intensity_map_size INTEGER NOT NULL, 
	PRIMARY KEY (field_illumination_image, bit_depth, saturation_threshold, corner_fraction, sigma, intensity_map_size), 
	FOREIGN KEY(field_illumination_image) REFERENCES "ImageAsNumpy" (image_url)
);

CREATE TABLE "FieldIlluminationOutput" (
	key_values TEXT, 
	intensity_profiles TEXT, 
	intensity_map TEXT, 
	roi_profiles TEXT, 
	roi_corners TEXT, 
	roi_centroids_weighted TEXT, 
	PRIMARY KEY (key_values, intensity_profiles, intensity_map, roi_profiles, roi_corners, roi_centroids_weighted), 
	FOREIGN KEY(intensity_map) REFERENCES "Image5D" (image_url), 
	FOREIGN KEY(roi_profiles) REFERENCES "RoiProfiles" (label), 
	FOREIGN KEY(roi_corners) REFERENCES "RoiMeasurements" (label)
);

CREATE TABLE "Line" (
	label TEXT NOT NULL, 
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
	"RoiProfiles_label" TEXT, 
	PRIMARY KEY (label), 
	FOREIGN KEY("RoiProfiles_label") REFERENCES "RoiProfiles" (label)
);

CREATE TABLE "Mask" (
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	fill_color TEXT, 
	stroke_color TEXT, 
	stroke_width INTEGER, 
	y INTEGER NOT NULL, 
	x INTEGER NOT NULL, 
	mask TEXT, 
	PRIMARY KEY (label), 
	FOREIGN KEY(mask) REFERENCES "ImageMask" (image_url)
);

CREATE TABLE "Rectangle" (
	label TEXT NOT NULL, 
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
	"RoiMeasurements_label" TEXT, 
	PRIMARY KEY (label), 
	FOREIGN KEY("RoiMeasurements_label") REFERENCES "RoiMeasurements" (label)
);

CREATE TABLE "Sample" (
	name TEXT, 
	description TEXT, 
	type TEXT NOT NULL, 
	protocol TEXT NOT NULL, 
	PRIMARY KEY (type), 
	FOREIGN KEY(protocol) REFERENCES "Protocol" (url)
);

CREATE TABLE "Vertex" (
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	"Polygon_label" TEXT, 
	PRIMARY KEY (x, y, "Polygon_label"), 
	FOREIGN KEY("Polygon_label") REFERENCES "Polygon" (label)
);

CREATE TABLE "Column_values" (
	backref_id TEXT, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (backref_id, "values"), 
	FOREIGN KEY(backref_id) REFERENCES "Column" (name)
);

CREATE TABLE "Image2D_source_image_url" (
	backref_id TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY (backref_id, source_image_url), 
	FOREIGN KEY(backref_id) REFERENCES "Image2D" (image_url)
);

CREATE TABLE "Image2D_data" (
	backref_id TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "Image2D" (image_url)
);

CREATE TABLE "Image5D_source_image_url" (
	backref_id TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY (backref_id, source_image_url), 
	FOREIGN KEY(backref_id) REFERENCES "Image5D" (image_url)
);

CREATE TABLE "Image5D_data" (
	backref_id TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "Image5D" (image_url)
);

CREATE TABLE "ImageAsNumpy_source_image_url" (
	backref_id TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY (backref_id, source_image_url), 
	FOREIGN KEY(backref_id) REFERENCES "ImageAsNumpy" (image_url)
);

CREATE TABLE "ImageMask_source_image_url" (
	backref_id TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY (backref_id, source_image_url), 
	FOREIGN KEY(backref_id) REFERENCES "ImageMask" (image_url)
);

CREATE TABLE "ImageMask_data" (
	backref_id TEXT, 
	data BOOLEAN NOT NULL, 
	PRIMARY KEY (backref_id, data), 
	FOREIGN KEY(backref_id) REFERENCES "ImageMask" (image_url)
);

CREATE TABLE "Roi_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "Roi" (label)
);

CREATE TABLE "Roi_shapes" (
	backref_id TEXT, 
	shapes TEXT, 
	PRIMARY KEY (backref_id, shapes), 
	FOREIGN KEY(backref_id) REFERENCES "Roi" (label)
);

CREATE TABLE "RoiGeometricCenters_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "RoiGeometricCenters" (label)
);

CREATE TABLE "RoiMassCenters_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "RoiMassCenters" (label)
);

CREATE TABLE "RoiMeasurements_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "RoiMeasurements" (label)
);

CREATE TABLE "RoiProfiles_image" (
	backref_id TEXT, 
	image TEXT, 
	PRIMARY KEY (backref_id, image), 
	FOREIGN KEY(backref_id) REFERENCES "RoiProfiles" (label)
);

CREATE TABLE "ArgolightBDataset" (
	name TEXT, 
	description TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	comment TEXT, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (name, description, microscope, sample, experimenter, acquisition_datetime, processed, processing_datetime, processing_log, comment, input, output), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type)
);

CREATE TABLE "ArgolightEDataset" (
	name TEXT, 
	description TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	comment TEXT, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (name, description, microscope, sample, experimenter, acquisition_datetime, processed, processing_datetime, processing_log, comment, input, output), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type)
);

CREATE TABLE "FieldIlluminationDataset" (
	name TEXT, 
	description TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	comment TEXT, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (name, description, microscope, sample, experimenter, acquisition_datetime, processed, processing_datetime, processing_log, comment, input, output), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type)
);

CREATE TABLE "MetricsDataset" (
	name TEXT, 
	description TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	comment TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (name, description, microscope, sample, experimenter, acquisition_datetime, processed, processing_datetime, processing_log, comment, input, output), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type)
);

CREATE TABLE "PSFBeadsDataset" (
	name TEXT, 
	description TEXT, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	comment TEXT, 
	input TEXT NOT NULL, 
	output TEXT, 
	PRIMARY KEY (name, description, microscope, sample, experimenter, acquisition_datetime, processed, processing_datetime, processing_log, comment, input, output), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type)
);
