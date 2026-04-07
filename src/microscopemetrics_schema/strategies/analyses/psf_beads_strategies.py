from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_metrics_object,
    st_mm_image,
    st_mm_dataset,
    st_mm_output,
)
from microscopemetrics_schema.strategies.samples.psf_beads_strategies import (
    st_mm_psf_beads_sample,
)


@st.composite
def st_mm_psf_beads_input_data(
    draw,
    psf_beads_images=st.lists(st_mm_image(), min_size=1, max_size=3),
) -> mm_schema.PSFBeadsInputData:
    return mm_schema.PSFBeadsInputData(
        psf_beads_images=draw(psf_beads_images),
    )


@st.composite
def st_mm_psf_beads_input_parameters(
    draw,
    min_lateral_distance_factor=st.floats(min_value=15.0, max_value=25.0),
    sigma_min=st.floats(min_value=1.0, max_value=1.2),
    sigma_max=st.floats(min_value=3.0, max_value=5.0),
    snr_threshold=st.just(10.0),
    fitting_airy_r2_threshold=st.just(0.85),
    fitting_gaussian_r2_threshold=st.just(0.85),
    intensity_robust_z_score_threshold=st.just(2.0),
) -> mm_schema.PSFBeadsInputParameters:
    return mm_schema.PSFBeadsInputParameters(
        min_lateral_distance_factor=draw(min_lateral_distance_factor),
        sigma_min=draw(sigma_min),
        sigma_max=draw(sigma_max),
        snr_threshold=draw(snr_threshold),
        fitting_airy_r2_threshold=draw(fitting_airy_r2_threshold),
        fitting_gaussian_r2_threshold=draw(fitting_gaussian_r2_threshold),
        intensity_robust_z_score_threshold=draw(intensity_robust_z_score_threshold),
    )


