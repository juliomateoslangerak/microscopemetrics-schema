from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_metrics_object,
    st_mm_image,
    st_mm_dataset,
    st_mm_output,
)
from microscopemetrics_schema.strategies.samples.homogeneous_field_strategies import (
    st_mm_homogeneous_thin_field_sample,
    st_mm_homogeneous_thick_field_sample,
)


@st.composite
def st_mm_field_illumination_input_data(
    draw,
    field_illumination_image=st.lists(st_mm_image(), min_size=1, max_size=3),
) -> mm_schema.FieldIlluminationInputData:
    return mm_schema.FieldIlluminationInputData(
        field_illumination_images=draw(field_illumination_image),
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
def st_mm_field_illumination_key_measurement(
    draw,
    image_name=st.just("field_illumination_image"),
    image_id=st.just("field_illumination_image_id"),
    channel_name=st.just("channel_0"),
    channel_nr=st.just(1),
    channel_id=st.just("channel_0_id"),
    center_region_intensity_fraction=st.just(0.1),
    center_region_area_fraction=st.just(0.1),
    center_of_mass_y=st.just(255),
    center_of_mass_y_relative=st.just(0.5),
    center_of_mass_x=st.just(255),
    center_of_mass_x_relative=st.just(0.5),
    center_of_mass_distance_relative=st.just(0.5),
    center_geometric_y=st.just(255),
    center_geometric_y_relative=st.just(0.5),
    center_geometric_x=st.just(255),
    center_geometric_x_relative=st.just(0.5),
    center_geometric_distance_relative=st.just(0.5),
    center_fitted_y=st.just(255),
    center_fitted_y_relative=st.just(0.5),
    center_fitted_x=st.just(255),
    center_fitted_x_relative=st.just(0.5),
    center_fitted_distance_relative=st.just(0.5),
    max_intensity=st.just(205),
    max_intensity_pos_y=st.just(255),
    max_intensity_pos_y_relative=st.just(0.5),
    max_intensity_pos_x=st.just(255),
    max_intensity_pos_x_relative=st.just(0.5),
    max_intensity_distance_relative=st.just(0.5),
    top_left_intensity_mean=st.just(105),
    top_left_intensity_ratio=st.just(0.4),
    top_center_intensity_mean=st.just(155),
    top_center_intensity_ratio=st.just(0.6),
    top_right_intensity_mean=st.just(205),
    top_right_intensity_ratio=st.just(0.8),
    middle_left_intensity_mean=st.just(125),
    middle_left_intensity_ratio=st.just(0.5),
    middle_center_intensity_mean=st.just(175),
    middle_center_intensity_ratio=st.just(0.7),
    middle_right_intensity_mean=st.just(225),
    middle_right_intensity_ratio=st.just(0.9),
    bottom_left_intensity_mean=st.just(115),
    bottom_left_intensity_ratio=st.just(0.3),
    bottom_center_intensity_mean=st.just(165),
    bottom_center_intensity_ratio=st.just(0.5),
    bottom_right_intensity_mean=st.just(215),
    bottom_right_intensity_ratio=st.just(0.7),
) -> mm_schema.FieldIlluminationKeyMeasurement:
    return mm_schema.FieldIlluminationKeyMeasurement(
        image_name=draw(image_name),
        image_id=draw(image_id),
        channel_name=draw(channel_name),
        channel_nr=draw(channel_nr),
        channel_id=draw(channel_id),
        center_region_intensity_fraction=draw(center_region_intensity_fraction),
        center_region_area_fraction=draw(center_region_area_fraction),
        center_of_mass_y=draw(center_of_mass_y),
        center_of_mass_y_relative=draw(center_of_mass_y_relative),
        center_of_mass_x=draw(center_of_mass_x),
        center_of_mass_x_relative=draw(center_of_mass_x_relative),
        center_of_mass_distance_relative=draw(center_of_mass_distance_relative),
        center_geometric_y=draw(center_geometric_y),
        center_geometric_y_relative=draw(center_geometric_y_relative),
        center_geometric_x=draw(center_geometric_x),
        center_geometric_x_relative=draw(center_geometric_x_relative),
        center_geometric_distance_relative=draw(center_geometric_distance_relative),
        center_fitted_y=draw(center_fitted_y),
        center_fitted_y_relative=draw(center_fitted_y_relative),
        center_fitted_x=draw(center_fitted_x),
        center_fitted_x_relative=draw(center_fitted_x_relative),
        center_fitted_distance_relative=draw(center_fitted_distance_relative),
        max_intensity=draw(max_intensity),
        max_intensity_pos_y=draw(max_intensity_pos_y),
        max_intensity_pos_y_relative=draw(max_intensity_pos_y_relative),
        max_intensity_pos_x=draw(max_intensity_pos_x),
        max_intensity_pos_x_relative=draw(max_intensity_pos_x_relative),
        max_intensity_distance_relative=draw(max_intensity_distance_relative),
        top_left_intensity_mean=draw(top_left_intensity_mean),
        top_left_intensity_ratio=draw(top_left_intensity_ratio),
        top_center_intensity_mean=draw(top_center_intensity_mean),
        top_center_intensity_ratio=draw(top_center_intensity_ratio),
        top_right_intensity_mean=draw(top_right_intensity_mean),
        top_right_intensity_ratio=draw(top_right_intensity_ratio),
        middle_left_intensity_mean=draw(middle_left_intensity_mean),
        middle_left_intensity_ratio=draw(middle_left_intensity_ratio),
        middle_center_intensity_mean=draw(middle_center_intensity_mean),
        middle_center_intensity_ratio=draw(middle_center_intensity_ratio),
        middle_right_intensity_mean=draw(middle_right_intensity_mean),
        middle_right_intensity_ratio=draw(middle_right_intensity_ratio),
        bottom_left_intensity_mean=draw(bottom_left_intensity_mean),
        bottom_left_intensity_ratio=draw(bottom_left_intensity_ratio),
        bottom_center_intensity_mean=draw(bottom_center_intensity_mean),
        bottom_center_intensity_ratio=draw(bottom_center_intensity_ratio),
        bottom_right_intensity_mean=draw(bottom_right_intensity_mean),
        bottom_right_intensity_ratio=draw(bottom_right_intensity_ratio),
    )


@st.composite
def st_mm_field_illumination_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("FieldIlluminationAnalysis"),
        key_measurements=st.lists(st_mm_field_illumination_key_measurement(), min_size=1, max_size=3),
    ),
) -> mm_schema.FieldIlluminationOutput:
    mm_output = draw(output)
    return mm_schema.FieldIlluminationOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        key_measurements=mm_output.key_measurements,
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_field_illumination_unprocessed_dataset(
    draw,
    processed=st.just(False),
    input_data=st_mm_field_illumination_input_data(),
    sample=st.one_of(
        st_mm_homogeneous_thin_field_sample(),
        st_mm_homogeneous_thick_field_sample(),
    ),
    input_parameters=st_mm_field_illumination_input_parameters(),
) -> mm_schema.FieldIlluminationDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.FieldIlluminationDataset,
            processed=processed,
            input_data=input_data,
            sample=sample,
            input_parameters=input_parameters,
        )
    )


@st.composite
def st_mm_field_illumination_processed_dataset(
    draw,
    processed=st.just(True),
    input_data=st_mm_field_illumination_input_data(),
    output=st_mm_field_illumination_output(),
    sample=st.one_of(
        st_mm_homogeneous_thin_field_sample(),
        st_mm_homogeneous_thick_field_sample(),
    ),
    input_parameters=st_mm_field_illumination_input_parameters(),
) -> mm_schema.FieldIlluminationDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.FieldIlluminationDataset,
            processed=processed,
            input_data=input_data,
            output=output,
            sample=sample,
            input_parameters=input_parameters,
        )
    )

