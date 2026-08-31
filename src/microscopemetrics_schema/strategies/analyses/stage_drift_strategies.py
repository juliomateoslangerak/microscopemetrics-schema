from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_image,
    st_mm_dataset,
    st_mm_output,
    st_mm_roi,
    st_mm_rectangle,
)
from microscopemetrics_schema.strategies.samples.fluorescent_beads_strategies import (
    st_mm_non_psf_beads_sample,
)


@st.composite
def st_mm_stage_drift_input_data(
    draw,
    beads_images=st.lists(st_mm_image(), min_size=1, max_size=3),
    analysis_rois=st.lists(
        st_mm_roi(
            shapes=st.lists(
                st_mm_rectangle(), min_size=1, max_size=1, unique_by=lambda shape: shape.name
            ),
        ),
        min_size=1, max_size=3
    ),
) -> mm_schema.StageDriftInputData:
    return mm_schema.StageDriftInputData(
        beads_images=draw(beads_images),
        analysis_rois=draw(analysis_rois),
    )


@st.composite
def st_mm_stage_drift_input_parameters(
    draw,
    channel_nr=st.just(0),
    reference_frame_nr=st.just(0),
    saturation_threshold=st.just(0.01),
    snr_threshold=st.just(10.0),
) -> mm_schema.StageDriftInputParameters:
    return mm_schema.StageDriftInputParameters(
        channel_nr=draw(channel_nr),
        reference_frame_nr=draw(reference_frame_nr),
        saturation_threshold=draw(saturation_threshold),
        snr_threshold=draw(snr_threshold),
    )