@st.composite
def st_mm_psf_beads_key_measurement(
    draw,
    channel_name=st.just("channel_0"),
    channel_nr=st.just(0),
    total_bead_count=st.just(15),
    considered_valid_count=st.just(10),
    considered_self_proximity_count=st.just(2),
    considered_lateral_edge_count=st.just(1),
    considered_axial_edge_count=st.just(1),
    considered_intensity_outlier_count=st.just(1),
    considered_bad_fit_airy_z_count=st.just(0),
    considered_bad_fit_airy_y_count=st.just(0),
    considered_bad_fit_airy_x_count=st.just(0),
    considered_bad_fit_gaussian_z_count=st.just(0),
    considered_bad_fit_gaussian_y_count=st.just(0),
    considered_bad_fit_gaussian_x_count=st.just(0),
    intensity_integrated_mean=st.just(128),
    intensity_integrated_median=st.just(128),
    intensity_integrated_std=st.just(3),
    intensity_max_mean=st.just(200),
    intensity_max_median=st.just(200),
    intensity_max_std=st.just(3),
    intensity_min_mean=st.just(5),
    intensity_min_median=st.just(5),
    intensity_min_std=st.just(2),
    intensity_std_mean=st.just(3),
    intensity_std_median=st.just(4),
    intensity_std_std=st.just(2),
    fit_airy_r2_z_mean=st.just(0.80),
    fit_airy_r2_z_median=st.just(0.80),
    fit_airy_r2_z_std=st.just(0.02),
    fit_airy_r2_y_mean=st.just(0.85),
    fit_airy_r2_y_median=st.just(0.85),
    fit_airy_r2_y_std=st.just(0.01),
    fit_airy_r2_x_mean=st.just(0.85),
    fit_airy_r2_x_median=st.just(0.86),
    fit_airy_r2_x_std=st.just(0.03),
    fit_gaussian_r2_z_mean=st.just(0.80),
    fit_gaussian_r2_z_median=st.just(0.80),
    fit_gaussian_r2_z_std=st.just(0.02),
    fit_gaussian_r2_y_mean=st.just(0.85),
    fit_gaussian_r2_y_median=st.just(0.85),
    fit_gaussian_r2_y_std=st.just(0.01),
    fit_gaussian_r2_x_mean=st.just(0.85),
    fit_gaussian_r2_x_median=st.just(0.86),
    fit_gaussian_r2_x_std=st.just(0.03),
    fwhm_pixel_z_mean=st.just(3.2),
    fwhm_pixel_z_median=st.just(3.2),
    fwhm_pixel_z_std=st.just(0.2),
    fwhm_pixel_y_mean=st.just(3.2),
    fwhm_pixel_y_median=st.just(3.2),
    fwhm_pixel_y_std=st.just(0.1),
    fwhm_pixel_x_mean=st.just(3.2),
    fwhm_pixel_x_median=st.just(3.2),
    fwhm_pixel_x_std=st.just(0.3),
    fwhm_micron_z_mean=st.just(0.5),
    fwhm_micron_z_median=st.just(0.5),
    fwhm_micron_z_std=st.just(0.05),
    fwhm_micron_y_mean=st.just(0.23),
    fwhm_micron_y_median=st.just(0.23),
    fwhm_micron_y_std=st.just(0.01),
    fwhm_micron_x_mean=st.just(0.23),
    fwhm_micron_x_median=st.just(0.23),
    fwhm_micron_x_std=st.just(0.02),
    fwhm_lateral_asymmetry_ratio_mean=st.just(1.1),
    fwhm_lateral_asymmetry_ratio_median=st.just(1.1),
    fwhm_lateral_asymmetry_ratio_std=st.just(0.02),
    average_bead_fit_airy_r2_z=st.just(0.85),
    average_bead_fit_airy_r2_y=st.just(0.86),
    average_bead_fit_airy_r2_x=st.just(0.90),
    average_bead_fit_gaussian_r2_z=st.just(0.85),
    average_bead_fit_gaussian_r2_y=st.just(0.86),
    average_bead_fit_gaussian_r2_x=st.just(0.90),
    average_bead_fwhm_pixel_z=st.just(3.2),
    average_bead_fwhm_pixel_y=st.just(3.2),
    average_bead_fwhm_pixel_x=st.just(3.2),
    average_bead_fwhm_micron_z=st.just(0.5),
    average_bead_fwhm_micron_y=st.just(0.23),
    average_bead_fwhm_micron_x=st.just(0.23),
    average_bead_fwhm_lateral_asymmetry_ratio=st.just(1.1),
    average_bead_intensity_integrated=st.just(666),
    average_bead_intensity_max=st.just(200),
    average_bead_intensity_min=st.just(20),
) -> mm_schema.PSFBeadsKeyMeasurement:
    return mm_schema.PSFBeadsKeyMeasurement(
        channel_name=draw(channel_name),
        channel_nr=draw(channel_nr),
        total_bead_count=draw(total_bead_count),
        considered_valid_count=draw(considered_valid_count),
        considered_self_proximity_count=draw(considered_self_proximity_count),
        considered_lateral_edge_count=draw(considered_lateral_edge_count),
        considered_axial_edge_count=draw(considered_axial_edge_count),
        considered_intensity_outlier_count=draw(considered_intensity_outlier_count),
        considered_bad_fit_airy_z_count=draw(considered_bad_fit_airy_z_count),
        considered_bad_fit_airy_y_count=draw(considered_bad_fit_airy_y_count),
        considered_bad_fit_airy_x_count=draw(considered_bad_fit_airy_x_count),
        considered_bad_fit_gaussian_z_count=draw(considered_bad_fit_gaussian_z_count),
        considered_bad_fit_gaussian_y_count=draw(considered_bad_fit_gaussian_y_count),
        considered_bad_fit_gaussian_x_count=draw(considered_bad_fit_gaussian_x_count),
        intensity_integrated_mean=draw(intensity_integrated_mean),
        intensity_integrated_median=draw(intensity_integrated_median),
        intensity_integrated_std=draw(intensity_integrated_std),
        intensity_max_mean=draw(intensity_max_mean),
        intensity_max_median=draw(intensity_max_median),
        intensity_max_std=draw(intensity_max_std),
        intensity_min_mean=draw(intensity_min_mean),
        intensity_min_median=draw(intensity_min_median),
        intensity_min_std=draw(intensity_min_std),
        intensity_std_mean=draw(intensity_std_mean),
        intensity_std_median=draw(intensity_std_median),
        intensity_std_std=draw(intensity_std_std),
        fit_airy_r2_z_mean=draw(fit_airy_r2_z_mean),
        fit_airy_r2_z_median=draw(fit_airy_r2_z_median),
        fit_airy_r2_z_std=draw(fit_airy_r2_z_std),
        fit_airy_r2_y_mean=draw(fit_airy_r2_y_mean),
        fit_airy_r2_y_median=draw(fit_airy_r2_y_median),
        fit_airy_r2_y_std=draw(fit_airy_r2_y_std),
        fit_airy_r2_x_mean=draw(fit_airy_r2_x_mean),
        fit_airy_r2_x_median=draw(fit_airy_r2_x_median),
        fit_airy_r2_x_std=draw(fit_airy_r2_x_std),
        fit_gaussian_r2_z_mean=draw(fit_gaussian_r2_z_mean),
        fit_gaussian_r2_z_median=draw(fit_gaussian_r2_z_median),
        fit_gaussian_r2_z_std=draw(fit_gaussian_r2_z_std),
        fit_gaussian_r2_y_mean=draw(fit_gaussian_r2_y_mean),
        fit_gaussian_r2_y_median=draw(fit_gaussian_r2_y_median),
        fit_gaussian_r2_y_std=draw(fit_gaussian_r2_y_std),
        fit_gaussian_r2_x_mean=draw(fit_gaussian_r2_x_mean),
        fit_gaussian_r2_x_median=draw(fit_gaussian_r2_x_median),
        fit_gaussian_r2_x_std=draw(fit_gaussian_r2_x_std),
        fwhm_pixel_z_mean=draw(fwhm_pixel_z_mean),
        fwhm_pixel_z_median=draw(fwhm_pixel_z_median),
        fwhm_pixel_z_std=draw(fwhm_pixel_z_std),
        fwhm_pixel_y_mean=draw(fwhm_pixel_y_mean),
        fwhm_pixel_y_median=draw(fwhm_pixel_y_median),
        fwhm_pixel_y_std=draw(fwhm_pixel_y_std),
        fwhm_pixel_x_mean=draw(fwhm_pixel_x_mean),
        fwhm_pixel_x_median=draw(fwhm_pixel_x_median),
        fwhm_pixel_x_std=draw(fwhm_pixel_x_std),
        fwhm_micron_z_mean=draw(fwhm_micron_z_mean),
        fwhm_micron_z_median=draw(fwhm_micron_z_median),
        fwhm_micron_z_std=draw(fwhm_micron_z_std),
        fwhm_micron_y_mean=draw(fwhm_micron_y_mean),
        fwhm_micron_y_median=draw(fwhm_micron_y_median),
        fwhm_micron_y_std=draw(fwhm_micron_y_std),
        fwhm_micron_x_mean=draw(fwhm_micron_x_mean),
        fwhm_micron_x_median=draw(fwhm_micron_x_median),
        fwhm_micron_x_std=draw(fwhm_micron_x_std),
        fwhm_lateral_asymmetry_ratio_mean=draw(fwhm_lateral_asymmetry_ratio_mean),
        fwhm_lateral_asymmetry_ratio_median=draw(fwhm_lateral_asymmetry_ratio_median),
        fwhm_lateral_asymmetry_ratio_std=draw(fwhm_lateral_asymmetry_ratio_std),
        average_bead_fit_airy_r2_z=draw(average_bead_fit_airy_r2_z),
        average_bead_fit_airy_r2_y=draw(average_bead_fit_airy_r2_y),
        average_bead_fit_airy_r2_x=draw(average_bead_fit_airy_r2_x),
        average_bead_fit_gaussian_r2_z=draw(average_bead_fit_gaussian_r2_z),
        average_bead_fit_gaussian_r2_y=draw(average_bead_fit_gaussian_r2_y),
        average_bead_fit_gaussian_r2_x=draw(average_bead_fit_gaussian_r2_x),
        average_bead_fwhm_pixel_z=draw(average_bead_fwhm_pixel_z),
        average_bead_fwhm_pixel_y=draw(average_bead_fwhm_pixel_y),
        average_bead_fwhm_pixel_x=draw(average_bead_fwhm_pixel_x),
        average_bead_fwhm_micron_z=draw(average_bead_fwhm_micron_z),
        average_bead_fwhm_micron_y=draw(average_bead_fwhm_micron_y),
        average_bead_fwhm_micron_x=draw(average_bead_fwhm_micron_x),
        average_bead_fwhm_lateral_asymmetry_ratio=draw(average_bead_fwhm_lateral_asymmetry_ratio),
        average_bead_intensity_integrated=draw(average_bead_intensity_integrated),
        average_bead_intensity_max=draw(average_bead_intensity_max),
        average_bead_intensity_min=draw(average_bead_intensity_min),
    )


