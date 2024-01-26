from typing import Callable
from hypothesis import strategies as st

from ..datamodel import microscopemetrics_schema as mm_schema


@st.composite
def st_mm_microscope(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Sample],
    name: str = "My Microscope A",
) -> mm_schema.Microscope:
    return mm_schema.Microscope(
        name=name,
        description=draw(st.text()),
        id=draw(st.integers()),
        type=draw(
            st.sampled_from(["WIDE-FIELD", "CONFOCAL", "STED", "3D-SIM", "OTHER"])
        ),
        manufacturer=draw(st.text()),
        model=draw(st.text()),
        serial_number=draw(st.text()),
        url=draw(st.uuids()),
    )


@st.composite
def st_mm_sample(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Sample],
    name: str = "My sample name",
) -> mm_schema.Sample:
    return mm_schema.Sample(
        name=name,
        description=draw(st.text()),
        type=draw(st.text()),
        protocol=draw(st_mm_protocol()),
    )


@st.composite
def st_mm_protocol(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Protocol],
    name: str = "My protocol name",
) -> mm_schema.Protocol:
    return mm_schema.Protocol(
        name=name,
        description=draw(st.text()),
        version=draw(st.text()),
        authors=draw(st.lists(st_mm_experimenter(), min_size=1, max_size=5)),
        url=draw(st.uuids()),
    )


@st.composite
def st_mm_experimenter(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Experimenter],
    name: str = "John Doe",
) -> mm_schema.Experimenter:
    return mm_schema.Experimenter(
        name=name,
        orcid=draw(
            st.from_regex(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", fullmatch=True)
        ),
    )


@st.composite
def st_mm_comment(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.Comment],
    text: str = "A useful comment",
) -> mm_schema.Comment:
    return mm_schema.Comment(
        datetime=draw(st.datetimes()),
        comment_type=draw(st.sampled_from(["ACQUISITION", "PROCESSING", "OTHER"])),
        text=text,
    )


@st.composite
def st_mm_dataset(
    draw: Callable[[st.SearchStrategy[str]], mm_schema.MetricsDataset],
    name: str = "AnalysisX",
    processed: bool = False,
    processing_datetime: str = None,
    processing_log: str = None,
    comment: mm_schema.Comment = None,
    input: mm_schema.MetricsInput = None,
    output: mm_schema.MetricsOutput = None,
) -> mm_schema.MetricsDataset:
    if processed:
        processing_datetime = draw(st.datetimes())
        processing_log = draw(st.text())
        comment = draw(st.lists(st_mm_comment(), min_size=1, max_size=2))
        input = draw(st_mm_input())
        output = draw(st_mm_output())

    return mm_schema.MetricsDataset(
        name=name,
        description=draw(st.text()),
        microscope=draw(st_mm_microscope()),
        sample=draw(st_mm_sample()),
        experimenter=draw(st_mm_experimenter()),
        acquisition_datetime=draw(st.datetimes()),
        processed=processed,
        processing_datetime=processing_datetime,
        processing_log=processing_log,
        comment=comment,
        input=input,
        output=output,
    )


@st.composite
def st_mm_input(
    draw: Callable[[st.SearchStrategy], mm_schema.MetricsInput],
) -> mm_schema.MetricsInput:
    return mm_schema.MetricsInput()


@st.composite
def st_mm_output(
    draw: Callable[[st.SearchStrategy], mm_schema.MetricsOutput],
) -> mm_schema.MetricsOutput:
    return mm_schema.MetricsOutput()


# Data sources
@st.composite
def st_mm_image_as_numpy(
    draw: Callable[[st.SearchStrategy], mm_schema.ImageAsNumpy],
    name: str = st.text(min_size=1, max_size=20),
    description: str = st.text(min_size=1, max_size=200),
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
def st_mm_shape(
    draw: Callable[[st.SearchStrategy], mm_schema.Shape],
    label: str = st.text(min_size=1, max_size=20),
    z: float = st.floats(min_value=0.0, max_value=30.0),
    c: int = st.integers(min_value=0, max_value=5),
    t: int = st.integers(min_value=0, max_value=5),
    fill_color: mm_schema.Color = st_mm_color(),
    stroke_color: mm_schema.Color = st_mm_color(),
    stroke_width: int = st.integers(min_value=1, max_value=5),
) -> mm_schema.Shape:
    params = {
        "label": draw(label),
        "z": draw(z),
        "c": draw(c),
        "t": draw(t),
        "fill_color": draw(fill_color),
        "stroke_color": draw(stroke_color),
        "stroke_width": draw(stroke_width),
    }

    return draw(
        st.sampled_from(
            [
                st_mm_point(**params),
                st_mm_line(**params),
                st_mm_rectangle(**params),
                st_mm_polygon(**params),
                st_mm_ellipse(**params),
            ]
        )
    )


@st.composite
def st_mm_roi(
    draw: Callable[[st.SearchStrategy], mm_schema.Roi],
    label: str = st.text(min_size=1, max_size=20),
    description: str = st.text(min_size=1, max_size=200),
    image: list[str] = st.lists(st.uuids(), min_size=1, max_size=5),
    shapes: list[mm_schema.Shape] = st.lists(st_mm_shape(), min_size=1, max_size=5),
) -> mm_schema.Roi:
    shapes = draw(shapes)
    labels = [shape.label for shape in shapes]
    return mm_schema.Roi(
        label=draw(label),
        description=draw(description),
        image=draw(image),
        # shapes=draw(shapes),
    )


@st.composite
def st_mm_point(
    draw: Callable[[st.SearchStrategy], mm_schema.Point],
    label: str = st.text(min_size=1, max_size=20),
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
    label: str = st.text(min_size=1, max_size=20),
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
    label: str = st.text(min_size=1, max_size=20),
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
    label: str = st.text(min_size=1, max_size=20),
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
    label: str = st.text(min_size=1, max_size=20),
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
) -> mm_schema.FieldIlluminationOutput:
    return mm_schema.FieldIlluminationOutput()


@st.composite
def st_mm_field_illumination(
    draw: Callable[[st.SearchStrategy], mm_schema.FieldIlluminationDataset],
) -> mm_schema.FieldIlluminationDataset:
    return mm_schema.FieldIlluminationDataset()
