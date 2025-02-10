from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_image,
    st_mm_dataset,
    st_mm_output,
)


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
    acquisition_datetime=st.datetimes(),
    light_source=st_mm_light_source(),
    sampling_location=st.sampled_from(
        [
            "SOURCE_EXIT",
            "FIBER_EXIT",
            "OBJECTIVE_BACKFOCAL",
            "OBJECTIVE_EXIT",
            "OBJECTIVE_FOCAL",
            "OTHER",
        ]
    ),
    power_set_point=st.floats(min_value=0.0, max_value=1.0),
    power_mw=st.floats(min_value=0.0, max_value=100.0),
    integration_time_ms=st.floats(min_value=0.0, max_value=1000.0),
) -> mm_schema.LightSourcePower:
    return mm_schema.PowerSample(
        acquisition_datetime=draw(acquisition_datetime),
        light_source=draw(light_source),
        sampling_location=draw(sampling_location),
        power_set_point=draw(power_set_point),
        power_mw=draw(power_mw),
        integration_time_ms=draw(integration_time_ms),
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


