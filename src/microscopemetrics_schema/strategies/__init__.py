from hypothesis import strategies as st
from hypothesis import assume
from dataclasses import fields

from ..datamodel import microscopemetrics_schema as mm_schema


@st.composite
def st_mm_microscope(
    draw,
    name=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    id=st.uuids(),
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
    url=st.uuids(),
) -> mm_schema.Microscope:
    return mm_schema.Microscope(
        name=draw(name),
        description=draw(description),
        id=draw(id),
        type=draw(type),
        manufacturer=draw(manufacturer),
        model=draw(model),
        serial_number=draw(serial_number),
        url=draw(url),
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
    output=st.just(mm_schema.MetricsOutput()),
) -> mm_schema.MetricsOutput:
    return draw(output)


@st.composite
def st_mm_dataset(
    draw,
    target_class=None,
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
    processing_datetime=st.just(None),
    processing_log=st.just(None),
    comment=st.just(None),
    input=st_mm_input(),
    output=st_mm_output(),
) -> mm_schema.MetricsDataset:
    processed = draw(processed)
    if processed:
        processing_datetime = st.datetimes()
        processing_log = st.text(
            alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
        )
        comment = st.lists(st_mm_comment(), min_size=1, max_size=2)

    if target_class is None:
        return mm_schema.MetricsDataset(
            name=draw(name),
            description=draw(description),
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            processing_datetime=draw(processing_datetime),
            processing_log=draw(processing_log),
            comment=draw(comment),
            input=draw(input),
            output=draw(output),
        )
    else:
        return target_class(
            name=draw(name),
            description=draw(description),
            microscope=draw(microscope),
            sample=draw(sample),
            experimenter=draw(experimenter),
            acquisition_datetime=draw(acquisition_datetime),
            processed=processed,
            processing_datetime=draw(processing_datetime),
            processing_log=draw(processing_log),
            comment=draw(comment),
            input=draw(input),
            output=draw(output),
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
    image_url=st.uuids(),
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
        image_url=draw(image_url),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
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
        label=draw(label),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
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
        label=draw(label),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
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
        label=draw(label),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
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
        label=draw(label),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
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
        label=draw(label),
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
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z=st.floats(min_value=0.0, max_value=30.0),
    c=st.integers(min_value=0, max_value=5),
    t=st.integers(min_value=0, max_value=5),
    fill_color=st_mm_color(),
    stroke_color=st_mm_color(),
    stroke_width=st.integers(min_value=1, max_value=5),
) -> mm_schema.Shape:
    params = {
        "label": label,
        "z": z,
        "c": c,
        "t": t,
        "fill_color": fill_color,
        "stroke_color": stroke_color,
        "stroke_width": stroke_width,
    }

    shape = st.one_of(
        [
            strategy
            for strategy in [
                st_mm_point(**params),
                st_mm_line(**params),
                st_mm_rectangle(**params),
                st_mm_ellipse(**params),
                st_mm_polygon(**params),
            ]
        ]
    )

    return draw(shape)


@st.composite
def st_mm_roi(
    draw,
    label=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description=st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    image=st.lists(st.uuids(), min_size=1, max_size=5),
    shapes=st.lists(
        st_mm_shape(), min_size=1, max_size=5, unique_by=lambda shape: shape.label
    ),
) -> mm_schema.Roi:
    return mm_schema.Roi(
        label=draw(label),
        description=draw(description),
        image=draw(image),
        shapes=draw(shapes),
    )


# Field Illumination
@st.composite
def st_mm_field_illumination_input(
    draw,
    field_illumination_image=st_mm_image_as_numpy(),
    bit_depth=st.sampled_from([8, 10, 11, 12, 15, 16, 32]),
    saturation_threshold=st.floats(min_value=0.01, max_value=0.05),
    center_threshold=st.floats(min_value=0.5, max_value=0.99),
    corner_fraction=st.floats(min_value=0.02, max_value=0.3),
    sigma=st.floats(min_value=2.0, max_value=10.0),
    intensity_map_size=st.integers(min_value=32, max_value=512),
) -> mm_schema.FieldIlluminationInput:
    return mm_schema.FieldIlluminationInput(
        field_illumination_image=draw(field_illumination_image),
        bit_depth=draw(bit_depth),
        saturation_threshold=draw(saturation_threshold),
        center_threshold=draw(center_threshold),
        corner_fraction=draw(corner_fraction),
        sigma=draw(sigma),
        intensity_map_size=draw(intensity_map_size),
    )


@st.composite
def st_mm_field_illumination_output(
    draw,
    output=st.just(
        mm_schema.FieldIlluminationOutput()
    ),
) -> mm_schema.FieldIlluminationOutput:
    return draw(output)


@st.composite
def st_mm_field_illumination_unprocessed_dataset(
    draw,
    input=st_mm_field_illumination_input(),
) -> mm_schema.FieldIlluminationDataset:
    return draw(st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(False),
        input=input,
        output=st_mm_field_illumination_output(),
    ))


@st.composite
def st_mm_field_illumination_processed_dataset(
    draw,
    input=st_mm_field_illumination_input(),
    output=st_mm_field_illumination_output(),
) -> mm_schema.FieldIlluminationDataset:
    return draw(st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(True),
        input=input,
        output=output,
    ))


# PSF Beads
@st.composite
def st_mm_psf_beads_input(
    draw,
    psf_beads_images=st_mm_image_as_numpy(),
    min_lateral_distance_factor=st.floats(min_value=15.0, max_value=25.0),
    sigma_z=st.floats(min_value=0.7, max_value=2.0),
    sigma_y=st.floats(min_value=0.7, max_value=2.0),
    sigma_x=st.floats(min_value=0.7, max_value=2.0),
    snr_threshold=st.floats(min_value=5.0, max_value=100.0),
) -> mm_schema.PSFBeadsInput:
    return mm_schema.PSFBeadsInput(
        psf_beads_images=draw(psf_beads_images),
        min_lateral_distance_factor=draw(min_lateral_distance_factor),
        sigma_z=draw(sigma_z),
        sigma_y=draw(sigma_y),
        sigma_x=draw(sigma_x),
        snr_threshold=draw(snr_threshold),
    )


@st.composite
def st_mm_psf_beads_output(
    draw,
    output=st.just(
        mm_schema.PSFBeadsOutput()
    ),
) -> mm_schema.PSFBeadsOutput:
    return draw(output)


@st.composite
def st_mm_psf_beads_unprocessed_dataset(
    draw,
    input=st_mm_psf_beads_input(),
) -> mm_schema.PSFBeadsDataset:
    return draw(st_mm_dataset(
        target_class=mm_schema.PSFBeadsDataset,
        processed=st.just(False),
        input=input,
        output=st_mm_psf_beads_output(),
    ))


@st.composite
def st_mm_psf_beads_processed_dataset(
    draw,
    input=st_mm_psf_beads_input(),
    output=st_mm_psf_beads_output(),
) -> mm_schema.PSFBeadsDataset:
    return draw(st_mm_dataset(
        target_class=mm_schema.PSFBeadsDataset,
        processed=st.just(True),
        input=input,
        output=output,
    ))


