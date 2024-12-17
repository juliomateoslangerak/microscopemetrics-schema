from microscopemetrics_schema.datamodel import microscopemetrics_schema as mm_schema
from hypothesis import given, assume
from hypothesis import strategies as st
from microscopemetrics_schema.strategies import *

import unittest


class TestCoreSchemaElements(unittest.TestCase):
    """Test the strategies."""
    @given(st_mm_data_reference())
    def test_data_reference(self, data_reference):
        self.assertIsInstance(data_reference, mm_schema.DataReference)

    @given(st_mm_metrics_object())
    def test_metrics_object(self, metrics_object):
        self.assertIsInstance(metrics_object, mm_schema.MetricsObject)

    @given(st_mm_microscope())
    def test_microscope(self, microscope):
        self.assertIsInstance(microscope, mm_schema.Microscope)

    @given(st_mm_experimenter())
    def test_experimenter(self, experimenter):
        self.assertIsInstance(experimenter, mm_schema.Experimenter)

    @given(st_mm_protocol())
    def test_protocol(self, protocol):
        self.assertIsInstance(protocol, mm_schema.Protocol)

    @given(st_mm_sample())
    def test_sample(self, sample):
        self.assertIsInstance(sample, mm_schema.Sample)

    @given(st_mm_comment())
    def test_comment(self, comment):
        self.assertIsInstance(comment, mm_schema.Comment)

    @given(st_mm_dataset(processed=st.just(False)))
    def test_empty_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.MetricsDataset)

    @given(st_mm_dataset(processed=st.just(True)))
    def test_processed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.MetricsDataset)
        self.assertTrue(dataset.processed)
        self.assertIsNotNone(dataset.output)

    @given(st_mm_image())
    def test_image(self, image):
        self.assertIsInstance(image, mm_schema.Image)

    @given(st_mm_color())
    def test_color(self, color):
        self.assertIsInstance(color, mm_schema.Color)

    @given(st_mm_point())
    def test_point(self, point):
        self.assertIsInstance(point, mm_schema.Point)

    @given(st_mm_line())
    def test_line(self, line):
        self.assertIsInstance(line, mm_schema.Line)

    @given(st_mm_rectangle())
    def test_rectangle(self, rectangle):
        self.assertIsInstance(rectangle, mm_schema.Rectangle)

    @given(st_mm_ellipse())
    def test_ellipse(self, ellipse):
        self.assertIsInstance(ellipse, mm_schema.Ellipse)

    @given(st_mm_vertex())
    def test_vertex(self, vertex):
        self.assertIsInstance(vertex, mm_schema.Vertex)

    @given(st_mm_polygon())
    def test_polygon(self, polygon):
        self.assertIsInstance(polygon, mm_schema.Polygon)

    @given(st_mm_shape())
    def test_shape(self, shape):
        self.assertIsInstance(shape, mm_schema.Shape)

    @given(st_mm_roi())
    def test_roi(self, roi):
        self.assertIsInstance(roi, mm_schema.Roi)

    @given(st_mm_key_values())
    def test_key_values(self, key_values):
        """Test the key_values strategy."""
        self.assertIsInstance(key_values, mm_schema.KeyValues)

    @given(st_mm_tag())
    def test_tag(self, tag):
        """Test the tag strategy."""
        self.assertIsInstance(tag, mm_schema.Tag)


class TestFieldIlluminationSchemaElements(unittest.TestCase):
    """Test the strategies for the FieldIllumination schema elements."""

    @given(st_mm_field_illumination_unprocessed_dataset())
    def test_field_illumination_unprocessed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.FieldIlluminationDataset)
        self.assertFalse(dataset.processed)

    @given(st_mm_field_illumination_processed_dataset())
    def test_field_illumination_processed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.FieldIlluminationDataset)
        self.assertTrue(dataset.processed)


class TestPSFBeadsSchemaElements(unittest.TestCase):
    """Test the strategies for the PSFBeads schema elements."""

    @given(st_mm_psf_beads_unprocessed_dataset())
    def test_psf_beads_unprocessed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.PSFBeadsDataset)
        self.assertFalse(dataset.processed)

    @given(st_mm_psf_beads_processed_dataset())
    def test_psf_beads_processed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.PSFBeadsDataset)
        self.assertTrue(dataset.processed)


class TestUserExperimentSchemaElements(unittest.TestCase):
    """Test the strategies for the UserExperiment schema elements."""

    @given(st_mm_user_experiment_unprocessed_dataset())
    def test_user_experiment_unprocessed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.UserExperimentDataset)
        self.assertFalse(dataset.processed)

    @given(st_mm_user_experiment_processed_dataset())
    def test_user_experiment_processed_dataset(self, dataset):
        self.assertIsInstance(dataset, mm_schema.UserExperimentDataset)
        self.assertTrue(dataset.processed)