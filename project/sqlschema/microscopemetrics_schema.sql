-- # Class: "MetaObject" Description: ""
--     * Slot: id Description: 
-- # Class: "NamedObject" Description: "An object with a name and a description"
--     * Slot: id Description: 
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "MetricsObject" Description: "A base object for all microscope-metrics objects"
--     * Slot: id Description: 
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Device" Description: "A base object for all microscope-metrics devices"
--     * Slot: id Description: 
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Microscope" Description: "A microscope"
--     * Slot: id Description: The unique identifier for an entity
--     * Slot: type Description: The type of the microscope
--     * Slot: manufacturer Description: The manufacturer of the microscope
--     * Slot: model Description: The model of the microscope
--     * Slot: serial_number Description: The serial number of the microscope
--     * Slot: url Description: The URL where the microscope can be found
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Sample" Description: "A sample is a standard physical object that is imaged by a microscope"
--     * Slot: type Description: The type of the sample
--     * Slot: protocol Description: The protocol used to prepare the sample
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Protocol" Description: "Set of instructions for preparing and imaging a sample"
--     * Slot: version Description: The version of the protocol
--     * Slot: url Description: The URL where the protocol can be found
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Experimenter" Description: "The person that performed the experiment or developed the protocol"
--     * Slot: name Description: The name of the experimenter
--     * Slot: orcid Description: The ORCID of the experimenter
-- # Class: "Comment" Description: "A comment"
--     * Slot: id Description: 
--     * Slot: datetime Description: The datetime to which the comment is referring
--     * Slot: author Description: The author of the comment
--     * Slot: comment_type Description: The type of the comment
--     * Slot: text Description: The text of the comment
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: MetricsDataset_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationDataset_id Description: Autocreated FK slot
--     * Slot: PSFBeadsDataset_id Description: Autocreated FK slot
--     * Slot: ArgolightBDataset_id Description: Autocreated FK slot
--     * Slot: ArgolightEDataset_id Description: Autocreated FK slot
-- # Class: "MetricsDataset" Description: "A base object on which microscope-metrics runs the analysis"
--     * Slot: id Description: 
--     * Slot: microscope Description: The microscope that was used to acquire the dataset
--     * Slot: sample Description: The sample that was imaged
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: input_id Description: The input of the analysis
--     * Slot: output_id Description: The output of the analysis
-- # Class: "MetricsInput" Description: "An abstract class for analysis inputs"
--     * Slot: id Description: 
-- # Class: "MetricsOutput" Description: "An abstract class for analysis outputs"
--     * Slot: id Description: 
-- # Class: "Image" Description: "A base object for all microscope-metrics images"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "ImageAsNumpy" Description: "An image as a numpy array in TZYXC order"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: PSFBeadsInput_id Description: Autocreated FK slot
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: data_id Description: 
-- # Class: "ImageInline" Description: "A base object for all microscope-metrics images that are stored as arrays in line"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "ImageMask" Description: "A base object for all microscope-metrics masks"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Image2D" Description: "A 2D image in YX order"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Image5D" Description: "A 5D image in TZYXC order"
--     * Slot: image_url Description: An URL linking to the image
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: time_series_id Description: 
--     * Slot: channel_series_id Description: 
-- # Class: "ChannelSeries" Description: "A series whose values represent channel"
--     * Slot: id Description: 
-- # Class: "Channel" Description: "A image channel"
--     * Slot: id Description: 
--     * Slot: excitation_wavelength_nm Description: The excitation wavelength in nm
--     * Slot: emission_wavelength_nm Description: The emission wavelength in nm
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "TimeSeries" Description: "A series whose values represent time"
--     * Slot: id Description: 
-- # Class: "Roi" Description: "A ROI (Region Of Interest). Collection of shapes and an image to which they are applied"
--     * Slot: label Description: The label of the ROI
--     * Slot: description Description: A description of the ROI
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
-- # Class: "Shape" Description: "A shape"
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: Roi_label Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Point" Description: "A point as defined by x and y coordinates"
--     * Slot: y Description: The y coordinate of the point
--     * Slot: x Description: The x coordinate of the point
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: RoiMassCenters_label Description: Autocreated FK slot
--     * Slot: RoiGeometricCenters_label Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Line" Description: "A line as defined by x1, y1, x2, y2 coordinates"
--     * Slot: x1 Description: The x coordinate of the first point of the line
--     * Slot: y1 Description: The y coordinate of the first point of the line
--     * Slot: x2 Description: The x coordinate of the second point of the line
--     * Slot: y2 Description: The y coordinate of the second point of the line
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: RoiProfiles_label Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Rectangle" Description: "A rectangle as defined by x, y coordinates and width, height"
--     * Slot: x Description: The x coordinate of the top left corner of the rectangle
--     * Slot: y Description: The y coordinate of the top left corner of the rectangle
--     * Slot: w Description: The width of the rectangle
--     * Slot: h Description: The height of the rectangle
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: RoiMeasurements_label Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Ellipse" Description: "An ellipse as defined by x, y coordinates and x and y radii"
--     * Slot: x Description: The x coordinate of the bounding box of the ellipse
--     * Slot: y Description: The y coordinate of the bounding box of the ellipse
--     * Slot: x_rad Description: The x radius of the ellipse
--     * Slot: y_rad Description: The y radius of the ellipse
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Polygon" Description: "A polygon as defined by a series of vertexes and a boolean to indicate if closed or not"
--     * Slot: is_open Description: Is the polygon open. By default, it is closed (false)
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Vertex" Description: "A vertex as defined by x and y coordinates"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate of the vertex
--     * Slot: y Description: The y coordinate of the vertex
--     * Slot: Polygon_label Description: Autocreated FK slot
-- # Class: "Mask" Description: "A mask as defined by a boolean image"
--     * Slot: y Description: The y coordinate of the top left corner of the mask
--     * Slot: x Description: The x coordinate of the top left corner of the mask
--     * Slot: label Description: The label of the shape
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: mask_image_url Description: The mask image
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Color" Description: "A color as defined by RGB values and an optional alpha value"
--     * Slot: id Description: 
--     * Slot: r Description: The red value of the color
--     * Slot: g Description: The green value of the color
--     * Slot: b Description: The blue value of the color
--     * Slot: alpha Description: The alpha value of the color (optional)
-- # Class: "RoiMassCenters" Description: "Point ROIs marking the center of mass of detected objects"
--     * Slot: label Description: The label of the ROI
--     * Slot: description Description: A description of the ROI
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
-- # Class: "RoiGeometricCenters" Description: "Point ROIs marking the geometric center of detected objects"
--     * Slot: label Description: The label of the ROI
--     * Slot: description Description: A description of the ROI
-- # Class: "RoiProfiles" Description: "line ROIs where profiles were computed."
--     * Slot: label Description: The label of the ROI
--     * Slot: description Description: A description of the ROI
-- # Class: "RoiMeasurements" Description: "ROIs delimiting where measurements were performed."
--     * Slot: label Description: The label of the ROI
--     * Slot: description Description: A description of the ROI
-- # Class: "KeyValues" Description: "A collection of key-value pairs"
--     * Slot: id Description: 
-- # Class: "Tag" Description: "A tag"
--     * Slot: id Description: The id of the tag
--     * Slot: text Description: The text of the tag
--     * Slot: description Description: The description of the tag
-- # Class: "Table" Description: "A table"
--     * Slot: id Description: 
--     * Slot: table_url Description: An URL linking to the table
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "TableAsPandasDF" Description: "A table as a Pandas DataFrame"
--     * Slot: id Description: 
--     * Slot: table_url Description: An URL linking to the table
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: df_id Description: A Pandas DataFrame object
-- # Class: "TableAsDict" Description: "A table inlined in a metrics dataset"
--     * Slot: id Description: 
--     * Slot: table_url Description: An URL linking to the table
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
-- # Class: "Column" Description: "A column"
--     * Slot: name Description: The name of the column
--     * Slot: description Description: The description of the column
--     * Slot: source_uri Description: The URI of the source of the column
--     * Slot: TableAsDict_id Description: Autocreated FK slot
-- # Class: "FieldIlluminationDataset" Description: "A field illumination dataset"
--     * Slot: id Description: 
--     * Slot: microscope Description: The microscope that was used to acquire the dataset
--     * Slot: sample Description: The sample that was imaged
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
-- # Class: "FieldIlluminationInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: corner_fraction Description: Input parameter: the proportion of the image to be considered as corner or center
--     * Slot: sigma Description: Input parameter: the sigma for the smoothing gaussian filter to be applied prior to analysis
--     * Slot: intensity_map_size Description: Input parameter: the size of the output intensity map in pixels
--     * Slot: field_illumination_image_image_url Description: Input parameter: homogeneity image provided as a numpy array in the order TZYXC. While the analysis accepts multiple channels, the T and Z dimensions are expected to be 1.
-- # Class: "FieldIlluminationOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: key_values_id Description: Key-Value pairs containing the Key measurements for the field illumination analysis
--     * Slot: intensity_profiles_id Description: Intensity profiles for the field illumination analysis in the different directions
--     * Slot: intensity_map_image_url Description: Intensity map of the field illumination
--     * Slot: roi_profiles_label Description: line ROIs used to compute the intensity profiles
--     * Slot: roi_corners_label Description: Rectangular ROIs used to compute the corner intensities
-- # Class: "FieldIlluminationKeyValues" Description: ""
--     * Slot: id Description: 
-- # Class: "PSFBeadsDataset" Description: "A PSF beads dataset"
--     * Slot: id Description: 
--     * Slot: microscope Description: The microscope that was used to acquire the dataset
--     * Slot: sample Description: The sample that was imaged
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
-- # Class: "PSFBeadsInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: min_lateral_distance_factor Description: Minimal distance that has to separate laterally the beads represented as the  number of times the FWHM of the beads.
--     * Slot: sigma_z Description: Gaussian smoothing sigma to be applied to the image in the Z axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: sigma_y Description: Gaussian smoothing sigma to be applied to the image in teh Y axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: sigma_x Description: Gaussian smoothing sigma to be applied to the image in the X axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: snr_threshold Description: Signal to noise ratio threshold to be used for bead detection.
--     * Slot: fitting_rss_threshold Description: Threshold for the residual sum of squares of the fit to be considered good.
--     * Slot: intensity_robust_z_score_threshold Description: Threshold for the robust z-score of the intensity of the bead to be considered good.
-- # Class: "PSFBeadsOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: key_values_id Description: The key measurements of the PSF beads analysis.
--     * Slot: bead_properties_id Description: Properties associated with the analysis of the beads. This properties include: dataset_id image_id roi_id channel_nr fit_parameters z_fit_rss y_fit_rss x_fit_rss considered_bad_z_fit considered_bad_y_fit considered_bad_x_fit resolution_fwhm_z_pixels resolution_fwhm_y_pixels resolution_fwhm_x_pixels resolution_fwhm_z_microns resolution_fwhm_y_microns resolution_fwhm_x_microns resolution_lateral_asymmetry_ratio
--     * Slot: bead_z_profiles_id Description: The intensity profiles along the z axis of the analyzed beads as well as the fits.
--     * Slot: bead_y_profiles_id Description: The intensity profiles along the y axis of the analyzed beads as well as the fits.
--     * Slot: bead_x_profiles_id Description: The intensity profiles along the x axis of the analyzed beads as well as the fits.
-- # Class: "PSFBeadsKeyMeasurements" Description: ""
--     * Slot: id Description: 
-- # Class: "ArgolightBDataset" Description: "An Argolight sample pattern B dataset. This pattern consists of an array of circles"
--     * Slot: id Description: 
--     * Slot: microscope Description: The microscope that was used to acquire the dataset
--     * Slot: sample Description: The sample that was imaged
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
-- # Class: "ArgolightBInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: spots_distance Description: Input parameter: distance between argolight spots
--     * Slot: sigma_z Description: Smoothing factor for objects detection in the Z axis
--     * Slot: sigma_y Description: Smoothing factor for objects detection in the Y axis
--     * Slot: sigma_x Description: Smoothing factor for objects detection in the X axis
--     * Slot: remove_center_cross Description: Input parameter: remove the center cross found in some Argolight patterns
--     * Slot: argolight_b_image_image_url Description: Input parameter: image of the argolight b pattern provided as a 5D numpy array in the order TZYXC
-- # Class: "ArgolightBOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: spots_labels_image Description: Labels image of the argolight segmented spots provided as a 5D numpy array in the order TZYXC. Image intensities correspond to ROI labels
--     * Slot: intensity_key_values_id Description: Key Intensity Measurements on Argolight spots
--     * Slot: distance_key_values_id Description: Key Distance Measurements on Argolight spots
--     * Slot: spots_properties_id Description: Table of properties of the argolight spots
--     * Slot: spots_distances_id Description: Table of distances between argolight spots
-- # Class: "ArgolightBIntensityKeyValues" Description: ""
--     * Slot: id Description: 
-- # Class: "ArgolightBDistanceKeyValues" Description: ""
--     * Slot: id Description: 
-- # Class: "ArgolightEDataset" Description: "An Argolight sample pattern E dataset.It contains resolution data on the axis indicated:- axis 1 = Y resolution = lines along X axis- axis 2 = X resolution = lines along Y axis"
--     * Slot: id Description: 
--     * Slot: microscope Description: The microscope that was used to acquire the dataset
--     * Slot: sample Description: The sample that was imaged
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: name Description: The name of an entity
--     * Slot: description Description: A description of an entity
--     * Slot: input_id Description: An input element for the analysis
--     * Slot: output_id Description: An output element from the analysis
-- # Class: "ArgolightEInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: orientation_axis Description: Axis along which resolution is being measured. 1=Y, 2=X
--     * Slot: measured_band Description: Fraction of the image across which intensity profiles are measured
--     * Slot: prominence_threshold Description: Peak prominence used as a threshold to distinguish two peaks.  Defaults to the value defined by the Rayleigh criteria
--     * Slot: argolight_e_image_image_url Description: Image of the argolight e pattern provided as a 5D numpy array in the order TZYXC
-- # Class: "ArgolightEOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: key_measurements_id Description: Key Measurements on Argolight E images
--     * Slot: intensity_profiles_id Description: Intensity profiles of the argolight lines provided as tables. One table per channel
-- # Class: "ArgolightEKeyValues" Description: ""
--     * Slot: id Description: 
-- # Class: "Protocol_authors" Description: ""
--     * Slot: Protocol_url Description: Autocreated FK slot
--     * Slot: authors_orcid Description: The authors of the protocol
-- # Class: "MetricsDataset_experimenter" Description: ""
--     * Slot: MetricsDataset_id Description: Autocreated FK slot
--     * Slot: experimenter_orcid Description: The experimenter that performed the imaging experiment
-- # Class: "Image_source_image_url" Description: ""
--     * Slot: Image_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "ImageAsNumpy_source_image_url" Description: ""
--     * Slot: ImageAsNumpy_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "ImageInline_source_image_url" Description: ""
--     * Slot: ImageInline_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "ImageMask_data" Description: ""
--     * Slot: ImageMask_image_url Description: Autocreated FK slot
--     * Slot: data Description: 
-- # Class: "ImageMask_source_image_url" Description: ""
--     * Slot: ImageMask_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "Image2D_data" Description: ""
--     * Slot: Image2D_image_url Description: Autocreated FK slot
--     * Slot: data Description: 
-- # Class: "Image2D_source_image_url" Description: ""
--     * Slot: Image2D_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "Image5D_data" Description: ""
--     * Slot: Image5D_image_url Description: Autocreated FK slot
--     * Slot: data Description: 
-- # Class: "Image5D_source_image_url" Description: ""
--     * Slot: Image5D_image_url Description: Autocreated FK slot
--     * Slot: source_image_url Description: A list of URLs linking to the images that were used as a source
-- # Class: "ChannelSeries_values" Description: ""
--     * Slot: ChannelSeries_id Description: Autocreated FK slot
--     * Slot: values_id Description: 
-- # Class: "TimeSeries_values" Description: ""
--     * Slot: TimeSeries_id Description: Autocreated FK slot
--     * Slot: values Description: 
-- # Class: "Roi_image" Description: ""
--     * Slot: Roi_label Description: Autocreated FK slot
--     * Slot: image_image_url Description: The image or images to which the ROI is applied
-- # Class: "RoiMassCenters_image" Description: ""
--     * Slot: RoiMassCenters_label Description: Autocreated FK slot
--     * Slot: image_image_url Description: The image or images to which the ROI is applied
-- # Class: "RoiGeometricCenters_image" Description: ""
--     * Slot: RoiGeometricCenters_label Description: Autocreated FK slot
--     * Slot: image_image_url Description: The image or images to which the ROI is applied
-- # Class: "RoiProfiles_image" Description: ""
--     * Slot: RoiProfiles_label Description: Autocreated FK slot
--     * Slot: image_image_url Description: The image or images to which the ROI is applied
-- # Class: "RoiMeasurements_image" Description: ""
--     * Slot: RoiMeasurements_label Description: Autocreated FK slot
--     * Slot: image_image_url Description: The image or images to which the ROI is applied
-- # Class: "Column_values" Description: ""
--     * Slot: Column_name Description: Autocreated FK slot
--     * Slot: values Description: The values of the column
-- # Class: "FieldIlluminationDataset_experimenter" Description: ""
--     * Slot: FieldIlluminationDataset_id Description: Autocreated FK slot
--     * Slot: experimenter_orcid Description: The experimenter that performed the imaging experiment
-- # Class: "FieldIlluminationKeyValues_channel_nr" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "FieldIlluminationKeyValues_center_region_intensity_fraction" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_region_intensity_fraction Description: The fraction of the upper intensity range occupied by the center of illumination region. That is, a value of 0.1 means that the center of illumination occupies the top 10% of the intensity range. microscope-metrics tries to adapt the threshold of this intensity so that the area occupied is not too large.
-- # Class: "FieldIlluminationKeyValues_center_region_area_fraction" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_region_area_fraction Description: The fraction of the area occupied by the center of illumination region. If the centre upper intensity fraction is 0.1, that means that the center of illumination occupies 10% of the area of the image.
-- # Class: "FieldIlluminationKeyValues_centroid_weighted_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_weighted_y Description: The y coordinate of the center of mass of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_weighted_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_weighted_y_relative Description: The relative y position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyValues_centroid_weighted_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_weighted_x Description: The x coordinate of the center of mass of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_weighted_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_weighted_x_relative Description: The relative x position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_centroid_weighted_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_weighted_distance_relative Description: The relative distance of the weighted centroid to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyValues_centroid_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_y Description: The y coordinate of the geometric center of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_y_relative Description: The relative y position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyValues_centroid_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_x Description: The x coordinate of the geometric center of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_x_relative Description: The relative x position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_centroid_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_distance_relative Description: The relative distance of the centroid to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyValues_centroid_fitted_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_fitted_y Description: The y coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_fitted_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_fitted_y_relative Description: The relative y position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyValues_centroid_fitted_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_fitted_x Description: The x coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_centroid_fitted_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_fitted_x_relative Description: The relative x position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_centroid_fitted_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: centroid_fitted_distance_relative Description: The relative distance of the fitted center of illumination to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyValues_max_intensity" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity Description: The maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_max_intensity_pos_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_y Description: The y coordinate of the maximum intensity of the center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_max_intensity_pos_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_y_relative Description: The relative y position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyValues_max_intensity_pos_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_x Description: The x coordinate of the maximum intensity of the center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_max_intensity_pos_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_x_relative Description: The relative x position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_max_intensity_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: max_intensity_distance_relative Description: The relative distance of the maximum intensity to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyValues_top_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_left_intensity_mean Description: The mean intensity of the top-left corner of the image
-- # Class: "FieldIlluminationKeyValues_top_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_left_intensity_ratio Description: The mean intensity of the top-left corner of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_top_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_center_intensity_mean Description: The mean intensity of the top-center of the image
-- # Class: "FieldIlluminationKeyValues_top_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_center_intensity_ratio Description: The mean intensity of the top-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_top_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_right_intensity_mean Description: The mean intensity of the top-right corner of the image
-- # Class: "FieldIlluminationKeyValues_top_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: top_right_intensity_ratio Description: The mean intensity of the top-right corner of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_middle_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_left_intensity_mean Description: The mean intensity of the middle-left of the image
-- # Class: "FieldIlluminationKeyValues_middle_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_left_intensity_ratio Description: The mean intensity of the middle-left of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_middle_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_center_intensity_mean Description: The mean intensity of the middle-center of the image
-- # Class: "FieldIlluminationKeyValues_middle_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_center_intensity_ratio Description: The mean intensity of the middle-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_middle_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_right_intensity_mean Description: The mean intensity of the middle-right of the image
-- # Class: "FieldIlluminationKeyValues_middle_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: middle_right_intensity_ratio Description: The mean intensity of the middle-right of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_bottom_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_left_intensity_mean Description: The mean intensity of the bottom-left of the image
-- # Class: "FieldIlluminationKeyValues_bottom_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_left_intensity_ratio Description: The mean intensity of the bottom-left of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_bottom_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_center_intensity_mean Description: The mean intensity of the bottom-center of the image
-- # Class: "FieldIlluminationKeyValues_bottom_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_center_intensity_ratio Description: The mean intensity of the bottom-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyValues_bottom_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_right_intensity_mean Description: The mean intensity of the bottom-right of the image
-- # Class: "FieldIlluminationKeyValues_bottom_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: bottom_right_intensity_ratio Description: The mean intensity of the bottom-right of the image  divided by the maximum intensity of the center of illumination
-- # Class: "PSFBeadsDataset_experimenter" Description: ""
--     * Slot: PSFBeadsDataset_id Description: Autocreated FK slot
--     * Slot: experimenter_orcid Description: The experimenter that performed the imaging experiment
-- # Class: "PSFBeadsKeyMeasurements_channel_nr" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_analyzed" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_analyzed Description: Number of beads analyzed. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_discarded_lateral_edge" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_discarded_lateral_edge Description: Number of beads discarded for being too close to the edge of the image. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_discarded_self_proximity" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_discarded_self_proximity Description: Number of beads discarded for being too close to another bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_considered_axial_edge" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_axial_edge Description: Number of beads considered as being too close to the top and or bottom of the image. These beads are not considered for the z axis FWHM measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_considered_intensity_outlier" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_intensity_outlier Description: Number of beads considered as being too intense and potentially represent a cluster of beads. These beads have a robust z-score over the requested threshold. Measurements on these beads are not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_z_fit" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_z_fit Description: Number of beads considered as having a bad fit quality in the z axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_y_fit" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_y_fit Description: Number of beads considered as having a bad fit quality in the y axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_x_fit" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_x_fit Description: Number of beads considered as having a bad fit quality in the x axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_z_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_mean Description: Mean residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_z_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_median Description: Median residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_z_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_std Description: Standard deviation of the residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_y_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_mean Description: Mean residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_y_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_median Description: Median residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_y_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_std Description: Standard deviation of the residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_x_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_mean Description: Mean residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_x_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_median Description: Median residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_rss_x_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_std Description: Standard deviation of the residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_z_pixels Description: Mean FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_z_pixels Description: Median FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_z_pixels Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_y_pixels Description: Mean FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_y_pixels Description: Median FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_y_pixels Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_x_pixels Description: Mean FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_x_pixels Description: Median FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_x_pixels Description: Standard deviation of the FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_z_microns Description: Mean FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_z_microns Description: Median FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_z_microns Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_y_microns Description: Mean FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_y_microns Description: Median FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_y_microns Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_x_microns Description: Mean FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_x_microns Description: Median FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_x_microns Description: Standard deviation of the FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_mean_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_lateral_asymmetry_ratio Description: Mean lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_median_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_lateral_asymmetry_ratio Description: Median lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_resolution_std_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_lateral_asymmetry_ratio Description: Standard deviation of the lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "ArgolightBDataset_experimenter" Description: ""
--     * Slot: ArgolightBDataset_id Description: Autocreated FK slot
--     * Slot: experimenter_orcid Description: The experimenter that performed the imaging experiment
-- # Class: "ArgolightBInput_lower_threshold_correction_factors" Description: ""
--     * Slot: ArgolightBInput_id Description: Autocreated FK slot
--     * Slot: lower_threshold_correction_factors Description: Input parameter: correction factor for the lower thresholds.  Must be a list with len = nr of channels or a float if all equal
-- # Class: "ArgolightBInput_upper_threshold_correction_factors" Description: ""
--     * Slot: ArgolightBInput_id Description: Autocreated FK slot
--     * Slot: upper_threshold_correction_factors Description: Input parameter: correction factor for the upper thresholds. Must be a tuple with len = nr of channels or a float if all equal
-- # Class: "ArgolightBIntensityKeyValues_channel_nr" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "ArgolightBIntensityKeyValues_nr_of_spots" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_spots Description: Number of argolight spots detected for each channel
-- # Class: "ArgolightBIntensityKeyValues_intensity_max_spot" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: intensity_max_spot Description: Integrated intensity of the most intense spot for each channel
-- # Class: "ArgolightBIntensityKeyValues_intensity_max_spot_roi" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: intensity_max_spot_roi Description: ROI number of the most intense spot for each channel
-- # Class: "ArgolightBIntensityKeyValues_intensity_min_spot" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: intensity_min_spot Description: Integrated intensity of the least intense spot for each channel
-- # Class: "ArgolightBIntensityKeyValues_intensity_min_spot_roi" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: intensity_min_spot_roi Description: ROI number of the least intense spot for each channel
-- # Class: "ArgolightBIntensityKeyValues_mean_intensity" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: mean_intensity Description: Mean of all spots integrated intensity for each channel
-- # Class: "ArgolightBIntensityKeyValues_median_intensity" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: median_intensity Description: Median of all spots integrated intensity for each channel
-- # Class: "ArgolightBIntensityKeyValues_std_mean_intensity" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: std_mean_intensity Description: Standard deviation of all spots integrated intensity for each channel
-- # Class: "ArgolightBIntensityKeyValues_mad_mean_intensity" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: mad_mean_intensity Description: Median absolute deviation of all spots integrated intensity for each channel
-- # Class: "ArgolightBIntensityKeyValues_min_max_intensity_ratio" Description: ""
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: min_max_intensity_ratio Description: Ratio between the integrated intensities between the most intense and the least intense spots for each channel
-- # Class: "ArgolightBDistanceKeyValues_channel_A" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_A Description: The first channel number to which the measurements apply
-- # Class: "ArgolightBDistanceKeyValues_channel_B" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_B Description: The second channel number to which the measurements apply
-- # Class: "ArgolightBDistanceKeyValues_mean_3d_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: mean_3d_dist Description: Mean of the 3D distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_median_3d_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: median_3d_dist Description: Median of the 3D distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_std_3d_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: std_3d_dist Description: Standard deviation of the 3D distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_mad_3d_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: mad_3d_dist Description: Median absolute deviation of the 3D distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_mean_z_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: mean_z_dist Description: Mean of the Z distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_median_z_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: median_z_dist Description: Median of the Z distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_std_z_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: std_z_dist Description: Standard deviation of the Z distances between spots for each permutation of channel A and B
-- # Class: "ArgolightBDistanceKeyValues_mad_z_dist" Description: ""
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: mad_z_dist Description: Median absolute deviation of the Z distances between spots for each permutation of channel A and B
-- # Class: "ArgolightEDataset_experimenter" Description: ""
--     * Slot: ArgolightEDataset_id Description: Autocreated FK slot
--     * Slot: experimenter_orcid Description: The experimenter that performed the imaging experiment
-- # Class: "ArgolightEKeyValues_channel_nr" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "ArgolightEKeyValues_focus_slice" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: focus_slice Description: Z position at which focus has been measured. One value per channel
-- # Class: "ArgolightEKeyValues_rayleigh_resolution_pixels" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: rayleigh_resolution_pixels Description: Rayleigh resolution measured in pixels. One value per channel
-- # Class: "ArgolightEKeyValues_rayleigh_resolution_microns" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: rayleigh_resolution_microns Description: Rayleigh resolution measured in microns. One value per channel
-- # Class: "ArgolightEKeyValues_peak_position_A" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_position_A Description: Position, in pixels, of first peak in the intensity profiles. One value per channel
-- # Class: "ArgolightEKeyValues_peak_position_B" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_position_B Description: Position, in pixels, of second peak in the intensity profiles. One value per channel
-- # Class: "ArgolightEKeyValues_peak_height_A" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_height_A Description: Height of first peak in the intensity profiles. One value per channel
-- # Class: "ArgolightEKeyValues_peak_height_B" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_height_B Description: Height of second peak in the intensity profiles. One value per channel
-- # Class: "ArgolightEKeyValues_peak_prominence_A" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_prominence_A Description: Prominence of first peak in the intensity profiles. One value per channel
-- # Class: "ArgolightEKeyValues_peak_prominence_B" Description: ""
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
--     * Slot: peak_prominence_B Description: Prominence of second peak in the intensity profiles. One value per channel

