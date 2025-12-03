-- # Class: MetaObject
--     * Slot: id
-- # Abstract Class: NamedObject Description: An object with a name and a description
--     * Slot: id
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: DataReference Description: A reference to a data resource
--     * Slot: id
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
--     * Slot: Table_id Description: Autocreated FK slot
--     * Slot: FieldIlluminationDataset_id Description: Autocreated FK slot
--     * Slot: PSFBeadsDataset_id Description: Autocreated FK slot
--     * Slot: LightSourcePowerDataset_id Description: Autocreated FK slot
--     * Slot: UserExperimentDataset_id Description: Autocreated FK slot
-- # Abstract Class: MetricsObject Description: A base object for all microscope-metrics objects.
--     * Slot: id
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: MicroscopeCollection Description: A collection of microscopes
--     * Slot: id
-- # Class: Microscope Description: A microscope
--     * Slot: id
--     * Slot: microscope_type Description: The type of the microscope
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: model Description: The model of a device
--     * Slot: serial_number Description: The serial number of a device
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: Sample Description: A sample is a standard physical object that is imaged by a microscope
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: Protocol Description: Set of instructions for preparing a sample or acquiring data
--     * Slot: version Description: The version of the protocol
--     * Slot: url Description: The URL where the protocol can be found
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: Experimenter Description: The person that performed the experiment or developed the protocol
--     * Slot: orcid Description: The ORCID of the experimenter
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: Comment Description: A comment
--     * Slot: id
--     * Slot: datetime Description: The datetime to which the comment is referring
--     * Slot: author Description: The author of the comment
--     * Slot: comment_type Description: The type of the comment
--     * Slot: text Description: The text of the comment
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: MetricsDatasetCollection Description: A collection of microscope-metrics datasets
--     * Slot: id
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: HarmonizedMetricsDatasetCollection Description: A collection of harmonized microscope-metrics datasets. All of the datasets  in the collection share the same analysis and processing parameters.
--     * Slot: id
--     * Slot: dataset_class Description: The class of the datasets in the collection
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: MetricsDataset Description: A base object on which microscope-metrics runs the analysis
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: MetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: HarmonizedMetricsDatasetCollection_id Description: Autocreated FK slot
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: HasSampleMixin Description: A mixin for objects that have a sample.
--     * Slot: id
--     * Slot: sample_id Description: The physical sample that was imaged
-- # Class: HasInputParametersMixin Description: A mixin for objects that have input parameters.
--     * Slot: id
--     * Slot: input_parameters_id Description: The input parameters for the analysis
-- # Abstract Class: MetricsInputData Description: An abstract class for analysis input data
--     * Slot: id
-- # Abstract Class: MetricsInputParameters Description: An abstract class for analysis inputs parameters
--     * Slot: id
-- # Abstract Class: MetricsOutput Description: An abstract class for analysis outputs
--     * Slot: id
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: comment_id Description: A human readable comment
-- # Class: Image Description: A microscope-metrics image
--     * Slot: id
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
--     * Slot: UserExperimentInputData_id Description: Autocreated FK slot
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: time_series_id Description: A series representing time for time-lapse images.
--     * Slot: channel_series_id Description: A series representing channels for multi-channel images.
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: ImageMask Description: A mask image. Either a binary image or a label image
--     * Slot: id
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
-- # Class: OrthogonalImage Description: An image that is orthogonal to the main image
--     * Slot: id
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
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: source_roi_id Description: The source ROI of the orthogonal image. The ROI has to contain a single point shape.
--     * Slot: time_series_id Description: A series representing time for time-lapse images.
--     * Slot: channel_series_id Description: A series representing channels for multi-channel images.
--     * Slot: array_data_id Description: A non-required slot for non-serializable array data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: ChannelSeries Description: A series representing channels
--     * Slot: id
-- # Class: Channel Description: A image channel
--     * Slot: id
--     * Slot: excitation_wavelength_nm Description: The excitation wavelength in nm
--     * Slot: emission_wavelength_nm Description: The emission wavelength in nm
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: TimeSeries Description: A series whose values represent time
--     * Slot: id
-- # Class: Column Description: Attributes of a column
--     * Slot: id
--     * Slot: data_type Description: The data type of the column
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: Table_id Description: Autocreated FK slot
--     * Slot: source_reference_id Description: The source object of the column
-- # Class: Roi Description: A ROI (Region Of Interest). Collection of shapes and an image to which they are applied
--     * Slot: id
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: UserExperimentInputData_id Description: Autocreated FK slot
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: Shape Description: A shape
--     * Slot: id
--     * Slot: z Description: The z coordinate
--     * Slot: c Description: The c coordinate
--     * Slot: t Description: The t coordinate
--     * Slot: stroke_width Description: The stroke width of the shape
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: fill_color_id Description: The fill color of the shape
--     * Slot: stroke_color_id Description: The stroke color of the shape
-- # Class: Point Description: A point as defined by x and y coordinates
--     * Slot: id
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
-- # Class: Line Description: A line as defined by x1, y1, x2, y2 coordinates
--     * Slot: id
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
-- # Class: Rectangle Description: A rectangle as defined by x, y coordinates and width, height
--     * Slot: id
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
-- # Class: Ellipse Description: An ellipse as defined by x, y coordinates and x and y radii
--     * Slot: id
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
-- # Class: Polygon Description: A polygon as defined by a series of vertexes and a boolean to indicate if closed or not
--     * Slot: id
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
-- # Class: Vertex Description: A vertex as defined by x and y coordinates
--     * Slot: id
--     * Slot: x Description: The x coordinate
--     * Slot: y Description: The y coordinate
-- # Class: Mask Description: A mask as defined by a boolean image
--     * Slot: id
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
-- # Class: Color Description: A color as defined by RGB values and an optional alpha value
--     * Slot: id
--     * Slot: r Description: The red value of the color
--     * Slot: g Description: The green value of the color
--     * Slot: b Description: The blue value of the color
--     * Slot: alpha Description: The alpha value of the color (optional)
-- # Class: CentersOfMass Description: The center of mass of detected objects. Intended to be used with ROIs.
--     * Slot: id
-- # Class: CentersGeometric Description: The geometric center of detected objects. Intended to be used with ROIs.
--     * Slot: id
-- # Class: CentersFitted Description: The fitted center of detected objects. Intended to be used with ROIs.
--     * Slot: id
-- # Class: CentersMaxIntensity Description: The position of maximum intensity of detected objects. Intended to be used with ROIs.
--     * Slot: id
-- # Class: ProfilesIntensity Description: Profiles computed on the image. Intended to be used with ROIs.
--     * Slot: id
--     * Slot: intensity_profiles_table_id Description: Linked table of profiles
-- # Class: RoiMeasurements Description: Measurements computed on the ROIs of an image. Intended to be used with ROIs.
--     * Slot: id
--     * Slot: measurements_table_id Description: Linked table of measurements
-- # Abstract Class: KeyMeasurement Description: A dict-like of key measurements.
--     * Slot: id
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
-- # Abstract Class: Table Description: A microscope-metrics table
--     * Slot: id
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: table_data_id Description: A non-required slot for non-serializable table data object
--     * Slot: data_reference_id Description: A reference to the data
-- # Abstract Class: HomogeneousField Description: An homogeneous field.
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: FluorescentHomogeneousThickField Description: An homogeneous field with a fluorescent thick sample. Similar to the Chroma slides.
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: FluorescentHomogeneousThinField Description: An homogeneous field with a fluorescent thin sample. Similar to a dye thin layer.
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: FieldIlluminationDataset Description: A field illumination dataset
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: FieldIlluminationInputData
--     * Slot: id
-- # Class: FieldIlluminationInputParameters
--     * Slot: id
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: corner_fraction Description: Input parameter: the proportion of the image to be considered as corner or center
--     * Slot: sigma Description: Input parameter: the sigma for the smoothing gaussian filter to be applied prior to analysis
-- # Class: FieldIlluminationOutput
--     * Slot: id
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: comment_id Description: A human readable comment
-- # Class: FieldIlluminationKeyMeasurement
--     * Slot: id
--     * Slot: image_name Description: The name of the image where the measurement was taken
--     * Slot: image_id Description: The id of the image where the measurement was taken. If images are originary in OMERO this is the image_id.
--     * Slot: channel_name Description: The channel name to which the measurements apply
--     * Slot: channel_nr Description: The channel number to which the measurements apply
--     * Slot: channel_id Description: The channel id to which the measurements apply
--     * Slot: center_region_intensity_fraction Description: The fraction of the upper intensity range occupied by the center of illumination region. That is, a value of 0.1 means that the center of illumination occupies the top 10% of the intensity range. microscope-metrics tries to adapt the threshold of this intensity so that the area occupied is not too large. One value per channel.
--     * Slot: center_region_area_fraction Description: The fraction of the area occupied by the center of illumination region. If the centre upper intensity fraction is 0.1, that means that the center of illumination occupies 10% of the area of the image. One value per channel.
--     * Slot: center_of_mass_y Description: The y coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
--     * Slot: center_of_mass_y_relative Description: The relative y position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
--     * Slot: center_of_mass_x Description: The x coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.
--     * Slot: center_of_mass_x_relative Description: The relative x position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge. One value per channel.
--     * Slot: center_of_mass_distance_relative Description: The relative distance of the centers of mass to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image. One value per channel.
--     * Slot: center_geometric_y Description: The y coordinate of the geometric center of the center of illumination region. In pixels. One value per channel.
--     * Slot: center_geometric_y_relative Description: The relative y position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.
--     * Slot: center_geometric_x Description: The x coordinate of the geometric center of the center of illumination region. In pixels
--     * Slot: center_geometric_x_relative Description: The relative x position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
--     * Slot: center_geometric_distance_relative Description: The relative distance of the geometric center to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
--     * Slot: center_fitted_y Description: The y coordinate of the fitted center of illumination. In pixels
--     * Slot: center_fitted_y_relative Description: The relative y position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
--     * Slot: center_fitted_x Description: The x coordinate of the fitted center of illumination. In pixels
--     * Slot: center_fitted_x_relative Description: The relative x position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
--     * Slot: center_fitted_distance_relative Description: The relative distance of the fitted center of illumination to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
--     * Slot: max_intensity Description: The maximum intensity of the center of illumination
--     * Slot: max_intensity_pos_y Description: The y coordinate of the maximum intensity of the center of illumination. In pixels
--     * Slot: max_intensity_pos_y_relative Description: The relative y position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.
--     * Slot: max_intensity_pos_x Description: The x coordinate of the maximum intensity of the center of illumination. In pixels
--     * Slot: max_intensity_pos_x_relative Description: The relative x position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.
--     * Slot: max_intensity_distance_relative Description: The relative distance of the maximum intensity to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.
--     * Slot: top_left_intensity_mean Description: The mean intensity of the top-left corner of the image
--     * Slot: top_left_intensity_ratio Description: The mean intensity of the top-left corner of the image  divided by the maximum intensity of the center of illumination
--     * Slot: top_center_intensity_mean Description: The mean intensity of the top-center of the image
--     * Slot: top_center_intensity_ratio Description: The mean intensity of the top-center of the image  divided by the maximum intensity of the center of illumination
--     * Slot: top_right_intensity_mean Description: The mean intensity of the top-right corner of the image
--     * Slot: top_right_intensity_ratio Description: The mean intensity of the top-right corner of the image  divided by the maximum intensity of the center of illumination
--     * Slot: middle_left_intensity_mean Description: The mean intensity of the middle-left of the image
--     * Slot: middle_left_intensity_ratio Description: The mean intensity of the middle-left of the image  divided by the maximum intensity of the center of illumination
--     * Slot: middle_center_intensity_mean Description: The mean intensity of the middle-center of the image
--     * Slot: middle_center_intensity_ratio Description: The mean intensity of the middle-center of the image  divided by the maximum intensity of the center of illumination
--     * Slot: middle_right_intensity_mean Description: The mean intensity of the middle-right of the image
--     * Slot: middle_right_intensity_ratio Description: The mean intensity of the middle-right of the image  divided by the maximum intensity of the center of illumination
--     * Slot: bottom_left_intensity_mean Description: The mean intensity of the bottom-left of the image
--     * Slot: bottom_left_intensity_ratio Description: The mean intensity of the bottom-left of the image  divided by the maximum intensity of the center of illumination
--     * Slot: bottom_center_intensity_mean Description: The mean intensity of the bottom-center of the image
--     * Slot: bottom_center_intensity_ratio Description: The mean intensity of the bottom-center of the image  divided by the maximum intensity of the center of illumination
--     * Slot: bottom_right_intensity_mean Description: The mean intensity of the bottom-right of the image
--     * Slot: bottom_right_intensity_ratio Description: The mean intensity of the bottom-right of the image  divided by the maximum intensity of the center of illumination
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
-- # Class: PSFBeads Description: A sample of sub-resolution sized beads used to measure the PSF of a microscope.
--     * Slot: id
--     * Slot: bead_diameter_micron Description: The diameter of the beads in the sample measured in microns.
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: PSFBeadsDataset Description: A PSF beads dataset
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: PSFBeadsInputData
--     * Slot: id
-- # Class: PSFBeadsInputParameters
--     * Slot: id
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
--     * Slot: min_lateral_distance_factor Description: Minimal distance that has to separate laterally the beads represented as the  number of times the expected FWHM of the beads.
--     * Slot: sigma_min Description: Min value for the range of sigmas used in for the detection of the beads. Lower values will tend to include  noisy pixels as beads.
--     * Slot: sigma_max Description: Max value for the range of sigmas used in for the detection of the beads. Higher values will tend to detect  larger objects as beads.
--     * Slot: snr_threshold Description: Signal to noise ratio threshold to be used for bead detection.
--     * Slot: fitting_r2_threshold Description: Threshold for the coefficient of determination (R^2) of the fit to be considered good.
--     * Slot: intensity_robust_z_score_threshold Description: Threshold for the robust z-score of the intensity of the bead to be considered good.
-- # Class: PSFBeadsOutput
--     * Slot: id
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: bead_properties_id Description: Properties associated with the analysis of the beads.
--     * Slot: bead_profiles_z_id Description: The intensity profiles along the z axis of the analyzed beads as well as the fits.
--     * Slot: bead_profiles_y_id Description: The intensity profiles along the y axis of the analyzed beads as well as the fits.
--     * Slot: bead_profiles_x_id Description: The intensity profiles along the x axis of the analyzed beads as well as the fits.
--     * Slot: average_bead_id Description: The average bead image created from all the beads considered valid. The average bead is calculated after aligning the beads in all three axes. This one image contains all the channels. If the analysis does not detect at least two beads in a channel, the average bead for this channel is not calculated.
--     * Slot: comment_id Description: A human readable comment
-- # Class: PSFBeadsKeyMeasurement
--     * Slot: id
--     * Slot: channel_name Description: The channel name to which the measurements apply
--     * Slot: channel_nr Description: The channel number to which the measurements apply
--     * Slot: total_bead_count Description: Total number of beads detected in the image. One value per channel.
--     * Slot: considered_valid_count Description: Number of beads analyzed. One value per channel.
--     * Slot: considered_self_proximity_count Description: Number of beads considered for being too close to another bead. One value per channel.
--     * Slot: considered_lateral_edge_count Description: Number of beads considered for being too close to the edge of the image. One value per channel.
--     * Slot: considered_axial_edge_count Description: Number of beads considered as being too close to the top and or bottom of the image. These beads are not considered for the z axis FWHM measurements. One value per channel.
--     * Slot: considered_intensity_outlier_count Description: Number of beads considered as being too intense and potentially represent a cluster of beads. These beads have a robust z-score over the requested threshold. Measurements on these beads are not averaged into the key measurements. One value per channel.
--     * Slot: considered_bad_fit_z_count Description: Number of beads considered as having a bad fit quality in the z axis. The fitting measurements are  not averaged into the key measurements. One value per channel.
--     * Slot: considered_bad_fit_y_count Description: Number of beads considered as having a bad fit quality in the y axis. The fitting measurements are  not averaged into the key measurements. One value per channel.
--     * Slot: considered_bad_fit_x_count Description: Number of beads considered as having a bad fit quality in the x axis. The fitting measurements are  not averaged into the key measurements. One value per channel.
--     * Slot: intensity_integrated_mean Description: Mean integrated intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_integrated_median Description: Median integrated intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_integrated_std Description: Standard deviation of the integrated intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_max_mean Description: Mean maximum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_max_median Description: Median maximum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_max_std Description: Standard deviation of the maximum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_min_mean Description: Mean minimum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_min_median Description: Median minimum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_min_std Description: Standard deviation of the minimum intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_std_mean Description: Mean standard deviation of the intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_std_median Description: Median standard deviation of the intensity of the analyzed beads. One value per channel.
--     * Slot: intensity_std_std Description: Standard deviation of the standard deviation of the intensity of the analyzed beads. One value per channel.
--     * Slot: fit_r2_z_mean Description: Mean coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_z_median Description: Median coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_z_std Description: Standard deviation of the coefficient of determination (R^2) in the z axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_y_mean Description: Mean coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_y_median Description: Median coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_y_std Description: Standard deviation of the coefficient of determination (R^2) in the y axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_x_mean Description: Mean coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_x_median Description: Median coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
--     * Slot: fit_r2_x_std Description: Standard deviation of the coefficient of determination (R^2) in the x axis for the analyzed beads. One value per channel.
--     * Slot: fwhm_pixel_z_mean Description: Mean FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_z_median Description: Median FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_z_std Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_y_mean Description: Mean FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_y_median Description: Median FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_y_std Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_x_mean Description: Mean FWHM for the analyzed beads in the X axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_x_median Description: Median FWHM for the analyzed beads in the X axis in pixels. One value per channel.
--     * Slot: fwhm_pixel_x_std Description: Standard deviation of the FWHM for the analyzed beads in the X axis in pixels. One value per channel.
--     * Slot: fwhm_micron_z_mean Description: Mean FWHM for the analyzed beads in the Z axis in microns. One value per channel.
--     * Slot: fwhm_micron_z_median Description: Median FWHM for the analyzed beads in the Z axis in microns. One value per channel.
--     * Slot: fwhm_micron_z_std Description: Standard deviation of the FWHM for the analyzed beads in the Z axis in microns. One value per channel.
--     * Slot: fwhm_micron_y_mean Description: Mean FWHM for the analyzed beads in the Y axis in microns. One value per channel.
--     * Slot: fwhm_micron_y_median Description: Median FWHM for the analyzed beads in the Y axis in microns. One value per channel.
--     * Slot: fwhm_micron_y_std Description: Standard deviation of the FWHM for the analyzed beads in the Y axis in microns. One value per channel.
--     * Slot: fwhm_micron_x_mean Description: Mean FWHM for the analyzed beads in the X axis in microns. One value per channel.
--     * Slot: fwhm_micron_x_median Description: Median FWHM for the analyzed beads in the X axis in microns. One value per channel.
--     * Slot: fwhm_micron_x_std Description: Standard deviation of the FWHM for the analyzed beads in the X axis in microns. One value per channel.
--     * Slot: fwhm_lateral_asymmetry_ratio_mean Description: Mean lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
--     * Slot: fwhm_lateral_asymmetry_ratio_median Description: Median lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
--     * Slot: fwhm_lateral_asymmetry_ratio_std Description: Standard deviation of the lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.
--     * Slot: average_bead_fit_r2_z Description: Average coefficient of determination (R^2) for the fits in the Z axis of the beads. One value per channel.
--     * Slot: average_bead_fit_r2_y Description: Average coefficient of determination (R^2) for the fits in the Y axis of the beads. One value per channel.
--     * Slot: average_bead_fit_r2_x Description: Average coefficient of determination (R^2) for the fits in the X axis of the beads. One value per channel.
--     * Slot: average_bead_fwhm_pixel_z Description: FWHM for the average bead in the Z axis in pixels. One value per channel.
--     * Slot: average_bead_fwhm_pixel_y Description: FWHM for the average bead in the Y axis in pixels. One value per channel.
--     * Slot: average_bead_fwhm_pixel_x Description: FWHM for the average bead in the X axis in pixels. One value per channel.
--     * Slot: average_bead_fwhm_micron_z Description: Average FWHM for the beads in the Z axis in microns. One value per channel.
--     * Slot: average_bead_fwhm_micron_y Description: FWHM for the average bead in the Y axis in microns. One value per channel.
--     * Slot: average_bead_fwhm_micron_x Description: FWHM for the average bead in the X axis in microns. One value per channel.
--     * Slot: average_bead_fwhm_lateral_asymmetry_ratio Description: Lateral FWHM asymmetry ratio for the average bead. One value per channel.
--     * Slot: average_bead_intensity_integrated Description: Integrated intensity for the average bead. One value per channel.
--     * Slot: average_bead_intensity_max Description: Maximum intensity for the average bead. One value per channel.
--     * Slot: average_bead_intensity_min Description: Minimum intensity for the average bead. One value per channel.
--     * Slot: average_bead_intensity_std Description: Standard deviation of the intensity for the average bead. One value per channel.
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
-- # Class: LightSourcePowerDataset Description: Power measurements dataset. A collection of power measurements.
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: LightSourcePowerInputData
--     * Slot: id
-- # Class: LightSourcePowerInputParameters
--     * Slot: id
--     * Slot: linearity_required_measurements Description: The minimum number of measurements required to calculate power linearity.
--     * Slot: short_term_stability_measurement_interval_seconds Description: The measurement interval, in seconds, used to calculate short term power stability.
--     * Slot: short_term_stability_required_measurements Description: The minimum number of measurements required to calculate short term power stability.
--     * Slot: short_term_stability_required_integration_time_seconds Description: The minimum integration time, in seconds, required to calculate short term power stability.
--     * Slot: long_term_stability_measurement_interval_seconds Description: The measurement interval, in seconds, used to calculate long term power stability.
--     * Slot: long_term_stability_required_measurements Description: The minimum number of measurements required to calculate long term power stability.
--     * Slot: long_term_stability_required_integration_time_seconds Description: The minimum integration time, in seconds, required to calculate long term power stability.
-- # Class: LightSourcePowerOutput
--     * Slot: id
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: comment_id Description: A human readable comment
-- # Class: LightSourcePowerKeyMeasurement
--     * Slot: id
--     * Slot: light_source Description: The light source under investigation.
--     * Slot: power_meter Description: The power meter used to measure the power.
--     * Slot: measuring_location Description: The location at which the measurement was taken.
--     * Slot: nr_of_measurements Description: The number of power measurements taken.
--     * Slot: power_mean_mw Description: The mean power measured in milliwatts.
--     * Slot: power_median_mw Description: The median power measured in milliwatts.
--     * Slot: power_std_mw Description: The standard deviation of the power measured in milliwatts.
--     * Slot: power_min_mw Description: The minimum power measured in milliwatts.
--     * Slot: power_max_mw Description: The maximum power measured in milliwatts.
--     * Slot: power_linearity_start_datetime Description: The datetime of the first measurement used to calculate power linearity.
--     * Slot: power_linearity_end_datetime Description: The datetime of the last measurement used to calculate power linearity.
--     * Slot: power_linearity_slope Description: The slope of the linear regression model that fits output power as a function of the set point.
--     * Slot: power_linearity_intercept Description: The intercept of the linear regression model that fits output power as a function of the set point.
--     * Slot: power_linearity_coefficient_of_determination Description: The coefficient of determination a linear regression model fits output power as a function of the set point.
--     * Slot: power_linearity_p_value Description: The p-value of the linear regression model that fits output power as a function of the set point.
--     * Slot: power_linearity_std_err Description: The standard error of the linear regression model that fits output power as a function of the set point.
--     * Slot: short_term_power_stability_start_datetime Description: The datetime of the first measurement used to calculate short term power stability.
--     * Slot: short_term_power_stability_end_datetime Description: The datetime of the last measurement used to calculate short term power stability.
--     * Slot: short_term_power_stability Description: The short term stability of the light source
--     * Slot: long_term_power_stability_start_datetime Description: The datetime of the first measurement used to calculate long term power stability.
--     * Slot: long_term_power_stability_end_datetime Description: The datetime of the last measurement used to calculate long term power stability.
--     * Slot: long_term_power_stability Description: The long term stability of the light source
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
-- # Class: PowerMeasurement Description: A single power measurement for a light source.
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: light_source Description: The light source under investigation.
--     * Slot: power_meter Description: The power meter used to measure the power.
--     * Slot: measuring_location Description: The location at which the measurement was taken.
--     * Slot: power_set_point Description: The power set point as a fraction of the nominal power of the light source.
--     * Slot: power_mw Description: The power measured in milliwatts.
--     * Slot: integration_time_seconds Description: The integration time in seconds.
--     * Slot: LightSourcePowerInputData_id Description: Autocreated FK slot
-- # Class: LightSource Description: A light source.
--     * Slot: wavelength_nm Description: The wavelength of the light source in nanometers.
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: PowerMeter
--     * Slot: manufacturer
--     * Slot: model
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: UserExperiment Description: A non-standardized microscope sample produced during regular operation of a research project.
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: UserExperimentDataset Description: A dataset of non-standardized microscope samples produced during regular operation of a research project.
--     * Slot: id
--     * Slot: acquisition_datetime Description: The datetime of the acquisition
--     * Slot: experimenter Description: The experimenter that performed the imaging experiment
--     * Slot: acquisition_protocol Description: The protocol used to acquire the dataset
--     * Slot: processed Description: Has the dataset been processed by microscope-metrics
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
--     * Slot: sample_id Description: The physical sample that was imaged
--     * Slot: input_parameters_id Description: The input parameters for the analysis
--     * Slot: input_data_id Description: The input data for the analysis
--     * Slot: output_id Description: The output of the analysis
--     * Slot: microscope_id Description: The microscope that was used to acquire the dataset
--     * Slot: data_reference_id Description: A reference to the data
-- # Class: UserExperimentInputData
--     * Slot: id
-- # Class: UserExperimentInputParameters
--     * Slot: id
--     * Slot: bit_depth Description: Detector bit depth
--     * Slot: saturation_threshold Description: Tolerated saturation threshold. If the amount of saturated pixels is above this threshold,  the image is considered as saturated and the analysis is not performed.
-- # Class: UserExperimentOutput
--     * Slot: id
--     * Slot: processing_datetime Description: The datetime of the processing by microscope-metrics
--     * Slot: processing_log Description: The log of the processing by microscope-metrics
--     * Slot: validated Description: Has the dataset been validated by a human
--     * Slot: validation_datetime Description: The datetime of the validation
--     * Slot: comment_id Description: A human readable comment
-- # Class: UserExperimentKeyMeasurement
--     * Slot: id
--     * Slot: channel_name Description: The channel name to which the measurements apply
--     * Slot: channel_nr Description: The channel number to which the measurements apply
--     * Slot: variation_coefficient Description: The variation coefficient of the signal of the image. One value per channel.
--     * Slot: saturated_channels Description: The channels that are saturated in the image. One value per channel.
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
-- # Class: LightSourcePower Description: A sample providing measurements on light source power.
--     * Slot: id
--     * Slot: preparation_protocol Description: The protocol used to prepare a sample
--     * Slot: preparation_datetime Description: The datetime when the sample was prepared
--     * Slot: manufacturer Description: A manufacturer
--     * Slot: name Description: The human readable name of an entity
--     * Slot: description Description: A human readable description of an entity
-- # Class: MicroscopeCollection_microscope_collection
--     * Slot: MicroscopeCollection_id Description: Autocreated FK slot
--     * Slot: microscope_collection_id Description: The microscopes of the collection
-- # Class: Microscope_comment_collection
--     * Slot: Microscope_id Description: Autocreated FK slot
--     * Slot: comment_collection_id Description: A collection of comments
-- # Class: Protocol_authors
--     * Slot: Protocol_url Description: Autocreated FK slot
--     * Slot: authors_orcid Description: The authors of the protocol
-- # Class: MetricsOutput_processing_application
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: MetricsOutput_processing_version
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: MetricsOutput_processing_entity
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: MetricsOutput_warnings
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: MetricsOutput_errors
--     * Slot: MetricsOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: ChannelSeries_channels
--     * Slot: ChannelSeries_id Description: Autocreated FK slot
--     * Slot: channels_id Description: The channels of the ChannelSeries
-- # Class: TimeSeries_time_points_sec
--     * Slot: TimeSeries_id Description: Autocreated FK slot
--     * Slot: time_points_sec Description: The relative times at which the time series were acquired in seconds
-- # Class: Column_values
--     * Slot: Column_id Description: Autocreated FK slot
--     * Slot: values Description: An optional container for the values of the column
-- # Class: Polygon_vertexes
--     * Slot: Polygon_id Description: Autocreated FK slot
--     * Slot: vertexes_id Description: A list of vertexes defining the polygon
-- # Class: FieldIlluminationOutput_roi_profiles
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_profiles_id Description: line ROIs used to compute the intensity profiles
-- # Class: FieldIlluminationOutput_roi_corners
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_corners_id Description: Rectangular ROIs used to compute the corner intensities. The sama ROI is assigned to multiple images.
-- # Class: FieldIlluminationOutput_roi_centers_of_mass
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_of_mass_id Description: Point ROIs marking the center of mass of the area of maximum illumination. When the image is very flat, the 99 percentile is used instead. One point per channel.
-- # Class: FieldIlluminationOutput_roi_centers_geometric
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_geometric_id Description: Point ROIs marking the geometric center of the area of maximum illumination. One point per channel.
-- # Class: FieldIlluminationOutput_roi_centers_fitted
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_fitted_id Description: Point ROIs marking the fitted center of the area of maximum illumination. One point per channel.
-- # Class: FieldIlluminationOutput_roi_centers_max_intensity
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_centers_max_intensity_id Description: Point ROIs marking the maximum intensity of the area of maximum illumination. One point per channel.
-- # Class: FieldIlluminationOutput_roi_center_region
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: roi_center_region_id Description: Mask ROIs marking the area of maximum illumination. One mask per channel.
-- # Class: FieldIlluminationOutput_processing_application
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: FieldIlluminationOutput_processing_version
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: FieldIlluminationOutput_processing_entity
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: FieldIlluminationOutput_warnings
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: FieldIlluminationOutput_errors
--     * Slot: FieldIlluminationOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: PSFBeadsOutput_processing_application
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: PSFBeadsOutput_processing_version
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: PSFBeadsOutput_processing_entity
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: PSFBeadsOutput_warnings
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: PSFBeadsOutput_errors
--     * Slot: PSFBeadsOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: LightSourcePowerOutput_processing_application
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: LightSourcePowerOutput_processing_version
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: LightSourcePowerOutput_processing_entity
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: LightSourcePowerOutput_warnings
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: LightSourcePowerOutput_errors
--     * Slot: LightSourcePowerOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics
-- # Class: UserExperimentOutput_processing_application
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: processing_application Description: The application used to process the dataset
-- # Class: UserExperimentOutput_processing_version
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: processing_version Description: The version of the application used to process the dataset
-- # Class: UserExperimentOutput_processing_entity
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: processing_entity Description: The entity that processed the dataset
-- # Class: UserExperimentOutput_warnings
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: warnings Description: The warnings of the processing by microscope-metrics
-- # Class: UserExperimentOutput_errors
--     * Slot: UserExperimentOutput_id Description: Autocreated FK slot
--     * Slot: errors Description: The errors of the processing by microscope-metrics

