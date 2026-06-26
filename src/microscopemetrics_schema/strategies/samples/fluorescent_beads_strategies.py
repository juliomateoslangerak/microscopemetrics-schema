from hypothesis import strategies as st
from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from microscopemetrics_schema.strategies import st_mm_sample


@st.composite
def st_mm_psf_beads_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.PSFBeads:
    nr_wavelengths = draw(st.integers(min_value=1, max_value=3))

    return mm_schema.PSFBeads(
        bead_diameter_micron=draw(st.floats(min_value=0.1, max_value=0.5)),
        excitation_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        emission_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        **draw(sample)._as_dict,
    )


@st.composite
def st_mm_non_psf_beads_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.NonPSFBeads:
    nr_wavelengths = draw(st.integers(min_value=1, max_value=3))

    return mm_schema.NonPSFBeads(
        bead_diameter_micron=draw(st.floats(min_value=0.1, max_value=0.5)),
        excitation_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        emission_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        **draw(sample)._as_dict,
    )


@st.composite
def st_mm_multi_wavelength_beads_sample(
    draw,
    sample=st_mm_sample(),
) -> mm_schema.MultiWavelengthBeads:
    nr_wavelengths = draw(st.integers(min_value=1, max_value=3))

    return mm_schema.MultiWavelengthBeads(
        bead_diameter_micron=draw(st.floats(min_value=0.1, max_value=0.5)),
        excitation_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        emission_wavelengths_nm=draw(
            st.lists(st.floats(min_value=400, max_value=700), min_size=nr_wavelengths, max_size=nr_wavelengths)
        ),
        **draw(sample)._as_dict,
    )

