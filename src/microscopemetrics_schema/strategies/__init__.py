from hypothesis import strategies as st
from pydantic.v1.schema import schema

from ..datamodel import microscopemetrics_schema as mm_schema


# Common
@st.composite
def st_mm_data_reference(
    draw,
    data_uri=st.uuids(),
    omero_host=st.from_regex(r"omero[0-9]{1,2}.example.org", fullmatch=True),
    omero_port=st.integers(min_value=4063, max_value=4064),
    omero_object_type=st.sampled_from(["IMAGE", "DATASET", "PROJECT"]),
    omero_object_id=st.integers(min_value=1),
) -> mm_schema.DataReference:
    return mm_schema.DataReference(
        data_uri=draw(data_uri),
        omero_host=draw(omero_host),
        omero_port=draw(omero_port),
        omero_object_type=draw(omero_object_type),
        omero_object_id=draw(omero_object_id),
    )


@st.composite
def st_mm_metrics_object(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    data_reference=st_mm_data_reference(),
) -> mm_schema.MetricsObject:
    return mm_schema.MetricsObject(
        name=draw(name),
        description=draw(description),
        data_reference=draw(data_reference),
    )


@st.composite
def st_mm_microscope(
    draw,
    metrics_object=st_mm_metrics_object(),
    type=st.sampled_from(["WIDEFIELD", "CONFOCAL", "STED", "SIM3D", "OTHER"]),
    manufacturer=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    model=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    serial_number=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    data_reference=st_mm_data_reference(),
) -> mm_schema.Microscope:
    metrics_object = draw(metrics_object)
    return mm_schema.Microscope(
        name=metrics_object.name,
        description=metrics_object.description,
        data_reference=draw(data_reference),
        type=draw(type),
        manufacturer=draw(manufacturer),
        model=draw(model),
        serial_number=draw(serial_number),
    )


