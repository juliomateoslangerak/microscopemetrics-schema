from typing import Callable
from hypothesis import strategies as st
from hypothesis import assume
from dataclasses import fields

from ..datamodel import microscopemetrics_schema as mm_schema


@st.composite
def st_mm_microscope(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Sample],
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    id: str = st.uuids(),
    type: str = st.sampled_from(["WIDE-FIELD", "CONFOCAL", "STED", "3D-SIM", "OTHER"]),
    manufacturer: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    model: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    serial_number: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    url: str = st.uuids(),
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
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Experimenter],
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    orcid: str = st.from_regex(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", fullmatch=True),
) -> mm_schema.Experimenter:
    return mm_schema.Experimenter(
        name=draw(name),
        orcid=draw(orcid),
    )


@st.composite
def st_mm_protocol(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Protocol],
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    version: str = st.from_regex(r"[0-9]\.[0-9]\.[0-9]{3}", fullmatch=True),
    authors: list[mm_schema.Experimenter] = st.lists(
        st_mm_experimenter(),
        min_size=1,
        max_size=5,
        unique_by=lambda experimenter: experimenter.orcid,
    ),
    url: str = st.uuids(),
) -> mm_schema.Protocol:
    return mm_schema.Protocol(
        name=name,
        description=draw(description),
        version=draw(version),
        authors=draw(authors),
        url=draw(url),
    )


@st.composite
def st_mm_sample(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Sample],
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    type: str = st.text(),
    protocol: mm_schema.Protocol = st_mm_protocol(),
) -> mm_schema.Sample:
    return mm_schema.Sample(
        name=draw(name),
        description=draw(description),
        type=draw(type),
        protocol=draw(protocol),
    )


@st.composite
def st_mm_comment(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Comment],
    datetime: str = st.datetimes(),
    text: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    comment_type: str = st.sampled_from(["ACQUISITION", "PROCESSING", "OTHER"]),
) -> mm_schema.Comment:
    return mm_schema.Comment(
        datetime=draw(datetime),
        comment_type=draw(comment_type),
        text=draw(text),
    )


@st.composite
def st_mm_input(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.MetricsInput],
    input: mm_schema.MetricsInput = st.just(mm_schema.MetricsInput()),
) -> mm_schema.MetricsInput:
    return draw(input)


@st.composite
def st_mm_output(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.MetricsOutput],
    output: mm_schema.MetricsOutput = st.just(mm_schema.MetricsOutput()),
) -> mm_schema.MetricsOutput:
    return draw(output)


@st.composite
def st_mm_dataset(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.MetricsDataset],
    target_class: mm_schema.MetricsDataset = None,
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    microscope: mm_schema.Microscope = st_mm_microscope(),
    sample: mm_schema.Sample = st_mm_sample(),
    experimenter: mm_schema.Experimenter = st_mm_experimenter(),
    acquisition_datetime: str = st.datetimes(),
    processed: bool = st.booleans(),
    processing_datetime: str = st.just(None),
    processing_log: str = st.just(None),
    comment: mm_schema.Comment = st.just(None),
    input: mm_schema.MetricsInput = st.just(st_mm_input()),
    output: mm_schema.MetricsOutput = st.just(None),
) -> mm_schema.MetricsDataset:
    processed = draw(processed)
    if processed:
        processing_datetime = st.datetimes()
        processing_log = st.text(
            alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
        )
        comment = st.lists(st_mm_comment(), min_size=1, max_size=2)
        output = draw(output)
        if output is None:
            output = st_mm_output()
    else:
        output = None

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
            output=output,
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
            output=output,
        )


# Data sources
@st.composite
def st_mm_image_as_numpy(
    draw: Callable[[st.SearchStrategy], mm_schema.ImageAsNumpy],
    name: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    image_url: str = st.uuids(),
    voxel_size_xy_micron: float = st.floats(min_value=0.1, max_value=1.0),
    voxel_size_z_micron: float = st.floats(min_value=0.3, max_value=3.0),
    shape: tuple = st.tuples(
        st.integers(min_value=1, max_value=20),  # T
        st.integers(min_value=1, max_value=100),  # Z
        st.integers(min_value=256, max_value=1024),  # Y
        st.integers(min_value=256, max_value=1024),  # X
        st.integers(min_value=1, max_value=5),  # C
    ),
    data=None,
) -> mm_schema.ImageAsNumpy:
    shape = data.shape if data is not None else draw(shape)

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
    draw: Callable[[st.SearchStrategy], mm_schema.Color],
    r: int = st.integers(min_value=0, max_value=255),
    g: int = st.integers(min_value=0, max_value=255),
    b: int = st.integers(min_value=0, max_value=255),
    alpha: int = st.integers(min_value=0, max_value=255),
) -> mm_schema.Color:
    return mm_schema.Color(r=draw(r), g=draw(g), b=draw(b), alpha=draw(alpha))


