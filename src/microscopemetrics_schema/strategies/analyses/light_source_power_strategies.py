from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import (
    st_mm_metrics_object,
    st_mm_dataset,
    st_mm_output,
)


# Light Source Power
@st.composite
def st_mm_light_source(
    draw,
    name=st.text(min_size=1, max_size=32),
    description=st.text(min_size=1, max_size=128),
    wavelength=st.floats(min_value=350.0, max_value=800.0),
) -> mm_schema.LightSource:
    return mm_schema.LightSource(
        name=draw(name),
        description=draw(description),
        wavelength_nm=draw(wavelength),
    )


@st.composite
def st_mm_power_meter(
    draw,
    name=st.text(min_size=1, max_size=32),
    description=st.text(min_size=1, max_size=128),
    manufacturer=st.text(min_size=1, max_size=32),
    model=st.text(min_size=1, max_size=32),
) -> mm_schema.PowerMeter:
    return mm_schema.PowerMeter(
        name=draw(name),
        description=draw(description),
        manufacturer=draw(manufacturer),
        model=draw(model),
    )


@st.composite
def st_mm_light_source_power_measurement(
    draw,
    acquisition_datetime=st.datetimes(),
    light_source=st_mm_light_source(),
    measuring_device=st_mm_power_meter(),
    measuring_location=st.sampled_from(
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
    integration_time_seconds=st.floats(min_value=0.0, max_value=0.5),
) -> mm_schema.LightSourcePower:
    return mm_schema.PowerMeasurement(
        acquisition_datetime=draw(acquisition_datetime),
        light_source=draw(light_source),
        measuring_location=draw(measuring_location),
        power_set_point=draw(power_set_point),
        power_mw=draw(power_mw),
        integration_time_seconds=draw(integration_time_seconds),
    )


@st.composite
def st_mm_light_source_power_input_data(
    draw,
    light_source_power_measurements=st.lists(st_mm_light_source_power_measurement(), min_size=1, max_size=5),
) -> mm_schema.LightSourcePowerInputData:
    return mm_schema.LightSourcePowerInputData(
        power_measurements=draw(light_source_power_measurements),
    )


@st.composite
def st_mm_light_source_power_input_parameters(
    draw,
    short_term_stability_measurement_interval_seconds=st.floats(min_value=1.0, max_value=2.0),
    short_term_stability_required_measurements=st.integers(min_value=3, max_value=20),
    short_term_stability_required_integration_time_seconds=st.floats(min_value=0.01, max_value=0.1),
    long_term_stability_measurement_interval_seconds=st.floats(min_value=10, max_value=60.0),
    long_term_stability_required_measurements=st.integers(min_value=10, max_value=200),
    long_term_stability_required_integration_time_seconds=st.floats(min_value=0.1, max_value=1.0),
) -> mm_schema.LightSourcePowerInputParameters:
    return mm_schema.LightSourcePowerInputParameters(
        short_term_stability_measurement_interval_seconds=draw(short_term_stability_measurement_interval_seconds),
        short_term_stability_required_measurements=draw(short_term_stability_required_measurements),
        short_term_stability_required_integration_time_seconds=draw(short_term_stability_required_integration_time_seconds),
        long_term_stability_measurement_interval_seconds=draw(long_term_stability_measurement_interval_seconds),
        long_term_stability_required_measurements=draw(long_term_stability_required_measurements),
        long_term_stability_required_integration_time_seconds=draw(long_term_stability_required_integration_time_seconds),
    )


@st.composite
def st_mm_light_source_power_output_key_measurements(
    draw,
    light_source=st_mm_light_source(),
    power_meter=st_mm_power_meter(),
    mm_object=st_mm_metrics_object(),
) -> mm_schema.LightSourcePowerKeyMeasurements:
    mm_object = draw(mm_object)
    return mm_schema.LightSourcePowerKeyMeasurements(
        name=mm_object.name,
        description=mm_object.description,
        light_source=draw(light_source),
        measurement_device=draw(power_meter),
        measuring_location="OBJECTIVE_FOCAL",
        nr_of_measurements=100,
        power_mean_mw=25.0,
        power_median_mw=25.0,
        power_std_mw=2.0,
        power_min_mw=20.0,
        power_max_mw=30.0,
        power_linearity=0.95,
        short_term_power_stability=0.9,
        long_term_power_stability=0.9,
    )


@st.composite
def st_mm_light_source_power_output(
    draw,
    output=st_mm_output(
        processing_entity=st.just("LightSourcePowerAnalysis"),
    ),
    key_measurements=st_mm_light_source_power_output_key_measurements(),
) -> mm_schema.LightSourcePowerOutput:
    mm_output = draw(output)
    return mm_schema.LightSourcePowerOutput(
        processing_application=mm_output.processing_application,
        processing_version=mm_output.processing_version,
        processing_entity=mm_output.processing_entity,
        processing_datetime=mm_output.processing_datetime,
        key_measurements=draw(key_measurements),
        processing_log=mm_output.processing_log,
        warnings=mm_output.warnings,
        errors=mm_output.errors,
        comment=mm_output.comment,
    )


@st.composite
def st_mm_light_source_power_unprocessed_dataset(
    draw,
    processed=st.just(False),
    input_data=st_mm_light_source_power_input_data(),
    input_parameters=st_mm_light_source_power_input_parameters(),
) -> mm_schema.LightSourcePowerDataset:
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.LightSourcePowerDataset,
            processed=processed,
            input_data=input_data,
            input_parameters=input_parameters,
        )
    )

@st.composite
def st_mm_light_source_power_processed_dataset(
    draw,
    processed=st.just(True),
    input_data=st_mm_light_source_power_input_data(),
    input_parameters=st_mm_light_source_power_input_parameters(),
    output=st_mm_light_source_power_output(),
) -> mm_schema.LightSourcePowerDataset:
    input_parameters = draw(input_parameters)
    return draw(
        st_mm_dataset(
            target_class=mm_schema.LightSourcePowerDataset,
            processed=processed,
            input_data=input_data,
            input_parameters=input_parameters,
            output=output,
        )
    )