CREATE TABLE "MetaObject" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedObject" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MetricsObject" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Device" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Microscope" (
	id TEXT NOT NULL, 
	type VARCHAR(10), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	url TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Protocol" (
	version TEXT NOT NULL, 
	url TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (url)
);
CREATE TABLE "Experimenter" (
	name TEXT NOT NULL, 
	orcid TEXT NOT NULL, 
	PRIMARY KEY (orcid)
);
CREATE TABLE "MetricsInput" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MetricsOutput" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Image" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (image_url)
);
CREATE TABLE "ImageInline" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (image_url)
);
CREATE TABLE "ImageMask" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (image_url)
);
CREATE TABLE "Image2D" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (image_url)
);
CREATE TABLE "ChannelSeries" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Channel" (
	id INTEGER NOT NULL, 
	excitation_wavelength_nm FLOAT, 
	emission_wavelength_nm FLOAT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TimeSeries" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Color" (
	id INTEGER NOT NULL, 
	r INTEGER NOT NULL, 
	g INTEGER NOT NULL, 
	b INTEGER NOT NULL, 
	alpha INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "RoiGeometricCenters" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);
CREATE TABLE "RoiProfiles" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);
CREATE TABLE "RoiMeasurements" (
	label TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (label)
);
CREATE TABLE "KeyValues" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tag" (
	id INTEGER NOT NULL, 
	text TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Table" (
	id INTEGER NOT NULL, 
	table_url TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TableAsDict" (
	id INTEGER NOT NULL, 
	table_url TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "FieldIlluminationKeyValues" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PSFBeadsInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT, 
	min_lateral_distance_factor FLOAT NOT NULL, 
	sigma_z FLOAT NOT NULL, 
	sigma_y FLOAT NOT NULL, 
	sigma_x FLOAT NOT NULL, 
	snr_threshold FLOAT NOT NULL, 
	fitting_rss_threshold FLOAT NOT NULL, 
	intensity_robust_z_score_threshold FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightEKeyValues" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	type TEXT NOT NULL, 
	protocol TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (type), 
	FOREIGN KEY(protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "Image5D" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	time_series_id INTEGER, 
	channel_series_id INTEGER, 
	PRIMARY KEY (image_url), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id)
);
CREATE TABLE "Line" (
	x1 FLOAT NOT NULL, 
	y1 FLOAT NOT NULL, 
	x2 FLOAT NOT NULL, 
	y2 FLOAT NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	"RoiProfiles_label" TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("RoiProfiles_label") REFERENCES "RoiProfiles" (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Rectangle" (
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	w FLOAT NOT NULL, 
	h FLOAT NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	"RoiMeasurements_label" TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("RoiMeasurements_label") REFERENCES "RoiMeasurements" (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Ellipse" (
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	x_rad FLOAT NOT NULL, 
	y_rad FLOAT NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Polygon" (
	is_open BOOLEAN NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Mask" (
	y INTEGER NOT NULL, 
	x INTEGER NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	mask_image_url TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY(mask_image_url) REFERENCES "ImageMask" (image_url), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "TableAsPandasDF" (
	id INTEGER NOT NULL, 
	table_url TEXT, 
	name TEXT, 
	description TEXT, 
	df_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(df_id) REFERENCES "MetaObject" (id)
);
CREATE TABLE "Column" (
	name TEXT NOT NULL, 
	description TEXT, 
	source_uri TEXT, 
	"TableAsDict_id" INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("TableAsDict_id") REFERENCES "TableAsDict" (id)
);
CREATE TABLE "PSFBeadsOutput" (
	id INTEGER NOT NULL, 
	key_values_id INTEGER, 
	bead_properties_id INTEGER, 
	bead_z_profiles_id INTEGER, 
	bead_y_profiles_id INTEGER, 
	bead_x_profiles_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_values_id) REFERENCES "PSFBeadsKeyMeasurements" (id), 
	FOREIGN KEY(bead_properties_id) REFERENCES "TableAsDict" (id), 
	FOREIGN KEY(bead_z_profiles_id) REFERENCES "TableAsDict" (id), 
	FOREIGN KEY(bead_y_profiles_id) REFERENCES "TableAsDict" (id), 
	FOREIGN KEY(bead_x_profiles_id) REFERENCES "TableAsDict" (id)
);
CREATE TABLE "ArgolightEOutput" (
	id INTEGER NOT NULL, 
	key_measurements_id INTEGER, 
	intensity_profiles_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_measurements_id) REFERENCES "ArgolightEKeyValues" (id), 
	FOREIGN KEY(intensity_profiles_id) REFERENCES "TableAsDict" (id)
);
CREATE TABLE "Protocol_authors" (
	"Protocol_url" TEXT, 
	authors_orcid TEXT, 
	PRIMARY KEY ("Protocol_url", authors_orcid), 
	FOREIGN KEY("Protocol_url") REFERENCES "Protocol" (url), 
	FOREIGN KEY(authors_orcid) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "Image_source_image_url" (
	"Image_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("Image_image_url", source_image_url), 
	FOREIGN KEY("Image_image_url") REFERENCES "Image" (image_url)
);
CREATE TABLE "ImageInline_source_image_url" (
	"ImageInline_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("ImageInline_image_url", source_image_url), 
	FOREIGN KEY("ImageInline_image_url") REFERENCES "ImageInline" (image_url)
);
CREATE TABLE "ImageMask_data" (
	"ImageMask_image_url" TEXT, 
	data BOOLEAN NOT NULL, 
	PRIMARY KEY ("ImageMask_image_url", data), 
	FOREIGN KEY("ImageMask_image_url") REFERENCES "ImageMask" (image_url)
);
CREATE TABLE "ImageMask_source_image_url" (
	"ImageMask_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("ImageMask_image_url", source_image_url), 
	FOREIGN KEY("ImageMask_image_url") REFERENCES "ImageMask" (image_url)
);
CREATE TABLE "Image2D_data" (
	"Image2D_image_url" TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY ("Image2D_image_url", data), 
	FOREIGN KEY("Image2D_image_url") REFERENCES "Image2D" (image_url)
);
CREATE TABLE "Image2D_source_image_url" (
	"Image2D_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("Image2D_image_url", source_image_url), 
	FOREIGN KEY("Image2D_image_url") REFERENCES "Image2D" (image_url)
);
CREATE TABLE "ChannelSeries_values" (
	"ChannelSeries_id" INTEGER, 
	values_id INTEGER NOT NULL, 
	PRIMARY KEY ("ChannelSeries_id", values_id), 
	FOREIGN KEY("ChannelSeries_id") REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(values_id) REFERENCES "Channel" (id)
);
CREATE TABLE "TimeSeries_values" (
	"TimeSeries_id" INTEGER, 
	"values" FLOAT NOT NULL, 
	PRIMARY KEY ("TimeSeries_id", "values"), 
	FOREIGN KEY("TimeSeries_id") REFERENCES "TimeSeries" (id)
);
CREATE TABLE "RoiGeometricCenters_image" (
	"RoiGeometricCenters_label" TEXT, 
	image_image_url TEXT, 
	PRIMARY KEY ("RoiGeometricCenters_label", image_image_url), 
	FOREIGN KEY("RoiGeometricCenters_label") REFERENCES "RoiGeometricCenters" (label), 
	FOREIGN KEY(image_image_url) REFERENCES "Image" (image_url)
);
CREATE TABLE "RoiProfiles_image" (
	"RoiProfiles_label" TEXT, 
	image_image_url TEXT, 
	PRIMARY KEY ("RoiProfiles_label", image_image_url), 
	FOREIGN KEY("RoiProfiles_label") REFERENCES "RoiProfiles" (label), 
	FOREIGN KEY(image_image_url) REFERENCES "Image" (image_url)
);
CREATE TABLE "RoiMeasurements_image" (
	"RoiMeasurements_label" TEXT, 
	image_image_url TEXT, 
	PRIMARY KEY ("RoiMeasurements_label", image_image_url), 
	FOREIGN KEY("RoiMeasurements_label") REFERENCES "RoiMeasurements" (label), 
	FOREIGN KEY(image_image_url) REFERENCES "Image" (image_url)
);
CREATE TABLE "FieldIlluminationKeyValues_channel_nr" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", channel_nr), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_region_intensity_fraction" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_region_intensity_fraction FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_region_intensity_fraction), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_region_area_fraction" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_region_area_fraction FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_region_area_fraction), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_weighted_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_weighted_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_weighted_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_weighted_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_weighted_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_weighted_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_weighted_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_weighted_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_weighted_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_weighted_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_weighted_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_weighted_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_weighted_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_weighted_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_weighted_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_fitted_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_fitted_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_fitted_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_fitted_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_fitted_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_fitted_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_fitted_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_fitted_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_fitted_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_fitted_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_fitted_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_fitted_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_centroid_fitted_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	centroid_fitted_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", centroid_fitted_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity_pos_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity_pos_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity_pos_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity_pos_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity_pos_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity_pos_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity_pos_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity_pos_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity_pos_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_max_intensity_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	max_intensity_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", max_intensity_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_left_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_left_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_center_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_center_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_right_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_top_right_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	top_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", top_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_left_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_left_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_center_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_center_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_right_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_middle_right_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	middle_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", middle_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_left_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_left_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_center_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_center_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_right_intensity_mean" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_bottom_right_intensity_ratio" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	bottom_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", bottom_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_channel_nr" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", channel_nr), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_analyzed" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_analyzed INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_analyzed), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_discarded_lateral_edge" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_discarded_lateral_edge INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_discarded_lateral_edge), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_discarded_self_proximity" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_discarded_self_proximity INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_discarded_self_proximity), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_considered_axial_edge" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_considered_axial_edge INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_considered_axial_edge), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_considered_intensity_outlier" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_considered_intensity_outlier INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_considered_intensity_outlier), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_z_fit" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_considered_bad_z_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_considered_bad_z_fit), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_y_fit" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_considered_bad_y_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_considered_bad_y_fit), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_nr_of_beads_considered_bad_x_fit" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	nr_of_beads_considered_bad_x_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", nr_of_beads_considered_bad_x_fit), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_z_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_z_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_z_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_z_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_z_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_z_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_z_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_z_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_z_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_y_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_y_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_y_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_y_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_y_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_y_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_y_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_y_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_y_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_x_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_x_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_x_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_x_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_x_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_x_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_rss_x_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_rss_x_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_rss_x_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_z_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_z_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_z_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_y_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_y_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_y_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_x_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_x_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_x_pixels" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_z_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_z_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_z_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_y_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_y_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_y_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_x_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_x_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_x_microns" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_mean_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_mean_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_mean_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_median_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_median_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_median_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_resolution_std_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	resolution_std_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", resolution_std_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_channel_nr" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", channel_nr), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_nr_of_spots" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	nr_of_spots INTEGER, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", nr_of_spots), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_intensity_max_spot" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	intensity_max_spot FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", intensity_max_spot), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_intensity_max_spot_roi" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	intensity_max_spot_roi INTEGER, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", intensity_max_spot_roi), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_intensity_min_spot" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	intensity_min_spot FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", intensity_min_spot), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_intensity_min_spot_roi" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	intensity_min_spot_roi INTEGER, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", intensity_min_spot_roi), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_mean_intensity" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	mean_intensity FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", mean_intensity), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_median_intensity" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	median_intensity FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", median_intensity), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_std_mean_intensity" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	std_mean_intensity FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", std_mean_intensity), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_mad_mean_intensity" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	mad_mean_intensity FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", mad_mean_intensity), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues_min_max_intensity_ratio" (
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	min_max_intensity_ratio FLOAT, 
	PRIMARY KEY ("ArgolightBIntensityKeyValues_id", min_max_intensity_ratio), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_channel_A" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	"channel_A" INTEGER, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", "channel_A"), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_channel_B" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	"channel_B" INTEGER, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", "channel_B"), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_mean_3d_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	mean_3d_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", mean_3d_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_median_3d_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	median_3d_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", median_3d_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_std_3d_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	std_3d_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", std_3d_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_mad_3d_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	mad_3d_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", mad_3d_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_mean_z_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	mean_z_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", mean_z_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_median_z_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	median_z_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", median_z_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_std_z_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	std_z_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", std_z_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues_mad_z_dist" (
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	mad_z_dist FLOAT, 
	PRIMARY KEY ("ArgolightBDistanceKeyValues_id", mad_z_dist), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_channel_nr" (
	"ArgolightEKeyValues_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("ArgolightEKeyValues_id", channel_nr), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_focus_slice" (
	"ArgolightEKeyValues_id" INTEGER, 
	focus_slice INTEGER, 
	PRIMARY KEY ("ArgolightEKeyValues_id", focus_slice), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_rayleigh_resolution_pixels" (
	"ArgolightEKeyValues_id" INTEGER, 
	rayleigh_resolution_pixels FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", rayleigh_resolution_pixels), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_rayleigh_resolution_microns" (
	"ArgolightEKeyValues_id" INTEGER, 
	rayleigh_resolution_microns FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", rayleigh_resolution_microns), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_position_A" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_position_A" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_position_A"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_position_B" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_position_B" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_position_B"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_height_A" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_height_A" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_height_A"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_height_B" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_height_B" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_height_B"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_prominence_A" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_prominence_A" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_prominence_A"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "ArgolightEKeyValues_peak_prominence_B" (
	"ArgolightEKeyValues_id" INTEGER, 
	"peak_prominence_B" FLOAT, 
	PRIMARY KEY ("ArgolightEKeyValues_id", "peak_prominence_B"), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "MetricsDataset" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type), 
	FOREIGN KEY(input_id) REFERENCES "MetricsInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "ImageAsNumpy" (
	image_url TEXT NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	"PSFBeadsInput_id" INTEGER, 
	"PSFBeadsOutput_id" INTEGER, 
	data_id INTEGER, 
	PRIMARY KEY (image_url), 
	FOREIGN KEY("PSFBeadsInput_id") REFERENCES "PSFBeadsInput" (id), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY(data_id) REFERENCES "MetaObject" (id)
);
CREATE TABLE "Roi" (
	label TEXT NOT NULL, 
	description TEXT, 
	"ArgolightEOutput_id" INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "Vertex" (
	id INTEGER NOT NULL, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	"Polygon_label" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Polygon_label") REFERENCES "Polygon" (label)
);
CREATE TABLE "FieldIlluminationOutput" (
	id INTEGER NOT NULL, 
	key_values_id INTEGER, 
	intensity_profiles_id INTEGER, 
	intensity_map_image_url TEXT, 
	roi_profiles_label TEXT, 
	roi_corners_label TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_values_id) REFERENCES "FieldIlluminationKeyValues" (id), 
	FOREIGN KEY(intensity_profiles_id) REFERENCES "TableAsDict" (id), 
	FOREIGN KEY(intensity_map_image_url) REFERENCES "Image5D" (image_url), 
	FOREIGN KEY(roi_profiles_label) REFERENCES "RoiProfiles" (label), 
	FOREIGN KEY(roi_corners_label) REFERENCES "RoiMeasurements" (label)
);
CREATE TABLE "PSFBeadsDataset" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER NOT NULL, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type), 
	FOREIGN KEY(input_id) REFERENCES "PSFBeadsInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "Image5D_data" (
	"Image5D_image_url" TEXT, 
	data FLOAT NOT NULL, 
	PRIMARY KEY ("Image5D_image_url", data), 
	FOREIGN KEY("Image5D_image_url") REFERENCES "Image5D" (image_url)
);
CREATE TABLE "Image5D_source_image_url" (
	"Image5D_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("Image5D_image_url", source_image_url), 
	FOREIGN KEY("Image5D_image_url") REFERENCES "Image5D" (image_url)
);
CREATE TABLE "Column_values" (
	"Column_name" TEXT, 
	"values" TEXT, 
	PRIMARY KEY ("Column_name", "values"), 
	FOREIGN KEY("Column_name") REFERENCES "Column" (name)
);
CREATE TABLE "Shape" (
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	"Roi_label" TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("Roi_label") REFERENCES "Roi" (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "FieldIlluminationInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	intensity_map_size INTEGER NOT NULL, 
	field_illumination_image_image_url TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(field_illumination_image_image_url) REFERENCES "ImageAsNumpy" (image_url)
);
CREATE TABLE "ArgolightBInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	spots_distance FLOAT NOT NULL, 
	sigma_z FLOAT NOT NULL, 
	sigma_y FLOAT NOT NULL, 
	sigma_x FLOAT NOT NULL, 
	remove_center_cross BOOLEAN, 
	argolight_b_image_image_url TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(argolight_b_image_image_url) REFERENCES "ImageAsNumpy" (image_url)
);
CREATE TABLE "ArgolightBOutput" (
	id INTEGER NOT NULL, 
	spots_labels_image TEXT, 
	intensity_key_values_id INTEGER, 
	distance_key_values_id INTEGER, 
	spots_properties_id INTEGER, 
	spots_distances_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(spots_labels_image) REFERENCES "ImageAsNumpy" (image_url), 
	FOREIGN KEY(intensity_key_values_id) REFERENCES "ArgolightBIntensityKeyValues" (id), 
	FOREIGN KEY(distance_key_values_id) REFERENCES "ArgolightBDistanceKeyValues" (id), 
	FOREIGN KEY(spots_properties_id) REFERENCES "TableAsDict" (id), 
	FOREIGN KEY(spots_distances_id) REFERENCES "TableAsDict" (id)
);
CREATE TABLE "ArgolightEInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	orientation_axis INTEGER NOT NULL, 
	measured_band FLOAT NOT NULL, 
	prominence_threshold FLOAT NOT NULL, 
	argolight_e_image_image_url TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(argolight_e_image_image_url) REFERENCES "ImageAsNumpy" (image_url)
);
CREATE TABLE "MetricsDataset_experimenter" (
	"MetricsDataset_id" INTEGER, 
	experimenter_orcid TEXT, 
	PRIMARY KEY ("MetricsDataset_id", experimenter_orcid), 
	FOREIGN KEY("MetricsDataset_id") REFERENCES "MetricsDataset" (id), 
	FOREIGN KEY(experimenter_orcid) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "ImageAsNumpy_source_image_url" (
	"ImageAsNumpy_image_url" TEXT, 
	source_image_url TEXT, 
	PRIMARY KEY ("ImageAsNumpy_image_url", source_image_url), 
	FOREIGN KEY("ImageAsNumpy_image_url") REFERENCES "ImageAsNumpy" (image_url)
);
CREATE TABLE "Roi_image" (
	"Roi_label" TEXT, 
	image_image_url TEXT, 
	PRIMARY KEY ("Roi_label", image_image_url), 
	FOREIGN KEY("Roi_label") REFERENCES "Roi" (label), 
	FOREIGN KEY(image_image_url) REFERENCES "Image" (image_url)
);
CREATE TABLE "PSFBeadsDataset_experimenter" (
	"PSFBeadsDataset_id" INTEGER, 
	experimenter_orcid TEXT, 
	PRIMARY KEY ("PSFBeadsDataset_id", experimenter_orcid), 
	FOREIGN KEY("PSFBeadsDataset_id") REFERENCES "PSFBeadsDataset" (id), 
	FOREIGN KEY(experimenter_orcid) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "RoiMassCenters" (
	label TEXT NOT NULL, 
	description TEXT, 
	"FieldIlluminationOutput_id" INTEGER, 
	"PSFBeadsOutput_id" INTEGER, 
	"ArgolightBOutput_id" INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "FieldIlluminationDataset" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER NOT NULL, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type), 
	FOREIGN KEY(input_id) REFERENCES "FieldIlluminationInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "ArgolightBDataset" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER NOT NULL, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type), 
	FOREIGN KEY(input_id) REFERENCES "ArgolightBInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightEDataset" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	sample TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	processing_datetime DATETIME, 
	processing_log TEXT, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER NOT NULL, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (type), 
	FOREIGN KEY(input_id) REFERENCES "ArgolightEInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "ArgolightBInput_lower_threshold_correction_factors" (
	"ArgolightBInput_id" INTEGER, 
	lower_threshold_correction_factors FLOAT, 
	PRIMARY KEY ("ArgolightBInput_id", lower_threshold_correction_factors), 
	FOREIGN KEY("ArgolightBInput_id") REFERENCES "ArgolightBInput" (id)
);
CREATE TABLE "ArgolightBInput_upper_threshold_correction_factors" (
	"ArgolightBInput_id" INTEGER, 
	upper_threshold_correction_factors FLOAT, 
	PRIMARY KEY ("ArgolightBInput_id", upper_threshold_correction_factors), 
	FOREIGN KEY("ArgolightBInput_id") REFERENCES "ArgolightBInput" (id)
);
CREATE TABLE "Comment" (
	id INTEGER NOT NULL, 
	datetime DATETIME NOT NULL, 
	author TEXT, 
	comment_type VARCHAR(11), 
	text TEXT NOT NULL, 
	"Microscope_id" TEXT, 
	"MetricsDataset_id" INTEGER, 
	"FieldIlluminationDataset_id" INTEGER, 
	"PSFBeadsDataset_id" INTEGER, 
	"ArgolightBDataset_id" INTEGER, 
	"ArgolightEDataset_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id), 
	FOREIGN KEY("MetricsDataset_id") REFERENCES "MetricsDataset" (id), 
	FOREIGN KEY("FieldIlluminationDataset_id") REFERENCES "FieldIlluminationDataset" (id), 
	FOREIGN KEY("PSFBeadsDataset_id") REFERENCES "PSFBeadsDataset" (id), 
	FOREIGN KEY("ArgolightBDataset_id") REFERENCES "ArgolightBDataset" (id), 
	FOREIGN KEY("ArgolightEDataset_id") REFERENCES "ArgolightEDataset" (id)
);
CREATE TABLE "Point" (
	y FLOAT NOT NULL, 
	x FLOAT NOT NULL, 
	label TEXT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	"RoiMassCenters_label" TEXT, 
	"RoiGeometricCenters_label" TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (label), 
	FOREIGN KEY("RoiMassCenters_label") REFERENCES "RoiMassCenters" (label), 
	FOREIGN KEY("RoiGeometricCenters_label") REFERENCES "RoiGeometricCenters" (label), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "RoiMassCenters_image" (
	"RoiMassCenters_label" TEXT, 
	image_image_url TEXT, 
	PRIMARY KEY ("RoiMassCenters_label", image_image_url), 
	FOREIGN KEY("RoiMassCenters_label") REFERENCES "RoiMassCenters" (label), 
	FOREIGN KEY(image_image_url) REFERENCES "Image" (image_url)
);
CREATE TABLE "FieldIlluminationDataset_experimenter" (
	"FieldIlluminationDataset_id" INTEGER, 
	experimenter_orcid TEXT, 
	PRIMARY KEY ("FieldIlluminationDataset_id", experimenter_orcid), 
	FOREIGN KEY("FieldIlluminationDataset_id") REFERENCES "FieldIlluminationDataset" (id), 
	FOREIGN KEY(experimenter_orcid) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "ArgolightBDataset_experimenter" (
	"ArgolightBDataset_id" INTEGER, 
	experimenter_orcid TEXT, 
	PRIMARY KEY ("ArgolightBDataset_id", experimenter_orcid), 
	FOREIGN KEY("ArgolightBDataset_id") REFERENCES "ArgolightBDataset" (id), 
	FOREIGN KEY(experimenter_orcid) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "ArgolightEDataset_experimenter" (
	"ArgolightEDataset_id" INTEGER, 
	experimenter_orcid TEXT, 
	PRIMARY KEY ("ArgolightEDataset_id", experimenter_orcid), 
	FOREIGN KEY("ArgolightEDataset_id") REFERENCES "ArgolightEDataset" (id), 
	FOREIGN KEY(experimenter_orcid) REFERENCES "Experimenter" (orcid)
);