@st.composite
def st_mm_stage_drift_key_measurement(
    draw,
    stabilization_timepoint_x=st.just(0),
    stabilization_timepoint_y=st.just(0),
    stabilization_timepoint_z=st.just(0),
    stabilization_timepoint_3d=st.just(0),
    relative_position_pixel_x_mean=st.just(0.5),
    relative_position_pixel_x_median=st.just(0.5),
    relative_position_pixel_x_std=st.just(0.1),
    relative_position_pixel_y_mean=st.just(0.5),
    relative_position_pixel_y_median=st.just(0.5),
    relative_position_pixel_y_std=st.just(0.1),
    relative_position_pixel_z_mean=st.just(0.5),
    relative_position_pixel_z_median=st.just(0.5),
    relative_position_micron_x_mean=st.just(0.5),
    relative_position_micron_x_median=st.just(0.5),
    relative_position_micron_x_std=st.just(0.5),
    relative_position_micron_y_mean=st.just(0.5),
    relative_position_micron_y_median=st.just(0.5),
    relative_position_micron_y_std=st.just(0.5),
    relative_position_micron_z_mean=st.just(0.5),
    relative_position_micron_z_median=st.just(0.5),
    relative_position_micron_z_std=st.just(0.5),
    displacement_pixel_x_mean=st.just(0.5),
    displacement_pixel_x_median=st.just(0.5),
    displacement_pixel_x_std=st.just(0.5),
    displacement_pixel_y_mean=st.just(0.5),
    displacement_pixel_y_median=st.just(0.5),
    displacement_pixel_y_std=st.just(0.5),
    displacement_pixel_z_mean=st.just(0.5),
    displacement_pixel_z_median=st.just(0.5),
    displacement_micron_x_mean=st.just(0.5),
    displacement_micron_x_median=st.just(0.5),
    displacement_micron_x_std=st.just(0.5),
    displacement_micron_y_mean=st.just(0.5),
    displacement_micron_y_median=st.just(0.5),
    displacement_micron_y_std=st.just(0.5),
    displacement_micron_z_mean=st.just(0.5),
    displacement_micron_z_median=st.just(0.5),
    displacement_micron_z_std=st.just(0.5),
    displacement_micron_3d_mean=st.just(0.5),
    displacement_micron_3d_median=st.just(0.5),
    displacement_micron_3d_std=st.just(0.5),
    velocity_micron_per_sec_x_mean=st.just(0.5),
    velocity_micron_per_sec_x_median=st.just(0.5),
    velocity_micron_per_sec_x_std=st.just(0.5),
    velocity_micron_per_sec_y_mean=st.just(0.5),
    velocity_micron_per_sec_y_median=st.just(0.5),
    velocity_micron_per_sec_y_std=st.just(0.5),
    velocity_micron_per_sec_z_mean=st.just(0.5),
    velocity_micron_per_sec_z_median=st.just(0.5),
    velocity_micron_per_sec_z_std=st.just(0.5),
    velocity_micron_per_sec_3d_mean=st.just(0.5),
    velocity_micron_per_sec_3d_median=st.just(0.5),
    velocity_micron_per_sec_3d_std=st.just(0.5),
    msd_slope_pixel_x=st.just(0.5),
    msd_slope_pixel_y=st.just(0.5),
    msd_slope_pixel_z=st.just(0.5),
    msd_slope_micron_x=st.just(0.5),
    msd_slope_micron_y=st.just(0.5),
    msd_slope_micron_z=st.just(0.5),
    msd_slope_micron_3d=st.just(0.5),
    msd_intercept_pixel_x=st.just(0.5),
    msd_intercept_pixel_y=st.just(0.5),
    msd_intercept_pixel_z=st.just(0.5),
    msd_intercept_micron_x=st.just(0.5),
    msd_intercept_micron_y=st.just(0.5),
    msd_intercept_micron_z=st.just(0.5),
    msd_intercept_micron_3d=st.just(0.5),
    msd_r2_x=st.just(0.5),
    msd_r2_y=st.just(0.5),
    msd_r2_z=st.just(0.5),
    msd_r2_3d=st.just(0.5),
) -> mm_schema.StageDriftKeyMeasurement:
    return mm_schema.StageDriftKeyMeasurement(
        stabilization_timepoint_x=draw(stabilization_timepoint_x),
        stabilization_timepoint_y=draw(stabilization_timepoint_y),
        stabilization_timepoint_z=draw(stabilization_timepoint_z),
        stabilization_timepoint_3d=draw(stabilization_timepoint_3d),
        relative_position_pixel_x_mean=draw(relative_position_pixel_x_mean),
        relative_position_pixel_x_median=draw(relative_position_pixel_x_median),
        relative_position_pixel_x_std=draw(relative_position_pixel_x_std),
        relative_position_pixel_y_mean=draw(relative_position_pixel_y_mean),
        relative_position_pixel_y_median=draw(relative_position_pixel_y_median),
        relative_position_pixel_y_std=draw(relative_position_pixel_y_std),
        relative_position_pixel_z_mean=draw(relative_position_pixel_z_mean),
        relative_position_pixel_z_median=draw(relative_position_pixel_z_median),
        relative_position_micron_x_mean=draw(relative_position_micron_x_mean),
        relative_position_micron_x_median=draw(relative_position_micron_x_median),
        relative_position_micron_x_std=draw(relative_position_micron_x_std),
        relative_position_micron_y_mean=draw(relative_position_micron_y_mean),
        relative_position_micron_y_median=draw(relative_position_micron_y_median),
        relative_position_micron_y_std=draw(relative_position_micron_y_std),
        relative_position_micron_z_mean=draw(relative_position_micron_z_mean),
        relative_position_micron_z_median=draw(relative_position_micron_z_median),
        relative_position_micron_z_std=draw(relative_position_micron_z_std),
        displacement_pixel_x_mean=draw(displacement_pixel_x_mean),
        displacement_pixel_x_median=draw(displacement_pixel_x_median),
        displacement_pixel_x_std=draw(displacement_pixel_x_std),
        displacement_pixel_y_mean=draw(displacement_pixel_y_mean),
        displacement_pixel_y_median=draw(displacement_pixel_y_median),
        displacement_pixel_y_std=draw(displacement_pixel_y_std),
        displacement_pixel_z_mean=draw(displacement_pixel_z_mean),
        displacement_pixel_z_median=draw(displacement_pixel_z_median),
        displacement_micron_x_mean=draw(displacement_micron_x_mean),
        displacement_micron_x_median=draw(displacement_micron_x_median),
        displacement_micron_x_std=draw(displacement_micron_x_std),
        displacement_micron_y_mean=draw(displacement_micron_y_mean),
        displacement_micron_y_median=draw(displacement_micron_y_median),
        displacement_micron_y_std=draw(displacement_micron_y_std),
        displacement_micron_z_mean=draw(displacement_micron_z_mean),
        displacement_micron_z_median=draw(displacement_micron_z_median),
        displacement_micron_z_std=draw(displacement_micron_z_std),
        displacement_micron_3d_mean=draw(displacement_micron_3d_mean),
        displacement_micron_3d_median=draw(displacement_micron_3d_median),
        displacement_micron_3d_std=draw(displacement_micron_3d_std),
        velocity_micron_per_sec_x_mean=draw(velocity_micron_per_sec_x_mean),
        velocity_micron_per_sec_x_median=draw(velocity_micron_per_sec_x_median),
        velocity_micron_per_sec_x_std=draw(velocity_micron_per_sec_x_std),
        velocity_micron_per_sec_y_mean=draw(velocity_micron_per_sec_y_mean),
        velocity_micron_per_sec_y_median=draw(velocity_micron_per_sec_y_median),
        velocity_micron_per_sec_y_std=draw(velocity_micron_per_sec_y_std),
        velocity_micron_per_sec_z_mean=draw(velocity_micron_per_sec_z_mean),
        velocity_micron_per_sec_z_median=draw(velocity_micron_per_sec_z_median),
        velocity_micron_per_sec_z_std=draw(velocity_micron_per_sec_z_std),
        velocity_micron_per_sec_3d_mean=draw(velocity_micron_per_sec_3d_mean),
        velocity_micron_per_sec_3d_median=draw(velocity_micron_per_sec_3d_median),
        velocity_micron_per_sec_3d_std=draw(velocity_micron_per_sec_3d_std),
        msd_slope_pixel_x=draw(msd_slope_pixel_x),
        msd_slope_pixel_y=draw(msd_slope_pixel_y),
        msd_slope_pixel_z=draw(msd_slope_pixel_z),
        msd_slope_micron_x=draw(msd_slope_micron_x),
        msd_slope_micron_y=draw(msd_slope_micron_y),
        msd_slope_micron_z=draw(msd_slope_micron_z),
        msd_slope_micron_3d=draw(msd_slope_micron_3d),
        msd_intercept_pixel_x=draw(msd_intercept_pixel_x),
        msd_intercept_pixel_y=draw(msd_intercept_pixel_y),
        msd_intercept_pixel_z=draw(msd_intercept_pixel_z),
        msd_intercept_micron_x=draw(msd_intercept_micron_x),
        msd_intercept_micron_y=draw(msd_intercept_micron_y),
        msd_intercept_micron_z=draw(msd_intercept_micron_z),
        msd_intercept_micron_3d=draw(msd_intercept_micron_3d),
        msd_r2_x=draw(msd_r2_x),
        msd_r2_y=draw(msd_r2_y),
        msd_r2_z=draw(msd_r2_z),
        msd_r2_3d=draw(msd_r2_3d),
    )