@st.composite
def st_mm_experimenter(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    orcid=st.from_regex(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", fullmatch=True),
) -> mm_schema.Experimenter:
    return mm_schema.Experimenter(
        name=draw(name),
        orcid=draw(orcid),
    )


@st.composite
def st_mm_protocol(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    version=st.from_regex(r"[0-9]\.[0-9]\.[0-9]{3}", fullmatch=True),
    authors=st.lists(
        st_mm_experimenter(),
        min_size=1,
        max_size=5,
        unique_by=lambda experimenter: experimenter.orcid,
    ),
    url=st.uuids(),
) -> mm_schema.Protocol:
    return mm_schema.Protocol(
        name=draw(name),
        description=draw(description),
        version=draw(version),
        authors=draw(authors),
        url=draw(url),
    )


@st.composite
def st_mm_sample(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    protocol=st_mm_protocol(),
    manufacturer=st.text(min_size=1, max_size=32),
) -> mm_schema.Sample:
    return mm_schema.Sample(
        name=draw(name),
        description=draw(description),
        protocol=draw(protocol),
        manufacturer=draw(manufacturer),
    )


@st.composite
def st_mm_comment(
    draw,
    datetime=st.datetimes(),
    author=st_mm_experimenter(),
    text=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    comment_type=st.sampled_from(["ACQUISITION", "PROCESSING", "OTHER"]),
) -> mm_schema.Comment:
    return mm_schema.Comment(
        datetime=draw(datetime),
        author=draw(author),
        comment_type=draw(comment_type),
        text=draw(text),
    )


@st.composite
def st_mm_input_data(
    draw,
    input=st.just(mm_schema.MetricsInputData(input_data=None)),
) -> mm_schema.MetricsInputData:
    return draw(input)

@st.composite
def st_mm_input_parameters(
    draw,
    input=st.just(mm_schema.MetricsInputParameters(input_data=None)),
) -> mm_schema.MetricsInputParameters:
    return draw(input)


@st.composite
def st_mm_output(
    draw,
    processing_application=st.just("MicroscopeMetrics"),
    processing_version=st.just("0.1.0"),
    processing_entity=st.just("MicroscopeMetricsAnalysis"),
    processing_datetime=st.datetimes(),
    processing_log=st.text(),
    warnings=st.lists(st.text(), max_size=5),
    errors=st.lists(st.text(), max_size=5),
    comment=st_mm_comment(),
) -> mm_schema.MetricsOutput:
    return mm_schema.MetricsOutput(
        processing_application=draw(processing_application),
        processing_version=draw(processing_version),
        processing_entity=draw(processing_entity),
        processing_datetime=draw(processing_datetime),
        processing_log=draw(processing_log),
        warnings=draw(warnings),
        errors=draw(errors),
        comment=draw(comment),
    )


@st.composite
def st_mm_dataset(
    draw,
    target_class=None,
    metrics_object=st_mm_metrics_object(),
    microscope=st_mm_microscope(),
    sample=st_mm_sample(),
    experimenter=st_mm_experimenter(),
    acquisition_datetime=st.datetimes(),
    processed=st.booleans(),
    input_data=st_mm_input_data(),
    input_parameters=st_mm_input_parameters(),
    output=st_mm_output(),
) -> mm_schema.MetricsDataset:
    metrics_object = draw(metrics_object)
    processed = draw(processed)
    output = draw(output) if processed else None
    
    if target_class is None:
        return mm_schema.MetricsDataset(
            name=metrics_object.name,
            description=metrics_object.description,
            data_reference=metrics_object.data_reference,
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            input_data=draw(input_data),
            input_parameters=draw(input_parameters),
            output=output,
        )
    else:
        return target_class(
            name=metrics_object.name,
            description=metrics_object.description,
            data_reference=metrics_object.data_reference,
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            input_data=draw(input_data),
            input_parameters=draw(input_parameters),
            output=output,
        )


# Data sources
@st.composite
def st_mm_image(
    draw,
    metrics_object=st_mm_metrics_object(),
    voxel_size_xy_micron=st.floats(min_value=0.1, max_value=1.0),
    voxel_size_z_micron=st.floats(min_value=0.3, max_value=3.0),
    shape=st.tuples(
        st.integers(min_value=1, max_value=20),  # T
        st.integers(min_value=1, max_value=100),  # Z
        st.integers(min_value=256, max_value=1024),  # Y
        st.integers(min_value=256, max_value=1024),  # X
        st.integers(min_value=1, max_value=5),  # C
    ),
    acquisition_datetime=st.datetimes(),
    data=None,
) -> mm_schema.Image:
    metrics_object = draw(metrics_object)

    if data is None:
        shape = draw(shape)
    else:
        try:
            shape = data.shape
        except AttributeError:
            shape = draw(shape)
        except Exception as e:
            raise e

    voxel_size_xy_micron = draw(voxel_size_xy_micron)

    return mm_schema.Image(
        name=metrics_object.name,
        description=metrics_object.description,
        data_reference=metrics_object.data_reference,
        voxel_size_x_micron=voxel_size_xy_micron,
        voxel_size_y_micron=voxel_size_xy_micron,
        voxel_size_z_micron=draw(voxel_size_z_micron),
        shape_t=shape[0],
        shape_z=shape[1],
        shape_y=shape[2],
        shape_x=shape[3],
        shape_c=shape[4],
        array_data=data,
        acquisition_datetime=draw(acquisition_datetime),
    )


@st.composite
def st_mm_color(
    draw,
    r=st.integers(min_value=0, max_value=255),
    g=st.integers(min_value=0, max_value=255),
    b=st.integers(min_value=0, max_value=255),
    alpha=st.integers(min_value=0, max_value=255),
) -> mm_schema.Color:
    return mm_schema.Color(r=draw(r), g=draw(g), b=draw(b), alpha=draw(alpha))


@st.composite
def st_mm_point(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
    x=st.floats(min_value=0.0, max_value=1024.0),
    y=st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Point:
    return mm_schema.Point(
        name=draw(name),
        description=draw(description),
        z=draw(z),
        c=draw(c),
        t=draw(t),
        fill_color=draw(fill_color),
        stroke_color=draw(stroke_color),
        stroke_width=draw(stroke_width),
        x=draw(x),
        y=draw(y),
    )


@st.composite
def st_mm_line(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
    x1=st.floats(min_value=0.0, max_value=1024.0),
    y1=st.floats(min_value=0.0, max_value=1024.0),
    x2=st.floats(min_value=0.0, max_value=1024.0),
    y2=st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Line:
    return mm_schema.Line(
        name=draw(name),
        description=draw(description),
        z=draw(z),
        c=draw(c),
        t=draw(t),
        fill_color=draw(fill_color),
        stroke_color=draw(stroke_color),
        stroke_width=draw(stroke_width),
        x1=draw(x1),
        y1=draw(y1),
        x2=draw(x2),
        y2=draw(y2),
    )


@st.composite
def st_mm_rectangle(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
    x=st.floats(min_value=0.0, max_value=1024.0),
    y=st.floats(min_value=0.0, max_value=1024.0),
    w=st.floats(min_value=0.0, max_value=1024.0),
    h=st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Rectangle:
    return mm_schema.Rectangle(
        name=draw(name),
        description=draw(description),
        z=draw(z),
        c=draw(c),
        t=draw(t),
        fill_color=draw(fill_color),
        stroke_color=draw(stroke_color),
        stroke_width=draw(stroke_width),
        x=draw(x),
        y=draw(y),
        w=draw(w),
        h=draw(h),
    )


@st.composite
def st_mm_ellipse(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
    x=st.floats(min_value=0.0, max_value=1024.0),
    y=st.floats(min_value=0.0, max_value=1024.0),
    x_rad=st.floats(min_value=0.0, max_value=1024.0),
    y_rad=st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Ellipse:
    return mm_schema.Ellipse(
        name=draw(name),
        description=draw(description),
        z=draw(z),
        c=draw(c),
        t=draw(t),
        fill_color=draw(fill_color),
        stroke_color=draw(stroke_color),
        stroke_width=draw(stroke_width),
        x=draw(x),
        y=draw(y),
        x_rad=draw(x_rad),
        y_rad=draw(y_rad),
    )


@st.composite
def st_mm_vertex(
    draw,
    x=st.floats(min_value=0.0, max_value=1024.0),
    y=st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Vertex:
    return mm_schema.Vertex(x=draw(x), y=draw(y))


@st.composite
def st_mm_polygon(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
    vertexes=st.lists(
        st_mm_vertex(), min_size=3, max_size=10
    ),
    is_open=st.booleans(),
) -> mm_schema.Polygon:
    return mm_schema.Polygon(
        name=draw(name),
        description=draw(description),
        z=draw(z),
        c=draw(c),
        t=draw(t),
        fill_color=draw(fill_color),
        stroke_color=draw(stroke_color),
        stroke_width=draw(stroke_width),
        vertexes=draw(vertexes),
        is_open=draw(is_open),
    )


@st.composite
def st_mm_shape(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
) -> mm_schema.Shape:
    params = {
        "name": name,
        "description": description,
        "z": z,
        "c": c,
        "t": t,
        "fill_color": fill_color,
        "stroke_color": stroke_color,
        "stroke_width": stroke_width,
    }

    shape = st.one_of(
        [
            st_mm_point(**params),
            st_mm_line(**params),
            st_mm_rectangle(**params),
            st_mm_ellipse(**params),
            st_mm_polygon(**params),
        ]
    )

    return draw(shape)


@st.composite
def st_mm_roi(
    draw,
    metrics_object=st_mm_metrics_object(),
    images=st.lists(st_mm_image(), min_size=1, max_size=2),
    shapes=st.lists(
        st_mm_shape(), min_size=1, max_size=5, unique_by=lambda shape: shape.name
    ),
) -> mm_schema.Roi:
    shapes = draw(shapes)
    metrics_object = draw(metrics_object)
    images = draw(images)
    image_links = [image.data_reference for image in images]
    return mm_schema.Roi(
        name=metrics_object.name,
        description=metrics_object.description,
        data_reference=metrics_object.data_reference,
        linked_references=image_links,
        points=[shape for shape in shapes if isinstance(shape, mm_schema.Point)],
        lines=[shape for shape in shapes if isinstance(shape, mm_schema.Line)],
        rectangles=[shape for shape in shapes if isinstance(shape, mm_schema.Rectangle)],
        ellipses=[shape for shape in shapes if isinstance(shape, mm_schema.Ellipse)],
        polygons=[shape for shape in shapes if isinstance(shape, mm_schema.Polygon)],
    )


@st.composite
def st_mm_key_values(
    draw,
    metrics_object=st_mm_metrics_object(),
    key_values=st.dictionaries(
        max_size=10,
        keys=st.text(min_size=1, max_size=32),
        values=st.one_of(st.text(), st.integers(), st.floats())
    )
) -> mm_schema.KeyValues:
    metrics_object = draw(metrics_object)
    key_values = draw(key_values)
    # NOTE: key values cannot be added arbitrarily as they are not part of the schema
    return mm_schema.KeyValues(
        name=metrics_object.name,
        description=metrics_object.description,
        data_reference=metrics_object.data_reference,
    )


@st.composite
def st_mm_tag(
    draw,
    metrics_object=st_mm_metrics_object(),
) -> mm_schema.Tag:
    metrics_object = draw(metrics_object)
    return mm_schema.Tag(
        name=metrics_object.name,
        description=metrics_object.description,
        data_reference=metrics_object.data_reference,
    )


# Field Illumination
@st.composite
def st_mm_homogeneous_field_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.HomogeneousField:
    return draw(sample)


@st.composite
def st_mm_homogeneous_thin_field_sample(
    draw,
    sample=st_mm_homogeneous_field_sample(),
) -> mm_schema.FluorescentHomogeneousThinField:
    return draw(sample)


@st.composite
def st_mm_homogeneous_thick_field_sample(
    draw,
    sample=st_mm_homogeneous_field_sample(),
) -> mm_schema.FluorescentHomogeneousThickField:
    return draw(sample)


@st.composite
def st_mm_field_illumination_input_data(
    draw,
    field_illumination_image=st.lists(st_mm_image(), min_size=1, max_size=3),
) -> mm_schema.FieldIlluminationInputData:
    return mm_schema.FieldIlluminationInputData(
        field_illumination_image=draw(field_illumination_image),
    )


@st.composite
def st_mm_field_illumination_input_parameters(
    draw,
    bit_depth=st.sampled_from([8, 10, 11, 12, 15, 16, 32]),
    saturation_threshold=st.floats(min_value=0.01, max_value=0.05),
    corner_fraction=st.floats(min_value=0.02, max_value=0.3),
    sigma=st.floats(min_value=2.0, max_value=4.0),
) -> mm_schema.FieldIlluminationInputParameters:
    return mm_schema.FieldIlluminationInputParameters(
        bit_depth=draw(bit_depth),
        saturation_threshold=draw(saturation_threshold),
        corner_fraction=draw(corner_fraction),
        sigma=draw(sigma),
    )


@st.composite
def st_mm_field_illumination_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("FieldIlluminationAnalysis"),
    ),
) -> mm_schema.FieldIlluminationOutput:
    mm_output = draw(output)
    return mm_schema.FieldIlluminationOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_field_illumination_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        sample=st.one_of(
            st_mm_homogeneous_thin_field_sample(),
            st_mm_homogeneous_thick_field_sample(),
        ),
        processed=st.just(False),
        input_data=st_mm_field_illumination_input_data(),
        input_parameters=st_mm_field_illumination_input_parameters(),
    )
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)


@st.composite
def st_mm_field_illumination_processed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(True),
        input_data=st_mm_field_illumination_input_data(),
        input_parameters=st_mm_field_illumination_input_parameters(),
        output=st_mm_field_illumination_output(),
        sample=st.one_of(
            st_mm_homogeneous_thin_field_sample(),
            st_mm_homogeneous_thick_field_sample(),
        )
    ),
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)


