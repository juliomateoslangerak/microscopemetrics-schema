from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
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
    reference_channel_nr=st.just(0),
    saturation_threshold=st.just(0.01),
    min_lateral_distance_px=st.floats(min_value=15.0, max_value=25.0),
    min_axial_distance_px=st.floats(min_value=15.0, max_value=25.0),
    sigma_min=st.floats(min_value=1.0, max_value=1.2),
    sigma_max=st.floats(min_value=3.0, max_value=5.0),
    snr_threshold=st.just(10.0),
    fitting_gaussian_r2_threshold=st.just(0.95),
    robust_z_score_threshold=st.just(2.0),
) -> mm_schema.CoRegistrationInputParameters:
    return mm_schema.CoRegistrationInputParameters(
        saturation_threshold=draw(saturation_threshold),
        min_lateral_distance_px=draw(min_lateral_distance_px),
        min_axial_distance_px=draw(min_axial_distance_px),
        sigma_min=draw(sigma_min),
        sigma_max=draw(sigma_max),
        snr_threshold=draw(snr_threshold),
        fitting_gaussian_r2_threshold=draw(fitting_gaussian_r2_threshold),
        robust_z_score_threshold=draw(robust_z_score_threshold),
        reference_channel_nr=draw(reference_channel_nr),
    )

@st.composite
def st_mm_co_registration_key_measurement(
    draw,
    reference_channel_name=st.just("channel_0"),
    reference_channel_nr=st.just(0),
    channel_name=st.just("channel_1"),
    channel_nr=st.just(1),
    excitation_wavelength_nm=st.just(488),
    emission_wavelength_nm=st.just(520),
    total_bead_count=st.just(15),
    considered_valid_count=st.just(10),
    considered_self_proximity_count=st.just(2),
    considered_lateral_edge_count=st.just(2),
    considered_axial_edge_count=st.just(1),
    considered_outlier_count=st.just(2),
    translation_abs_mean_pixel_x=st.just(0.1),
    translation_abs_median_pixel_x=st.just(0.1),
    translation_abs_std_pixel_x=st.just(0.1),
    translation_abs_mean_pixel_y=st.just(0.2),
    translation_abs_median_pixel_y=st.just(0.2),
    translation_abs_std_pixel_y=st.just(0.2),
    translation_abs_mean_pixel_z=st.just(0.3),
    translation_abs_median_pixel_z=st.just(0.3),
    translation_abs_std_pixel_z=st.just(0.3),
    translation_abs_mean_micron_x=st.just(0.1),
    translation_abs_median_micron_x=st.just(0.1),
    translation_abs_std_micron_x=st.just(0.1),
    translation_abs_mean_micron_y=st.just(0.2),
    translation_abs_median_micron_y=st.just(0.2),
    translation_abs_std_micron_y=st.just(0.2),
    translation_abs_mean_micron_z=st.just(0.3),
    translation_abs_median_micron_z=st.just(0.3),
    translation_abs_std_micron_z=st.just(0.3),
    distance_mean_micron_3d=st.just(0.4),
    distance_median_micron_3d=st.just(0.4),
    distance_std_micron_3d=st.just(0.4),
    rotation_z_mean=st.just(0.4),
) -> mm_schema.CoRegistrationKeyMeasurement:
    return mm_schema.CoRegistrationKeyMeasurement(
        reference_channel_name=draw(reference_channel_name),
        reference_channel_nr=draw(reference_channel_nr),
        channel_name=draw(channel_name),
        channel_nr=draw(channel_nr),
        excitation_wavelength_nm=draw(excitation_wavelength_nm),
        emission_wavelength_nm=draw(emission_wavelength_nm),
        total_bead_count=draw(total_bead_count),
        considered_valid_count=draw(considered_valid_count),
        considered_self_proximity_count=draw(considered_self_proximity_count),
        considered_lateral_edge_count=draw(considered_lateral_edge_count),
        considered_axial_edge_count=draw(considered_axial_edge_count),
        considered_outlier_count=draw(considered_outlier_count),
        translation_abs_mean_pixel_x=draw(translation_abs_mean_pixel_x),
        translation_abs_median_pixel_x=draw(translation_abs_median_pixel_x),
        translation_abs_std_pixel_x=draw(translation_abs_std_pixel_x),
        translation_abs_mean_pixel_y=draw(translation_abs_mean_pixel_y),
        translation_abs_median_pixel_y=draw(translation_abs_median_pixel_y),
        translation_abs_std_pixel_y=draw(translation_abs_std_pixel_y),
        translation_abs_mean_pixel_z=draw(translation_abs_mean_pixel_z),
        translation_abs_median_pixel_z=draw(translation_abs_median_pixel_z),
        translation_abs_std_pixel_z=draw(translation_abs_std_pixel_z),
        translation_abs_mean_micron_x=draw(translation_abs_mean_micron_x),
        translation_abs_median_micron_y=draw(translation_abs_median_micron_y),
        translation_abs_std_micron_z=draw(translation_abs_std_micron_z),
        distance_mean_micron_3d=draw(distance_mean_micron_3d),
        distance_median_micron_3d=draw(distance_median_micron_3d),
        distance_std_micron_3d=draw(distance_std_micron_3d),
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
