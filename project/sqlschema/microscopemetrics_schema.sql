-- # Class: "MetaObject" Description: ""
--     * Slot: id Description: 
-- # Abstract Class: "NamedObject" Description: "An object with a name and a description"
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
--     * Slot: MetricsObject_id Description: Autocreated FK slot
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: Experimenter_orcid Description: Autocreated FK slot
--     * Slot: Comment_id Description: Autocreated FK slot
--     * Slot: MetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: HarmonizedMetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: MetricsDataset_id Description: Autocreated FK slot
--     * Slot: Image_id Description: Autocreated FK slot
--     * Slot: ImageMask_id Description: Autocreated FK slot
--     * Slot: OrthogonalImage_id Description: Autocreated FK slot
--     * Slot: Channel_id Description: Autocreated FK slot
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: KeyMeasurements_id Description: Autocreated FK slot
--     * Slot: Table_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationDataset_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: PSFBeadsDataset_id Description: Autocreated FK slot
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
-- # Abstract Class: "MetricsObject" Description: "A base object for all microscope-metrics objects."
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "MicroscopeCollection" Description: "A collection of microscopes"
--     * Slot: id Description: 
-- # Class: "Microscope" Description: "A microscope"
--     * Slot: id Description: 
--     * Slot: microscope_type Description: The type of the microscope
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: model Description: The model of a device
--     * Slot: serial_number Description: The serial number of a device
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "Sample" Description: "A sample is a standard physical object that is imaged by a microscope"
--     * Slot: id Description: 
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Protocol" Description: "Set of instructions for preparing a sample or acquiring data"
--     * Slot: version Description: The version of the protocol
--     * Slot: url Description: The URL where the protocol can be found
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "Experimenter" Description: "The person that performed the experiment or developed the protocol"
--     * Slot: orcid Description: The ORCID of the experimenter
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "Comment" Description: "A comment"
--     * Slot: id Description: 
--     * Slot: datetime Description: The datetime to which the comment is referring
--     * Slot: author Description: The author of the comment
--     * Slot: comment_type Description: The type of the comment
--     * Slot: text Description: The text of the comment
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "MetricsDatasetCollection" Description: "A collection of microscope-metrics datasets"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "HarmonizedMetricsDatasetCollection" Description: "A collection of harmonized microscope-metrics datasets. All of the datasets  in the collection share the same analysis and processing parameters."
--     * Slot: id Description: 
--     * Slot: dataset_class Description: The class of the datasets in the collection
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "MetricsDataset" Description: "A base object on which microscope-metrics runs the analysis"
--     * Slot: id Description: 
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: MetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: HarmonizedMetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "MetricsInputData" Description: "An abstract class for analysis input data"
--     * Slot: id Description: 
-- # Abstract Class: "MetricsInputParameters" Description: "An abstract class for analysis inputs parameters"
--     * Slot: id Description: 
-- # Abstract Class: "MetricsOutput" Description: "An abstract class for analysis outputs"
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: key_measurements_id Description: Key measurements is a table summarizing the most important  measurements as a function of, for example, channels
--     * Slot: comment_id Description: A human readable comment
-- # Class: "Image" Description: "A microscope-metrics image"
--     * Slot: id Description: 
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of an image in the x dimension
--     * Slot: shape_y Description: The shape of an image in the y dimension
--     * Slot: shape_z Description: The shape of an image in the z dimension
--     * Slot: shape_c Description: The shape of an image in the c dimension
--     * Slot: shape_t Description: The shape of an image in the t dimension
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: FieldIlluminationInputData_id Description: Autocreated FK slot
--     * Slot: PSFBeadsInputData_id Description: Autocreated FK slot
--     * Slot: time_series_id Description: A series representing time for time-lapse images.
--     * Slot: channel_series_id Description: A series representing channels for multi-channel images.
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "ImageMask" Description: "A mask image. Either a binary image or a label image"
--     * Slot: id Description: 
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of an image in the x dimension
--     * Slot: shape_y Description: The shape of an image in the y dimension
--     * Slot: shape_z Description: The shape of an image in the z dimension
--     * Slot: shape_c Description: The shape of an image in the c dimension
--     * Slot: shape_t Description: The shape of an image in the t dimension
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: time_series_id Description: A series representing time for time-lapse images.
--     * Slot: channel_series_id Description: A series representing channels for multi-channel images.
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "OrthogonalImage" Description: "An image that is orthogonal to the main image"
--     * Slot: id Description: 
--     * Slot: axis Description: The axis of the orthogonal image
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: voxel_size_x_micron Description: The physical size in the voxel in the x dimension in microns
--     * Slot: voxel_size_y_micron Description: The physical size in the voxel in the y dimension in microns
--     * Slot: voxel_size_z_micron Description: The physical size in the voxel in the z dimension in microns
--     * Slot: shape_x Description: The shape of an image in the x dimension
--     * Slot: shape_y Description: The shape of an image in the y dimension
--     * Slot: shape_z Description: The shape of an image in the z dimension
--     * Slot: shape_c Description: The shape of an image in the c dimension
--     * Slot: shape_t Description: The shape of an image in the t dimension
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: source_roi_id Description: The source ROI of the orthogonal image. The ROI has to contain a single point shape.
--     * Slot: time_series_id Description: A series representing time for time-lapse images.
--     * Slot: channel_series_id Description: A series representing channels for multi-channel images.
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "ChannelSeries" Description: "A series representing channels"
--     * Slot: id Description: 
-- # Class: "Channel" Description: "A image channel"
--     * Slot: id Description: 
--     * Slot: excitation_wavelength_nm Description: The excitation wavelength in nm
--     * Slot: emission_wavelength_nm Description: The emission wavelength in nm
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "TimeSeries" Description: "A series whose values represent time"
--     * Slot: id Description: 
-- # Class: "Column" Description: "Attributes of a column"
--     * Slot: id Description: 
--     * Slot: data_type Description: The data type of the column
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Table_id Description: Autocreated FK slot
--     * Slot: source_reference_id Description: The source object of the column
-- # Class: "Roi" Description: "A ROI (Region Of Interest). Collection of shapes and an image to which they are applied"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "Shape" Description: "A shape"
--     * Slot: id Description: 
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Point" Description: "A point as defined by x and y coordinates"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Line" Description: "A line as defined by x1, y1, x2, y2 coordinates"
--     * Slot: id Description: 
--     * Slot: x1 Description: The x coordinate of the first point of the line
--     * Slot: y1 Description: The y coordinate of the first point of the line
--     * Slot: x2 Description: The x coordinate of the second point of the line
--     * Slot: y2 Description: The y coordinate of the second point of the line
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Rectangle" Description: "A rectangle as defined by x, y coordinates and width, height"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
--     * Slot: w Description: The width
--     * Slot: h Description: The height
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Ellipse" Description: "An ellipse as defined by x, y coordinates and x and y radii"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
--     * Slot: w Description: The width
--     * Slot: h Description: The height
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Polygon" Description: "A polygon as defined by a series of vertexes and a boolean to indicate if closed or not"
--     * Slot: id Description: 
--     * Slot: is_open Description: Is the polygon open. By default, it is closed (false)
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: "Vertex" Description: "A vertex as defined by x and y coordinates"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
-- # Class: "Mask" Description: "A mask as defined by a boolean image"
--     * Slot: id Description: 
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Roi_id Description: Autocreated FK slot
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
-- # Abstract Class: "KeyMeasurements" Description: "A table of key measurements"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "Table" Description: "A microscope-metrics table"
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: "HomogeneousField" Description: "An homogeneous field."
--     * Slot: id Description: 
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "FluorescentHomogeneousThickField" Description: "An homogeneous field with a fluorescent thick sample. Similar to the Chroma slides."
--     * Slot: id Description: 
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "FluorescentHomogeneousThinField" Description: "An homogeneous field with a fluorescent thin sample. Similar to a dye thin layer."
--     * Slot: id Description: 
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "FieldIlluminationDataset" Description: "A field illumination dataset"
--     * Slot: id Description: 
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "FieldIlluminationInputData" Description: ""
--     * Slot: id Description: 
-- # Class: "FieldIlluminationInputParameters" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: corner_fraction Description: Input parameter: the proportion of the image to be considered as corner or center
--     * Slot: sigma Description: Input parameter: the sigma for the smoothing gaussian filter to be applied prior to analysis
-- # Class: "FieldIlluminationOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: key_measurements_id Description: Key-Value pairs containing the Key measurements for the field illumination analysis
--     * Slot: comment_id Description: A human readable comment
-- # Class: "FieldIlluminationKeyMeasurements" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "PSFBeads" Description: "A sample of sub-resolution sized beads used to measure the PSF of a microscope."
--     * Slot: id Description: 
--     * Slot: bead_diameter_micron Description: The diameter of the beads in the sample measured in microns.
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: "PSFBeadsDataset" Description: "A PSF beads dataset"
--     * Slot: id Description: 
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "PSFBeadsInputData" Description: ""
--     * Slot: id Description: 
-- # Class: "PSFBeadsInputParameters" Description: ""
--     * Slot: id Description: 
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: min_lateral_distance_factor Description: Minimal distance that has to separate laterally the beads represented as the  number of times the FWHM of the beads.
--     * Slot: sigma_z Description: Gaussian smoothing sigma to be applied to the image in the Z axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: sigma_y Description: Gaussian smoothing sigma to be applied to the image in teh Y axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: sigma_x Description: Gaussian smoothing sigma to be applied to the image in the X axis prior to bead detection. Does not apply to resolution measurements
--     * Slot: snr_threshold Description: Signal to noise ratio threshold to be used for bead detection.
--     * Slot: fitting_r2_threshold Description: Threshold for the coefficient of determination (R^2) of the fit to be considered good.
--     * Slot: intensity_robust_z_score_threshold Description: Threshold for the robust z-score of the intensity of the bead to be considered good.
-- # Class: "PSFBeadsOutput" Description: ""
--     * Slot: id Description: 
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: key_measurements_id Description: The key measurements of the PSF beads analysis.
--     * Slot: bead_properties_id Description: Properties associated with the analysis of the beads.
--     * Slot: bead_profiles_z_id Description: The intensity profiles along the z axis of the analyzed beads as well as the fits.
--     * Slot: bead_profiles_y_id Description: The intensity profiles along the y axis of the analyzed beads as well as the fits.
--     * Slot: bead_profiles_x_id Description: The intensity profiles along the x axis of the analyzed beads as well as the fits.
--     * Slot: average_bead_id Description: The average bead image created from all the beads considered valid. The average bead is calculated after aligning the beads in all three axes. This one image contains all the channels. If the analysis does not detect at least two beads in a channel, the average bead for this channel is not calculated.
--     * Slot: comment_id Description: A human readable comment
-- # Class: "PSFBeadsKeyMeasurements" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: "MicroscopeCollection_microscope_collection" Description: ""
--     * Slot: MicroscopeCollection_id Description: Autocreated FK slot
--     * Slot: microscope_collection_id Description: The microscopes of the collection
-- # Class: "Microscope_comment_collection" Description: ""
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: comment_collection_id Description: A collection of comments
-- # Class: "Protocol_authors" Description: ""
--     * Slot: Protocol_url Description: Autocreated FK slot
--     * Slot: authors_orcid Description: The authors of the protocol
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
-- # Class: "ChannelSeries_channels" Description: ""
--     * Slot: ChannelSeries_id Description: Autocreated FK slot
--     * Slot: channels_id Description: The channels of the ChannelSeries
-- # Class: "TimeSeries_time_points_sec" Description: ""
--     * Slot: TimeSeries_id Description: Autocreated FK slot
--     * Slot: time_points_sec Description: The relative times at which the time series were acquired in seconds
-- # Class: "Column_values" Description: ""
--     * Slot: Column_id Description: Autocreated FK slot
--     * Slot: values Description: An optional container for the values of the column
-- # Class: "Polygon_vertexes" Description: ""
--     * Slot: Polygon_id Description: Autocreated FK slot
--     * Slot: vertexes_id Description: A list of vertexes defining the polygon
-- # Class: "FieldIlluminationOutput_roi_profiles" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_profiles_id Description: line ROIs used to compute the intensity profiles
-- # Class: "FieldIlluminationOutput_roi_corners" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_corners_id Description: Rectangular ROIs used to compute the corner intensities. The sama ROI is assigned to multiple images.
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
-- # Class: "FieldIlluminationOutput_roi_center_region" Description: ""
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_center_region_id Description: Mask ROIs marking the area of maximum illumination. One mask per channel.
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
-- # Class: "FieldIlluminationKeyMeasurements_image_name" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: image_name Description: The name of the image where the measurement was taken
-- # Class: "FieldIlluminationKeyMeasurements_image_id" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: image_id Description: The id of the image where the measurement was taken. If images are originary in OMERO this is the image_id.
-- # Class: "FieldIlluminationKeyMeasurements_channel_name" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_name Description: The channel name to which the measurements apply
-- # Class: "FieldIlluminationKeyMeasurements_channel_nr" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "FieldIlluminationKeyMeasurements_channel_id" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_id Description: The channel id to which the measurements apply
-- # Class: "FieldIlluminationKeyMeasurements_center_region_intensity_fraction" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_region_intensity_fraction Description: The fraction of the upper intensity range occupied by the center of illumination region. That is, a value of 0.1 means that the center of illumination occupies the top 10% of the intensity range. microscope-metrics tries to adapt the threshold of this intensity so that the area occupied is not too large. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_region_area_fraction" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_region_area_fraction Description: The fraction of the area occupied by the center of illumination region. If the centre upper intensity fraction is 0.1, that means that the center of illumination occupies 10% of the area of the image. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_of_mass_y" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_of_mass_y Description: The y coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_of_mass_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_of_mass_y_relative Description: The relative y position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_of_mass_x" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_of_mass_x Description: The x coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_of_mass_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_of_mass_x_relative Description: The relative x position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_of_mass_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_of_mass_distance_relative Description: The relative distance of the centers of mass to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_geometric_y" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_geometric_y Description: The y coordinate of the geometric center of the center of illumination region. In pixels. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_geometric_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_geometric_y_relative Description: The relative y position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
-- # Class: "FieldIlluminationKeyMeasurements_center_geometric_x" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_geometric_x Description: The x coordinate of the geometric center of the center of illumination region. In pixels
-- # Class: "FieldIlluminationKeyMeasurements_center_geometric_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_geometric_x_relative Description: The relative x position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyMeasurements_center_geometric_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_geometric_distance_relative Description: The relative distance of the geometric center to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyMeasurements_center_fitted_y" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_fitted_y Description: The y coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyMeasurements_center_fitted_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_fitted_y_relative Description: The relative y position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyMeasurements_center_fitted_x" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_fitted_x Description: The x coordinate of the fitted center of illumination. In pixels
-- # Class: "FieldIlluminationKeyMeasurements_center_fitted_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_fitted_x_relative Description: The relative x position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyMeasurements_center_fitted_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: center_fitted_distance_relative Description: The relative distance of the fitted center of illumination to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity Description: The maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity_pos_y" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_y Description: The y coordinate of the maximum intensity of the center of illumination. In pixels
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity_pos_y_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_y_relative Description: The relative y position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity_pos_x" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_x Description: The x coordinate of the maximum intensity of the center of illumination. In pixels
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity_pos_x_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity_pos_x_relative Description: The relative x position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
-- # Class: "FieldIlluminationKeyMeasurements_max_intensity_distance_relative" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: max_intensity_distance_relative Description: The relative distance of the maximum intensity to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
-- # Class: "FieldIlluminationKeyMeasurements_top_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_left_intensity_mean Description: The mean intensity of the top-left corner of the image
-- # Class: "FieldIlluminationKeyMeasurements_top_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_left_intensity_ratio Description: The mean intensity of the top-left corner of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_top_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_center_intensity_mean Description: The mean intensity of the top-center of the image
-- # Class: "FieldIlluminationKeyMeasurements_top_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_center_intensity_ratio Description: The mean intensity of the top-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_top_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_right_intensity_mean Description: The mean intensity of the top-right corner of the image
-- # Class: "FieldIlluminationKeyMeasurements_top_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: top_right_intensity_ratio Description: The mean intensity of the top-right corner of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_middle_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_left_intensity_mean Description: The mean intensity of the middle-left of the image
-- # Class: "FieldIlluminationKeyMeasurements_middle_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_left_intensity_ratio Description: The mean intensity of the middle-left of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_middle_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_center_intensity_mean Description: The mean intensity of the middle-center of the image
-- # Class: "FieldIlluminationKeyMeasurements_middle_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_center_intensity_ratio Description: The mean intensity of the middle-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_middle_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_right_intensity_mean Description: The mean intensity of the middle-right of the image
-- # Class: "FieldIlluminationKeyMeasurements_middle_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: middle_right_intensity_ratio Description: The mean intensity of the middle-right of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_bottom_left_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: bottom_left_intensity_mean Description: The mean intensity of the bottom-left of the image
-- # Class: "FieldIlluminationKeyMeasurements_bottom_left_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: bottom_left_intensity_ratio Description: The mean intensity of the bottom-left of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_bottom_center_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: bottom_center_intensity_mean Description: The mean intensity of the bottom-center of the image
-- # Class: "FieldIlluminationKeyMeasurements_bottom_center_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: bottom_center_intensity_ratio Description: The mean intensity of the bottom-center of the image  divided by the maximum intensity of the center of illumination
-- # Class: "FieldIlluminationKeyMeasurements_bottom_right_intensity_mean" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: bottom_right_intensity_mean Description: The mean intensity of the bottom-right of the image
-- # Class: "FieldIlluminationKeyMeasurements_bottom_right_intensity_ratio" Description: ""
--     * Slot: FieldIlluminationKeyMeasurements_id Description: Autocreated FK slot
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
-- # Class: "PSFBeadsKeyMeasurements_channel_name" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_name Description: The channel name to which the measurements apply
-- # Class: "PSFBeadsKeyMeasurements_channel_nr" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: channel_nr Description: The channel number to which the measurements apply
-- # Class: "PSFBeadsKeyMeasurements_total_bead_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: total_bead_count Description: Total number of beads detected in the image. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_valid_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_valid_count Description: Number of beads analyzed. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_self_proximity_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_self_proximity_count Description: Number of beads considered for being too close to another bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_lateral_edge_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_lateral_edge_count Description: Number of beads considered for being too close to the edge of the image. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_axial_edge_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_axial_edge_count Description: Number of beads considered as being too close to the top and or bottom of the image. These beads are not considered for the z axis FWHM measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_intensity_outlier_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_intensity_outlier_count Description: Number of beads considered as being too intense and potentially represent a cluster of beads. These beads have a robust z-score over the requested threshold. Measurements on these beads are not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_bad_fit_z_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_bad_fit_z_count Description: Number of beads considered as having a bad fit quality in the z axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_bad_fit_y_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_bad_fit_y_count Description: Number of beads considered as having a bad fit quality in the y axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_considered_bad_fit_x_count" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: considered_bad_fit_x_count Description: Number of beads considered as having a bad fit quality in the x axis. The fitting meassureemnts are  not averaged into the key measurements. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_integrated_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_integrated_mean Description: Mean integrated intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_integrated_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_integrated_median Description: Median integrated intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_integrated_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_integrated_std Description: Standard deviation of the integrated intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_max_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_max_mean Description: Mean maximum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_max_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_max_median Description: Median maximum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_max_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_max_std Description: Standard deviation of the maximum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_min_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_min_mean Description: Mean minimum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_min_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_min_median Description: Median minimum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_min_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_min_std Description: Standard deviation of the minimum intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_std_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_std_mean Description: Mean standard deviation of the intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_std_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_std_median Description: Median standard deviation of the intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_intensity_std_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: intensity_std_std Description: Standard deviation of the standard deviation of the intensity of the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_z_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_z_mean Description: Mean coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_z_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_z_median Description: Median coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_z_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_z_std Description: Standard deviation of the coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_y_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_y_mean Description: Mean coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_y_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_y_median Description: Median coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_y_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_y_std Description: Standard deviation of the coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_x_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_x_mean Description: Mean coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_x_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_x_median Description: Median coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fit_r2_x_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fit_r2_x_std Description: Standard deviation of the coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_z_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_z_mean Description: Mean FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_z_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_z_median Description: Median FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_z_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_z_std Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_y_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_y_mean Description: Mean FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_y_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_y_median Description: Median FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_y_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_y_std Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_x_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_x_mean Description: Mean FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_x_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_x_median Description: Median FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_pixel_x_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_pixel_x_std Description: Standard deviation of the FWHM for the analyzed beads in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_z_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_z_mean Description: Mean FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_z_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_z_median Description: Median FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_z_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_z_std Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_y_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_y_mean Description: Mean FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_y_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_y_median Description: Median FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_y_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_y_std Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_x_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_x_mean Description: Mean FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_x_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_x_median Description: Median FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_micron_x_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_micron_x_std Description: Standard deviation of the FWHM for the analyzed beads in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_mean" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_lateral_asymmetry_ratio_mean Description: Mean lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_median" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_lateral_asymmetry_ratio_median Description: Median lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: fwhm_lateral_asymmetry_ratio_std Description: Standard deviation of the lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fit_r2_z" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fit_r2_z Description: Average coefficient of determination (R^2) for the fits in the Z axis of the beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fit_r2_y" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fit_r2_y Description: Average coefficient of determination (R^2) for the fits in the Y axis of the beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fit_r2_x" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fit_r2_x Description: Average coefficient of determination (R^2) for the fits in the X axis of the beads. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_z" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_pixel_z Description: FWHM for the average bead in the Z axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_y" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_pixel_y Description: FWHM for the average bead in the Y axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_x" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_pixel_x Description: FWHM for the average bead in the X axis in pixels. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_z" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_micron_z Description: Average FWHM for the beads in the Z axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_y" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_micron_y Description: FWHM for the average bead in the Y axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_x" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_micron_x Description: FWHM for the average bead in the X axis in microns. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_fwhm_lateral_asymmetry_ratio" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_fwhm_lateral_asymmetry_ratio Description: Lateral FWHM asymmetry ratio for the average bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_intensity_integrated" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_intensity_integrated Description: Integrated intensity for the average bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_intensity_max" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_intensity_max Description: Maximum intensity for the average bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_intensity_min" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_intensity_min Description: Minimum intensity for the average bead. One value per channel.
-- # Class: "PSFBeadsKeyMeasurements_average_bead_intensity_std" Description: ""
--     * Slot: PSFBeadsKeyMeasurements_id Description: Autocreated FK slot
--     * Slot: average_bead_intensity_std Description: Standard deviation of the intensity for the average bead. One value per channel.

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
CREATE TABLE "DataReference" (
	id INTEGER NOT NULL, 
	data_uri TEXT, 
	omero_host TEXT, 
	omero_port INTEGER, 
	omero_object_type VARCHAR(17), 
	omero_object_id INTEGER, 
	"MetricsObject_id" INTEGER, 
	"Microscope_id" INTEGER, 
	"Experimenter_orcid" TEXT, 
	"Comment_id" INTEGER, 
	"MetricsDatasetCollection_id" INTEGER, 
	"HarmonizedMetricsDatasetCollection_id" INTEGER, 
	"MetricsDataset_id" INTEGER, 
	"Image_id" INTEGER, 
	"ImageMask_id" INTEGER, 
	"OrthogonalImage_id" INTEGER, 
	"Channel_id" INTEGER, 
	"Roi_id" INTEGER, 
	"KeyMeasurements_id" INTEGER, 
	"Table_id" INTEGER, 
	"FieldIlluminationDataset_id" INTEGER, 
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	"PSFBeadsDataset_id" INTEGER, 
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (omero_host, omero_object_type, omero_object_id), 
	FOREIGN KEY("MetricsObject_id") REFERENCES "MetricsObject" (id), 
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id), 
	FOREIGN KEY("Experimenter_orcid") REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY("Comment_id") REFERENCES "Comment" (id), 
	FOREIGN KEY("MetricsDatasetCollection_id") REFERENCES "MetricsDatasetCollection" (id), 
	FOREIGN KEY("HarmonizedMetricsDatasetCollection_id") REFERENCES "HarmonizedMetricsDatasetCollection" (id), 
	FOREIGN KEY("MetricsDataset_id") REFERENCES "MetricsDataset" (id), 
	FOREIGN KEY("Image_id") REFERENCES "Image" (id), 
	FOREIGN KEY("ImageMask_id") REFERENCES "ImageMask" (id), 
	FOREIGN KEY("OrthogonalImage_id") REFERENCES "OrthogonalImage" (id), 
	FOREIGN KEY("Channel_id") REFERENCES "Channel" (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY("KeyMeasurements_id") REFERENCES "KeyMeasurements" (id), 
	FOREIGN KEY("Table_id") REFERENCES "Table" (id), 
	FOREIGN KEY("FieldIlluminationDataset_id") REFERENCES "FieldIlluminationDataset" (id), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id), 
	FOREIGN KEY("PSFBeadsDataset_id") REFERENCES "PSFBeadsDataset" (id), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "MetricsObject" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "MicroscopeCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Microscope" (
	id INTEGER NOT NULL, 
	microscope_type VARCHAR(9), 
	manufacturer TEXT, 
	model TEXT, 
	serial_number TEXT, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "Protocol" (
	version TEXT NOT NULL, 
	url TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (url)
);
CREATE TABLE "Experimenter" (
	orcid TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (orcid), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "Comment" (
	id INTEGER NOT NULL, 
	datetime DATETIME NOT NULL, 
	author TEXT, 
	comment_type VARCHAR(11) NOT NULL, 
	text TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "MetricsDatasetCollection" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "HarmonizedMetricsDatasetCollection" (
	id INTEGER NOT NULL, 
	dataset_class TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "MetricsDataset" (
	id INTEGER NOT NULL, 
	acquisition_datetime DATETIME, 
	experimenter TEXT, 
	acquisition_protocol TEXT, 
	processed BOOLEAN NOT NULL, 
	name TEXT, 
	description TEXT, 
	"MetricsDatasetCollection_id" INTEGER, 
	"HarmonizedMetricsDatasetCollection_id" INTEGER, 
	sample_id INTEGER, 
	input_data_id INTEGER NOT NULL, 
	input_parameters_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url), 
	FOREIGN KEY("MetricsDatasetCollection_id") REFERENCES "MetricsDatasetCollection" (id), 
	FOREIGN KEY("HarmonizedMetricsDatasetCollection_id") REFERENCES "HarmonizedMetricsDatasetCollection" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id), 
	FOREIGN KEY(input_data_id) REFERENCES "MetricsInputData" (id), 
	FOREIGN KEY(input_parameters_id) REFERENCES "MetricsInputParameters" (id), 
	FOREIGN KEY(output_id) REFERENCES "MetricsOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "MetricsInputData" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MetricsInputParameters" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MetricsOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	key_measurements_id INTEGER NOT NULL, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_measurements_id) REFERENCES "KeyMeasurements" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "Image" (
	id INTEGER NOT NULL, 
	acquisition_datetime DATETIME, 
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
	"FieldIlluminationInputData_id" INTEGER, 
	"PSFBeadsInputData_id" INTEGER, 
	time_series_id INTEGER, 
	channel_series_id INTEGER, 
	array_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("FieldIlluminationInputData_id") REFERENCES "FieldIlluminationInputData" (id), 
	FOREIGN KEY("PSFBeadsInputData_id") REFERENCES "PSFBeadsInputData" (id), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "ImageMask" (
	id INTEGER NOT NULL, 
	acquisition_datetime DATETIME, 
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
	array_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "OrthogonalImage" (
	id INTEGER NOT NULL, 
	axis VARCHAR(2) NOT NULL, 
	acquisition_datetime DATETIME, 
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
	source_roi_id INTEGER NOT NULL, 
	time_series_id INTEGER, 
	channel_series_id INTEGER, 
	array_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(source_roi_id) REFERENCES "Roi" (id), 
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id), 
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
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
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "TimeSeries" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Roi" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	"PSFBeadsOutput_id" INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
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
CREATE TABLE "KeyMeasurements" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	table_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "Table" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	"FieldIlluminationOutput_id" INTEGER, 
	table_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "FieldIlluminationDataset" (
	id INTEGER NOT NULL, 
	acquisition_datetime DATETIME, 
	experimenter TEXT, 
	acquisition_protocol TEXT, 
	processed BOOLEAN NOT NULL, 
	name TEXT, 
	description TEXT, 
	sample_id INTEGER, 
	input_data_id INTEGER NOT NULL, 
	input_parameters_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url), 
	FOREIGN KEY(sample_id) REFERENCES "HomogeneousField" (id), 
	FOREIGN KEY(input_data_id) REFERENCES "FieldIlluminationInputData" (id), 
	FOREIGN KEY(input_parameters_id) REFERENCES "FieldIlluminationInputParameters" (id), 
	FOREIGN KEY(output_id) REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "FieldIlluminationInputData" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FieldIlluminationInputParameters" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT NOT NULL, 
	corner_fraction FLOAT NOT NULL, 
	sigma FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FieldIlluminationOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	key_measurements_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_measurements_id) REFERENCES "FieldIlluminationKeyMeasurements" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	table_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "PSFBeadsDataset" (
	id INTEGER NOT NULL, 
	acquisition_datetime DATETIME, 
	experimenter TEXT, 
	acquisition_protocol TEXT, 
	processed BOOLEAN NOT NULL, 
	name TEXT, 
	description TEXT, 
	sample_id INTEGER, 
	input_data_id INTEGER NOT NULL, 
	input_parameters_id INTEGER, 
	output_id INTEGER, 
	microscope_id INTEGER NOT NULL, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid), 
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url), 
	FOREIGN KEY(sample_id) REFERENCES "PSFBeads" (id), 
	FOREIGN KEY(input_data_id) REFERENCES "PSFBeadsInputData" (id), 
	FOREIGN KEY(input_parameters_id) REFERENCES "PSFBeadsInputParameters" (id), 
	FOREIGN KEY(output_id) REFERENCES "PSFBeadsOutput" (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "PSFBeadsInputData" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PSFBeadsInputParameters" (
	id INTEGER NOT NULL, 
	bit_depth INTEGER, 
	saturation_threshold FLOAT, 
	min_lateral_distance_factor FLOAT NOT NULL, 
	sigma_z FLOAT NOT NULL, 
	sigma_y FLOAT NOT NULL, 
	sigma_x FLOAT NOT NULL, 
	snr_threshold FLOAT NOT NULL, 
	fitting_r2_threshold FLOAT NOT NULL, 
	intensity_robust_z_score_threshold FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PSFBeadsOutput" (
	id INTEGER NOT NULL, 
	processing_datetime DATETIME NOT NULL, 
	processing_log TEXT, 
	validated BOOLEAN NOT NULL, 
	validation_datetime DATETIME, 
	key_measurements_id INTEGER, 
	bead_properties_id INTEGER, 
	bead_profiles_z_id INTEGER, 
	bead_profiles_y_id INTEGER, 
	bead_profiles_x_id INTEGER, 
	average_bead_id INTEGER, 
	comment_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(key_measurements_id) REFERENCES "PSFBeadsKeyMeasurements" (id), 
	FOREIGN KEY(bead_properties_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_profiles_z_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_profiles_y_id) REFERENCES "Table" (id), 
	FOREIGN KEY(bead_profiles_x_id) REFERENCES "Table" (id), 
	FOREIGN KEY(average_bead_id) REFERENCES "Image" (id), 
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	table_data_id INTEGER, 
	data_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id), 
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	preparation_protocol TEXT NOT NULL, 
	manufacturer TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "Column" (
	id INTEGER NOT NULL, 
	data_type TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"Table_id" INTEGER, 
	source_reference_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Table_id") REFERENCES "Table" (id), 
	FOREIGN KEY(source_reference_id) REFERENCES "DataReference" (id)
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
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
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
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
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
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Ellipse" (
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
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
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
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY(fill_color_id) REFERENCES "Color" (id), 
	FOREIGN KEY(stroke_color_id) REFERENCES "Color" (id)
);
CREATE TABLE "Mask" (
	id INTEGER NOT NULL, 
	x FLOAT NOT NULL, 
	y FLOAT NOT NULL, 
	z FLOAT, 
	c INTEGER, 
	t INTEGER, 
	stroke_width INTEGER, 
	name TEXT, 
	description TEXT, 
	"Roi_id" INTEGER, 
	mask_id INTEGER, 
	fill_color_id INTEGER, 
	stroke_color_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Roi_id") REFERENCES "Roi" (id), 
	FOREIGN KEY(mask_id) REFERENCES "ImageMask" (id), 
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
CREATE TABLE "HomogeneousField" (
	id INTEGER NOT NULL, 
	preparation_protocol TEXT NOT NULL, 
	manufacturer TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "FluorescentHomogeneousThickField" (
	id INTEGER NOT NULL, 
	preparation_protocol TEXT NOT NULL, 
	manufacturer TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "FluorescentHomogeneousThinField" (
	id INTEGER NOT NULL, 
	preparation_protocol TEXT NOT NULL, 
	manufacturer TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "PSFBeads" (
	id INTEGER NOT NULL, 
	bead_diameter_micron FLOAT NOT NULL, 
	preparation_protocol TEXT NOT NULL, 
	manufacturer TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);
CREATE TABLE "MicroscopeCollection_microscope_collection" (
	"MicroscopeCollection_id" INTEGER, 
	microscope_collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("MicroscopeCollection_id", microscope_collection_id), 
	FOREIGN KEY("MicroscopeCollection_id") REFERENCES "MicroscopeCollection" (id), 
	FOREIGN KEY(microscope_collection_id) REFERENCES "Microscope" (id)
);
CREATE TABLE "Microscope_comment_collection" (
	"Microscope_id" INTEGER, 
	comment_collection_id INTEGER, 
	PRIMARY KEY ("Microscope_id", comment_collection_id), 
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id), 
	FOREIGN KEY(comment_collection_id) REFERENCES "Comment" (id)
);
CREATE TABLE "Protocol_authors" (
	"Protocol_url" TEXT, 
	authors_orcid TEXT, 
	PRIMARY KEY ("Protocol_url", authors_orcid), 
	FOREIGN KEY("Protocol_url") REFERENCES "Protocol" (url), 
	FOREIGN KEY(authors_orcid) REFERENCES "Experimenter" (orcid)
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
CREATE TABLE "ChannelSeries_channels" (
	"ChannelSeries_id" INTEGER, 
	channels_id INTEGER NOT NULL, 
	PRIMARY KEY ("ChannelSeries_id", channels_id), 
	FOREIGN KEY("ChannelSeries_id") REFERENCES "ChannelSeries" (id), 
	FOREIGN KEY(channels_id) REFERENCES "Channel" (id)
);
CREATE TABLE "TimeSeries_time_points_sec" (
	"TimeSeries_id" INTEGER, 
	time_points_sec FLOAT NOT NULL, 
	PRIMARY KEY ("TimeSeries_id", time_points_sec), 
	FOREIGN KEY("TimeSeries_id") REFERENCES "TimeSeries" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_profiles" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_profiles_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_profiles_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_profiles_id) REFERENCES "Roi" (id)
);
CREATE TABLE "FieldIlluminationOutput_roi_corners" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_corners_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_corners_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_corners_id) REFERENCES "Roi" (id)
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
CREATE TABLE "FieldIlluminationOutput_roi_center_region" (
	"FieldIlluminationOutput_id" INTEGER, 
	roi_center_region_id INTEGER, 
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_center_region_id), 
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id), 
	FOREIGN KEY(roi_center_region_id) REFERENCES "Roi" (id)
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
CREATE TABLE "FieldIlluminationKeyMeasurements_image_name" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	image_name TEXT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", image_name), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_image_id" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	image_id TEXT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", image_id), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_channel_name" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	channel_name TEXT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", channel_name), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_channel_nr" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", channel_nr), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_channel_id" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	channel_id TEXT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", channel_id), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_region_intensity_fraction" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_region_intensity_fraction FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_region_intensity_fraction), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_region_area_fraction" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_region_area_fraction FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_region_area_fraction), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_of_mass_y" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_of_mass_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_of_mass_y), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_of_mass_y_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_of_mass_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_of_mass_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_of_mass_x" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_of_mass_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_of_mass_x), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_of_mass_x_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_of_mass_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_of_mass_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_of_mass_distance_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_of_mass_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_of_mass_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_geometric_y" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_geometric_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_geometric_y), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_geometric_y_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_geometric_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_geometric_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_geometric_x" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_geometric_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_geometric_x), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_geometric_x_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_geometric_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_geometric_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_geometric_distance_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_geometric_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_geometric_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_fitted_y" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_fitted_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_fitted_y), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_fitted_y_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_fitted_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_fitted_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_fitted_x" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_fitted_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_fitted_x), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_fitted_x_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_fitted_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_fitted_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_center_fitted_distance_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	center_fitted_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", center_fitted_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity_pos_y" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity_pos_y FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity_pos_y), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity_pos_y_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity_pos_y_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity_pos_y_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity_pos_x" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity_pos_x FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity_pos_x), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity_pos_x_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity_pos_x_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity_pos_x_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_max_intensity_distance_relative" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	max_intensity_distance_relative FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", max_intensity_distance_relative), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_left_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_left_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_center_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_center_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_right_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_top_right_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	top_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", top_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_left_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_left_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_center_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_center_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_right_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_middle_right_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	middle_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", middle_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_left_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_left_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_left_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_left_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_left_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_left_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_center_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_center_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_center_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_center_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_center_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_center_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_right_intensity_mean" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_right_intensity_mean FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_right_intensity_mean), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
);
CREATE TABLE "FieldIlluminationKeyMeasurements_bottom_right_intensity_ratio" (
	"FieldIlluminationKeyMeasurements_id" INTEGER, 
	bottom_right_intensity_ratio FLOAT, 
	PRIMARY KEY ("FieldIlluminationKeyMeasurements_id", bottom_right_intensity_ratio), 
	FOREIGN KEY("FieldIlluminationKeyMeasurements_id") REFERENCES "FieldIlluminationKeyMeasurements" (id)
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
CREATE TABLE "PSFBeadsKeyMeasurements_channel_name" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	channel_name TEXT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", channel_name), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_channel_nr" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	channel_nr INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", channel_nr), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_total_bead_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	total_bead_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", total_bead_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_valid_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_valid_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_valid_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_self_proximity_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_self_proximity_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_self_proximity_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_lateral_edge_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_lateral_edge_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_lateral_edge_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_axial_edge_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_axial_edge_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_axial_edge_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_intensity_outlier_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_intensity_outlier_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_intensity_outlier_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_bad_fit_z_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_bad_fit_z_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_bad_fit_z_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_bad_fit_y_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_bad_fit_y_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_bad_fit_y_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_considered_bad_fit_x_count" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	considered_bad_fit_x_count INTEGER, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", considered_bad_fit_x_count), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_integrated_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_integrated_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_integrated_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_integrated_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_integrated_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_integrated_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_integrated_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_integrated_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_integrated_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_max_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_max_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_max_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_max_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_max_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_max_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_max_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_max_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_max_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_min_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_min_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_min_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_min_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_min_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_min_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_min_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_min_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_min_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_std_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_std_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_std_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_std_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_std_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_std_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_intensity_std_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	intensity_std_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", intensity_std_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_z_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_z_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_z_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_z_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_z_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_z_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_z_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_z_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_z_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_y_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_y_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_y_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_y_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_y_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_y_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_y_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_y_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_y_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_x_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_x_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_x_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_x_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_x_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_x_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fit_r2_x_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fit_r2_x_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fit_r2_x_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_z_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_z_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_z_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_z_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_z_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_z_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_z_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_z_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_z_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_y_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_y_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_y_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_y_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_y_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_y_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_y_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_y_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_y_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_x_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_x_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_x_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_x_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_x_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_x_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_pixel_x_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_pixel_x_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_pixel_x_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_z_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_z_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_z_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_z_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_z_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_z_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_z_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_z_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_z_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_y_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_y_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_y_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_y_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_y_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_y_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_y_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_y_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_y_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_x_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_x_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_x_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_x_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_x_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_x_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_micron_x_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_micron_x_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_micron_x_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_mean" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_lateral_asymmetry_ratio_mean FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_lateral_asymmetry_ratio_mean), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_median" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_lateral_asymmetry_ratio_median FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_lateral_asymmetry_ratio_median), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_fwhm_lateral_asymmetry_ratio_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	fwhm_lateral_asymmetry_ratio_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", fwhm_lateral_asymmetry_ratio_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fit_r2_z" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fit_r2_z FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fit_r2_z), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fit_r2_y" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fit_r2_y FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fit_r2_y), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fit_r2_x" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fit_r2_x FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fit_r2_x), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_z" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_pixel_z FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_pixel_z), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_y" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_pixel_y FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_pixel_y), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_pixel_x" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_pixel_x FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_pixel_x), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_z" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_micron_z FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_micron_z), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_y" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_micron_y FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_micron_y), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_micron_x" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_micron_x FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_micron_x), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_fwhm_lateral_asymmetry_ratio" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_fwhm_lateral_asymmetry_ratio FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_fwhm_lateral_asymmetry_ratio), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_intensity_integrated" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_intensity_integrated FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_intensity_integrated), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_intensity_max" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_intensity_max FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_intensity_max), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_intensity_min" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_intensity_min FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_intensity_min), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "PSFBeadsKeyMeasurements_average_bead_intensity_std" (
	"PSFBeadsKeyMeasurements_id" INTEGER, 
	average_bead_intensity_std FLOAT, 
	PRIMARY KEY ("PSFBeadsKeyMeasurements_id", average_bead_intensity_std), 
	FOREIGN KEY("PSFBeadsKeyMeasurements_id") REFERENCES "PSFBeadsKeyMeasurements" (id)
);
CREATE TABLE "Column_values" (
	"Column_id" INTEGER, 
	"values" TEXT, 
	PRIMARY KEY ("Column_id", "values"), 
	FOREIGN KEY("Column_id") REFERENCES "Column" (id)
);
CREATE TABLE "Polygon_vertexes" (
	"Polygon_id" INTEGER, 
	vertexes_id INTEGER NOT NULL, 
	PRIMARY KEY ("Polygon_id", vertexes_id), 
	FOREIGN KEY("Polygon_id") REFERENCES "Polygon" (id), 
	FOREIGN KEY(vertexes_id) REFERENCES "Vertex" (id)
);