# PSF Beads
@st.composite
def st_mm_psf_beads_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.PSFBeads:
    return mm_schema.PSFBeads(
        bead_diameter_micron=draw(st.floats(min_value=0.1, max_value=0.5)),
        **draw(sample)._as_dict,
    )


@st.composite
def st_mm_psf_beads_input_data(
    draw,
    psf_beads_images=st_mm_image(),
) -> mm_schema.PSFBeadsInputData:
    return mm_schema.PSFBeadsInputData(
        psf_beads_images=draw(psf_beads_images),
    )


@st.composite
def st_mm_psf_beads_input_parameters(
    draw,
    min_lateral_distance_factor=st.floats(min_value=15.0, max_value=25.0),
    sigma_z=st.floats(min_value=0.7, max_value=2.0),
    sigma_y=st.floats(min_value=0.7, max_value=2.0),
    sigma_x=st.floats(min_value=0.7, max_value=2.0),
    snr_threshold=st.just(10.0),
    fitting_r2_threshold=st.just(0.85),
    intensity_robust_z_score_threshold=st.just(2.0),
) -> mm_schema.PSFBeadsInputParameters:
    return mm_schema.PSFBeadsInputParameters(
        min_lateral_distance_factor=draw(min_lateral_distance_factor),
        sigma_z=draw(sigma_z),
        sigma_y=draw(sigma_y),
        sigma_x=draw(sigma_x),
        snr_threshold=draw(snr_threshold),
        fitting_r2_threshold=draw(fitting_r2_threshold),
        intensity_robust_z_score_threshold=draw(intensity_robust_z_score_threshold),
    )