@st.composite
def st_mm_stage_drift_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("StageDriftAnalysis"),
        key_measurements=st.lists(st_mm_stage_drift_key_measurement(), min_size=1, max_size=1),
    ),
) -> mm_schema.StageDriftOutput:
    mm_output = draw(output)
    return mm_schema.StageDriftOutput(
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
def st_mm_stage_drift_unprocessed_dataset(
    draw,
    processed=st.just(False),
    input_data=st_mm_stage_drift_input_data(),
    sample=st_mm_non_psf_beads_sample(),
    input_parameters=st_mm_stage_drift_input_parameters(),
) -> mm_schema.StageDriftDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.StageDriftDataset,
            processed=processed,
            input_data=input_data,
            sample=sample,
            input_parameters=input_parameters,
        )
    )


@st.composite
def st_mm_stage_drift_processed_dataset(
    draw,
    processed=st.just(True),
    input_data=st_mm_stage_drift_input_data(),
    output=st_mm_stage_drift_output(),
    sample=st_mm_non_psf_beads_sample(),
    input_parameters=st_mm_stage_drift_input_parameters(),
) -> mm_schema.StageDriftDataset:
    sample = draw(sample)
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.StageDriftDataset,
            processed=processed,
            input_data=input_data,
            output=output,
            sample=sample,
            input_parameters=input_parameters,
        )
    )
