from hypothesis import strategies as st
from hypothesis import assume
from dataclasses import fields

from ..datamodel import microscopemetrics_schema as mm_schema


@st.composite
def st_mm_microscope(
    draw,
    data_uri=st.uuids(),
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    type=st.sampled_from(["WIDE-FIELD", "CONFOCAL", "STED", "3D-SIM", "OTHER"]),
    manufacturer=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    model=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    serial_number=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
) -> mm_schema.Microscope:
    return mm_schema.Microscope(
        name=draw(name),
        description=draw(description),
        data_uri=draw(data_uri),
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
    type=st.text(),
    protocol=st_mm_protocol(),
) -> mm_schema.Sample:
    return mm_schema.Sample(
        name=draw(name),
        description=draw(description),
        type=draw(type),
        protocol=draw(protocol),
    )


@st.composite
def st_mm_comment(
    draw,
    datetime=st.datetimes(),
    text=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    comment_type=st.sampled_from(["ACQUISITION", "PROCESSING", "OTHER"]),
) -> mm_schema.Comment:
    return mm_schema.Comment(
        datetime=draw(datetime),
        comment_type=draw(comment_type),
        text=draw(text),
    )


@st.composite
def st_mm_input(
    draw,
    input=st.just(mm_schema.MetricsInput()),
) -> mm_schema.MetricsInput:
    return draw(input)


@st.composite
def st_mm_output(
    draw,
    processing_application=st.just("MicroscopeMetrics"),
    processing_version=st.just("0.1.0"),
    processing_entity=st.just("MicroscopeMetricsAnalysis"),
    processing_datetime=st.datetimes(),
    processing_log=st.text(),
    warnings=st.text(),
    errors=st.text(),
    comments=st_mm_comment(),
) -> mm_schema.MetricsOutput:
    return mm_schema.MetricsOutput(
        processing_application=draw(processing_application),
        processing_version=draw(processing_version),
        processing_entity=draw(processing_entity),
        processing_datetime=draw(processing_datetime),
        processing_log=draw(processing_log),
        warnings=draw(warnings),
        errors=draw(errors),
        comments=draw(comments),
    )


@st.composite
def st_mm_dataset(
    draw,
    target_class=None,
    data_uri=st.uuids(),
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    microscope=st_mm_microscope(),
    sample=st_mm_sample(),
    experimenter=st_mm_experimenter(),
    acquisition_datetime=st.datetimes(),
    processed=st.booleans(),
    input=st_mm_input(),
    output=st_mm_output(),
) -> mm_schema.MetricsDataset:
    processed = draw(processed)
    output = draw(output) if processed else None
    
    if target_class is None:
        return mm_schema.MetricsDataset(
            data_uri=draw(data_uri),
            name=draw(name),
            description=draw(description),
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            input=draw(input),
            output=output,
        )
    else:
        return target_class(
            data_uri=draw(data_uri),
            name=draw(name),
            description=draw(description),
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            input=draw(input),
            output=output,
        )


# Data sources
@st.composite
def st_mm_image_as_numpy(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    data_uri=st.uuids(),
    voxel_size_xy_micron=st.floats(min_value=0.1, max_value=1.0),
    voxel_size_z_micron=st.floats(min_value=0.3, max_value=3.0),
    shape=st.tuples(
        st.integers(min_value=1, max_value=20),  # T
        st.integers(min_value=1, max_value=100),  # Z
        st.integers(min_value=256, max_value=1024),  # Y
        st.integers(min_value=256, max_value=1024),  # X
        st.integers(min_value=1, max_value=5),  # C
    ),
    data=None,
) -> mm_schema.ImageAsNumpy:
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

    return mm_schema.ImageAsNumpy(
        name=draw(name),
        description=draw(description),
        data_uri=draw(data_uri),
        voxel_size_x_micron=voxel_size_xy_micron,
        voxel_size_y_micron=voxel_size_xy_micron,
        voxel_size_z_micron=draw(voxel_size_z_micron),
        shape_t=shape[0],
        shape_z=shape[1],
        shape_y=shape[2],
        shape_x=shape[3],
        shape_c=shape[4],
        data=data,
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
    data_uri=st.uuids(),
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
        data_uri=draw(data_uri),
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
    data_uri=st.uuids(),
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
        data_uri=draw(data_uri),
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
    data_uri=st.uuids(),
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
        data_uri=draw(data_uri),
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
    data_uri=st.uuids(),
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
        data_uri=draw(data_uri),
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
    data_uri=st.uuids(),
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
        data_uri=draw(data_uri),
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
    data_uri=st.uuids(),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
) -> mm_schema.Shape:
    params = {
        "name": name,
        "data_uri": data_uri,
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
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    data_uri=st.uuids(),
    image=st.lists(st.uuids(), min_size=1, max_size=5),
    shapes=st.lists(
        st_mm_shape(), min_size=1, max_size=5, unique_by=lambda shape: shape.name
    ),
) -> mm_schema.Roi:
    shapes = draw(shapes)
    return mm_schema.Roi(
        name=draw(name),
        data_uri=draw(data_uri),
        description=draw(description),
        image=draw(image),
        points=[shape for shape in shapes if isinstance(shape, mm_schema.Point)],
        lines=[shape for shape in shapes if isinstance(shape, mm_schema.Line)],
        rectangles=[shape for shape in shapes if isinstance(shape, mm_schema.Rectangle)],
        ellipses=[shape for shape in shapes if isinstance(shape, mm_schema.Ellipse)],
        polygons=[shape for shape in shapes if isinstance(shape, mm_schema.Polygon)],
    )