@st.composite
def st_mm_psf_beads_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("PSFBeadsAnalysis"),
    ),
) -> mm_schema.PSFBeadsOutput:
    mm_output = draw(output)
    return mm_schema.PSFBeadsOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_psf_beads_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.PSFBeadsDataset,
        sample=st_mm_psf_beads_sample(),
        processed=st.just(False),
        input_data=st_mm_psf_beads_input_data(),
        input_parameters=st_mm_psf_beads_input_parameters(),
    )
) -> mm_schema.PSFBeadsDataset:
    return draw(dataset)


@st.composite
def st_mm_psf_beads_processed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.PSFBeadsDataset,
        sample=st_mm_psf_beads_sample(),
        processed=st.just(True),
        input_data=st_mm_psf_beads_input_data(),
        input_parameters=st_mm_psf_beads_input_parameters(),
        output=st_mm_psf_beads_output(),
    )
) -> mm_schema.PSFBeadsDataset:
    return draw(dataset)


# Light Source Power
@st.composite
def st_mm_light_source(
    draw,
    wavelength=st.floats(min_value=350.0, max_value=800.0),
) -> mm_schema.LightSource:
    return mm_schema.LightSource(
        wavelength_nm=draw(wavelength),
    )


@st.composite
def st_mm_power_meter(
    draw,
    manufacturer=st.text(min_size=1, max_size=32),
    model=st.text(min_size=1, max_size=32),
) -> mm_schema.PowerMeter:
    return mm_schema.PowerMeter(
        manufacturer=draw(manufacturer),
        model=draw(model),
    )


