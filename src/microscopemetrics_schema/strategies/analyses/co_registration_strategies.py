from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_metrics_object,
    st_mm_image,
    st_mm_dataset,
    st_mm_output,
)
from microscopemetrics_schema.strategies.samples.fluorescent_beads_strategies import (
    st_mm_multi_wavelength_beads_sample,
)


@st.composite
def st_mm_co_registration_input_data(
    draw,
    multiwavelength_beads_images=st.lists(st_mm_image(), min_size=1, max_size=3),
) -> mm_schema.CoRegistrationInputData:
    return mm_schema.CoRegistrationInputData(
        multiwavelength_beads_images=draw(multiwavelength_beads_images),
    )


@st.composite
def st_mm_co_registration_input_parameters(
    draw,
    sigma_min=st.floats(min_value=1.0, max_value=1.2),
    sigma_max=st.floats(min_value=3.0, max_value=5.0),
    snr_threshold=st.just(10.0),
    reference_channel_nr=st.just(0),
) -> mm_schema.CoRegistrationInputParameters:
    return mm_schema.CoRegistrationInputParameters(
        sigma_min=draw(sigma_min),
        sigma_max=draw(sigma_max),
        snr_threshold=draw(snr_threshold),
        reference_channel_nr=draw(reference_channel_nr),
    )

@st.composite
def st_mm_co_registration_key_measurement(
    draw,
    reference_channel_name=st.just("channel_0"),
    reference_channel_nr=st.just(0),
    moving_channel_name=st.just("channel_1"),
    moving_channel_nr=st.just(1),
    total_bead_count=st.just(15),
    considered_valid_count=st.just(10),
    considered_self_proximity_count=st.just(2),
    considered_lateral_edge_count=st.just(2),
    considered_axial_edge_count=st.just(1),
    translation_x_mean=st.just(0.1),
    translation_y_mean=st.just(0.2),
    translation_z_mean=st.just(0.3),
    rotation_z_mean=st.just(0.4),
) -> mm_schema.CoRegistrationKeyMeasurement:
    return mm_schema.CoRegistrationKeyMeasurement(
        reference_channel_name=draw(reference_channel_name),
        reference_channel_nr=draw(reference_channel_nr),
        moving_channel_name=draw(moving_channel_name),
        moving_channel_nr=draw(moving_channel_nr),
        total_bead_count=draw(total_bead_count),
        considered_valid_count=draw(considered_valid_count),
        considered_self_proximity_count=draw(considered_self_proximity_count),
        considered_lateral_edge_count=draw(considered_lateral_edge_count),
        considered_axial_edge_count=draw(considered_axial_edge_count),
        translation_x_mean=draw(translation_x_mean),
        translation_y_mean=draw(translation_y_mean),
        translation_z_mean=draw(translation_z_mean),
        rotation_z_mean=draw(rotation_z_mean),
    )


@st.composite
def st_mm_co_registration_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("CoRegistrationAnalysis"),
        key_measurements=st.lists(st_mm_co_registration_key_measurement(), min_size=1, max_size=3),
    ),
) -> mm_schema.CoRegistrationOutput:
    mm_output = draw(output)
    return mm_schema.CoRegistrationOutput(
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
def st_mm_co_registration_unprocessed_dataset(
    draw,
    processed=st.just(False),
    input_data=st_mm_co_registration_input_data(),
    sample=st_mm_multi_wavelength_beads_sample(),
    input_parameters=st_mm_co_registration_input_parameters(),
) -> mm_schema.CoRegistrationDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.CoRegistrationDataset,
            processed=processed,
            input_data=input_data,
            sample=sample,
            input_parameters=input_parameters,
        )
    )


@st.composite
def st_mm_co_registration_processed_dataset(
    draw,
    processed=st.just(True),
    input_data=st_mm_co_registration_input_data(),
    output=st_mm_co_registration_output(),
    sample=st_mm_multi_wavelength_beads_sample(),
    input_parameters=st_mm_co_registration_input_parameters(),
) -> mm_schema.CoRegistrationDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.CoRegistrationDataset,
            processed=processed,
            input_data=input_data,
            output=output,
            sample=sample,
            input_parameters=input_parameters,
        )
    )
