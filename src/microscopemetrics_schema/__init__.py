"""microscopemetrics-schema.

A schema for microscope-metrics, a python package for microscope QC
"""

try:
    from microscopemetrics_schema._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