@st.composite
def st_mm_light_source_power_sample(
    draw,
    light_source=st_mm_light_source(),
    sampling_datetime=st.datetimes(),
    power_mw=st.floats(min_value=0.0, max_value=100.0),
) -> mm_schema.LightSourcePower:
    return mm_schema.PowerSample(
        light_source=draw(light_source),
        sampling_datetime=draw(sampling_datetime),
        power_mw=draw(power_mw),
    )


@st.composite
def st_mm_light_source_power_input_data(
    draw,
    measurement_device=st_mm_power_meter(),
    light_source_power_samples=st.lists(st_mm_light_source_power_sample(), min_size=1, max_size=5),
) -> mm_schema.LightSourcePowerInputData:
    return mm_schema.LightSourcePowerInputData(
        measurement_device=draw(measurement_device),
        power_samples=draw(light_source_power_samples),
    )


@st.composite
def st_mm_light_source_power_input_parameters(
    draw,
) -> mm_schema.LightSourcePowerInputParameters:
    return mm_schema.LightSourcePowerInputParameters()


@st.composite
def st_mm_light_source_power_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("LightSourcePowerAnalysis"),
    ),
) -> mm_schema.LightSourcePowerOutput:
    mm_output = draw(output)
    return mm_schema.LightSourcePowerOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_light_source_power_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.LightSourcePowerDataset,
        processed=st.just(False),
        input_data=st_mm_light_source_power_input_data(),
    )
) -> mm_schema.LightSourcePowerDataset:
    return draw(dataset)


@st.composite
def st_mm_light_source_power_processed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.LightSourcePowerDataset,
        processed=st.just(True),
        input_data=st_mm_light_source_power_input_data(),
        output=st_mm_light_source_power_output(),
    )
) -> mm_schema.LightSourcePowerDataset:
    return draw(dataset)


# User Experiment
@st.composite
def st_mm_user_experiment_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.UserExperiment:
    return mm_schema.UserExperiment(
        **draw(sample)._as_dict,
    )


@st.composite
def st_mm_user_experiment_input_data(
    draw,
    user_experiment_images=st.lists(st_mm_image(), min_size=1, max_size=3),
) -> mm_schema.UserExperimentInputData:
    return mm_schema.UserExperimentInputData(
        user_experiment_images=draw(user_experiment_images),
    )


@st.composite
def st_mm_user_experiment_input_parameters(
    draw,
    bit_depth=st.sampled_from([8, 10, 11, 12, 15, 16, 32]),
    saturation_threshold=st.floats(min_value=0.01, max_value=0.05),
) -> mm_schema.UserExperimentInputParameters:
    return mm_schema.UserExperimentInputParameters(
        bit_depth=draw(bit_depth),
        saturation_threshold=draw(saturation_threshold),
    )


@st.composite
def st_mm_user_experiment_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("UserExperimentAnalysis"),
    ),
) -> mm_schema.UserExperimentOutput:
    mm_output = draw(output)
    return mm_schema.UserExperimentOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_user_experiment_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.UserExperimentDataset,
        sample=st_mm_user_experiment_sample(),
        processed=st.just(False),
        input_data=st_mm_user_experiment_input_data(),
        input_parameters=st_mm_user_experiment_input_parameters(),
    )
) -> mm_schema.UserExperimentDataset:
    return draw(dataset)


@st.composite
def st_mm_user_experiment_processed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.UserExperimentDataset,
        sample=st_mm_user_experiment_sample(),
        processed=st.just(True),
        input_data=st_mm_user_experiment_input_data(),
        input_parameters=st_mm_user_experiment_input_parameters(),
        output=st_mm_user_experiment_output(),
    )
) -> mm_schema.UserExperimentDataset:
    return draw(dataset)