@st.composite
def st_mm_point(
    draw: Callable[[st.SearchStrategy], mm_schema.Point],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
    x: float = st.floats(min_value=0.0, max_value=1024.0),
    y: float = st.floats(min_value=0.0, max_value=1024.0),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Line],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
    x1: float = st.floats(min_value=0.0, max_value=1024.0),
    y1: float = st.floats(min_value=0.0, max_value=1024.0),
    x2: float = st.floats(min_value=0.0, max_value=1024.0),
    y2: float = st.floats(min_value=0.0, max_value=1024.0),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Rectangle],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
    x: float = st.floats(min_value=0.0, max_value=1024.0),
    y: float = st.floats(min_value=0.0, max_value=1024.0),
    w: float = st.floats(min_value=0.0, max_value=1024.0),
    h: float = st.floats(min_value=0.0, max_value=1024.0),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Ellipse],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
    x: float = st.floats(min_value=0.0, max_value=1024.0),
    y: float = st.floats(min_value=0.0, max_value=1024.0),
    x_rad: float = st.floats(min_value=0.0, max_value=1024.0),
    y_rad: float = st.floats(min_value=0.0, max_value=1024.0),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Vertex],
    x: float = st.floats(min_value=0.0, max_value=1024.0),
    y: float = st.floats(min_value=0.0, max_value=1024.0),
) -> mm_schema.Vertex:
    return mm_schema.Vertex(x=draw(x), y=draw(y))


@st.composite
def st_mm_polygon(
    draw: Callable[[st.SearchStrategy], mm_schema.Polygon],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
    vertexes: list[mm_schema.Vertex] = st.lists(
        st_mm_vertex(), min_size=3, max_size=10
    ),
    is_open: bool = st.booleans(),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Shape],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
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
    draw: Callable[[st.SearchStrategy], mm_schema.Roi],
    label: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=32
    ),
    description: str = st.text(
        alphabet=st.characters(codec="latin-1"), min_size=1, max_size=256
    ),
    image: list[str] = st.lists(st.uuids(), min_size=1, max_size=5),
    shapes: list[mm_schema.Shape] = st.lists(
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
    draw: Callable[[st.SearchStrategy], mm_schema.FieldIlluminationInput],
    field_illumination_image: mm_schema.ImageAsNumpy = st_mm_image_as_numpy(),
    bit_depth: int = st.sampled_from([8, 10, 11, 12, 15, 16, 32]),
    saturation_threshold: float = st.floats(min_value=0.0, max_value=0.1),
    center_threshold: float = st.floats(min_value=0.5, max_value=0.99),
    corner_fraction: float = st.floats(min_value=0.02, max_value=0.3),
    sigma: float = st.floats(min_value=0.0, max_value=100.0),
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
    draw: Callable[[st.SearchStrategy], mm_schema.FieldIlluminationOutput],
    output: mm_schema.FieldIlluminationOutput = st.just(
        mm_schema.FieldIlluminationOutput()
    ),
) -> mm_schema.FieldIlluminationOutput:
    return draw(output)


@st.composite
def st_mm_field_illumination_unprocessed_dataset(
    draw: Callable[[st.SearchStrategy], mm_schema.FieldIlluminationDataset],
    dataset: st_mm_dataset = st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(False),
        input=st_mm_field_illumination_input(),
        output=st.just(None),
    ),
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)


@st.composite
def st_mm_field_illumination_processed_dataset(
    draw: Callable[[st.SearchStrategy], mm_schema.FieldIlluminationDataset],
    dataset: st_mm_dataset = st_mm_dataset(
        target_class=mm_schema.FieldIlluminationDataset,
        processed=st.just(True),
        input=st_mm_field_illumination_input(),
        output=st_mm_field_illumination_output(),
    ),
) -> mm_schema.FieldIlluminationDataset:
    return draw(dataset)