@st.composite
def st_mm_psf_beads_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("PSFBeadsAnalysis"),
        key_measurements=st.lists(st_mm_psf_beads_key_measurement(), min_size=1, max_size=3),
    ),
) -> mm_schema.PSFBeadsOutput:
    mm_output = draw(output)
    return mm_schema.PSFBeadsOutput(
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
def st_mm_psf_beads_unprocessed_dataset(
    draw,
    processed=st.just(False),
    input_data=st_mm_psf_beads_input_data(),
    sample=st_mm_psf_beads_sample(),
    input_parameters=st_mm_psf_beads_input_parameters(),
) -> mm_schema.PSFBeadsDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.PSFBeadsDataset,
            processed=processed,
            input_data=input_data,
            sample=sample,
            input_parameters=input_parameters,
        )
    )


@st.composite
def st_mm_psf_beads_processed_dataset(
    draw,
    processed=st.just(True),
    input_data=st_mm_psf_beads_input_data(),
    output=st_mm_psf_beads_output(),
    sample=st_mm_psf_beads_sample(),
    input_parameters=st_mm_psf_beads_input_parameters(),
) -> mm_schema.PSFBeadsDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.PSFBeadsDataset,
            processed=processed,
            input_data=input_data,
            output=output,
            sample=sample,
            input_parameters=input_parameters,
        )
    )
