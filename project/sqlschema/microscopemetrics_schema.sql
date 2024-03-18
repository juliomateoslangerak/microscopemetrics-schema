-- # Class: "MetaObject" Description: ""
--     * Slot: id Description: 
-- # Class: "NamedObject" Description: "An object with a name and a description"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "DataReference" Description: "A reference to a data resource"
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: DataReference_id Description: Autocreated FK slot
--     * Slot: MetricsObject_id Description: Autocreated FK slot
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: MetricsDataset_id Description: Autocreated FK slot
--     * Slot: Image_id Description: Autocreated FK slot
--     * Slot: ImageMask_id Description: Autocreated FK slot
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: KeyValues_id Description: Autocreated FK slot
--     * Slot: Tag_id Description: Autocreated FK slot
--     * Slot: Table_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationDataset_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: PSFBeadsDataset_id Description: Autocreated FK slot
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: ArgolightBDataset_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: ArgolightBIntensityKeyValues_id Description: Autocreated FK slot
--     * Slot: ArgolightBDistanceKeyValues_id Description: Autocreated FK slot
--     * Slot: ArgolightEDataset_id Description: Autocreated FK slot
--     * Slot: ArgolightEKeyValues_id Description: Autocreated FK slot
-- # Class: "MetricsObject" Description: "A base object for all microscope-metrics objects."
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "MicroscopeCollection" Description: "A collection of microscopes"
--     * Slot: id Description: 
-- # Class: "Microscope" Description: "A microscope"
--     * Slot: id Description: 
--     * Slot: type Description: The type of the microscope
--     * Slot: manufacturer Description: The manufacturer of the microscope
--     * Slot: model Description: The model of the microscope
--     * Slot: serial_number Description: The serial number of the microscope
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Sample" Description: "A sample is a standard physical object that is imaged by a microscope"
--     * Slot: id Description: 
--     * Slot: type Description: The type of the sample
--     * Slot: protocol Description: The protocol used to prepare the sample
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Protocol" Description: "Set of instructions for preparing and imaging a sample"
--     * Slot: version Description: The version of the protocol
--     * Slot: url Description: The URL where the protocol can be found
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Experimenter" Description: "The person that performed the experiment or developed the protocol"
--     * Slot: name Description: The name of the experimenter
--     * Slot: orcid Description: The ORCID of the experimenter
-- # Class: "Comment" Description: "A comment"
--     * Slot: id Description: 
--     * Slot: datetime Description: The datetime to which the comment is referring
--     * Slot: author Description: The author of the comment
--     * Slot: comment_type Description: The type of the comment
--     * Slot: text Description: The text of the comment
-- # Class: "MetricsDatasetCollection" Description: "A collection of microscope-metrics datasets"
--     * Slot: id Description: 
-- # Class: "HarmonizedMetricsDatasetCollection" Description: "A collection of harmonized microscope-metrics datasets. All of the datasets  in the collection share the same analysis and processing parameters."
--     * Slot: id Description: 
--     * Slot: dataset_class Description: The class of the datasets in the collection
-- # Class: "MetricsDataset" Description: "A base object on which microscope-metrics runs the analysis"
--     * Slot: id Description: 
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: sample_id Description: The sample that was imaged
--     * Slot: input_id Description: The input of the analysis
--     * Slot: output_id Description: The output of the analysis
-- # Class: "MetricsInput" Description: "An abstract class for analysis inputs"
--     * Slot: id Description: 
-- # Class: "MetricsOutput" Description: "An abstract class for analysis outputs"
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: comment_id Description: A human readable comment about the dataset
-- # Class: "Image" Description: "A microscope-metrics image"
--     * Slot: id Description: 
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: FieldIlluminationInput_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: PSFBeadsInput_id Description: Autocreated FK slot
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: time_series_id Description: 
--     * Slot: channel_series_id Description: 
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
-- # Class: "ImageMask" Description: "A mask image. Either a binary image or a label image"
--     * Slot: id Description: 
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of the image in the x dimension
--     * Slot: shape_y Description: The shape of the image in the y dimension
--     * Slot: shape_z Description: The shape of the image in the z dimension
--     * Slot: shape_c Description: The shape of the image in the c dimension
--     * Slot: shape_t Description: The shape of the image in the t dimension
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: time_series_id Description: 
--     * Slot: channel_series_id Description: 
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
-- # Class: "ChannelSeries" Description: "A series whose values represent channel"
--     * Slot: id Description: 
-- # Class: "Channel" Description: "A image channel"
--     * Slot: id Description: 
--     * Slot: excitation_wavelength_nm Description: The excitation wavelength in nm
--     * Slot: emission_wavelength_nm Description: The emission wavelength in nm
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "TimeSeries" Description: "A series whose values represent time"
--     * Slot: id Description: 
-- # Class: "ColumnSeries" Description: "A series of columns"
--     * Slot: id Description: 
-- # Class: "Column" Description: "Attributes of a column"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: source_object_id Description: The source object of the column
-- # Class: "Roi" Description: "A ROI (Region Of Interest). Collection of shapes and an image to which they are applied"
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
-- # Class: "Shape" Description: "A shape"
--     * Slot: id Description: 
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Point" Description: "A point as defined by x and y coordinates"
--     * Slot: id Description: 
--     * Slot: y Description: The y coordinate of the point
--     * Slot: x Description: The x coordinate of the point
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Line" Description: "A line as defined by x1, y1, x2, y2 coordinates"
--     * Slot: id Description: 
--     * Slot: x1 Description: The x coordinate of the first point of the line
--     * Slot: y1 Description: The y coordinate of the first point of the line
--     * Slot: x2 Description: The x coordinate of the second point of the line
--     * Slot: y2 Description: The y coordinate of the second point of the line
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Rectangle" Description: "A rectangle as defined by x, y coordinates and width, height"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate of the top left corner of the rectangle
--     * Slot: y Description: The y coordinate of the top left corner of the rectangle
--     * Slot: w Description: The width of the rectangle
--     * Slot: h Description: The height of the rectangle
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Ellipse" Description: "An ellipse as defined by x, y coordinates and x and y radii"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate of the bounding box of the ellipse
--     * Slot: y Description: The y coordinate of the bounding box of the ellipse
--     * Slot: x_rad Description: The x radius of the ellipse
--     * Slot: y_rad Description: The y radius of the ellipse
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Polygon" Description: "A polygon as defined by a series of vertexes and a boolean to indicate if closed or not"
--     * Slot: id Description: 
--     * Slot: is_open Description: Is the polygon open. By default, it is closed (false)
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Vertex" Description: "A vertex as defined by x and y coordinates"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate of the vertex
--     * Slot: y Description: The y coordinate of the vertex
-- # Class: "Mask" Description: "A mask as defined by a boolean image"
--     * Slot: id Description: 
--     * Slot: y Description: The y coordinate of the top left corner of the mask
--     * Slot: x Description: The x coordinate of the top left corner of the mask
--     * Slot: z Description: The z coordinate of the shape
--     * Slot: c Description: The c coordinate of the shape
--     * Slot: t Description: The t coordinate of the shape
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: mask_id Description: The mask image
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Color" Description: "A color as defined by RGB values and an optional alpha value"
--     * Slot: id Description: 
--     * Slot: r Description: The red value of the color
--     * Slot: g Description: The green value of the color
--     * Slot: b Description: The blue value of the color
--     * Slot: alpha Description: The alpha value of the color (optional)
-- # Class: "CentersOfMass" Description: "The center of mass of detected objects. Intended to be used with ROIs."
--     * Slot: id Description: 
-- # Class: "CentersGeometric" Description: "The geometric center of detected objects. Intended to be used with ROIs."
--     * Slot: id Description: 
-- # Class: "CentersFitted" Description: "The fitted center of detected objects. Intended to be used with ROIs."
--     * Slot: id Description: 
-- # Class: "CentersMaxIntensity" Description: "The position of maximum intensity of detected objects. Intended to be used with ROIs."
--     * Slot: id Description: 
-- # Class: "ProfilesIntensity" Description: "Profiles computed on the image. Intended to be used with ROIs."
--     * Slot: id Description: 
--     * Slot: intensity_profiles_table_id Description: Linked table of profiles
-- # Class: "RoiMeasurements" Description: "Measurements computed on the ROIs of an image. Intended to be used with ROIs."
--     * Slot: id Description: 
--     * Slot: measurements_table_id Description: Linked table of measurements
-- # Class: "KeyValues" Description: "A collection of key-value pairs"
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Tag" Description: "A tag"
--     * Slot: id Description: 
--     * Slot: text Description: The text of the tag
--     * Slot: description Description: The description of the tag
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
-- # Class: "Table" Description: "A microscope-metrics table"
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: column_series_id Description: 
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
-- # Class: "FieldIlluminationDataset" Description: "A field illumination dataset"
--     * Slot: id Description: 
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: sample_id Description: The sample that was imaged
-- # Class: "FieldIlluminationInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: corner_fraction Description: Input parameter: the proportion of the image to be considered as corner or center
--     * Slot: sigma Description: Input parameter: the sigma for the smoothing gaussian filter to be applied prior to analysis
--     * Slot: intensity_map_size Description: Input parameter: the size of the output intensity map in pixels
-- # Class: "FieldIlluminationOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: key_values_id Description: Key-Value pairs containing the Key measurements for the field illumination analysis
--     * Slot: roi_corners_id Description: Rectangular ROIs used to compute the corner intensities. The sama ROI is assigned to multiple images.
--     * Slot: comment_id Description: A human readable comment about the dataset
-- # Class: "FieldIlluminationKeyValues" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "PSFBeadsDataset" Description: "A PSF beads dataset"
--     * Slot: id Description: 
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: sample_id Description: The sample that was imaged
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
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: key_values_id Description: The key measurements of the PSF beads analysis.
--     * Slot: bead_properties_id Description: Properties associated with the analysis of the beads.
--     * Slot: bead_z_profiles_id Description: The intensity profiles along the z axis of the analyzed beads as well as the fits.
--     * Slot: bead_y_profiles_id Description: The intensity profiles along the y axis of the analyzed beads as well as the fits.
--     * Slot: bead_x_profiles_id Description: The intensity profiles along the x axis of the analyzed beads as well as the fits.
--     * Slot: comment_id Description: A human readable comment about the dataset
-- # Class: "PSFBeadsKeyValues" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "ArgolightBDataset" Description: "An Argolight sample pattern B dataset. This pattern consists of an array of circles"
--     * Slot: id Description: 
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: sample_id Description: The sample that was imaged
-- # Class: "ArgolightBInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: spots_distance Description: Input parameter: distance between argolight spots
--     * Slot: sigma_z Description: Smoothing factor for objects detection in the Z axis
--     * Slot: sigma_y Description: Smoothing factor for objects detection in the Y axis
--     * Slot: sigma_x Description: Smoothing factor for objects detection in the X axis
--     * Slot: remove_center_cross Description: Input parameter: remove the center cross found in some Argolight patterns
--     * Slot: argolight_b_image_id Description: Input parameter: image of the argolight b pattern in the order TZYXC
-- # Class: "ArgolightBOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: spots_labels_image_id Description: Labels image of the argolight segmented spots provided in the order TZYXC. Image intensities correspond to ROI labels
--     * Slot: intensity_key_values_id Description: Key Intensity Measurements on Argolight spots
--     * Slot: distance_key_values_id Description: Key Distance Measurements on Argolight spots
--     * Slot: spots_properties_id Description: Table of properties of the argolight spots
--     * Slot: spots_distances_id Description: Table of distances between argolight spots
--     * Slot: comment_id Description: A human readable comment about the dataset
-- # Class: "ArgolightBCentersOfMass" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "ArgolightBIntensityKeyValues" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "ArgolightBDistanceKeyValues" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "ArgolightEDataset" Description: "An Argolight sample pattern E dataset.It contains resolution data on the axis indicated:- axis 1 = Y resolution = lines along X axis- axis 2 = X resolution = lines along Y axis"
--     * Slot: id Description: 
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: input_id Description: 
--     * Slot: output_id Description: 
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: sample_id Description: The sample that was imaged
-- # Class: "ArgolightEInput" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: orientation_axis Description: Axis along which resolution is being measured. 1=Y, 2=X
--     * Slot: measured_band Description: Fraction of the image across which intensity profiles are measured
--     * Slot: prominence_threshold Description: Peak prominence used as a threshold to distinguish two peaks.  Defaults to the value defined by the Rayleigh criteria
--     * Slot: argolight_e_image_id Description: Image of the argolight e pattern provided in the order TZYXC
-- # Class: "ArgolightEOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: key_measurements_id Description: Key Measurements on Argolight E images
--     * Slot: intensity_profiles_id Description: Intensity profiles of the argolight lines provided as tables. One table per channel
--     * Slot: comment_id Description: A human readable comment about the dataset
-- # Class: "ArgolightEKeyValues" Description: ""
--     * Slot: id Description: 
--     * Slot: data_uri Description: The URI of the object data
--     * Slot: omero_host Description: The host of the OMERO server
--     * Slot: omero_port Description: The port of the OMERO server
--     * Slot: omero_object_type Description: The type of the OMERO object
--     * Slot: omero_object_id Description: The ID of the OMERO object
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "MicroscopeCollection_microscopes" Description: ""
--     * Slot: MicroscopeCollection_id Description: Autocreated FK slot
--     * Slot: microscopes_id Description: The microscopes of the collection
-- # Class: "Microscope_comments" Description: ""
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: comments_id Description: A list of comments linked to the microscope
-- # Class: "Protocol_authors" Description: ""
--     * Slot: Protocol_url Description: Autocreated FK slot
--     * Slot: authors_orcid Description: The authors of the protocol
-- # Class: "MetricsDatasetCollection_datasets" Description: ""
--     * Slot: MetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: datasets_id Description: The datasets of the collection
-- # Class: "HarmonizedMetricsDatasetCollection_datasets" Description: ""
--     * Slot: HarmonizedMetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: datasets_id Description: The datasets of the collection
-- # Class: "MetricsOutput_processing_application" Description: ""
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: "MetricsOutput_processing_version" Description: ""
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: "MetricsOutput_processing_entity" Description: ""
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: "MetricsOutput_warnings" Description: ""
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: "MetricsOutput_errors" Description: ""
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: "ChannelSeries_values" Description: ""
--     * Slot: ChannelSeries_id Description: Autocreated FK slot
--     * Slot: values_id Description: 
-- # Class: "TimeSeries_values" Description: ""
--     * Slot: TimeSeries_id Description: Autocreated FK slot
--     * Slot: values Description: 
-- # Class: "ColumnSeries_columns" Description: ""
--     * Slot: ColumnSeries_id Description: Autocreated FK slot
--     * Slot: columns_id Description: 
-- # Class: "Roi_masks" Description: ""
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: masks_id Description: A list of masks included in the ROI
-- # Class: "Polygon_vertexes" Description: ""
--     * Slot: Polygon_id Description: Autocreated FK slot
--     * Slot: vertexes_id Description: A list of vertexes defining the polygon
-- # Class: "FieldIlluminationOutput_roi_profiles" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_profiles_id Description: line ROIs used to compute the intensity profiles
-- # Class: "FieldIlluminationOutput_roi_centers_of_mass" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_of_mass_id Description: Point ROIs marking the center of mass of the area of maximum illumination. When the image is very flat, the 99 percentile is used instead. One point per channel.
-- # Class: "FieldIlluminationOutput_roi_centers_geometric" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_geometric_id Description: Point ROIs marking the geometric center of the area of maximum illumination. One point per channel.
-- # Class: "FieldIlluminationOutput_roi_centers_fitted" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_fitted_id Description: Point ROIs marking the fitted center of the area of maximum illumination. One point per channel.
-- # Class: "FieldIlluminationOutput_roi_centers_max_intensity" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_max_intensity_id Description: Point ROIs marking the maximum intensity of the area of maximum illumination. One point per channel.
-- # Class: "FieldIlluminationOutput_processing_application" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: "FieldIlluminationOutput_processing_version" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: "FieldIlluminationOutput_processing_entity" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: "FieldIlluminationOutput_warnings" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: "FieldIlluminationOutput_errors" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: "FieldIlluminationKeyValues_channel_name" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_name Description: The channel name to which the measurements apply
-- # Class: "FieldIlluminationKeyValues_center_region_intensity_fraction" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_region_intensity_fraction Description: The fraction of the upper intensity range occupied by the center of illumination region. That is, a value of 0.1 means that the center of illumination occupies the top 10% of the intensity range. microscope-metrics tries to adapt the threshold of this intensity so that the area occupied is not too large. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_region_area_fraction" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_region_area_fraction Description: The fraction of the area occupied by the center of illumination region. If the centre upper intensity fraction is 0.1, that means that the center of illumination occupies 10% of the area of the image. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_of_mass_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_of_mass_y Description: The y coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_of_mass_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_of_mass_y_relative Description: The relative y position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_of_mass_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_of_mass_x Description: The x coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_of_mass_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_of_mass_x_relative Description: The relative x position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_of_mass_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_of_mass_distance_relative Description: The relative distance of the centers of mass to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_geometric_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_geometric_y Description: The y coordinate of the geometric center of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_geometric_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_geometric_y_relative Description: The relative y position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
-- # Class: "FieldIlluminationKeyValues_center_geometric_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_geometric_x Description: The x coordinate of the geometric center of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyValues_center_geometric_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_geometric_x_relative Description: The relative x position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_center_geometric_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_geometric_distance_relative Description: The relative distance of the geometric center to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyValues_center_fitted_y" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_fitted_y Description: The y coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_center_fitted_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_fitted_y_relative Description: The relative y position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyValues_center_fitted_x" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_fitted_x Description: The x coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyValues_center_fitted_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_fitted_x_relative Description: The relative x position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyValues_center_fitted_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyValues_id Description: Autocreated FK slot
--     * Slot: center_fitted_distance_relative Description: The relative distance of the fitted center of illumination to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
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
-- # Class: "PSFBeadsOutput_processing_application" Description: ""
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: "PSFBeadsOutput_processing_version" Description: ""
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: "PSFBeadsOutput_processing_entity" Description: ""
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: "PSFBeadsOutput_warnings" Description: ""
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: "PSFBeadsOutput_errors" Description: ""
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: "PSFBeadsKeyValues_channel_nr" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "PSFBeadsKeyValues_nr_of_beads_analyzed" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_analyzed Description: Number of beads analyzed. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_discarded_lateral_edge" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_discarded_lateral_edge Description: Number of beads discarded for being too close to the edge of the image. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_discarded_self_proximity" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_discarded_self_proximity Description: Number of beads discarded for being too close to another bead. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_considered_axial_edge" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_axial_edge Description: Number of beads considered as being too close to the top and or bottom of the image. These beads are not considered for the z axis FWHM measurements. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_considered_intensity_outlier" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_intensity_outlier Description: Number of beads considered as being too intense and potentially represent a cluster of beads. These beads have a robust z-score over the requested threshold. Measurements on these beads are not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_considered_bad_z_fit" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_z_fit Description: Number of beads considered as having a bad fit quality in the z axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_considered_bad_y_fit" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_y_fit Description: Number of beads considered as having a bad fit quality in the y axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyValues_nr_of_beads_considered_bad_x_fit" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: nr_of_beads_considered_bad_x_fit Description: Number of beads considered as having a bad fit quality in the x axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_z_mean" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_mean Description: Mean residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_z_median" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_median Description: Median residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_z_std" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_z_std Description: Standard deviation of the residual sum of squares in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_y_mean" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_mean Description: Mean residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_y_median" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_median Description: Median residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_y_std" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_y_std Description: Standard deviation of the residual sum of squares in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_x_mean" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_mean Description: Mean residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_x_median" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_median Description: Median residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_fit_rss_x_std" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: fit_rss_x_std Description: Standard deviation of the residual sum of squares in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_z_pixels Description: Mean FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_z_pixels Description: Median FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_z_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_z_pixels Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_y_pixels Description: Mean FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_y_pixels Description: Median FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_y_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_y_pixels Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_x_pixels Description: Mean FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_x_pixels Description: Median FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_x_pixels" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_x_pixels Description: Standard deviation of the FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_z_microns Description: Mean FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_z_microns Description: Median FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_z_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_z_microns Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_y_microns Description: Mean FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_y_microns Description: Median FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_y_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_y_microns Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_x_microns Description: Mean FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_x_microns Description: Median FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_x_microns" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_x_microns Description: Standard deviation of the FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_mean_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_mean_fwhm_lateral_asymmetry_ratio Description: Mean lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_median_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_median_fwhm_lateral_asymmetry_ratio Description: Median lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyValues_resolution_std_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyValues_id Description: Autocreated FK slot
--     * Slot: resolution_std_fwhm_lateral_asymmetry_ratio Description: Standard deviation of the lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "ArgolightBInput_lower_threshold_correction_factors" Description: ""
--     * Slot: ArgolightBInput_id Description: Autocreated FK slot
--     * Slot: lower_threshold_correction_factors Description: Input parameter: correction factor for the lower thresholds.  Must be a list with length equal to the number of channels or a single float if all equal
-- # Class: "ArgolightBInput_upper_threshold_correction_factors" Description: ""
--     * Slot: ArgolightBInput_id Description: Autocreated FK slot
--     * Slot: upper_threshold_correction_factors Description: Input parameter: correction factor for the upper thresholds. Must be a tuple with length equal to the number of channels or a single float if all equal
-- # Class: "ArgolightBOutput_spots_centers_of_mass" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: spots_centers_of_mass_id Description: Centers of mass of the argolight spots provided as a list of ROIs. One per channel
-- # Class: "ArgolightBOutput_processing_application" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: "ArgolightBOutput_processing_version" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: "ArgolightBOutput_processing_entity" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: "ArgolightBOutput_warnings" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: "ArgolightBOutput_errors" Description: ""
--     * Slot: ArgolightBOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: "ArgolightBCentersOfMass_masks" Description: ""
--     * Slot: ArgolightBCentersOfMass_id Description: Autocreated FK slot
--     * Slot: masks_id Description: A list of masks included in the ROI
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
-- # Class: "ArgolightEOutput_peaks_rois" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: peaks_rois_id Description: ROIs of the peaks found in the argolight images. One per channel
-- # Class: "ArgolightEOutput_processing_application" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: "ArgolightEOutput_processing_version" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: "ArgolightEOutput_processing_entity" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: "ArgolightEOutput_warnings" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: "ArgolightEOutput_errors" Description: ""
--     * Slot: ArgolightEOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
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
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MicroscopeCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Microscope" (
	id INTEGER NOT NULL, 
	type VARCHAR(10), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
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
CREATE TABLE "MetricsDatasetCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "HarmonizedMetricsDatasetCollection" (
	id INTEGER NOT NULL, 
	dataset_class TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MetricsInput" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
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
CREATE TABLE "ColumnSeries" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Roi" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	"PSFBeadsOutput_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "Vertex" (
	id INTEGER NOT NULL, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
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
CREATE TABLE "CentersOfMass" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CentersGeometric" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CentersFitted" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CentersMaxIntensity" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "KeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tag" (
	id INTEGER NOT NULL, 
	text TEXT NOT NULL, 
	description TEXT, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Table" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	"FieldIlluminationOutput_id" INTEGER, 
	column_series_id INTEGER NOT NULL, 
	table_data_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(column_series_id) REFERENCES "ColumnSeries" (id), 
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id)
);
CREATE TABLE "FieldIlluminationInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	intensity_map_size INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FieldIlluminationOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	key_values_id INTEGER, 
	roi_corners_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_values_id) REFERENCES "FieldIlluminationKeyValues" (id), 
	FOREIGN KEY(roi_corners_id) REFERENCES "Roi" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "FieldIlluminationKeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
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
CREATE TABLE "PSFBeadsOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	key_values_id INTEGER, 
	bead_properties_id INTEGER, 
	bead_z_profiles_id INTEGER, 
	bead_y_profiles_id INTEGER, 
	bead_x_profiles_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_values_id) REFERENCES "PSFBeadsKeyValues" (id), 
	FOREIGN KEY(bead_properties_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_z_profiles_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_y_profiles_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_x_profiles_id) REFERENCES "Table" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "PSFBeadsKeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightBCentersOfMass" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightBIntensityKeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightBDistanceKeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ArgolightEKeyValues" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	type TEXT NOT NULL, 
	protocol TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "Comment" (
	id INTEGER NOT NULL, 
	datetime DATETIME NOT NULL, 
	author TEXT, 
	comment_type VARCHAR(11) NOT NULL, 
	text TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES "Experimenter" (orcid)
);
CREATE TABLE "Image" (
	id INTEGER NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	"FieldIlluminationInput_id" INTEGER, 
	"FieldIlluminationOutput_id" INTEGER, 
	"PSFBeadsInput_id" INTEGER, 
	"PSFBeadsOutput_id" INTEGER, 
	time_series_id INTEGER, 
	channel_series_id INTEGER, 
	array_data_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("FieldIlluminationInput_id") REFERENCES "FieldIlluminationInput" (id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY("PSFBeadsInput_id") REFERENCES "PSFBeadsInput" (id), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id)
);
CREATE TABLE "ImageMask" (
	id INTEGER NOT NULL, 
	voxel_size_x_micron FLOAT, 
	voxel_size_y_micron FLOAT, 
	voxel_size_z_micron FLOAT, 
	shape_x INTEGER NOT NULL, 
	shape_y INTEGER NOT NULL, 
	shape_z INTEGER NOT NULL, 
	shape_c INTEGER NOT NULL, 
	shape_t INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	time_series_id INTEGER, 
	channel_series_id INTEGER, 
	array_data_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id)
);
CREATE TABLE "Shape" (
	id INTEGER NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Point" (
	id INTEGER NOT NULL, 
	y FLOAT NOT NULL, 
	x FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Line" (
	id INTEGER NOT NULL, 
	x1 FLOAT NOT NULL, 
	y1 FLOAT NOT NULL, 
	x2 FLOAT NOT NULL, 
	y2 FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Rectangle" (
	id INTEGER NOT NULL, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	w FLOAT NOT NULL, 
	h FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Ellipse" (
	id INTEGER NOT NULL, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	x_rad FLOAT NOT NULL, 
	y_rad FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Polygon" (
	id INTEGER NOT NULL, 
	is_open BOOLEAN NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "ProfilesIntensity" (
	id INTEGER NOT NULL, 
	intensity_profiles_table_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(intensity_profiles_table_id) REFERENCES "Table" (id)
);
CREATE TABLE "RoiMeasurements" (
	id INTEGER NOT NULL, 
	measurements_table_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(measurements_table_id) REFERENCES "Table" (id)
);
CREATE TABLE "MicroscopeCollection_microscopes" (
	"MicroscopeCollection_id" INTEGER, 
	microscopes_id INTEGER NOT NULL, 
	PRIMARY KEY ("MicroscopeCollection_id", microscopes_id), 
	FOREIGN KEY("MicroscopeCollection_id") REFERENCES "MicroscopeCollection" (id), 
	FOREIGN KEY(microscopes_id) REFERENCES "Microscope" (id)
);
CREATE TABLE "Protocol_authors" (
	"Protocol_url" TEXT, 
	authors_orcid TEXT, 
	PRIMARY KEY ("Protocol_url", authors_orcid), 
	FOREIGN KEY("Protocol_url") REFERENCES "Protocol" (url), 
	FOREIGN KEY(authors_orcid) REFERENCES "Experimenter" (orcid)
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
CREATE TABLE "FieldIlluminationOutput_roi_profiles" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_profiles_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_profiles_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_profiles_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_centers_of_mass" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_centers_of_mass_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_of_mass_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_centers_of_mass_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_centers_geometric" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_centers_geometric_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_geometric_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_centers_geometric_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_centers_fitted" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_centers_fitted_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_fitted_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_centers_fitted_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_centers_max_intensity" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_centers_max_intensity_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_max_intensity_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_centers_max_intensity_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_processing_application" (
	"FieldIlluminationOutput_id" INTEGER, 
	processing_application TEXT NOT NULL, 
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_application), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "FieldIlluminationOutput_processing_version" (
	"FieldIlluminationOutput_id" INTEGER, 
	processing_version TEXT NOT NULL, 
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_version), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "FieldIlluminationOutput_processing_entity" (
	"FieldIlluminationOutput_id" INTEGER, 
	processing_entity TEXT, 
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_entity), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "FieldIlluminationOutput_warnings" (
	"FieldIlluminationOutput_id" INTEGER, 
	warnings TEXT, 
	PRIMARY KEY ("FieldIlluminationOutput_id", warnings), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "FieldIlluminationOutput_errors" (
	"FieldIlluminationOutput_id" INTEGER, 
	errors TEXT, 
	PRIMARY KEY ("FieldIlluminationOutput_id", errors), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_channel_name" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	channel_name TEXT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", channel_name), 
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
CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_of_mass_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_of_mass_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_of_mass_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_of_mass_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_of_mass_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_of_mass_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_of_mass_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_of_mass_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_of_mass_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_of_mass_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_of_mass_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_geometric_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_geometric_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_geometric_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_geometric_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_geometric_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_geometric_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_geometric_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_geometric_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_geometric_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_geometric_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_geometric_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_geometric_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_geometric_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_geometric_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_geometric_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_fitted_y" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_fitted_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_fitted_y), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_fitted_y_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_fitted_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_fitted_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_fitted_x" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_fitted_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_fitted_x), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_fitted_x_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_fitted_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_fitted_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id)
);
CREATE TABLE "FieldIlluminationKeyValues_center_fitted_distance_relative" (
	"FieldIlluminationKeyValues_id" INTEGER, 
	center_fitted_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyValues_id", center_fitted_distance_relative), 
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
CREATE TABLE "PSFBeadsOutput_processing_application" (
	"PSFBeadsOutput_id" INTEGER, 
	processing_application TEXT NOT NULL, 
	PRIMARY KEY ("PSFBeadsOutput_id", processing_application), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "PSFBeadsOutput_processing_version" (
	"PSFBeadsOutput_id" INTEGER, 
	processing_version TEXT NOT NULL, 
	PRIMARY KEY ("PSFBeadsOutput_id", processing_version), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "PSFBeadsOutput_processing_entity" (
	"PSFBeadsOutput_id" INTEGER, 
	processing_entity TEXT, 
	PRIMARY KEY ("PSFBeadsOutput_id", processing_entity), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "PSFBeadsOutput_warnings" (
	"PSFBeadsOutput_id" INTEGER, 
	warnings TEXT, 
	PRIMARY KEY ("PSFBeadsOutput_id", warnings), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "PSFBeadsOutput_errors" (
	"PSFBeadsOutput_id" INTEGER, 
	errors TEXT, 
	PRIMARY KEY ("PSFBeadsOutput_id", errors), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);
CREATE TABLE "PSFBeadsKeyValues_channel_nr" (
	"PSFBeadsKeyValues_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", channel_nr), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_analyzed" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_analyzed INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_analyzed), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_discarded_lateral_edge" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_discarded_lateral_edge INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_discarded_lateral_edge), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_discarded_self_proximity" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_discarded_self_proximity INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_discarded_self_proximity), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_axial_edge" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_considered_axial_edge INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_considered_axial_edge), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_intensity_outlier" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_considered_intensity_outlier INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_considered_intensity_outlier), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_z_fit" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_considered_bad_z_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_considered_bad_z_fit), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_y_fit" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_considered_bad_y_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_considered_bad_y_fit), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_nr_of_beads_considered_bad_x_fit" (
	"PSFBeadsKeyValues_id" INTEGER, 
	nr_of_beads_considered_bad_x_fit INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", nr_of_beads_considered_bad_x_fit), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_mean" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_z_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_z_mean), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_median" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_z_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_z_median), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_z_std" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_z_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_z_std), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_mean" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_y_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_y_mean), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_median" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_y_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_y_median), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_y_std" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_y_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_y_std), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_mean" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_x_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_x_mean), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_median" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_x_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_x_median), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_fit_rss_x_std" (
	"PSFBeadsKeyValues_id" INTEGER, 
	fit_rss_x_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", fit_rss_x_std), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_z_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_z_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_z_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_z_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_z_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_y_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_y_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_y_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_y_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_y_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_x_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_x_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_x_pixels" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_x_pixels FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_x_pixels), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_z_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_z_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_z_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_z_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_z_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_y_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_y_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_y_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_y_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_y_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_x_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_x_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_x_microns" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_x_microns FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_x_microns), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_mean_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_mean_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_mean_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_median_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_median_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_median_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
);
CREATE TABLE "PSFBeadsKeyValues_resolution_std_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyValues_id" INTEGER, 
	resolution_std_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyValues_id", resolution_std_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id)
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
CREATE TABLE "MetricsOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "Mask" (
	id INTEGER NOT NULL, 
	y INTEGER NOT NULL, 
	x INTEGER NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	mask_id INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(mask_id) REFERENCES "ImageMask" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "FieldIlluminationDataset" (
	id INTEGER NOT NULL, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	sample_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(input_id) REFERENCES "FieldIlluminationInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "PSFBeadsDataset" (
	id INTEGER NOT NULL, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	sample_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(input_id) REFERENCES "PSFBeadsInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
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
	argolight_b_image_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(argolight_b_image_id) REFERENCES "Image" (id)
);
CREATE TABLE "ArgolightBOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	spots_labels_image_id INTEGER, 
	intensity_key_values_id INTEGER, 
	distance_key_values_id INTEGER, 
	spots_properties_id INTEGER, 
	spots_distances_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(spots_labels_image_id) REFERENCES "ImageMask" (id), 
	FOREIGN KEY(intensity_key_values_id) REFERENCES "ArgolightBIntensityKeyValues" (id), 
	FOREIGN KEY(distance_key_values_id) REFERENCES "ArgolightBDistanceKeyValues" (id), 
	FOREIGN KEY(spots_properties_id) REFERENCES "Table" (id), 
	FOREIGN KEY(spots_distances_id) REFERENCES "Table" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "ArgolightEInput" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	orientation_axis INTEGER NOT NULL, 
	measured_band FLOAT NOT NULL, 
	prominence_threshold FLOAT NOT NULL, 
	argolight_e_image_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(argolight_e_image_id) REFERENCES "Image" (id)
);
CREATE TABLE "ArgolightEOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	key_measurements_id INTEGER, 
	intensity_profiles_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_measurements_id) REFERENCES "ArgolightEKeyValues" (id), 
	FOREIGN KEY(intensity_profiles_id) REFERENCES "Table" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "Microscope_comments" (
	"Microscope_id" INTEGER, 
	comments_id INTEGER, 
	PRIMARY KEY ("Microscope_id", comments_id), 
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id), 
	FOREIGN KEY(comments_id) REFERENCES "Comment" (id)
);
CREATE TABLE "Polygon_vertexes" (
	"Polygon_id" INTEGER, 
	vertexes_id INTEGER NOT NULL, 
	PRIMARY KEY ("Polygon_id", vertexes_id), 
	FOREIGN KEY("Polygon_id") REFERENCES "Polygon" (id), 
	FOREIGN KEY(vertexes_id) REFERENCES "Vertex" (id)
);
CREATE TABLE "MetricsDataset" (
	id INTEGER NOT NULL, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	microscope_id INTEGER NOT NULL, 
	sample_id INTEGER, 
	input_id INTEGER NOT NULL, 
	output_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id), 
	FOREIGN KEY(input_id) REFERENCES "MetricsInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "ArgolightBDataset" (
	id INTEGER NOT NULL, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	sample_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(input_id) REFERENCES "ArgolightBInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "ArgolightBOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "ArgolightEDataset" (
	id INTEGER NOT NULL, 
	experimenter TEXT, 
	acquisition_datetime DATETIME, 
	processed BOOLEAN NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	name TEXT, 
	description TEXT, 
	input_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	sample_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(input_id) REFERENCES "ArgolightEInput" (id), 
	FOREIGN KEY(output_id) REFERENCES "ArgolightEOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "MetricsOutput_processing_application" (
	"MetricsOutput_id" INTEGER, 
	processing_application TEXT NOT NULL, 
	PRIMARY KEY ("MetricsOutput_id", processing_application), 
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "MetricsOutput_processing_version" (
	"MetricsOutput_id" INTEGER, 
	processing_version TEXT NOT NULL, 
	PRIMARY KEY ("MetricsOutput_id", processing_version), 
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "MetricsOutput_processing_entity" (
	"MetricsOutput_id" INTEGER, 
	processing_entity TEXT, 
	PRIMARY KEY ("MetricsOutput_id", processing_entity), 
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "MetricsOutput_warnings" (
	"MetricsOutput_id" INTEGER, 
	warnings TEXT, 
	PRIMARY KEY ("MetricsOutput_id", warnings), 
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "MetricsOutput_errors" (
	"MetricsOutput_id" INTEGER, 
	errors TEXT, 
	PRIMARY KEY ("MetricsOutput_id", errors), 
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);
CREATE TABLE "Roi_masks" (
	"Roi_id" INTEGER, 
	masks_id INTEGER, 
	PRIMARY KEY ("Roi_id", masks_id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY(masks_id) REFERENCES "Mask" (id)
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
CREATE TABLE "ArgolightBOutput_spots_centers_of_mass" (
	"ArgolightBOutput_id" INTEGER, 
	spots_centers_of_mass_id INTEGER, 
	PRIMARY KEY ("ArgolightBOutput_id", spots_centers_of_mass_id), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id), 
	FOREIGN KEY(spots_centers_of_mass_id) REFERENCES "ArgolightBCentersOfMass" (id)
);
CREATE TABLE "ArgolightBOutput_processing_application" (
	"ArgolightBOutput_id" INTEGER, 
	processing_application TEXT NOT NULL, 
	PRIMARY KEY ("ArgolightBOutput_id", processing_application), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightBOutput_processing_version" (
	"ArgolightBOutput_id" INTEGER, 
	processing_version TEXT NOT NULL, 
	PRIMARY KEY ("ArgolightBOutput_id", processing_version), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightBOutput_processing_entity" (
	"ArgolightBOutput_id" INTEGER, 
	processing_entity TEXT, 
	PRIMARY KEY ("ArgolightBOutput_id", processing_entity), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightBOutput_warnings" (
	"ArgolightBOutput_id" INTEGER, 
	warnings TEXT, 
	PRIMARY KEY ("ArgolightBOutput_id", warnings), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightBOutput_errors" (
	"ArgolightBOutput_id" INTEGER, 
	errors TEXT, 
	PRIMARY KEY ("ArgolightBOutput_id", errors), 
	FOREIGN KEY("ArgolightBOutput_id") REFERENCES "ArgolightBOutput" (id)
);
CREATE TABLE "ArgolightBCentersOfMass_masks" (
	"ArgolightBCentersOfMass_id" INTEGER, 
	masks_id INTEGER, 
	PRIMARY KEY ("ArgolightBCentersOfMass_id", masks_id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY(masks_id) REFERENCES "Mask" (id)
);
CREATE TABLE "ArgolightEOutput_peaks_rois" (
	"ArgolightEOutput_id" INTEGER, 
	peaks_rois_id INTEGER, 
	PRIMARY KEY ("ArgolightEOutput_id", peaks_rois_id), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id), 
	FOREIGN KEY(peaks_rois_id) REFERENCES "Roi" (id)
);
CREATE TABLE "ArgolightEOutput_processing_application" (
	"ArgolightEOutput_id" INTEGER, 
	processing_application TEXT NOT NULL, 
	PRIMARY KEY ("ArgolightEOutput_id", processing_application), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "ArgolightEOutput_processing_version" (
	"ArgolightEOutput_id" INTEGER, 
	processing_version TEXT NOT NULL, 
	PRIMARY KEY ("ArgolightEOutput_id", processing_version), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "ArgolightEOutput_processing_entity" (
	"ArgolightEOutput_id" INTEGER, 
	processing_entity TEXT, 
	PRIMARY KEY ("ArgolightEOutput_id", processing_entity), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "ArgolightEOutput_warnings" (
	"ArgolightEOutput_id" INTEGER, 
	warnings TEXT, 
	PRIMARY KEY ("ArgolightEOutput_id", warnings), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "ArgolightEOutput_errors" (
	"ArgolightEOutput_id" INTEGER, 
	errors TEXT, 
	PRIMARY KEY ("ArgolightEOutput_id", errors), 
	FOREIGN KEY("ArgolightEOutput_id") REFERENCES "ArgolightEOutput" (id)
);
CREATE TABLE "DataReference" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(10), 
	omero_object_id INTEGER, 
	"DataReference_id" INTEGER, 
	"MetricsObject_id" INTEGER, 
	"Microscope_id" INTEGER, 
	"MetricsDataset_id" INTEGER, 
	"Image_id" INTEGER, 
	"ImageMask_id" INTEGER, 
	"Roi_id" INTEGER, 
	"KeyValues_id" INTEGER, 
	"Tag_id" INTEGER, 
	"Table_id" INTEGER, 
	"FieldIlluminationDataset_id" INTEGER, 
	"FieldIlluminationKeyValues_id" INTEGER, 
	"PSFBeadsDataset_id" INTEGER, 
	"PSFBeadsKeyValues_id" INTEGER, 
	"ArgolightBDataset_id" INTEGER, 
	"ArgolightBCentersOfMass_id" INTEGER, 
	"ArgolightBIntensityKeyValues_id" INTEGER, 
	"ArgolightBDistanceKeyValues_id" INTEGER, 
	"ArgolightEDataset_id" INTEGER, 
	"ArgolightEKeyValues_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (omero_host, omero_object_type, omero_object_id), 
	FOREIGN KEY("DataReference_id") REFERENCES "DataReference" (id), 
	FOREIGN KEY("MetricsObject_id") REFERENCES "MetricsObject" (id), 
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id), 
	FOREIGN KEY("MetricsDataset_id") REFERENCES "MetricsDataset" (id), 
	FOREIGN KEY("Image_id") REFERENCES "Image" (id), 
	FOREIGN KEY("ImageMask_id") REFERENCES "ImageMask" (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("KeyValues_id") REFERENCES "KeyValues" (id), 
	FOREIGN KEY("Tag_id") REFERENCES "Tag" (id), 
	FOREIGN KEY("Table_id") REFERENCES "Table" (id), 
	FOREIGN KEY("FieldIlluminationDataset_id") REFERENCES "FieldIlluminationDataset" (id), 
	FOREIGN KEY("FieldIlluminationKeyValues_id") REFERENCES "FieldIlluminationKeyValues" (id), 
	FOREIGN KEY("PSFBeadsDataset_id") REFERENCES "PSFBeadsDataset" (id), 
	FOREIGN KEY("PSFBeadsKeyValues_id") REFERENCES "PSFBeadsKeyValues" (id), 
	FOREIGN KEY("ArgolightBDataset_id") REFERENCES "ArgolightBDataset" (id), 
	FOREIGN KEY("ArgolightBCentersOfMass_id") REFERENCES "ArgolightBCentersOfMass" (id), 
	FOREIGN KEY("ArgolightBIntensityKeyValues_id") REFERENCES "ArgolightBIntensityKeyValues" (id), 
	FOREIGN KEY("ArgolightBDistanceKeyValues_id") REFERENCES "ArgolightBDistanceKeyValues" (id), 
	FOREIGN KEY("ArgolightEDataset_id") REFERENCES "ArgolightEDataset" (id), 
	FOREIGN KEY("ArgolightEKeyValues_id") REFERENCES "ArgolightEKeyValues" (id)
);
CREATE TABLE "MetricsDatasetCollection_datasets" (
	"MetricsDatasetCollection_id" INTEGER, 
	datasets_id INTEGER NOT NULL, 
	PRIMARY KEY ("MetricsDatasetCollection_id", datasets_id), 
	FOREIGN KEY("MetricsDatasetCollection_id") REFERENCES "MetricsDatasetCollection" (id), 
	FOREIGN KEY(datasets_id) REFERENCES "MetricsDataset" (id)
);
CREATE TABLE "HarmonizedMetricsDatasetCollection_datasets" (
	"HarmonizedMetricsDatasetCollection_id" INTEGER, 
	datasets_id INTEGER NOT NULL, 
	PRIMARY KEY ("HarmonizedMetricsDatasetCollection_id", datasets_id), 
	FOREIGN KEY("HarmonizedMetricsDatasetCollection_id") REFERENCES "HarmonizedMetricsDatasetCollection" (id), 
	FOREIGN KEY(datasets_id) REFERENCES "MetricsDataset" (id)
);
CREATE TABLE "Column" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_object_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(source_object_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "ColumnSeries_columns" (
	"ColumnSeries_id" INTEGER, 
	columns_id INTEGER NOT NULL, 
	PRIMARY KEY ("ColumnSeries_id", columns_id), 
	FOREIGN KEY("ColumnSeries_id") REFERENCES "ColumnSeries" (id), 
	FOREIGN KEY(columns_id) REFERENCES "Column" (id)
);