# Field Illumination
@st.composite
def st_mm_field_illumination_input(
    draw,
    field_illumination_image=st_mm_image_as_numpy(),
    bit_depth=st.sampled_from([8, 10, 11, 12, 15, 16, 32]),
    saturation_threshold=st.floats(min_value=0.01, max_value=0.05),
    corner_fraction=st.floats(min_value=0.02, max_value=0.3),
    sigma=st.floats(min_value=2.0, max_value=4.0),
    intensity_map_size=st.integers(min_value=32, max_value=512),
) -> mm_schema.FieldIlluminationInput:
    return mm_schema.FieldIlluminationInput(
        field_illumination_image=draw(field_illumination_image),
        bit_depth=draw(bit_depth),
        saturation_threshold=draw(saturation_threshold),
        corner_fraction=draw(corner_fraction),
        sigma=draw(sigma),
        intensity_map_size=draw(intensity_map_size),
    )


@st.composite
def st_mm_field_illumination_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("FieldIlluminationAnalysis"),
    ),
) -> mm_schema.FieldIlluminationOutput:
    return draw(output)


@st.composite
def st_mm_field_illumination_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(False),
        input=st_mm_field_illumination_input(),
    ),
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)


@st.composite
def st_mm_field_illumination_processed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(True),
        input=st_mm_field_illumination_input(),
        output=st_mm_field_illumination_output(),
    ),
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)


# PSF Beads
@st.composite
def st_mm_psf_beads_input(
    draw,
    psf_beads_images=st_mm_image_as_numpy(),
    min_lateral_distance_factor=st.floats(min_value=15.0, max_value=25.0),
    sigma_z=st.floats(min_value=0.7, max_value=2.0),
    sigma_y=st.floats(min_value=0.7, max_value=2.0),
    sigma_x=st.floats(min_value=0.7, max_value=2.0),
    snr_threshold=st.just(10.0),
    fitting_rss_threshold=st.just(20.0),
    intensity_robust_z_score_threshold=st.just(3.0),
) -> mm_schema.PSFBeadsInput:
    return mm_schema.PSFBeadsInput(
        psf_beads_images=draw(psf_beads_images),
        min_lateral_distance_factor=draw(min_lateral_distance_factor),
        sigma_z=draw(sigma_z),
        sigma_y=draw(sigma_y),
        sigma_x=draw(sigma_x),
        snr_threshold=draw(snr_threshold),
        fitting_rss_threshold=draw(fitting_rss_threshold),
        intensity_robust_z_score_threshold=draw(intensity_robust_z_score_threshold),
    )


@st.composite
def st_mm_psf_beads_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("PSFBeadsAnalysis"),
    ),
) -> mm_schema.PSFBeadsOutput:
    return draw(output)


@st.composite
def st_mm_psf_beads_unprocessed_dataset(
    draw,
    dataset=st_mm_dataset(
        target_class=mm_schema.PSFBeadsDataset,
        processed=st.just(False),
        input=st_mm_psf_beads_input(),
    )
) -> mm_schema.PSFBeadsDataset:
    return draw(dataset)


@st.composite
def st_mm_psf_beads_processed_dataset(
    draw,
    dataset=st_mm_dataset(
    target_class=mm_schema.PSFBeadsDataset,
    processed=st.just(True),
    input=st_mm_psf_beads_input(),
    output=st_mm_psf_beads_output(),
    )
) -> mm_schema.PSFBeadsDataset:
    return draw(dataset)


