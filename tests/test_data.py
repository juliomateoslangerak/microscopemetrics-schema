"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from microscopemetrics_schema.datamodel.microscopemetrics_schema import (
    MetricsDataset,
    PSFBeadsDataset,
    FieldIlluminationDataset,
    # ArgolightBDataset,
)

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_MetricsDataset(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            if "MetricsDataset" in path:
                obj = yaml_loader.load(path, target_class=MetricsDataset)
                assert obj

    def test_FieldIlluminationDataset(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            if "FieldIlluminationDataset" in path:
                obj = yaml_loader.load(path, target_class=FieldIlluminationDataset)
                assert obj

    # def test_ArgolightBDataset(self):
    #     """Data test."""
    #     for path in EXAMPLE_FILES:
    #         if "ArgolightBDataset" in path:
    #             obj = yaml_loader.load(path, target_class=ArgolightBDataset)
    #             assert obj