CREATE TABLE "MetaObject" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MetaObject_id" ON "MetaObject" (id);
CREATE TABLE "NamedObject" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedObject_id" ON "NamedObject" (id);
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
	"Table_id" INTEGER,
	"FieldIlluminationDataset_id" INTEGER,
	"PSFBeadsDataset_id" INTEGER,
	"LightSourcePowerDataset_id" INTEGER,
	"UserExperimentDataset_id" INTEGER,
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
	FOREIGN KEY("Table_id") REFERENCES "Table" (id),
	FOREIGN KEY("FieldIlluminationDataset_id") REFERENCES "FieldIlluminationDataset" (id),
	FOREIGN KEY("PSFBeadsDataset_id") REFERENCES "PSFBeadsDataset" (id),
	FOREIGN KEY("LightSourcePowerDataset_id") REFERENCES "LightSourcePowerDataset" (id),
	FOREIGN KEY("UserExperimentDataset_id") REFERENCES "UserExperimentDataset" (id)
);CREATE INDEX "DataReference_omero_host_omero_object_type_omero_object_id_idx" ON "DataReference" (omero_host, omero_object_type, omero_object_id);CREATE INDEX "ix_DataReference_id" ON "DataReference" (id);
CREATE TABLE "MetricsObject" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_MetricsObject_id" ON "MetricsObject" (id);
CREATE TABLE "MicroscopeCollection" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MicroscopeCollection_id" ON "MicroscopeCollection" (id);
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
);CREATE INDEX "ix_Microscope_id" ON "Microscope" (id);
CREATE TABLE "Protocol" (
	version TEXT NOT NULL,
	url TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (url)
);CREATE INDEX "ix_Protocol_url" ON "Protocol" (url);
CREATE TABLE "Experimenter" (
	orcid TEXT NOT NULL,
	name TEXT,
	description TEXT,
	data_reference_id INTEGER,
	PRIMARY KEY (orcid),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_Experimenter_orcid" ON "Experimenter" (orcid);
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
);CREATE INDEX "ix_Comment_id" ON "Comment" (id);
CREATE TABLE "MetricsDatasetCollection" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_MetricsDatasetCollection_id" ON "MetricsDatasetCollection" (id);
CREATE TABLE "HarmonizedMetricsDatasetCollection" (
	id INTEGER NOT NULL,
	dataset_class TEXT NOT NULL,
	name TEXT,
	description TEXT,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_HarmonizedMetricsDatasetCollection_id" ON "HarmonizedMetricsDatasetCollection" (id);
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
	input_data_id INTEGER NOT NULL,
	output_id INTEGER,
	microscope_id INTEGER NOT NULL,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid),
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url),
	FOREIGN KEY("MetricsDatasetCollection_id") REFERENCES "MetricsDatasetCollection" (id),
	FOREIGN KEY("HarmonizedMetricsDatasetCollection_id") REFERENCES "HarmonizedMetricsDatasetCollection" (id),
	FOREIGN KEY(input_data_id) REFERENCES "MetricsInputData" (id),
	FOREIGN KEY(output_id) REFERENCES "MetricsOutput" (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_MetricsDataset_id" ON "MetricsDataset" (id);
CREATE TABLE "MetricsInputData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MetricsInputData_id" ON "MetricsInputData" (id);
CREATE TABLE "MetricsInputParameters" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MetricsInputParameters_id" ON "MetricsInputParameters" (id);
CREATE TABLE "MetricsOutput" (
	id INTEGER NOT NULL,
	processing_datetime DATETIME NOT NULL,
	processing_log TEXT,
	validated BOOLEAN NOT NULL,
	validation_datetime DATETIME,
	comment_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_MetricsOutput_id" ON "MetricsOutput" (id);
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
	"UserExperimentInputData_id" INTEGER,
	"UserExperimentOutput_id" INTEGER,
	time_series_id INTEGER,
	channel_series_id INTEGER,
	array_data_id INTEGER,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FieldIlluminationInputData_id") REFERENCES "FieldIlluminationInputData" (id),
	FOREIGN KEY("PSFBeadsInputData_id") REFERENCES "PSFBeadsInputData" (id),
	FOREIGN KEY("UserExperimentInputData_id") REFERENCES "UserExperimentInputData" (id),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id),
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id),
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id),
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_Image_id" ON "Image" (id);
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
);CREATE INDEX "ix_ImageMask_id" ON "ImageMask" (id);
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
	"UserExperimentOutput_id" INTEGER,
	source_roi_id INTEGER NOT NULL,
	time_series_id INTEGER,
	channel_series_id INTEGER,
	array_data_id INTEGER,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id),
	FOREIGN KEY(source_roi_id) REFERENCES "Roi" (id),
	FOREIGN KEY(time_series_id) REFERENCES "TimeSeries" (id),
	FOREIGN KEY(channel_series_id) REFERENCES "ChannelSeries" (id),
	FOREIGN KEY(array_data_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_OrthogonalImage_id" ON "OrthogonalImage" (id);
CREATE TABLE "ChannelSeries" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ChannelSeries_id" ON "ChannelSeries" (id);
CREATE TABLE "Channel" (
	id INTEGER NOT NULL,
	excitation_wavelength_nm FLOAT,
	emission_wavelength_nm FLOAT,
	name TEXT,
	description TEXT,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_Channel_id" ON "Channel" (id);
CREATE TABLE "TimeSeries" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TimeSeries_id" ON "TimeSeries" (id);
CREATE TABLE "Roi" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	"PSFBeadsOutput_id" INTEGER,
	"UserExperimentInputData_id" INTEGER,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id),
	FOREIGN KEY("UserExperimentInputData_id") REFERENCES "UserExperimentInputData" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_Roi_id" ON "Roi" (id);
CREATE TABLE "Vertex" (
	id INTEGER NOT NULL,
	x FLOAT NOT NULL,
	y FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Vertex_id" ON "Vertex" (id);
CREATE TABLE "Color" (
	id INTEGER NOT NULL,
	r INTEGER NOT NULL,
	g INTEGER NOT NULL,
	b INTEGER NOT NULL,
	alpha INTEGER,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Color_id" ON "Color" (id);
CREATE TABLE "CentersOfMass" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CentersOfMass_id" ON "CentersOfMass" (id);
CREATE TABLE "CentersGeometric" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CentersGeometric_id" ON "CentersGeometric" (id);
CREATE TABLE "CentersFitted" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CentersFitted_id" ON "CentersFitted" (id);
CREATE TABLE "CentersMaxIntensity" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CentersMaxIntensity_id" ON "CentersMaxIntensity" (id);
CREATE TABLE "Table" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	"FieldIlluminationOutput_id" INTEGER,
	"UserExperimentOutput_id" INTEGER,
	table_data_id INTEGER,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id),
	FOREIGN KEY(table_data_id) REFERENCES "MetaObject" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_Table_id" ON "Table" (id);
CREATE TABLE "FieldIlluminationDataset" (
	id INTEGER NOT NULL,
	acquisition_datetime DATETIME,
	experimenter TEXT,
	acquisition_protocol TEXT,
	processed BOOLEAN NOT NULL,
	name TEXT,
	description TEXT,
	sample_id INTEGER,
	input_parameters_id INTEGER,
	input_data_id INTEGER NOT NULL,
	output_id INTEGER,
	microscope_id INTEGER NOT NULL,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid),
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url),
	FOREIGN KEY(sample_id) REFERENCES "HomogeneousField" (id),
	FOREIGN KEY(input_parameters_id) REFERENCES "FieldIlluminationInputParameters" (id),
	FOREIGN KEY(input_data_id) REFERENCES "FieldIlluminationInputData" (id),
	FOREIGN KEY(output_id) REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_FieldIlluminationDataset_id" ON "FieldIlluminationDataset" (id);
CREATE TABLE "FieldIlluminationInputData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FieldIlluminationInputData_id" ON "FieldIlluminationInputData" (id);
CREATE TABLE "FieldIlluminationInputParameters" (
	id INTEGER NOT NULL,
	bit_depth INTEGER,
	saturation_threshold FLOAT NOT NULL,
	corner_fraction FLOAT NOT NULL,
	sigma FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FieldIlluminationInputParameters_id" ON "FieldIlluminationInputParameters" (id);
CREATE TABLE "FieldIlluminationOutput" (
	id INTEGER NOT NULL,
	processing_datetime DATETIME NOT NULL,
	processing_log TEXT,
	validated BOOLEAN NOT NULL,
	validation_datetime DATETIME,
	comment_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_id" ON "FieldIlluminationOutput" (id);
CREATE TABLE "PSFBeadsDataset" (
	id INTEGER NOT NULL,
	acquisition_datetime DATETIME,
	experimenter TEXT,
	acquisition_protocol TEXT,
	processed BOOLEAN NOT NULL,
	name TEXT,
	description TEXT,
	sample_id INTEGER,
	input_parameters_id INTEGER,
	input_data_id INTEGER NOT NULL,
	output_id INTEGER,
	microscope_id INTEGER NOT NULL,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid),
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url),
	FOREIGN KEY(sample_id) REFERENCES "PSFBeads" (id),
	FOREIGN KEY(input_parameters_id) REFERENCES "PSFBeadsInputParameters" (id),
	FOREIGN KEY(input_data_id) REFERENCES "PSFBeadsInputData" (id),
	FOREIGN KEY(output_id) REFERENCES "PSFBeadsOutput" (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_PSFBeadsDataset_id" ON "PSFBeadsDataset" (id);
CREATE TABLE "PSFBeadsInputData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_PSFBeadsInputData_id" ON "PSFBeadsInputData" (id);
CREATE TABLE "PSFBeadsInputParameters" (
	id INTEGER NOT NULL,
	bit_depth INTEGER,
	saturation_threshold FLOAT,
	min_lateral_distance_factor FLOAT NOT NULL,
	sigma_min FLOAT NOT NULL,
	sigma_max FLOAT NOT NULL,
	snr_threshold FLOAT NOT NULL,
	fitting_r2_threshold FLOAT NOT NULL,
	intensity_robust_z_score_threshold FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_PSFBeadsInputParameters_id" ON "PSFBeadsInputParameters" (id);
CREATE TABLE "PSFBeadsOutput" (
	id INTEGER NOT NULL,
	processing_datetime DATETIME NOT NULL,
	processing_log TEXT,
	validated BOOLEAN NOT NULL,
	validation_datetime DATETIME,
	bead_properties_id INTEGER,
	bead_profiles_z_id INTEGER,
	bead_profiles_y_id INTEGER,
	bead_profiles_x_id INTEGER,
	average_bead_id INTEGER,
	comment_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(bead_properties_id) REFERENCES "Table" (id),
	FOREIGN KEY(bead_profiles_z_id) REFERENCES "Table" (id),
	FOREIGN KEY(bead_profiles_y_id) REFERENCES "Table" (id),
	FOREIGN KEY(bead_profiles_x_id) REFERENCES "Table" (id),
	FOREIGN KEY(average_bead_id) REFERENCES "Image" (id),
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_PSFBeadsOutput_id" ON "PSFBeadsOutput" (id);
CREATE TABLE "LightSourcePowerDataset" (
	id INTEGER NOT NULL,
	acquisition_datetime DATETIME,
	experimenter TEXT,
	acquisition_protocol TEXT,
	processed BOOLEAN NOT NULL,
	name TEXT,
	description TEXT,
	input_data_id INTEGER NOT NULL,
	output_id INTEGER,
	microscope_id INTEGER NOT NULL,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid),
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url),
	FOREIGN KEY(input_data_id) REFERENCES "LightSourcePowerInputData" (id),
	FOREIGN KEY(output_id) REFERENCES "LightSourcePowerOutput" (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_LightSourcePowerDataset_id" ON "LightSourcePowerDataset" (id);
CREATE TABLE "LightSourcePowerInputData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_LightSourcePowerInputData_id" ON "LightSourcePowerInputData" (id);
CREATE TABLE "LightSourcePowerInputParameters" (
	id INTEGER NOT NULL,
	linearity_required_measurements INTEGER,
	short_term_stability_measurement_interval_seconds FLOAT,
	short_term_stability_required_measurements INTEGER,
	short_term_stability_required_integration_time_seconds FLOAT,
	long_term_stability_measurement_interval_seconds FLOAT,
	long_term_stability_required_measurements INTEGER,
	long_term_stability_required_integration_time_seconds FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_LightSourcePowerInputParameters_id" ON "LightSourcePowerInputParameters" (id);
CREATE TABLE "LightSourcePowerOutput" (
	id INTEGER NOT NULL,
	processing_datetime DATETIME NOT NULL,
	processing_log TEXT,
	validated BOOLEAN NOT NULL,
	validation_datetime DATETIME,
	comment_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_id" ON "LightSourcePowerOutput" (id);
CREATE TABLE "LightSource" (
	wavelength_nm FLOAT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_LightSource_name" ON "LightSource" (name);
CREATE TABLE "PowerMeter" (
	manufacturer TEXT,
	model TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (name)
);CREATE INDEX "ix_PowerMeter_name" ON "PowerMeter" (name);
CREATE TABLE "UserExperimentDataset" (
	id INTEGER NOT NULL,
	acquisition_datetime DATETIME,
	experimenter TEXT,
	acquisition_protocol TEXT,
	processed BOOLEAN NOT NULL,
	name TEXT,
	description TEXT,
	sample_id INTEGER,
	input_parameters_id INTEGER,
	input_data_id INTEGER NOT NULL,
	output_id INTEGER,
	microscope_id INTEGER NOT NULL,
	data_reference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(experimenter) REFERENCES "Experimenter" (orcid),
	FOREIGN KEY(acquisition_protocol) REFERENCES "Protocol" (url),
	FOREIGN KEY(sample_id) REFERENCES "UserExperiment" (id),
	FOREIGN KEY(input_parameters_id) REFERENCES "UserExperimentInputParameters" (id),
	FOREIGN KEY(input_data_id) REFERENCES "UserExperimentInputData" (id),
	FOREIGN KEY(output_id) REFERENCES "UserExperimentOutput" (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(data_reference_id) REFERENCES "DataReference" (id)
);CREATE INDEX "ix_UserExperimentDataset_id" ON "UserExperimentDataset" (id);
CREATE TABLE "UserExperimentInputData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_UserExperimentInputData_id" ON "UserExperimentInputData" (id);
CREATE TABLE "UserExperimentInputParameters" (
	id INTEGER NOT NULL,
	bit_depth INTEGER,
	saturation_threshold FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_UserExperimentInputParameters_id" ON "UserExperimentInputParameters" (id);
CREATE TABLE "UserExperimentOutput" (
	id INTEGER NOT NULL,
	processing_datetime DATETIME NOT NULL,
	processing_log TEXT,
	validated BOOLEAN NOT NULL,
	validation_datetime DATETIME,
	comment_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(comment_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_UserExperimentOutput_id" ON "UserExperimentOutput" (id);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_Sample_id" ON "Sample" (id);
CREATE TABLE "HasInputParametersMixin" (
	id INTEGER NOT NULL,
	input_parameters_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(input_parameters_id) REFERENCES "MetricsInputParameters" (id)
);CREATE INDEX "ix_HasInputParametersMixin_id" ON "HasInputParametersMixin" (id);
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
);CREATE INDEX "ix_Column_id" ON "Column" (id);
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
);CREATE INDEX "ix_Shape_id" ON "Shape" (id);
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
);CREATE INDEX "ix_Point_id" ON "Point" (id);
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
);CREATE INDEX "ix_Line_id" ON "Line" (id);
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
);CREATE INDEX "ix_Rectangle_id" ON "Rectangle" (id);
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
);CREATE INDEX "ix_Ellipse_id" ON "Ellipse" (id);
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
);CREATE INDEX "ix_Polygon_id" ON "Polygon" (id);
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
);CREATE INDEX "ix_Mask_id" ON "Mask" (id);
CREATE TABLE "ProfilesIntensity" (
	id INTEGER NOT NULL,
	intensity_profiles_table_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(intensity_profiles_table_id) REFERENCES "Table" (id)
);CREATE INDEX "ix_ProfilesIntensity_id" ON "ProfilesIntensity" (id);
CREATE TABLE "RoiMeasurements" (
	id INTEGER NOT NULL,
	measurements_table_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(measurements_table_id) REFERENCES "Table" (id)
);CREATE INDEX "ix_RoiMeasurements_id" ON "RoiMeasurements" (id);
CREATE TABLE "KeyMeasurement" (
	id INTEGER NOT NULL,
	"MetricsOutput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_KeyMeasurement_id" ON "KeyMeasurement" (id);
CREATE TABLE "HomogeneousField" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_HomogeneousField_id" ON "HomogeneousField" (id);
CREATE TABLE "FluorescentHomogeneousThickField" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_FluorescentHomogeneousThickField_id" ON "FluorescentHomogeneousThickField" (id);
CREATE TABLE "FluorescentHomogeneousThinField" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_FluorescentHomogeneousThinField_id" ON "FluorescentHomogeneousThinField" (id);
CREATE TABLE "FieldIlluminationKeyMeasurement" (
	id INTEGER NOT NULL,
	image_name TEXT,
	image_id TEXT,
	channel_name TEXT,
	channel_nr INTEGER,
	channel_id TEXT,
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
	"FieldIlluminationOutput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationKeyMeasurement_id" ON "FieldIlluminationKeyMeasurement" (id);
CREATE TABLE "PSFBeads" (
	id INTEGER NOT NULL,
	bead_diameter_micron FLOAT NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_PSFBeads_id" ON "PSFBeads" (id);
CREATE TABLE "PSFBeadsKeyMeasurement" (
	id INTEGER NOT NULL,
	channel_name TEXT,
	channel_nr INTEGER,
	total_bead_count INTEGER,
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
	"PSFBeadsOutput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsKeyMeasurement_id" ON "PSFBeadsKeyMeasurement" (id);
CREATE TABLE "LightSourcePowerKeyMeasurement" (
	id INTEGER NOT NULL,
	light_source TEXT,
	power_meter TEXT,
	measuring_location VARCHAR(19),
	nr_of_measurements INTEGER,
	power_mean_mw FLOAT,
	power_median_mw FLOAT,
	power_std_mw FLOAT,
	power_min_mw FLOAT,
	power_max_mw FLOAT,
	power_linearity_start_datetime DATETIME,
	power_linearity_end_datetime DATETIME,
	power_linearity_slope FLOAT,
	power_linearity_intercept FLOAT,
	power_linearity_coefficient_of_determination FLOAT,
	power_linearity_p_value FLOAT,
	power_linearity_std_err FLOAT,
	short_term_power_stability_start_datetime DATETIME,
	short_term_power_stability_end_datetime DATETIME,
	short_term_power_stability FLOAT,
	long_term_power_stability_start_datetime DATETIME,
	long_term_power_stability_end_datetime DATETIME,
	long_term_power_stability FLOAT,
	"LightSourcePowerOutput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(light_source) REFERENCES "LightSource" (name),
	FOREIGN KEY(power_meter) REFERENCES "PowerMeter" (name),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerKeyMeasurement_id" ON "LightSourcePowerKeyMeasurement" (id);
CREATE TABLE "PowerMeasurement" (
	id INTEGER NOT NULL,
	acquisition_datetime DATETIME,
	light_source TEXT,
	power_meter TEXT,
	measuring_location VARCHAR(19),
	power_set_point FLOAT,
	power_mw FLOAT,
	integration_time_seconds FLOAT,
	"LightSourcePowerInputData_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(light_source) REFERENCES "LightSource" (name),
	FOREIGN KEY(power_meter) REFERENCES "PowerMeter" (name),
	FOREIGN KEY("LightSourcePowerInputData_id") REFERENCES "LightSourcePowerInputData" (id)
);CREATE INDEX "ix_PowerMeasurement_id" ON "PowerMeasurement" (id);
CREATE TABLE "UserExperiment" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_UserExperiment_id" ON "UserExperiment" (id);
CREATE TABLE "UserExperimentKeyMeasurement" (
	id INTEGER NOT NULL,
	channel_name TEXT,
	channel_nr INTEGER,
	variation_coefficient FLOAT,
	saturated_channels INTEGER,
	"UserExperimentOutput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentKeyMeasurement_id" ON "UserExperimentKeyMeasurement" (id);
CREATE TABLE "LightSourcePower" (
	id INTEGER NOT NULL,
	preparation_protocol TEXT NOT NULL,
	preparation_datetime DATETIME,
	manufacturer TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(preparation_protocol) REFERENCES "Protocol" (url)
);CREATE INDEX "ix_LightSourcePower_id" ON "LightSourcePower" (id);
CREATE TABLE "MicroscopeCollection_microscope_collection" (
	"MicroscopeCollection_id" INTEGER,
	microscope_collection_id INTEGER NOT NULL,
	PRIMARY KEY ("MicroscopeCollection_id", microscope_collection_id),
	FOREIGN KEY("MicroscopeCollection_id") REFERENCES "MicroscopeCollection" (id),
	FOREIGN KEY(microscope_collection_id) REFERENCES "Microscope" (id)
);CREATE INDEX "ix_MicroscopeCollection_microscope_collection_microscope_collection_id" ON "MicroscopeCollection_microscope_collection" (microscope_collection_id);CREATE INDEX "ix_MicroscopeCollection_microscope_collection_MicroscopeCollection_id" ON "MicroscopeCollection_microscope_collection" ("MicroscopeCollection_id");
CREATE TABLE "Microscope_comment_collection" (
	"Microscope_id" INTEGER,
	comment_collection_id INTEGER,
	PRIMARY KEY ("Microscope_id", comment_collection_id),
	FOREIGN KEY("Microscope_id") REFERENCES "Microscope" (id),
	FOREIGN KEY(comment_collection_id) REFERENCES "Comment" (id)
);CREATE INDEX "ix_Microscope_comment_collection_comment_collection_id" ON "Microscope_comment_collection" (comment_collection_id);CREATE INDEX "ix_Microscope_comment_collection_Microscope_id" ON "Microscope_comment_collection" ("Microscope_id");
CREATE TABLE "Protocol_authors" (
	"Protocol_url" TEXT,
	authors_orcid TEXT,
	PRIMARY KEY ("Protocol_url", authors_orcid),
	FOREIGN KEY("Protocol_url") REFERENCES "Protocol" (url),
	FOREIGN KEY(authors_orcid) REFERENCES "Experimenter" (orcid)
);CREATE INDEX "ix_Protocol_authors_authors_orcid" ON "Protocol_authors" (authors_orcid);CREATE INDEX "ix_Protocol_authors_Protocol_url" ON "Protocol_authors" ("Protocol_url");
CREATE TABLE "MetricsOutput_processing_application" (
	"MetricsOutput_id" INTEGER,
	processing_application TEXT NOT NULL,
	PRIMARY KEY ("MetricsOutput_id", processing_application),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_MetricsOutput_processing_application_processing_application" ON "MetricsOutput_processing_application" (processing_application);CREATE INDEX "ix_MetricsOutput_processing_application_MetricsOutput_id" ON "MetricsOutput_processing_application" ("MetricsOutput_id");
CREATE TABLE "MetricsOutput_processing_version" (
	"MetricsOutput_id" INTEGER,
	processing_version TEXT NOT NULL,
	PRIMARY KEY ("MetricsOutput_id", processing_version),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_MetricsOutput_processing_version_processing_version" ON "MetricsOutput_processing_version" (processing_version);CREATE INDEX "ix_MetricsOutput_processing_version_MetricsOutput_id" ON "MetricsOutput_processing_version" ("MetricsOutput_id");
CREATE TABLE "MetricsOutput_processing_entity" (
	"MetricsOutput_id" INTEGER,
	processing_entity TEXT,
	PRIMARY KEY ("MetricsOutput_id", processing_entity),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_MetricsOutput_processing_entity_processing_entity" ON "MetricsOutput_processing_entity" (processing_entity);CREATE INDEX "ix_MetricsOutput_processing_entity_MetricsOutput_id" ON "MetricsOutput_processing_entity" ("MetricsOutput_id");
CREATE TABLE "MetricsOutput_warnings" (
	"MetricsOutput_id" INTEGER,
	warnings TEXT,
	PRIMARY KEY ("MetricsOutput_id", warnings),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_MetricsOutput_warnings_warnings" ON "MetricsOutput_warnings" (warnings);CREATE INDEX "ix_MetricsOutput_warnings_MetricsOutput_id" ON "MetricsOutput_warnings" ("MetricsOutput_id");
CREATE TABLE "MetricsOutput_errors" (
	"MetricsOutput_id" INTEGER,
	errors TEXT,
	PRIMARY KEY ("MetricsOutput_id", errors),
	FOREIGN KEY("MetricsOutput_id") REFERENCES "MetricsOutput" (id)
);CREATE INDEX "ix_MetricsOutput_errors_errors" ON "MetricsOutput_errors" (errors);CREATE INDEX "ix_MetricsOutput_errors_MetricsOutput_id" ON "MetricsOutput_errors" ("MetricsOutput_id");
CREATE TABLE "ChannelSeries_channels" (
	"ChannelSeries_id" INTEGER,
	channels_id INTEGER NOT NULL,
	PRIMARY KEY ("ChannelSeries_id", channels_id),
	FOREIGN KEY("ChannelSeries_id") REFERENCES "ChannelSeries" (id),
	FOREIGN KEY(channels_id) REFERENCES "Channel" (id)
);CREATE INDEX "ix_ChannelSeries_channels_channels_id" ON "ChannelSeries_channels" (channels_id);CREATE INDEX "ix_ChannelSeries_channels_ChannelSeries_id" ON "ChannelSeries_channels" ("ChannelSeries_id");
CREATE TABLE "TimeSeries_time_points_sec" (
	"TimeSeries_id" INTEGER,
	time_points_sec FLOAT NOT NULL,
	PRIMARY KEY ("TimeSeries_id", time_points_sec),
	FOREIGN KEY("TimeSeries_id") REFERENCES "TimeSeries" (id)
);CREATE INDEX "ix_TimeSeries_time_points_sec_time_points_sec" ON "TimeSeries_time_points_sec" (time_points_sec);CREATE INDEX "ix_TimeSeries_time_points_sec_TimeSeries_id" ON "TimeSeries_time_points_sec" ("TimeSeries_id");
CREATE TABLE "FieldIlluminationOutput_roi_profiles" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_profiles_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_profiles_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_profiles_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_profiles_roi_profiles_id" ON "FieldIlluminationOutput_roi_profiles" (roi_profiles_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_profiles_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_profiles" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_corners" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_corners_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_corners_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_corners_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_corners_roi_corners_id" ON "FieldIlluminationOutput_roi_corners" (roi_corners_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_corners_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_corners" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_centers_of_mass" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_centers_of_mass_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_of_mass_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_centers_of_mass_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_of_mass_roi_centers_of_mass_id" ON "FieldIlluminationOutput_roi_centers_of_mass" (roi_centers_of_mass_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_of_mass_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_centers_of_mass" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_centers_geometric" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_centers_geometric_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_geometric_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_centers_geometric_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_geometric_roi_centers_geometric_id" ON "FieldIlluminationOutput_roi_centers_geometric" (roi_centers_geometric_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_geometric_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_centers_geometric" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_centers_fitted" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_centers_fitted_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_fitted_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_centers_fitted_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_fitted_roi_centers_fitted_id" ON "FieldIlluminationOutput_roi_centers_fitted" (roi_centers_fitted_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_fitted_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_centers_fitted" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_centers_max_intensity" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_centers_max_intensity_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_centers_max_intensity_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_centers_max_intensity_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_max_intensity_roi_centers_max_intensity_id" ON "FieldIlluminationOutput_roi_centers_max_intensity" (roi_centers_max_intensity_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_centers_max_intensity_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_centers_max_intensity" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_roi_center_region" (
	"FieldIlluminationOutput_id" INTEGER,
	roi_center_region_id INTEGER,
	PRIMARY KEY ("FieldIlluminationOutput_id", roi_center_region_id),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id),
	FOREIGN KEY(roi_center_region_id) REFERENCES "Roi" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_roi_center_region_roi_center_region_id" ON "FieldIlluminationOutput_roi_center_region" (roi_center_region_id);CREATE INDEX "ix_FieldIlluminationOutput_roi_center_region_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_roi_center_region" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_processing_application" (
	"FieldIlluminationOutput_id" INTEGER,
	processing_application TEXT NOT NULL,
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_application),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_processing_application_processing_application" ON "FieldIlluminationOutput_processing_application" (processing_application);CREATE INDEX "ix_FieldIlluminationOutput_processing_application_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_processing_application" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_processing_version" (
	"FieldIlluminationOutput_id" INTEGER,
	processing_version TEXT NOT NULL,
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_version),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_processing_version_processing_version" ON "FieldIlluminationOutput_processing_version" (processing_version);CREATE INDEX "ix_FieldIlluminationOutput_processing_version_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_processing_version" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_processing_entity" (
	"FieldIlluminationOutput_id" INTEGER,
	processing_entity TEXT,
	PRIMARY KEY ("FieldIlluminationOutput_id", processing_entity),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_processing_entity_processing_entity" ON "FieldIlluminationOutput_processing_entity" (processing_entity);CREATE INDEX "ix_FieldIlluminationOutput_processing_entity_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_processing_entity" ("FieldIlluminationOutput_id");
CREATE TABLE "FieldIlluminationOutput_warnings" (
	"FieldIlluminationOutput_id" INTEGER,
	warnings TEXT,
	PRIMARY KEY ("FieldIlluminationOutput_id", warnings),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_warnings_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_warnings" ("FieldIlluminationOutput_id");CREATE INDEX "ix_FieldIlluminationOutput_warnings_warnings" ON "FieldIlluminationOutput_warnings" (warnings);
CREATE TABLE "FieldIlluminationOutput_errors" (
	"FieldIlluminationOutput_id" INTEGER,
	errors TEXT,
	PRIMARY KEY ("FieldIlluminationOutput_id", errors),
	FOREIGN KEY("FieldIlluminationOutput_id") REFERENCES "FieldIlluminationOutput" (id)
);CREATE INDEX "ix_FieldIlluminationOutput_errors_FieldIlluminationOutput_id" ON "FieldIlluminationOutput_errors" ("FieldIlluminationOutput_id");CREATE INDEX "ix_FieldIlluminationOutput_errors_errors" ON "FieldIlluminationOutput_errors" (errors);
CREATE TABLE "PSFBeadsOutput_processing_application" (
	"PSFBeadsOutput_id" INTEGER,
	processing_application TEXT NOT NULL,
	PRIMARY KEY ("PSFBeadsOutput_id", processing_application),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsOutput_processing_application_PSFBeadsOutput_id" ON "PSFBeadsOutput_processing_application" ("PSFBeadsOutput_id");CREATE INDEX "ix_PSFBeadsOutput_processing_application_processing_application" ON "PSFBeadsOutput_processing_application" (processing_application);
CREATE TABLE "PSFBeadsOutput_processing_version" (
	"PSFBeadsOutput_id" INTEGER,
	processing_version TEXT NOT NULL,
	PRIMARY KEY ("PSFBeadsOutput_id", processing_version),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsOutput_processing_version_processing_version" ON "PSFBeadsOutput_processing_version" (processing_version);CREATE INDEX "ix_PSFBeadsOutput_processing_version_PSFBeadsOutput_id" ON "PSFBeadsOutput_processing_version" ("PSFBeadsOutput_id");
CREATE TABLE "PSFBeadsOutput_processing_entity" (
	"PSFBeadsOutput_id" INTEGER,
	processing_entity TEXT,
	PRIMARY KEY ("PSFBeadsOutput_id", processing_entity),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsOutput_processing_entity_PSFBeadsOutput_id" ON "PSFBeadsOutput_processing_entity" ("PSFBeadsOutput_id");CREATE INDEX "ix_PSFBeadsOutput_processing_entity_processing_entity" ON "PSFBeadsOutput_processing_entity" (processing_entity);
CREATE TABLE "PSFBeadsOutput_warnings" (
	"PSFBeadsOutput_id" INTEGER,
	warnings TEXT,
	PRIMARY KEY ("PSFBeadsOutput_id", warnings),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsOutput_warnings_PSFBeadsOutput_id" ON "PSFBeadsOutput_warnings" ("PSFBeadsOutput_id");CREATE INDEX "ix_PSFBeadsOutput_warnings_warnings" ON "PSFBeadsOutput_warnings" (warnings);
CREATE TABLE "PSFBeadsOutput_errors" (
	"PSFBeadsOutput_id" INTEGER,
	errors TEXT,
	PRIMARY KEY ("PSFBeadsOutput_id", errors),
	FOREIGN KEY("PSFBeadsOutput_id") REFERENCES "PSFBeadsOutput" (id)
);CREATE INDEX "ix_PSFBeadsOutput_errors_PSFBeadsOutput_id" ON "PSFBeadsOutput_errors" ("PSFBeadsOutput_id");CREATE INDEX "ix_PSFBeadsOutput_errors_errors" ON "PSFBeadsOutput_errors" (errors);
CREATE TABLE "LightSourcePowerOutput_processing_application" (
	"LightSourcePowerOutput_id" INTEGER,
	processing_application TEXT NOT NULL,
	PRIMARY KEY ("LightSourcePowerOutput_id", processing_application),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_processing_application_LightSourcePowerOutput_id" ON "LightSourcePowerOutput_processing_application" ("LightSourcePowerOutput_id");CREATE INDEX "ix_LightSourcePowerOutput_processing_application_processing_application" ON "LightSourcePowerOutput_processing_application" (processing_application);
CREATE TABLE "LightSourcePowerOutput_processing_version" (
	"LightSourcePowerOutput_id" INTEGER,
	processing_version TEXT NOT NULL,
	PRIMARY KEY ("LightSourcePowerOutput_id", processing_version),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_processing_version_processing_version" ON "LightSourcePowerOutput_processing_version" (processing_version);CREATE INDEX "ix_LightSourcePowerOutput_processing_version_LightSourcePowerOutput_id" ON "LightSourcePowerOutput_processing_version" ("LightSourcePowerOutput_id");
CREATE TABLE "LightSourcePowerOutput_processing_entity" (
	"LightSourcePowerOutput_id" INTEGER,
	processing_entity TEXT,
	PRIMARY KEY ("LightSourcePowerOutput_id", processing_entity),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_processing_entity_processing_entity" ON "LightSourcePowerOutput_processing_entity" (processing_entity);CREATE INDEX "ix_LightSourcePowerOutput_processing_entity_LightSourcePowerOutput_id" ON "LightSourcePowerOutput_processing_entity" ("LightSourcePowerOutput_id");
CREATE TABLE "LightSourcePowerOutput_warnings" (
	"LightSourcePowerOutput_id" INTEGER,
	warnings TEXT,
	PRIMARY KEY ("LightSourcePowerOutput_id", warnings),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_warnings_warnings" ON "LightSourcePowerOutput_warnings" (warnings);CREATE INDEX "ix_LightSourcePowerOutput_warnings_LightSourcePowerOutput_id" ON "LightSourcePowerOutput_warnings" ("LightSourcePowerOutput_id");
CREATE TABLE "LightSourcePowerOutput_errors" (
	"LightSourcePowerOutput_id" INTEGER,
	errors TEXT,
	PRIMARY KEY ("LightSourcePowerOutput_id", errors),
	FOREIGN KEY("LightSourcePowerOutput_id") REFERENCES "LightSourcePowerOutput" (id)
);CREATE INDEX "ix_LightSourcePowerOutput_errors_errors" ON "LightSourcePowerOutput_errors" (errors);CREATE INDEX "ix_LightSourcePowerOutput_errors_LightSourcePowerOutput_id" ON "LightSourcePowerOutput_errors" ("LightSourcePowerOutput_id");
CREATE TABLE "UserExperimentOutput_processing_application" (
	"UserExperimentOutput_id" INTEGER,
	processing_application TEXT NOT NULL,
	PRIMARY KEY ("UserExperimentOutput_id", processing_application),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentOutput_processing_application_processing_application" ON "UserExperimentOutput_processing_application" (processing_application);CREATE INDEX "ix_UserExperimentOutput_processing_application_UserExperimentOutput_id" ON "UserExperimentOutput_processing_application" ("UserExperimentOutput_id");
CREATE TABLE "UserExperimentOutput_processing_version" (
	"UserExperimentOutput_id" INTEGER,
	processing_version TEXT NOT NULL,
	PRIMARY KEY ("UserExperimentOutput_id", processing_version),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentOutput_processing_version_processing_version" ON "UserExperimentOutput_processing_version" (processing_version);CREATE INDEX "ix_UserExperimentOutput_processing_version_UserExperimentOutput_id" ON "UserExperimentOutput_processing_version" ("UserExperimentOutput_id");
CREATE TABLE "UserExperimentOutput_processing_entity" (
	"UserExperimentOutput_id" INTEGER,
	processing_entity TEXT,
	PRIMARY KEY ("UserExperimentOutput_id", processing_entity),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentOutput_processing_entity_processing_entity" ON "UserExperimentOutput_processing_entity" (processing_entity);CREATE INDEX "ix_UserExperimentOutput_processing_entity_UserExperimentOutput_id" ON "UserExperimentOutput_processing_entity" ("UserExperimentOutput_id");
CREATE TABLE "UserExperimentOutput_warnings" (
	"UserExperimentOutput_id" INTEGER,
	warnings TEXT,
	PRIMARY KEY ("UserExperimentOutput_id", warnings),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentOutput_warnings_warnings" ON "UserExperimentOutput_warnings" (warnings);CREATE INDEX "ix_UserExperimentOutput_warnings_UserExperimentOutput_id" ON "UserExperimentOutput_warnings" ("UserExperimentOutput_id");
CREATE TABLE "UserExperimentOutput_errors" (
	"UserExperimentOutput_id" INTEGER,
	errors TEXT,
	PRIMARY KEY ("UserExperimentOutput_id", errors),
	FOREIGN KEY("UserExperimentOutput_id") REFERENCES "UserExperimentOutput" (id)
);CREATE INDEX "ix_UserExperimentOutput_errors_errors" ON "UserExperimentOutput_errors" (errors);CREATE INDEX "ix_UserExperimentOutput_errors_UserExperimentOutput_id" ON "UserExperimentOutput_errors" ("UserExperimentOutput_id");
CREATE TABLE "HasSampleMixin" (
	id INTEGER NOT NULL,
	sample_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);CREATE INDEX "ix_HasSampleMixin_id" ON "HasSampleMixin" (id);
CREATE TABLE "Column_values" (
	"Column_id" INTEGER,
	"values" TEXT,
	PRIMARY KEY ("Column_id", "values"),
	FOREIGN KEY("Column_id") REFERENCES "Column" (id)
);CREATE INDEX "ix_Column_values_Column_id" ON "Column_values" ("Column_id");CREATE INDEX "ix_Column_values_values" ON "Column_values" ("values");
CREATE TABLE "Polygon_vertexes" (
	"Polygon_id" INTEGER,
	vertexes_id INTEGER NOT NULL,
	PRIMARY KEY ("Polygon_id", vertexes_id),
	FOREIGN KEY("Polygon_id") REFERENCES "Polygon" (id),
	FOREIGN KEY(vertexes_id) REFERENCES "Vertex" (id)
);CREATE INDEX "ix_Polygon_vertexes_vertexes_id" ON "Polygon_vertexes" (vertexes_id);CREATE INDEX "ix_Polygon_vertexes_Polygon_id" ON "Polygon_vertexes" ("Polygon_id");
