# Auto generated from microscopemetrics_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-06-14T15:58:56
# Schema: microscopemetrics-schema
#
# id: https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema
# description: A schema for microscope-metrics, a python package for microscope QC
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MICROSCOPEMETRICS_SCHEMA = CurieNamespace('microscopemetrics_schema', 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/')
DEFAULT_ = MICROSCOPEMETRICS_SCHEMA


# Types

# Class references
class ProtocolUrl(extended_str):
    pass


class ExperimenterOrcid(extended_str):
    pass


MetaObject = Any

@dataclass
class NamedObject(YAMLRoot):
    """
    An object with a name and a description
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/NamedObject"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/NamedObject"
    class_name: ClassVar[str] = "NamedObject"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.NamedObject

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class DataReference(YAMLRoot):
    """
    A reference to a data resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/DataReference"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/DataReference"
    class_name: ClassVar[str] = "DataReference"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.DataReference

    data_uri: Optional[str] = None
    omero_host: Optional[str] = None
    omero_port: Optional[int] = None
    omero_object_type: Optional[Union[str, "OMEROObjectTypeEnum"]] = None
    omero_object_id: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.data_uri is not None and not isinstance(self.data_uri, str):
            self.data_uri = str(self.data_uri)

        if self.omero_host is not None and not isinstance(self.omero_host, str):
            self.omero_host = str(self.omero_host)

        if self.omero_port is not None and not isinstance(self.omero_port, int):
            self.omero_port = int(self.omero_port)

        if self.omero_object_type is not None and not isinstance(self.omero_object_type, OMEROObjectTypeEnum):
            self.omero_object_type = OMEROObjectTypeEnum(self.omero_object_type)

        if self.omero_object_id is not None and not isinstance(self.omero_object_id, int):
            self.omero_object_id = int(self.omero_object_id)

        super().__post_init__(**kwargs)


@dataclass
class MetricsObject(NamedObject):
    """
    A base object for all microscope-metrics objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsObject"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsObject"
    class_name: ClassVar[str] = "MetricsObject"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsObject

    data_reference: Optional[Union[dict, DataReference]] = None
    linked_references: Optional[Union[Union[dict, DataReference], List[Union[dict, DataReference]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.data_reference is not None and not isinstance(self.data_reference, DataReference):
            self.data_reference = DataReference(**as_dict(self.data_reference))

        if not isinstance(self.linked_references, list):
            self.linked_references = [self.linked_references] if self.linked_references is not None else []
        self.linked_references = [v if isinstance(v, DataReference) else DataReference(**as_dict(v)) for v in self.linked_references]

        super().__post_init__(**kwargs)


@dataclass
class MicroscopeCollection(YAMLRoot):
    """
    A collection of microscopes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MicroscopeCollection"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MicroscopeCollection"
    class_name: ClassVar[str] = "MicroscopeCollection"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MicroscopeCollection

    microscopes: Union[Union[dict, "Microscope"], List[Union[dict, "Microscope"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.microscopes):
            self.MissingRequiredField("microscopes")
        if not isinstance(self.microscopes, list):
            self.microscopes = [self.microscopes] if self.microscopes is not None else []
        self.microscopes = [v if isinstance(v, Microscope) else Microscope(**as_dict(v)) for v in self.microscopes]

        super().__post_init__(**kwargs)


@dataclass
class Microscope(MetricsObject):
    """
    A microscope
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Microscope"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Microscope"
    class_name: ClassVar[str] = "Microscope"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Microscope

    type: Optional[Union[str, "MicroscopeTypeEnum"]] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    comments: Optional[Union[Union[dict, "Comment"], List[Union[dict, "Comment"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, MicroscopeTypeEnum):
            self.type = MicroscopeTypeEnum(self.type)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        self._normalize_inlined_as_dict(slot_name="comments", slot_type=Comment, key_name="datetime", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedObject):
    """
    A sample is a standard physical object that is imaged by a microscope
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Sample"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Sample

    type: str = None
    protocol: Union[str, ProtocolUrl] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.protocol):
            self.MissingRequiredField("protocol")
        if not isinstance(self.protocol, ProtocolUrl):
            self.protocol = ProtocolUrl(self.protocol)

        super().__post_init__(**kwargs)


@dataclass
class Protocol(NamedObject):
    """
    Set of instructions for preparing and imaging a sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Protocol"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Protocol

    url: Union[str, ProtocolUrl] = None
    version: str = None
    authors: Optional[Union[Union[str, ExperimenterOrcid], List[Union[str, ExperimenterOrcid]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, ProtocolUrl):
            self.url = ProtocolUrl(self.url)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, ExperimenterOrcid) else ExperimenterOrcid(v) for v in self.authors]

        super().__post_init__(**kwargs)


@dataclass
class Experimenter(YAMLRoot):
    """
    The person that performed the experiment or developed the protocol
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Experimenter"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Experimenter"
    class_name: ClassVar[str] = "Experimenter"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Experimenter

    orcid: Union[str, ExperimenterOrcid] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.orcid):
            self.MissingRequiredField("orcid")
        if not isinstance(self.orcid, ExperimenterOrcid):
            self.orcid = ExperimenterOrcid(self.orcid)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Comment(YAMLRoot):
    """
    A comment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Comment"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Comment"
    class_name: ClassVar[str] = "Comment"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Comment

    datetime: Union[str, XSDDateTime] = None
    comment_type: Union[str, "CommentTypesEnum"] = None
    text: str = None
    author: Optional[Union[str, ExperimenterOrcid]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datetime):
            self.MissingRequiredField("datetime")
        if not isinstance(self.datetime, XSDDateTime):
            self.datetime = XSDDateTime(self.datetime)

        if self._is_empty(self.comment_type):
            self.MissingRequiredField("comment_type")
        if not isinstance(self.comment_type, CommentTypesEnum):
            self.comment_type = CommentTypesEnum(self.comment_type)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.author is not None and not isinstance(self.author, ExperimenterOrcid):
            self.author = ExperimenterOrcid(self.author)

        super().__post_init__(**kwargs)


@dataclass
class MetricsDatasetCollection(MetricsObject):
    """
    A collection of microscope-metrics datasets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsDatasetCollection"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsDatasetCollection"
    class_name: ClassVar[str] = "MetricsDatasetCollection"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsDatasetCollection

    datasets: Optional[Union[Union[dict, "MetricsDataset"], List[Union[dict, "MetricsDataset"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, MetricsDataset) else MetricsDataset(**as_dict(v)) for v in self.datasets]

        super().__post_init__(**kwargs)


@dataclass
class HarmonizedMetricsDatasetCollection(MetricsDatasetCollection):
    """
    A collection of harmonized microscope-metrics datasets. All of the datasets in the collection share the same
    analysis and processing parameters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/HarmonizedMetricsDatasetCollection"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/HarmonizedMetricsDatasetCollection"
    class_name: ClassVar[str] = "HarmonizedMetricsDatasetCollection"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.HarmonizedMetricsDatasetCollection

    dataset_class: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dataset_class):
            self.MissingRequiredField("dataset_class")
        if not isinstance(self.dataset_class, str):
            self.dataset_class = str(self.dataset_class)

        super().__post_init__(**kwargs)


@dataclass
class MetricsDataset(MetricsObject):
    """
    A base object on which microscope-metrics runs the analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsDataset"
    class_name: ClassVar[str] = "MetricsDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsDataset

    microscope: Union[dict, Microscope] = None
    input: Union[dict, "MetricsInput"] = None
    processed: Union[bool, Bool] = False
    sample: Optional[Union[dict, Sample]] = None
    experimenter: Optional[Union[str, ExperimenterOrcid]] = None
    acquisition_datetime: Optional[Union[str, XSDDateTime]] = None
    output: Optional[Union[dict, "MetricsOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.microscope):
            self.MissingRequiredField("microscope")
        if not isinstance(self.microscope, Microscope):
            self.microscope = Microscope(**as_dict(self.microscope))

        if self._is_empty(self.processed):
            self.MissingRequiredField("processed")
        if not isinstance(self.processed, Bool):
            self.processed = Bool(self.processed)

        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, MetricsInput):
            self.input = MetricsInput()

        if self.sample is not None and not isinstance(self.sample, Sample):
            self.sample = Sample(**as_dict(self.sample))

        if self.experimenter is not None and not isinstance(self.experimenter, ExperimenterOrcid):
            self.experimenter = ExperimenterOrcid(self.experimenter)

        if self.acquisition_datetime is not None and not isinstance(self.acquisition_datetime, XSDDateTime):
            self.acquisition_datetime = XSDDateTime(self.acquisition_datetime)

        if self.output is not None and not isinstance(self.output, MetricsOutput):
            self.output = MetricsOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


class MetricsInput(YAMLRoot):
    """
    An abstract class for analysis inputs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsInput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsInput"
    class_name: ClassVar[str] = "MetricsInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsInput


@dataclass
class MetricsOutput(YAMLRoot):
    """
    An abstract class for analysis outputs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsOutput"
    class_name: ClassVar[str] = "MetricsOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsOutput

    processing_application: Union[str, List[str]] = None
    processing_version: Union[str, List[str]] = None
    processing_datetime: Union[str, XSDDateTime] = None
    validated: Union[bool, Bool] = False
    processing_entity: Optional[Union[str, List[str]]] = empty_list()
    processing_log: Optional[str] = None
    warnings: Optional[Union[str, List[str]]] = empty_list()
    errors: Optional[Union[str, List[str]]] = empty_list()
    validation_datetime: Optional[Union[str, XSDDateTime]] = None
    comment: Optional[Union[dict, Comment]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.processing_application):
            self.MissingRequiredField("processing_application")
        if not isinstance(self.processing_application, list):
            self.processing_application = [self.processing_application] if self.processing_application is not None else []
        self.processing_application = [v if isinstance(v, str) else str(v) for v in self.processing_application]

        if self._is_empty(self.processing_version):
            self.MissingRequiredField("processing_version")
        if not isinstance(self.processing_version, list):
            self.processing_version = [self.processing_version] if self.processing_version is not None else []
        self.processing_version = [v if isinstance(v, str) else str(v) for v in self.processing_version]

        if self._is_empty(self.processing_datetime):
            self.MissingRequiredField("processing_datetime")
        if not isinstance(self.processing_datetime, XSDDateTime):
            self.processing_datetime = XSDDateTime(self.processing_datetime)

        if self._is_empty(self.validated):
            self.MissingRequiredField("validated")
        if not isinstance(self.validated, Bool):
            self.validated = Bool(self.validated)

        if not isinstance(self.processing_entity, list):
            self.processing_entity = [self.processing_entity] if self.processing_entity is not None else []
        self.processing_entity = [v if isinstance(v, str) else str(v) for v in self.processing_entity]

        if self.processing_log is not None and not isinstance(self.processing_log, str):
            self.processing_log = str(self.processing_log)

        if not isinstance(self.warnings, list):
            self.warnings = [self.warnings] if self.warnings is not None else []
        self.warnings = [v if isinstance(v, str) else str(v) for v in self.warnings]

        if not isinstance(self.errors, list):
            self.errors = [self.errors] if self.errors is not None else []
        self.errors = [v if isinstance(v, str) else str(v) for v in self.errors]

        if self.validation_datetime is not None and not isinstance(self.validation_datetime, XSDDateTime):
            self.validation_datetime = XSDDateTime(self.validation_datetime)

        if self.comment is not None and not isinstance(self.comment, Comment):
            self.comment = Comment(**as_dict(self.comment))

        super().__post_init__(**kwargs)


@dataclass
class Image(MetricsObject):
    """
    A microscope-metrics image
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Image"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Image

    shape_x: int = None
    shape_y: int = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1
    voxel_size_x_micron: Optional[float] = None
    voxel_size_y_micron: Optional[float] = None
    voxel_size_z_micron: Optional[float] = None
    time_series: Optional[Union[dict, "TimeSeries"]] = None
    channel_series: Optional[Union[dict, "ChannelSeries"]] = None
    acquisition_datetime: Optional[Union[str, XSDDateTime]] = None
    source_images: Optional[Union[Union[dict, DataReference], List[Union[dict, DataReference]]]] = empty_list()
    array_data: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.shape_x):
            self.MissingRequiredField("shape_x")
        if not isinstance(self.shape_x, int):
            self.shape_x = int(self.shape_x)

        if self._is_empty(self.shape_y):
            self.MissingRequiredField("shape_y")
        if not isinstance(self.shape_y, int):
            self.shape_y = int(self.shape_y)

        if self._is_empty(self.shape_z):
            self.MissingRequiredField("shape_z")
        if not isinstance(self.shape_z, int):
            self.shape_z = int(self.shape_z)

        if self._is_empty(self.shape_c):
            self.MissingRequiredField("shape_c")
        if not isinstance(self.shape_c, int):
            self.shape_c = int(self.shape_c)

        if self._is_empty(self.shape_t):
            self.MissingRequiredField("shape_t")
        if not isinstance(self.shape_t, int):
            self.shape_t = int(self.shape_t)

        if self.voxel_size_x_micron is not None and not isinstance(self.voxel_size_x_micron, float):
            self.voxel_size_x_micron = float(self.voxel_size_x_micron)

        if self.voxel_size_y_micron is not None and not isinstance(self.voxel_size_y_micron, float):
            self.voxel_size_y_micron = float(self.voxel_size_y_micron)

        if self.voxel_size_z_micron is not None and not isinstance(self.voxel_size_z_micron, float):
            self.voxel_size_z_micron = float(self.voxel_size_z_micron)

        if self.time_series is not None and not isinstance(self.time_series, TimeSeries):
            self.time_series = TimeSeries(**as_dict(self.time_series))

        if self.channel_series is not None and not isinstance(self.channel_series, ChannelSeries):
            self.channel_series = ChannelSeries(**as_dict(self.channel_series))

        if self.acquisition_datetime is not None and not isinstance(self.acquisition_datetime, XSDDateTime):
            self.acquisition_datetime = XSDDateTime(self.acquisition_datetime)

        if not isinstance(self.source_images, list):
            self.source_images = [self.source_images] if self.source_images is not None else []
        self.source_images = [v if isinstance(v, DataReference) else DataReference(**as_dict(v)) for v in self.source_images]

        super().__post_init__(**kwargs)


@dataclass
class ImageMask(Image):
    """
    A mask image. Either a binary image or a label image
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ImageMask"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ImageMask"
    class_name: ClassVar[str] = "ImageMask"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ImageMask

    shape_x: int = None
    shape_y: int = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1

@dataclass
class ChannelSeries(YAMLRoot):
    """
    A series representing channels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ChannelSeries"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ChannelSeries"
    class_name: ClassVar[str] = "ChannelSeries"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ChannelSeries

    channels: Union[Union[dict, "Channel"], List[Union[dict, "Channel"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.channels):
            self.MissingRequiredField("channels")
        if not isinstance(self.channels, list):
            self.channels = [self.channels] if self.channels is not None else []
        self.channels = [v if isinstance(v, Channel) else Channel(**as_dict(v)) for v in self.channels]

        super().__post_init__(**kwargs)


@dataclass
class Channel(NamedObject):
    """
    A image channel
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Channel"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Channel"
    class_name: ClassVar[str] = "Channel"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Channel

    excitation_wavelength_nm: Optional[float] = None
    emission_wavelength_nm: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.excitation_wavelength_nm is not None and not isinstance(self.excitation_wavelength_nm, float):
            self.excitation_wavelength_nm = float(self.excitation_wavelength_nm)

        if self.emission_wavelength_nm is not None and not isinstance(self.emission_wavelength_nm, float):
            self.emission_wavelength_nm = float(self.emission_wavelength_nm)

        super().__post_init__(**kwargs)


@dataclass
class TimeSeries(YAMLRoot):
    """
    A series whose values represent time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/TimeSeries"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/TimeSeries"
    class_name: ClassVar[str] = "TimeSeries"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.TimeSeries

    values: Union[float, List[float]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass
class Column(NamedObject):
    """
    Attributes of a column
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Column"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Column"
    class_name: ClassVar[str] = "Column"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Column

    data_type: str = "str"
    source_reference: Optional[Union[dict, DataReference]] = None
    values: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.data_type):
            self.MissingRequiredField("data_type")
        if not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        if self.source_reference is not None and not isinstance(self.source_reference, DataReference):
            self.source_reference = DataReference(**as_dict(self.source_reference))

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass
class Roi(MetricsObject):
    """
    A ROI (Region Of Interest). Collection of shapes and an image to which they are applied
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Roi"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Roi"
    class_name: ClassVar[str] = "Roi"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Roi

    points: Optional[Union[Union[dict, "Point"], List[Union[dict, "Point"]]]] = empty_list()
    lines: Optional[Union[Union[dict, "Line"], List[Union[dict, "Line"]]]] = empty_list()
    rectangles: Optional[Union[Union[dict, "Rectangle"], List[Union[dict, "Rectangle"]]]] = empty_list()
    ellipses: Optional[Union[Union[dict, "Ellipse"], List[Union[dict, "Ellipse"]]]] = empty_list()
    polygons: Optional[Union[Union[dict, "Polygon"], List[Union[dict, "Polygon"]]]] = empty_list()
    masks: Optional[Union[Union[dict, "Mask"], List[Union[dict, "Mask"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.points, list):
            self.points = [self.points] if self.points is not None else []
        self.points = [v if isinstance(v, Point) else Point(**as_dict(v)) for v in self.points]

        if not isinstance(self.lines, list):
            self.lines = [self.lines] if self.lines is not None else []
        self.lines = [v if isinstance(v, Line) else Line(**as_dict(v)) for v in self.lines]

        if not isinstance(self.rectangles, list):
            self.rectangles = [self.rectangles] if self.rectangles is not None else []
        self.rectangles = [v if isinstance(v, Rectangle) else Rectangle(**as_dict(v)) for v in self.rectangles]

        if not isinstance(self.ellipses, list):
            self.ellipses = [self.ellipses] if self.ellipses is not None else []
        self.ellipses = [v if isinstance(v, Ellipse) else Ellipse(**as_dict(v)) for v in self.ellipses]

        if not isinstance(self.polygons, list):
            self.polygons = [self.polygons] if self.polygons is not None else []
        self.polygons = [v if isinstance(v, Polygon) else Polygon(**as_dict(v)) for v in self.polygons]

        if not isinstance(self.masks, list):
            self.masks = [self.masks] if self.masks is not None else []
        self.masks = [v if isinstance(v, Mask) else Mask(**as_dict(v)) for v in self.masks]

        super().__post_init__(**kwargs)


@dataclass
class Shape(NamedObject):
    """
    A shape
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Shape"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Shape

    z: Optional[float] = None
    c: Optional[int] = None
    t: Optional[int] = None
    fill_color: Optional[Union[dict, "Color"]] = None
    stroke_color: Optional[Union[dict, "Color"]] = None
    stroke_width: Optional[int] = 1

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.z is not None and not isinstance(self.z, float):
            self.z = float(self.z)

        if self.c is not None and not isinstance(self.c, int):
            self.c = int(self.c)

        if self.t is not None and not isinstance(self.t, int):
            self.t = int(self.t)

        if self.fill_color is not None and not isinstance(self.fill_color, Color):
            self.fill_color = Color(**as_dict(self.fill_color))

        if self.stroke_color is not None and not isinstance(self.stroke_color, Color):
            self.stroke_color = Color(**as_dict(self.stroke_color))

        if self.stroke_width is not None and not isinstance(self.stroke_width, int):
            self.stroke_width = int(self.stroke_width)

        super().__post_init__(**kwargs)


@dataclass
class Point(Shape):
    """
    A point as defined by x and y coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Point"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Point"
    class_name: ClassVar[str] = "Point"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Point

    y: float = None
    x: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        super().__post_init__(**kwargs)


@dataclass
class Line(Shape):
    """
    A line as defined by x1, y1, x2, y2 coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Line"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Line"
    class_name: ClassVar[str] = "Line"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Line

    x1: float = None
    y1: float = None
    x2: float = None
    y2: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.x1):
            self.MissingRequiredField("x1")
        if not isinstance(self.x1, float):
            self.x1 = float(self.x1)

        if self._is_empty(self.y1):
            self.MissingRequiredField("y1")
        if not isinstance(self.y1, float):
            self.y1 = float(self.y1)

        if self._is_empty(self.x2):
            self.MissingRequiredField("x2")
        if not isinstance(self.x2, float):
            self.x2 = float(self.x2)

        if self._is_empty(self.y2):
            self.MissingRequiredField("y2")
        if not isinstance(self.y2, float):
            self.y2 = float(self.y2)

        super().__post_init__(**kwargs)


@dataclass
class Rectangle(Shape):
    """
    A rectangle as defined by x, y coordinates and width, height
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Rectangle"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Rectangle"
    class_name: ClassVar[str] = "Rectangle"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Rectangle

    x: float = None
    y: float = None
    w: float = None
    h: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.w):
            self.MissingRequiredField("w")
        if not isinstance(self.w, float):
            self.w = float(self.w)

        if self._is_empty(self.h):
            self.MissingRequiredField("h")
        if not isinstance(self.h, float):
            self.h = float(self.h)

        super().__post_init__(**kwargs)


@dataclass
class Ellipse(Shape):
    """
    An ellipse as defined by x, y coordinates and x and y radii
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Ellipse"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Ellipse"
    class_name: ClassVar[str] = "Ellipse"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Ellipse

    x: float = None
    y: float = None
    x_rad: float = None
    y_rad: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.x_rad):
            self.MissingRequiredField("x_rad")
        if not isinstance(self.x_rad, float):
            self.x_rad = float(self.x_rad)

        if self._is_empty(self.y_rad):
            self.MissingRequiredField("y_rad")
        if not isinstance(self.y_rad, float):
            self.y_rad = float(self.y_rad)

        super().__post_init__(**kwargs)


@dataclass
class Polygon(Shape):
    """
    A polygon as defined by a series of vertexes and a boolean to indicate if closed or not
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Polygon"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Polygon"
    class_name: ClassVar[str] = "Polygon"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Polygon

    vertexes: Union[Union[dict, "Vertex"], List[Union[dict, "Vertex"]]] = None
    is_open: Union[bool, Bool] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vertexes):
            self.MissingRequiredField("vertexes")
        self._normalize_inlined_as_dict(slot_name="vertexes", slot_type=Vertex, key_name="x", keyed=False)

        if self._is_empty(self.is_open):
            self.MissingRequiredField("is_open")
        if not isinstance(self.is_open, Bool):
            self.is_open = Bool(self.is_open)

        super().__post_init__(**kwargs)


@dataclass
class Vertex(YAMLRoot):
    """
    A vertex as defined by x and y coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Vertex"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Vertex"
    class_name: ClassVar[str] = "Vertex"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Vertex

    x: float = None
    y: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        super().__post_init__(**kwargs)


@dataclass
class Mask(Shape):
    """
    A mask as defined by a boolean image
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Mask"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Mask"
    class_name: ClassVar[str] = "Mask"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Mask

    y: int = 0
    x: int = 0
    mask: Optional[Union[dict, ImageMask]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, int):
            self.y = int(self.y)

        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, int):
            self.x = int(self.x)

        if self.mask is not None and not isinstance(self.mask, ImageMask):
            self.mask = ImageMask(**as_dict(self.mask))

        super().__post_init__(**kwargs)


@dataclass
class Color(YAMLRoot):
    """
    A color as defined by RGB values and an optional alpha value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Color"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Color"
    class_name: ClassVar[str] = "Color"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Color

    r: int = 128
    g: int = 128
    b: int = 128
    alpha: Optional[int] = 255

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.r):
            self.MissingRequiredField("r")
        if not isinstance(self.r, int):
            self.r = int(self.r)

        if self._is_empty(self.g):
            self.MissingRequiredField("g")
        if not isinstance(self.g, int):
            self.g = int(self.g)

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, int):
            self.b = int(self.b)

        if self.alpha is not None and not isinstance(self.alpha, int):
            self.alpha = int(self.alpha)

        super().__post_init__(**kwargs)


class CentersOfMass(YAMLRoot):
    """
    The center of mass of detected objects. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/CentersOfMass"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/CentersOfMass"
    class_name: ClassVar[str] = "CentersOfMass"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.CentersOfMass


class CentersGeometric(YAMLRoot):
    """
    The geometric center of detected objects. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/CentersGeometric"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/CentersGeometric"
    class_name: ClassVar[str] = "CentersGeometric"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.CentersGeometric


class CentersFitted(YAMLRoot):
    """
    The fitted center of detected objects. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/CentersFitted"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/CentersFitted"
    class_name: ClassVar[str] = "CentersFitted"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.CentersFitted


class CentersMaxIntensity(YAMLRoot):
    """
    The position of maximum intensity of detected objects. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/CentersMaxIntensity"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/CentersMaxIntensity"
    class_name: ClassVar[str] = "CentersMaxIntensity"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.CentersMaxIntensity


@dataclass
class ProfilesIntensity(YAMLRoot):
    """
    Profiles computed on the image. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ProfilesIntensity"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ProfilesIntensity"
    class_name: ClassVar[str] = "ProfilesIntensity"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ProfilesIntensity

    intensity_profiles_table: Optional[Union[dict, "Table"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.intensity_profiles_table is not None and not isinstance(self.intensity_profiles_table, Table):
            self.intensity_profiles_table = Table(**as_dict(self.intensity_profiles_table))

        super().__post_init__(**kwargs)


@dataclass
class RoiMeasurements(YAMLRoot):
    """
    Measurements computed on the ROIs of an image. Intended to be used with ROIs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/RoiMeasurements"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/RoiMeasurements"
    class_name: ClassVar[str] = "RoiMeasurements"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.RoiMeasurements

    measurements_table: Optional[Union[dict, "Table"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurements_table is not None and not isinstance(self.measurements_table, Table):
            self.measurements_table = Table(**as_dict(self.measurements_table))

        super().__post_init__(**kwargs)


class KeyValues(MetricsObject):
    """
    A collection of key-value pairs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/KeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/KeyValues"
    class_name: ClassVar[str] = "KeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.KeyValues


class KeyMeasurements(KeyValues):
    """
    A table of key measurements
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/KeyMeasurements"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/KeyMeasurements"
    class_name: ClassVar[str] = "KeyMeasurements"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.KeyMeasurements


@dataclass
class Tag(MetricsObject):
    """
    A tag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Tag"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Tag"
    class_name: ClassVar[str] = "Tag"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Tag

    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Table(MetricsObject):
    """
    A microscope-metrics table
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Table"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Table"
    class_name: ClassVar[str] = "Table"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Table

    columns: Union[Union[dict, Column], List[Union[dict, Column]]] = None
    table_data: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.columns):
            self.MissingRequiredField("columns")
        if not isinstance(self.columns, list):
            self.columns = [self.columns] if self.columns is not None else []
        self.columns = [v if isinstance(v, Column) else Column(**as_dict(v)) for v in self.columns]

        super().__post_init__(**kwargs)


@dataclass
class FieldIlluminationDataset(MetricsDataset):
    """
    A field illumination dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/field_illumination_schema/FieldIlluminationDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/field_illumination_schema/FieldIlluminationDataset"
    class_name: ClassVar[str] = "FieldIlluminationDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.FieldIlluminationDataset

    microscope: Union[dict, Microscope] = None
    processed: Union[bool, Bool] = False
    input: Optional[Union[dict, "FieldIlluminationInput"]] = None
    output: Optional[Union[dict, "FieldIlluminationOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, FieldIlluminationInput):
            self.input = FieldIlluminationInput(**as_dict(self.input))

        if self.output is not None and not isinstance(self.output, FieldIlluminationOutput):
            self.output = FieldIlluminationOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


@dataclass
class FieldIlluminationInput(MetricsInput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/field_illumination_schema/FieldIlluminationInput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/field_illumination_schema/FieldIlluminationInput"
    class_name: ClassVar[str] = "FieldIlluminationInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.FieldIlluminationInput

    field_illumination_image: Union[Union[dict, Image], List[Union[dict, Image]]] = None
    saturation_threshold: float = 0.01
    corner_fraction: float = 0.1
    sigma: float = 5.0
    bit_depth: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.field_illumination_image):
            self.MissingRequiredField("field_illumination_image")
        if not isinstance(self.field_illumination_image, list):
            self.field_illumination_image = [self.field_illumination_image] if self.field_illumination_image is not None else []
        self.field_illumination_image = [v if isinstance(v, Image) else Image(**as_dict(v)) for v in self.field_illumination_image]

        if self._is_empty(self.saturation_threshold):
            self.MissingRequiredField("saturation_threshold")
        if not isinstance(self.saturation_threshold, float):
            self.saturation_threshold = float(self.saturation_threshold)

        if self._is_empty(self.corner_fraction):
            self.MissingRequiredField("corner_fraction")
        if not isinstance(self.corner_fraction, float):
            self.corner_fraction = float(self.corner_fraction)

        if self._is_empty(self.sigma):
            self.MissingRequiredField("sigma")
        if not isinstance(self.sigma, float):
            self.sigma = float(self.sigma)

        if self.bit_depth is not None and not isinstance(self.bit_depth, int):
            self.bit_depth = int(self.bit_depth)

        super().__post_init__(**kwargs)


@dataclass
class FieldIlluminationOutput(MetricsOutput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/field_illumination_schema/FieldIlluminationOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/field_illumination_schema/FieldIlluminationOutput"
    class_name: ClassVar[str] = "FieldIlluminationOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.FieldIlluminationOutput

    processing_application: Union[str, List[str]] = None
    processing_version: Union[str, List[str]] = None
    processing_datetime: Union[str, XSDDateTime] = None
    validated: Union[bool, Bool] = False
    key_values: Optional[Union[dict, "FieldIlluminationKeyValues"]] = None
    intensity_profiles: Optional[Union[Union[dict, Table], List[Union[dict, Table]]]] = empty_list()
    roi_profiles: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    roi_corners: Optional[Union[dict, Roi]] = None
    roi_centers_of_mass: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    roi_centers_geometric: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    roi_centers_fitted: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    roi_centers_max_intensity: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    roi_center_region: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key_values is not None and not isinstance(self.key_values, FieldIlluminationKeyValues):
            self.key_values = FieldIlluminationKeyValues(**as_dict(self.key_values))

        if not isinstance(self.intensity_profiles, list):
            self.intensity_profiles = [self.intensity_profiles] if self.intensity_profiles is not None else []
        self.intensity_profiles = [v if isinstance(v, Table) else Table(**as_dict(v)) for v in self.intensity_profiles]

        if not isinstance(self.roi_profiles, list):
            self.roi_profiles = [self.roi_profiles] if self.roi_profiles is not None else []
        self.roi_profiles = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_profiles]

        if self.roi_corners is not None and not isinstance(self.roi_corners, Roi):
            self.roi_corners = Roi(**as_dict(self.roi_corners))

        if not isinstance(self.roi_centers_of_mass, list):
            self.roi_centers_of_mass = [self.roi_centers_of_mass] if self.roi_centers_of_mass is not None else []
        self.roi_centers_of_mass = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_centers_of_mass]

        if not isinstance(self.roi_centers_geometric, list):
            self.roi_centers_geometric = [self.roi_centers_geometric] if self.roi_centers_geometric is not None else []
        self.roi_centers_geometric = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_centers_geometric]

        if not isinstance(self.roi_centers_fitted, list):
            self.roi_centers_fitted = [self.roi_centers_fitted] if self.roi_centers_fitted is not None else []
        self.roi_centers_fitted = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_centers_fitted]

        if not isinstance(self.roi_centers_max_intensity, list):
            self.roi_centers_max_intensity = [self.roi_centers_max_intensity] if self.roi_centers_max_intensity is not None else []
        self.roi_centers_max_intensity = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_centers_max_intensity]

        if not isinstance(self.roi_center_region, list):
            self.roi_center_region = [self.roi_center_region] if self.roi_center_region is not None else []
        self.roi_center_region = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.roi_center_region]

        super().__post_init__(**kwargs)


@dataclass
class FieldIlluminationKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/field_illumination_schema/FieldIlluminationKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/field_illumination_schema/FieldIlluminationKeyValues"
    class_name: ClassVar[str] = "FieldIlluminationKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.FieldIlluminationKeyValues

    channel_name: Optional[Union[str, List[str]]] = empty_list()
    center_region_intensity_fraction: Optional[Union[float, List[float]]] = empty_list()
    center_region_area_fraction: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_y: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_y_relative: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_x: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_x_relative: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_distance_relative: Optional[Union[float, List[float]]] = empty_list()
    center_geometric_y: Optional[Union[float, List[float]]] = empty_list()
    center_geometric_y_relative: Optional[Union[float, List[float]]] = empty_list()
    center_geometric_x: Optional[Union[float, List[float]]] = empty_list()
    center_geometric_x_relative: Optional[Union[float, List[float]]] = empty_list()
    center_geometric_distance_relative: Optional[Union[float, List[float]]] = empty_list()
    center_fitted_y: Optional[Union[float, List[float]]] = empty_list()
    center_fitted_y_relative: Optional[Union[float, List[float]]] = empty_list()
    center_fitted_x: Optional[Union[float, List[float]]] = empty_list()
    center_fitted_x_relative: Optional[Union[float, List[float]]] = empty_list()
    center_fitted_distance_relative: Optional[Union[float, List[float]]] = empty_list()
    max_intensity: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_y: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_y_relative: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_x: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_x_relative: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_distance_relative: Optional[Union[float, List[float]]] = empty_list()
    top_left_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    top_left_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    top_center_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    top_center_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    top_right_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    top_right_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    middle_left_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    middle_left_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    middle_center_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    middle_center_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    middle_right_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    middle_right_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    bottom_left_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    bottom_left_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    bottom_center_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    bottom_center_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()
    bottom_right_intensity_mean: Optional[Union[float, List[float]]] = empty_list()
    bottom_right_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel_name, list):
            self.channel_name = [self.channel_name] if self.channel_name is not None else []
        self.channel_name = [v if isinstance(v, str) else str(v) for v in self.channel_name]

        if not isinstance(self.center_region_intensity_fraction, list):
            self.center_region_intensity_fraction = [self.center_region_intensity_fraction] if self.center_region_intensity_fraction is not None else []
        self.center_region_intensity_fraction = [v if isinstance(v, float) else float(v) for v in self.center_region_intensity_fraction]

        if not isinstance(self.center_region_area_fraction, list):
            self.center_region_area_fraction = [self.center_region_area_fraction] if self.center_region_area_fraction is not None else []
        self.center_region_area_fraction = [v if isinstance(v, float) else float(v) for v in self.center_region_area_fraction]

        if not isinstance(self.center_of_mass_y, list):
            self.center_of_mass_y = [self.center_of_mass_y] if self.center_of_mass_y is not None else []
        self.center_of_mass_y = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_y]

        if not isinstance(self.center_of_mass_y_relative, list):
            self.center_of_mass_y_relative = [self.center_of_mass_y_relative] if self.center_of_mass_y_relative is not None else []
        self.center_of_mass_y_relative = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_y_relative]

        if not isinstance(self.center_of_mass_x, list):
            self.center_of_mass_x = [self.center_of_mass_x] if self.center_of_mass_x is not None else []
        self.center_of_mass_x = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_x]

        if not isinstance(self.center_of_mass_x_relative, list):
            self.center_of_mass_x_relative = [self.center_of_mass_x_relative] if self.center_of_mass_x_relative is not None else []
        self.center_of_mass_x_relative = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_x_relative]

        if not isinstance(self.center_of_mass_distance_relative, list):
            self.center_of_mass_distance_relative = [self.center_of_mass_distance_relative] if self.center_of_mass_distance_relative is not None else []
        self.center_of_mass_distance_relative = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_distance_relative]

        if not isinstance(self.center_geometric_y, list):
            self.center_geometric_y = [self.center_geometric_y] if self.center_geometric_y is not None else []
        self.center_geometric_y = [v if isinstance(v, float) else float(v) for v in self.center_geometric_y]

        if not isinstance(self.center_geometric_y_relative, list):
            self.center_geometric_y_relative = [self.center_geometric_y_relative] if self.center_geometric_y_relative is not None else []
        self.center_geometric_y_relative = [v if isinstance(v, float) else float(v) for v in self.center_geometric_y_relative]

        if not isinstance(self.center_geometric_x, list):
            self.center_geometric_x = [self.center_geometric_x] if self.center_geometric_x is not None else []
        self.center_geometric_x = [v if isinstance(v, float) else float(v) for v in self.center_geometric_x]

        if not isinstance(self.center_geometric_x_relative, list):
            self.center_geometric_x_relative = [self.center_geometric_x_relative] if self.center_geometric_x_relative is not None else []
        self.center_geometric_x_relative = [v if isinstance(v, float) else float(v) for v in self.center_geometric_x_relative]

        if not isinstance(self.center_geometric_distance_relative, list):
            self.center_geometric_distance_relative = [self.center_geometric_distance_relative] if self.center_geometric_distance_relative is not None else []
        self.center_geometric_distance_relative = [v if isinstance(v, float) else float(v) for v in self.center_geometric_distance_relative]

        if not isinstance(self.center_fitted_y, list):
            self.center_fitted_y = [self.center_fitted_y] if self.center_fitted_y is not None else []
        self.center_fitted_y = [v if isinstance(v, float) else float(v) for v in self.center_fitted_y]

        if not isinstance(self.center_fitted_y_relative, list):
            self.center_fitted_y_relative = [self.center_fitted_y_relative] if self.center_fitted_y_relative is not None else []
        self.center_fitted_y_relative = [v if isinstance(v, float) else float(v) for v in self.center_fitted_y_relative]

        if not isinstance(self.center_fitted_x, list):
            self.center_fitted_x = [self.center_fitted_x] if self.center_fitted_x is not None else []
        self.center_fitted_x = [v if isinstance(v, float) else float(v) for v in self.center_fitted_x]

        if not isinstance(self.center_fitted_x_relative, list):
            self.center_fitted_x_relative = [self.center_fitted_x_relative] if self.center_fitted_x_relative is not None else []
        self.center_fitted_x_relative = [v if isinstance(v, float) else float(v) for v in self.center_fitted_x_relative]

        if not isinstance(self.center_fitted_distance_relative, list):
            self.center_fitted_distance_relative = [self.center_fitted_distance_relative] if self.center_fitted_distance_relative is not None else []
        self.center_fitted_distance_relative = [v if isinstance(v, float) else float(v) for v in self.center_fitted_distance_relative]

        if not isinstance(self.max_intensity, list):
            self.max_intensity = [self.max_intensity] if self.max_intensity is not None else []
        self.max_intensity = [v if isinstance(v, float) else float(v) for v in self.max_intensity]

        if not isinstance(self.max_intensity_pos_y, list):
            self.max_intensity_pos_y = [self.max_intensity_pos_y] if self.max_intensity_pos_y is not None else []
        self.max_intensity_pos_y = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_y]

        if not isinstance(self.max_intensity_pos_y_relative, list):
            self.max_intensity_pos_y_relative = [self.max_intensity_pos_y_relative] if self.max_intensity_pos_y_relative is not None else []
        self.max_intensity_pos_y_relative = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_y_relative]

        if not isinstance(self.max_intensity_pos_x, list):
            self.max_intensity_pos_x = [self.max_intensity_pos_x] if self.max_intensity_pos_x is not None else []
        self.max_intensity_pos_x = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_x]

        if not isinstance(self.max_intensity_pos_x_relative, list):
            self.max_intensity_pos_x_relative = [self.max_intensity_pos_x_relative] if self.max_intensity_pos_x_relative is not None else []
        self.max_intensity_pos_x_relative = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_x_relative]

        if not isinstance(self.max_intensity_distance_relative, list):
            self.max_intensity_distance_relative = [self.max_intensity_distance_relative] if self.max_intensity_distance_relative is not None else []
        self.max_intensity_distance_relative = [v if isinstance(v, float) else float(v) for v in self.max_intensity_distance_relative]

        if not isinstance(self.top_left_intensity_mean, list):
            self.top_left_intensity_mean = [self.top_left_intensity_mean] if self.top_left_intensity_mean is not None else []
        self.top_left_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.top_left_intensity_mean]

        if not isinstance(self.top_left_intensity_ratio, list):
            self.top_left_intensity_ratio = [self.top_left_intensity_ratio] if self.top_left_intensity_ratio is not None else []
        self.top_left_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.top_left_intensity_ratio]

        if not isinstance(self.top_center_intensity_mean, list):
            self.top_center_intensity_mean = [self.top_center_intensity_mean] if self.top_center_intensity_mean is not None else []
        self.top_center_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.top_center_intensity_mean]

        if not isinstance(self.top_center_intensity_ratio, list):
            self.top_center_intensity_ratio = [self.top_center_intensity_ratio] if self.top_center_intensity_ratio is not None else []
        self.top_center_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.top_center_intensity_ratio]

        if not isinstance(self.top_right_intensity_mean, list):
            self.top_right_intensity_mean = [self.top_right_intensity_mean] if self.top_right_intensity_mean is not None else []
        self.top_right_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.top_right_intensity_mean]

        if not isinstance(self.top_right_intensity_ratio, list):
            self.top_right_intensity_ratio = [self.top_right_intensity_ratio] if self.top_right_intensity_ratio is not None else []
        self.top_right_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.top_right_intensity_ratio]

        if not isinstance(self.middle_left_intensity_mean, list):
            self.middle_left_intensity_mean = [self.middle_left_intensity_mean] if self.middle_left_intensity_mean is not None else []
        self.middle_left_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.middle_left_intensity_mean]

        if not isinstance(self.middle_left_intensity_ratio, list):
            self.middle_left_intensity_ratio = [self.middle_left_intensity_ratio] if self.middle_left_intensity_ratio is not None else []
        self.middle_left_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.middle_left_intensity_ratio]

        if not isinstance(self.middle_center_intensity_mean, list):
            self.middle_center_intensity_mean = [self.middle_center_intensity_mean] if self.middle_center_intensity_mean is not None else []
        self.middle_center_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.middle_center_intensity_mean]

        if not isinstance(self.middle_center_intensity_ratio, list):
            self.middle_center_intensity_ratio = [self.middle_center_intensity_ratio] if self.middle_center_intensity_ratio is not None else []
        self.middle_center_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.middle_center_intensity_ratio]

        if not isinstance(self.middle_right_intensity_mean, list):
            self.middle_right_intensity_mean = [self.middle_right_intensity_mean] if self.middle_right_intensity_mean is not None else []
        self.middle_right_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.middle_right_intensity_mean]

        if not isinstance(self.middle_right_intensity_ratio, list):
            self.middle_right_intensity_ratio = [self.middle_right_intensity_ratio] if self.middle_right_intensity_ratio is not None else []
        self.middle_right_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.middle_right_intensity_ratio]

        if not isinstance(self.bottom_left_intensity_mean, list):
            self.bottom_left_intensity_mean = [self.bottom_left_intensity_mean] if self.bottom_left_intensity_mean is not None else []
        self.bottom_left_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.bottom_left_intensity_mean]

        if not isinstance(self.bottom_left_intensity_ratio, list):
            self.bottom_left_intensity_ratio = [self.bottom_left_intensity_ratio] if self.bottom_left_intensity_ratio is not None else []
        self.bottom_left_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.bottom_left_intensity_ratio]

        if not isinstance(self.bottom_center_intensity_mean, list):
            self.bottom_center_intensity_mean = [self.bottom_center_intensity_mean] if self.bottom_center_intensity_mean is not None else []
        self.bottom_center_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.bottom_center_intensity_mean]

        if not isinstance(self.bottom_center_intensity_ratio, list):
            self.bottom_center_intensity_ratio = [self.bottom_center_intensity_ratio] if self.bottom_center_intensity_ratio is not None else []
        self.bottom_center_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.bottom_center_intensity_ratio]

        if not isinstance(self.bottom_right_intensity_mean, list):
            self.bottom_right_intensity_mean = [self.bottom_right_intensity_mean] if self.bottom_right_intensity_mean is not None else []
        self.bottom_right_intensity_mean = [v if isinstance(v, float) else float(v) for v in self.bottom_right_intensity_mean]

        if not isinstance(self.bottom_right_intensity_ratio, list):
            self.bottom_right_intensity_ratio = [self.bottom_right_intensity_ratio] if self.bottom_right_intensity_ratio is not None else []
        self.bottom_right_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.bottom_right_intensity_ratio]

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsDataset(MetricsDataset):
    """
    A PSF beads dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/psf_beads_schema/PSFBeadsDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/psf_beads_schema/PSFBeadsDataset"
    class_name: ClassVar[str] = "PSFBeadsDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsDataset

    microscope: Union[dict, Microscope] = None
    processed: Union[bool, Bool] = False
    input: Optional[Union[dict, "PSFBeadsInput"]] = None
    output: Optional[Union[dict, "PSFBeadsOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, PSFBeadsInput):
            self.input = PSFBeadsInput(**as_dict(self.input))

        if self.output is not None and not isinstance(self.output, PSFBeadsOutput):
            self.output = PSFBeadsOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsInput(MetricsInput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/psf_beads_schema/PSFBeadsInput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/psf_beads_schema/PSFBeadsInput"
    class_name: ClassVar[str] = "PSFBeadsInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsInput

    psf_beads_images: Union[Union[dict, Image], List[Union[dict, Image]]] = None
    min_lateral_distance_factor: float = 20.0
    sigma_z: float = 1.0
    sigma_y: float = 1.0
    sigma_x: float = 1.0
    snr_threshold: float = 10.0
    fitting_r2_threshold: float = 0.85
    intensity_robust_z_score_threshold: float = 2.0
    bit_depth: Optional[int] = None
    saturation_threshold: Optional[float] = 0.01

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.psf_beads_images):
            self.MissingRequiredField("psf_beads_images")
        if not isinstance(self.psf_beads_images, list):
            self.psf_beads_images = [self.psf_beads_images] if self.psf_beads_images is not None else []
        self.psf_beads_images = [v if isinstance(v, Image) else Image(**as_dict(v)) for v in self.psf_beads_images]

        if self._is_empty(self.min_lateral_distance_factor):
            self.MissingRequiredField("min_lateral_distance_factor")
        if not isinstance(self.min_lateral_distance_factor, float):
            self.min_lateral_distance_factor = float(self.min_lateral_distance_factor)

        if self._is_empty(self.sigma_z):
            self.MissingRequiredField("sigma_z")
        if not isinstance(self.sigma_z, float):
            self.sigma_z = float(self.sigma_z)

        if self._is_empty(self.sigma_y):
            self.MissingRequiredField("sigma_y")
        if not isinstance(self.sigma_y, float):
            self.sigma_y = float(self.sigma_y)

        if self._is_empty(self.sigma_x):
            self.MissingRequiredField("sigma_x")
        if not isinstance(self.sigma_x, float):
            self.sigma_x = float(self.sigma_x)

        if self._is_empty(self.snr_threshold):
            self.MissingRequiredField("snr_threshold")
        if not isinstance(self.snr_threshold, float):
            self.snr_threshold = float(self.snr_threshold)

        if self._is_empty(self.fitting_r2_threshold):
            self.MissingRequiredField("fitting_r2_threshold")
        if not isinstance(self.fitting_r2_threshold, float):
            self.fitting_r2_threshold = float(self.fitting_r2_threshold)

        if self._is_empty(self.intensity_robust_z_score_threshold):
            self.MissingRequiredField("intensity_robust_z_score_threshold")
        if not isinstance(self.intensity_robust_z_score_threshold, float):
            self.intensity_robust_z_score_threshold = float(self.intensity_robust_z_score_threshold)

        if self.bit_depth is not None and not isinstance(self.bit_depth, int):
            self.bit_depth = int(self.bit_depth)

        if self.saturation_threshold is not None and not isinstance(self.saturation_threshold, float):
            self.saturation_threshold = float(self.saturation_threshold)

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsOutput(MetricsOutput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/psf_beads_schema/PSFBeadsOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/psf_beads_schema/PSFBeadsOutput"
    class_name: ClassVar[str] = "PSFBeadsOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsOutput

    processing_application: Union[str, List[str]] = None
    processing_version: Union[str, List[str]] = None
    processing_datetime: Union[str, XSDDateTime] = None
    validated: Union[bool, Bool] = False
    analyzed_bead_centers: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_lateral_edge: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_self_proximity: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_axial_edge: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_intensity_outlier: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_z_fit_quality: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_y_fit_quality: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    considered_bead_centers_x_fit_quality: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    key_measurements: Optional[Union[dict, "PSFBeadsKeyMeasurements"]] = None
    bead_properties: Optional[Union[dict, Table]] = None
    bead_z_profiles: Optional[Union[dict, Table]] = None
    bead_y_profiles: Optional[Union[dict, Table]] = None
    bead_x_profiles: Optional[Union[dict, Table]] = None
    average_bead: Optional[Union[dict, Image]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.analyzed_bead_centers, list):
            self.analyzed_bead_centers = [self.analyzed_bead_centers] if self.analyzed_bead_centers is not None else []
        self.analyzed_bead_centers = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.analyzed_bead_centers]

        if not isinstance(self.considered_bead_centers_lateral_edge, list):
            self.considered_bead_centers_lateral_edge = [self.considered_bead_centers_lateral_edge] if self.considered_bead_centers_lateral_edge is not None else []
        self.considered_bead_centers_lateral_edge = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_lateral_edge]

        if not isinstance(self.considered_bead_centers_self_proximity, list):
            self.considered_bead_centers_self_proximity = [self.considered_bead_centers_self_proximity] if self.considered_bead_centers_self_proximity is not None else []
        self.considered_bead_centers_self_proximity = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_self_proximity]

        if not isinstance(self.considered_bead_centers_axial_edge, list):
            self.considered_bead_centers_axial_edge = [self.considered_bead_centers_axial_edge] if self.considered_bead_centers_axial_edge is not None else []
        self.considered_bead_centers_axial_edge = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_axial_edge]

        if not isinstance(self.considered_bead_centers_intensity_outlier, list):
            self.considered_bead_centers_intensity_outlier = [self.considered_bead_centers_intensity_outlier] if self.considered_bead_centers_intensity_outlier is not None else []
        self.considered_bead_centers_intensity_outlier = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_intensity_outlier]

        if not isinstance(self.considered_bead_centers_z_fit_quality, list):
            self.considered_bead_centers_z_fit_quality = [self.considered_bead_centers_z_fit_quality] if self.considered_bead_centers_z_fit_quality is not None else []
        self.considered_bead_centers_z_fit_quality = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_z_fit_quality]

        if not isinstance(self.considered_bead_centers_y_fit_quality, list):
            self.considered_bead_centers_y_fit_quality = [self.considered_bead_centers_y_fit_quality] if self.considered_bead_centers_y_fit_quality is not None else []
        self.considered_bead_centers_y_fit_quality = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_y_fit_quality]

        if not isinstance(self.considered_bead_centers_x_fit_quality, list):
            self.considered_bead_centers_x_fit_quality = [self.considered_bead_centers_x_fit_quality] if self.considered_bead_centers_x_fit_quality is not None else []
        self.considered_bead_centers_x_fit_quality = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.considered_bead_centers_x_fit_quality]

        if self.key_measurements is not None and not isinstance(self.key_measurements, PSFBeadsKeyMeasurements):
            self.key_measurements = PSFBeadsKeyMeasurements(**as_dict(self.key_measurements))

        if self.bead_properties is not None and not isinstance(self.bead_properties, Table):
            self.bead_properties = Table(**as_dict(self.bead_properties))

        if self.bead_z_profiles is not None and not isinstance(self.bead_z_profiles, Table):
            self.bead_z_profiles = Table(**as_dict(self.bead_z_profiles))

        if self.bead_y_profiles is not None and not isinstance(self.bead_y_profiles, Table):
            self.bead_y_profiles = Table(**as_dict(self.bead_y_profiles))

        if self.bead_x_profiles is not None and not isinstance(self.bead_x_profiles, Table):
            self.bead_x_profiles = Table(**as_dict(self.bead_x_profiles))

        if self.average_bead is not None and not isinstance(self.average_bead, Image):
            self.average_bead = Image(**as_dict(self.average_bead))

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsKeyMeasurements(KeyMeasurements):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/psf_beads_schema/PSFBeadsKeyMeasurements"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/psf_beads_schema/PSFBeadsKeyMeasurements"
    class_name: ClassVar[str] = "PSFBeadsKeyMeasurements"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsKeyMeasurements

    channel_nr: Optional[Union[int, List[int]]] = empty_list()
    considered_valid_count: Optional[Union[int, List[int]]] = empty_list()
    considered_self_proximity_count: Optional[Union[int, List[int]]] = empty_list()
    considered_lateral_edge_count: Optional[Union[int, List[int]]] = empty_list()
    considered_axial_edge_count: Optional[Union[int, List[int]]] = empty_list()
    considered_intensity_outlier_count: Optional[Union[int, List[int]]] = empty_list()
    considered_bad_fit_z_count: Optional[Union[int, List[int]]] = empty_list()
    considered_bad_fit_y_count: Optional[Union[int, List[int]]] = empty_list()
    considered_bad_fit_x_count: Optional[Union[int, List[int]]] = empty_list()
    intensity_max_mean: Optional[Union[float, List[float]]] = empty_list()
    intensity_max_median: Optional[Union[float, List[float]]] = empty_list()
    intensity_max_std: Optional[Union[float, List[float]]] = empty_list()
    intensity_min_mean: Optional[Union[float, List[float]]] = empty_list()
    intensity_min_median: Optional[Union[float, List[float]]] = empty_list()
    intensity_min_std: Optional[Union[float, List[float]]] = empty_list()
    intensity_std_mean: Optional[Union[float, List[float]]] = empty_list()
    intensity_std_median: Optional[Union[float, List[float]]] = empty_list()
    intensity_std_std: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_z_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_z_median: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_z_std: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_y_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_y_median: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_y_std: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_x_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_x_median: Optional[Union[float, List[float]]] = empty_list()
    fit_r2_x_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_z_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_z_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_z_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_y_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_y_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_y_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_x_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_x_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_pixel_x_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_z_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_z_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_z_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_y_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_y_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_y_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_x_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_x_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_micron_x_std: Optional[Union[float, List[float]]] = empty_list()
    fwhm_lateral_asymmetry_ratio_mean: Optional[Union[float, List[float]]] = empty_list()
    fwhm_lateral_asymmetry_ratio_median: Optional[Union[float, List[float]]] = empty_list()
    fwhm_lateral_asymmetry_ratio_std: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fit_r2_z: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fit_r2_y: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fit_r2_x: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_pixel_z: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_pixel_y: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_pixel_x: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_micron_z: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_micron_y: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_micron_x: Optional[Union[float, List[float]]] = empty_list()
    average_bead_fwhm_lateral_asymmetry_ratio: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel_nr, list):
            self.channel_nr = [self.channel_nr] if self.channel_nr is not None else []
        self.channel_nr = [v if isinstance(v, int) else int(v) for v in self.channel_nr]

        if not isinstance(self.considered_valid_count, list):
            self.considered_valid_count = [self.considered_valid_count] if self.considered_valid_count is not None else []
        self.considered_valid_count = [v if isinstance(v, int) else int(v) for v in self.considered_valid_count]

        if not isinstance(self.considered_self_proximity_count, list):
            self.considered_self_proximity_count = [self.considered_self_proximity_count] if self.considered_self_proximity_count is not None else []
        self.considered_self_proximity_count = [v if isinstance(v, int) else int(v) for v in self.considered_self_proximity_count]

        if not isinstance(self.considered_lateral_edge_count, list):
            self.considered_lateral_edge_count = [self.considered_lateral_edge_count] if self.considered_lateral_edge_count is not None else []
        self.considered_lateral_edge_count = [v if isinstance(v, int) else int(v) for v in self.considered_lateral_edge_count]

        if not isinstance(self.considered_axial_edge_count, list):
            self.considered_axial_edge_count = [self.considered_axial_edge_count] if self.considered_axial_edge_count is not None else []
        self.considered_axial_edge_count = [v if isinstance(v, int) else int(v) for v in self.considered_axial_edge_count]

        if not isinstance(self.considered_intensity_outlier_count, list):
            self.considered_intensity_outlier_count = [self.considered_intensity_outlier_count] if self.considered_intensity_outlier_count is not None else []
        self.considered_intensity_outlier_count = [v if isinstance(v, int) else int(v) for v in self.considered_intensity_outlier_count]

        if not isinstance(self.considered_bad_fit_z_count, list):
            self.considered_bad_fit_z_count = [self.considered_bad_fit_z_count] if self.considered_bad_fit_z_count is not None else []
        self.considered_bad_fit_z_count = [v if isinstance(v, int) else int(v) for v in self.considered_bad_fit_z_count]

        if not isinstance(self.considered_bad_fit_y_count, list):
            self.considered_bad_fit_y_count = [self.considered_bad_fit_y_count] if self.considered_bad_fit_y_count is not None else []
        self.considered_bad_fit_y_count = [v if isinstance(v, int) else int(v) for v in self.considered_bad_fit_y_count]

        if not isinstance(self.considered_bad_fit_x_count, list):
            self.considered_bad_fit_x_count = [self.considered_bad_fit_x_count] if self.considered_bad_fit_x_count is not None else []
        self.considered_bad_fit_x_count = [v if isinstance(v, int) else int(v) for v in self.considered_bad_fit_x_count]

        if not isinstance(self.intensity_max_mean, list):
            self.intensity_max_mean = [self.intensity_max_mean] if self.intensity_max_mean is not None else []
        self.intensity_max_mean = [v if isinstance(v, float) else float(v) for v in self.intensity_max_mean]

        if not isinstance(self.intensity_max_median, list):
            self.intensity_max_median = [self.intensity_max_median] if self.intensity_max_median is not None else []
        self.intensity_max_median = [v if isinstance(v, float) else float(v) for v in self.intensity_max_median]

        if not isinstance(self.intensity_max_std, list):
            self.intensity_max_std = [self.intensity_max_std] if self.intensity_max_std is not None else []
        self.intensity_max_std = [v if isinstance(v, float) else float(v) for v in self.intensity_max_std]

        if not isinstance(self.intensity_min_mean, list):
            self.intensity_min_mean = [self.intensity_min_mean] if self.intensity_min_mean is not None else []
        self.intensity_min_mean = [v if isinstance(v, float) else float(v) for v in self.intensity_min_mean]

        if not isinstance(self.intensity_min_median, list):
            self.intensity_min_median = [self.intensity_min_median] if self.intensity_min_median is not None else []
        self.intensity_min_median = [v if isinstance(v, float) else float(v) for v in self.intensity_min_median]

        if not isinstance(self.intensity_min_std, list):
            self.intensity_min_std = [self.intensity_min_std] if self.intensity_min_std is not None else []
        self.intensity_min_std = [v if isinstance(v, float) else float(v) for v in self.intensity_min_std]

        if not isinstance(self.intensity_std_mean, list):
            self.intensity_std_mean = [self.intensity_std_mean] if self.intensity_std_mean is not None else []
        self.intensity_std_mean = [v if isinstance(v, float) else float(v) for v in self.intensity_std_mean]

        if not isinstance(self.intensity_std_median, list):
            self.intensity_std_median = [self.intensity_std_median] if self.intensity_std_median is not None else []
        self.intensity_std_median = [v if isinstance(v, float) else float(v) for v in self.intensity_std_median]

        if not isinstance(self.intensity_std_std, list):
            self.intensity_std_std = [self.intensity_std_std] if self.intensity_std_std is not None else []
        self.intensity_std_std = [v if isinstance(v, float) else float(v) for v in self.intensity_std_std]

        if not isinstance(self.fit_r2_z_mean, list):
            self.fit_r2_z_mean = [self.fit_r2_z_mean] if self.fit_r2_z_mean is not None else []
        self.fit_r2_z_mean = [v if isinstance(v, float) else float(v) for v in self.fit_r2_z_mean]

        if not isinstance(self.fit_r2_z_median, list):
            self.fit_r2_z_median = [self.fit_r2_z_median] if self.fit_r2_z_median is not None else []
        self.fit_r2_z_median = [v if isinstance(v, float) else float(v) for v in self.fit_r2_z_median]

        if not isinstance(self.fit_r2_z_std, list):
            self.fit_r2_z_std = [self.fit_r2_z_std] if self.fit_r2_z_std is not None else []
        self.fit_r2_z_std = [v if isinstance(v, float) else float(v) for v in self.fit_r2_z_std]

        if not isinstance(self.fit_r2_y_mean, list):
            self.fit_r2_y_mean = [self.fit_r2_y_mean] if self.fit_r2_y_mean is not None else []
        self.fit_r2_y_mean = [v if isinstance(v, float) else float(v) for v in self.fit_r2_y_mean]

        if not isinstance(self.fit_r2_y_median, list):
            self.fit_r2_y_median = [self.fit_r2_y_median] if self.fit_r2_y_median is not None else []
        self.fit_r2_y_median = [v if isinstance(v, float) else float(v) for v in self.fit_r2_y_median]

        if not isinstance(self.fit_r2_y_std, list):
            self.fit_r2_y_std = [self.fit_r2_y_std] if self.fit_r2_y_std is not None else []
        self.fit_r2_y_std = [v if isinstance(v, float) else float(v) for v in self.fit_r2_y_std]

        if not isinstance(self.fit_r2_x_mean, list):
            self.fit_r2_x_mean = [self.fit_r2_x_mean] if self.fit_r2_x_mean is not None else []
        self.fit_r2_x_mean = [v if isinstance(v, float) else float(v) for v in self.fit_r2_x_mean]

        if not isinstance(self.fit_r2_x_median, list):
            self.fit_r2_x_median = [self.fit_r2_x_median] if self.fit_r2_x_median is not None else []
        self.fit_r2_x_median = [v if isinstance(v, float) else float(v) for v in self.fit_r2_x_median]

        if not isinstance(self.fit_r2_x_std, list):
            self.fit_r2_x_std = [self.fit_r2_x_std] if self.fit_r2_x_std is not None else []
        self.fit_r2_x_std = [v if isinstance(v, float) else float(v) for v in self.fit_r2_x_std]

        if not isinstance(self.fwhm_pixel_z_mean, list):
            self.fwhm_pixel_z_mean = [self.fwhm_pixel_z_mean] if self.fwhm_pixel_z_mean is not None else []
        self.fwhm_pixel_z_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_z_mean]

        if not isinstance(self.fwhm_pixel_z_median, list):
            self.fwhm_pixel_z_median = [self.fwhm_pixel_z_median] if self.fwhm_pixel_z_median is not None else []
        self.fwhm_pixel_z_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_z_median]

        if not isinstance(self.fwhm_pixel_z_std, list):
            self.fwhm_pixel_z_std = [self.fwhm_pixel_z_std] if self.fwhm_pixel_z_std is not None else []
        self.fwhm_pixel_z_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_z_std]

        if not isinstance(self.fwhm_pixel_y_mean, list):
            self.fwhm_pixel_y_mean = [self.fwhm_pixel_y_mean] if self.fwhm_pixel_y_mean is not None else []
        self.fwhm_pixel_y_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_y_mean]

        if not isinstance(self.fwhm_pixel_y_median, list):
            self.fwhm_pixel_y_median = [self.fwhm_pixel_y_median] if self.fwhm_pixel_y_median is not None else []
        self.fwhm_pixel_y_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_y_median]

        if not isinstance(self.fwhm_pixel_y_std, list):
            self.fwhm_pixel_y_std = [self.fwhm_pixel_y_std] if self.fwhm_pixel_y_std is not None else []
        self.fwhm_pixel_y_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_y_std]

        if not isinstance(self.fwhm_pixel_x_mean, list):
            self.fwhm_pixel_x_mean = [self.fwhm_pixel_x_mean] if self.fwhm_pixel_x_mean is not None else []
        self.fwhm_pixel_x_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_x_mean]

        if not isinstance(self.fwhm_pixel_x_median, list):
            self.fwhm_pixel_x_median = [self.fwhm_pixel_x_median] if self.fwhm_pixel_x_median is not None else []
        self.fwhm_pixel_x_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_x_median]

        if not isinstance(self.fwhm_pixel_x_std, list):
            self.fwhm_pixel_x_std = [self.fwhm_pixel_x_std] if self.fwhm_pixel_x_std is not None else []
        self.fwhm_pixel_x_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_pixel_x_std]

        if not isinstance(self.fwhm_micron_z_mean, list):
            self.fwhm_micron_z_mean = [self.fwhm_micron_z_mean] if self.fwhm_micron_z_mean is not None else []
        self.fwhm_micron_z_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_z_mean]

        if not isinstance(self.fwhm_micron_z_median, list):
            self.fwhm_micron_z_median = [self.fwhm_micron_z_median] if self.fwhm_micron_z_median is not None else []
        self.fwhm_micron_z_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_z_median]

        if not isinstance(self.fwhm_micron_z_std, list):
            self.fwhm_micron_z_std = [self.fwhm_micron_z_std] if self.fwhm_micron_z_std is not None else []
        self.fwhm_micron_z_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_z_std]

        if not isinstance(self.fwhm_micron_y_mean, list):
            self.fwhm_micron_y_mean = [self.fwhm_micron_y_mean] if self.fwhm_micron_y_mean is not None else []
        self.fwhm_micron_y_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_y_mean]

        if not isinstance(self.fwhm_micron_y_median, list):
            self.fwhm_micron_y_median = [self.fwhm_micron_y_median] if self.fwhm_micron_y_median is not None else []
        self.fwhm_micron_y_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_y_median]

        if not isinstance(self.fwhm_micron_y_std, list):
            self.fwhm_micron_y_std = [self.fwhm_micron_y_std] if self.fwhm_micron_y_std is not None else []
        self.fwhm_micron_y_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_y_std]

        if not isinstance(self.fwhm_micron_x_mean, list):
            self.fwhm_micron_x_mean = [self.fwhm_micron_x_mean] if self.fwhm_micron_x_mean is not None else []
        self.fwhm_micron_x_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_x_mean]

        if not isinstance(self.fwhm_micron_x_median, list):
            self.fwhm_micron_x_median = [self.fwhm_micron_x_median] if self.fwhm_micron_x_median is not None else []
        self.fwhm_micron_x_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_x_median]

        if not isinstance(self.fwhm_micron_x_std, list):
            self.fwhm_micron_x_std = [self.fwhm_micron_x_std] if self.fwhm_micron_x_std is not None else []
        self.fwhm_micron_x_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_micron_x_std]

        if not isinstance(self.fwhm_lateral_asymmetry_ratio_mean, list):
            self.fwhm_lateral_asymmetry_ratio_mean = [self.fwhm_lateral_asymmetry_ratio_mean] if self.fwhm_lateral_asymmetry_ratio_mean is not None else []
        self.fwhm_lateral_asymmetry_ratio_mean = [v if isinstance(v, float) else float(v) for v in self.fwhm_lateral_asymmetry_ratio_mean]

        if not isinstance(self.fwhm_lateral_asymmetry_ratio_median, list):
            self.fwhm_lateral_asymmetry_ratio_median = [self.fwhm_lateral_asymmetry_ratio_median] if self.fwhm_lateral_asymmetry_ratio_median is not None else []
        self.fwhm_lateral_asymmetry_ratio_median = [v if isinstance(v, float) else float(v) for v in self.fwhm_lateral_asymmetry_ratio_median]

        if not isinstance(self.fwhm_lateral_asymmetry_ratio_std, list):
            self.fwhm_lateral_asymmetry_ratio_std = [self.fwhm_lateral_asymmetry_ratio_std] if self.fwhm_lateral_asymmetry_ratio_std is not None else []
        self.fwhm_lateral_asymmetry_ratio_std = [v if isinstance(v, float) else float(v) for v in self.fwhm_lateral_asymmetry_ratio_std]

        if not isinstance(self.average_bead_fit_r2_z, list):
            self.average_bead_fit_r2_z = [self.average_bead_fit_r2_z] if self.average_bead_fit_r2_z is not None else []
        self.average_bead_fit_r2_z = [v if isinstance(v, float) else float(v) for v in self.average_bead_fit_r2_z]

        if not isinstance(self.average_bead_fit_r2_y, list):
            self.average_bead_fit_r2_y = [self.average_bead_fit_r2_y] if self.average_bead_fit_r2_y is not None else []
        self.average_bead_fit_r2_y = [v if isinstance(v, float) else float(v) for v in self.average_bead_fit_r2_y]

        if not isinstance(self.average_bead_fit_r2_x, list):
            self.average_bead_fit_r2_x = [self.average_bead_fit_r2_x] if self.average_bead_fit_r2_x is not None else []
        self.average_bead_fit_r2_x = [v if isinstance(v, float) else float(v) for v in self.average_bead_fit_r2_x]

        if not isinstance(self.average_bead_fwhm_pixel_z, list):
            self.average_bead_fwhm_pixel_z = [self.average_bead_fwhm_pixel_z] if self.average_bead_fwhm_pixel_z is not None else []
        self.average_bead_fwhm_pixel_z = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_pixel_z]

        if not isinstance(self.average_bead_fwhm_pixel_y, list):
            self.average_bead_fwhm_pixel_y = [self.average_bead_fwhm_pixel_y] if self.average_bead_fwhm_pixel_y is not None else []
        self.average_bead_fwhm_pixel_y = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_pixel_y]

        if not isinstance(self.average_bead_fwhm_pixel_x, list):
            self.average_bead_fwhm_pixel_x = [self.average_bead_fwhm_pixel_x] if self.average_bead_fwhm_pixel_x is not None else []
        self.average_bead_fwhm_pixel_x = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_pixel_x]

        if not isinstance(self.average_bead_fwhm_micron_z, list):
            self.average_bead_fwhm_micron_z = [self.average_bead_fwhm_micron_z] if self.average_bead_fwhm_micron_z is not None else []
        self.average_bead_fwhm_micron_z = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_micron_z]

        if not isinstance(self.average_bead_fwhm_micron_y, list):
            self.average_bead_fwhm_micron_y = [self.average_bead_fwhm_micron_y] if self.average_bead_fwhm_micron_y is not None else []
        self.average_bead_fwhm_micron_y = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_micron_y]

        if not isinstance(self.average_bead_fwhm_micron_x, list):
            self.average_bead_fwhm_micron_x = [self.average_bead_fwhm_micron_x] if self.average_bead_fwhm_micron_x is not None else []
        self.average_bead_fwhm_micron_x = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_micron_x]

        if not isinstance(self.average_bead_fwhm_lateral_asymmetry_ratio, list):
            self.average_bead_fwhm_lateral_asymmetry_ratio = [self.average_bead_fwhm_lateral_asymmetry_ratio] if self.average_bead_fwhm_lateral_asymmetry_ratio is not None else []
        self.average_bead_fwhm_lateral_asymmetry_ratio = [v if isinstance(v, float) else float(v) for v in self.average_bead_fwhm_lateral_asymmetry_ratio]

        super().__post_init__(**kwargs)


@dataclass
class ArgolightBDataset(MetricsDataset):
    """
    An Argolight sample pattern B dataset. This pattern consists of an array of circles
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBDataset"
    class_name: ClassVar[str] = "ArgolightBDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBDataset

    microscope: Union[dict, Microscope] = None
    processed: Union[bool, Bool] = False
    input: Optional[Union[dict, "ArgolightBInput"]] = None
    output: Optional[Union[dict, "ArgolightBOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, ArgolightBInput):
            self.input = ArgolightBInput(**as_dict(self.input))

        if self.output is not None and not isinstance(self.output, ArgolightBOutput):
            self.output = ArgolightBOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


@dataclass
class ArgolightBInput(MetricsInput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBInput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBInput"
    class_name: ClassVar[str] = "ArgolightBInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBInput

    argolight_b_image: Union[dict, Image] = None
    spots_distance: float = None
    saturation_threshold: float = 0.01
    sigma_z: float = 1.0
    sigma_y: float = 3.0
    sigma_x: float = 3.0
    bit_depth: Optional[int] = None
    lower_threshold_correction_factors: Optional[Union[float, List[float]]] = empty_list()
    upper_threshold_correction_factors: Optional[Union[float, List[float]]] = empty_list()
    remove_center_cross: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.argolight_b_image):
            self.MissingRequiredField("argolight_b_image")
        if not isinstance(self.argolight_b_image, Image):
            self.argolight_b_image = Image(**as_dict(self.argolight_b_image))

        if self._is_empty(self.saturation_threshold):
            self.MissingRequiredField("saturation_threshold")
        if not isinstance(self.saturation_threshold, float):
            self.saturation_threshold = float(self.saturation_threshold)

        if self._is_empty(self.spots_distance):
            self.MissingRequiredField("spots_distance")
        if not isinstance(self.spots_distance, float):
            self.spots_distance = float(self.spots_distance)

        if self._is_empty(self.sigma_z):
            self.MissingRequiredField("sigma_z")
        if not isinstance(self.sigma_z, float):
            self.sigma_z = float(self.sigma_z)

        if self._is_empty(self.sigma_y):
            self.MissingRequiredField("sigma_y")
        if not isinstance(self.sigma_y, float):
            self.sigma_y = float(self.sigma_y)

        if self._is_empty(self.sigma_x):
            self.MissingRequiredField("sigma_x")
        if not isinstance(self.sigma_x, float):
            self.sigma_x = float(self.sigma_x)

        if self.bit_depth is not None and not isinstance(self.bit_depth, int):
            self.bit_depth = int(self.bit_depth)

        if not isinstance(self.lower_threshold_correction_factors, list):
            self.lower_threshold_correction_factors = [self.lower_threshold_correction_factors] if self.lower_threshold_correction_factors is not None else []
        self.lower_threshold_correction_factors = [v if isinstance(v, float) else float(v) for v in self.lower_threshold_correction_factors]

        if not isinstance(self.upper_threshold_correction_factors, list):
            self.upper_threshold_correction_factors = [self.upper_threshold_correction_factors] if self.upper_threshold_correction_factors is not None else []
        self.upper_threshold_correction_factors = [v if isinstance(v, float) else float(v) for v in self.upper_threshold_correction_factors]

        if self.remove_center_cross is not None and not isinstance(self.remove_center_cross, Bool):
            self.remove_center_cross = Bool(self.remove_center_cross)

        super().__post_init__(**kwargs)


@dataclass
class ArgolightBOutput(MetricsOutput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBOutput"
    class_name: ClassVar[str] = "ArgolightBOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBOutput

    processing_application: Union[str, List[str]] = None
    processing_version: Union[str, List[str]] = None
    processing_datetime: Union[str, XSDDateTime] = None
    validated: Union[bool, Bool] = False
    spots_labels_image: Optional[Union[dict, ImageMask]] = None
    spots_centers_of_mass: Optional[Union[Union[dict, "ArgolightBCentersOfMass"], List[Union[dict, "ArgolightBCentersOfMass"]]]] = empty_list()
    intensity_key_values: Optional[Union[dict, "ArgolightBIntensityKeyValues"]] = None
    distance_key_values: Optional[Union[dict, "ArgolightBDistanceKeyValues"]] = None
    spots_properties: Optional[Union[dict, Table]] = None
    spots_distances: Optional[Union[dict, Table]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.spots_labels_image is not None and not isinstance(self.spots_labels_image, ImageMask):
            self.spots_labels_image = ImageMask(**as_dict(self.spots_labels_image))

        if not isinstance(self.spots_centers_of_mass, list):
            self.spots_centers_of_mass = [self.spots_centers_of_mass] if self.spots_centers_of_mass is not None else []
        self.spots_centers_of_mass = [v if isinstance(v, ArgolightBCentersOfMass) else ArgolightBCentersOfMass(**as_dict(v)) for v in self.spots_centers_of_mass]

        if self.intensity_key_values is not None and not isinstance(self.intensity_key_values, ArgolightBIntensityKeyValues):
            self.intensity_key_values = ArgolightBIntensityKeyValues(**as_dict(self.intensity_key_values))

        if self.distance_key_values is not None and not isinstance(self.distance_key_values, ArgolightBDistanceKeyValues):
            self.distance_key_values = ArgolightBDistanceKeyValues(**as_dict(self.distance_key_values))

        if self.spots_properties is not None and not isinstance(self.spots_properties, Table):
            self.spots_properties = Table(**as_dict(self.spots_properties))

        if self.spots_distances is not None and not isinstance(self.spots_distances, Table):
            self.spots_distances = Table(**as_dict(self.spots_distances))

        super().__post_init__(**kwargs)


class ArgolightBCentersOfMass(Roi):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBCentersOfMass"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBCentersOfMass"
    class_name: ClassVar[str] = "ArgolightBCentersOfMass"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBCentersOfMass


@dataclass
class ArgolightBIntensityKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBIntensityKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBIntensityKeyValues"
    class_name: ClassVar[str] = "ArgolightBIntensityKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBIntensityKeyValues

    channel_nr: Optional[Union[int, List[int]]] = empty_list()
    nr_of_spots: Optional[Union[int, List[int]]] = empty_list()
    intensity_max_spot: Optional[Union[float, List[float]]] = empty_list()
    intensity_max_spot_roi: Optional[Union[int, List[int]]] = empty_list()
    intensity_min_spot: Optional[Union[float, List[float]]] = empty_list()
    intensity_min_spot_roi: Optional[Union[int, List[int]]] = empty_list()
    mean_intensity: Optional[Union[float, List[float]]] = empty_list()
    median_intensity: Optional[Union[float, List[float]]] = empty_list()
    std_mean_intensity: Optional[Union[float, List[float]]] = empty_list()
    mad_mean_intensity: Optional[Union[float, List[float]]] = empty_list()
    min_max_intensity_ratio: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel_nr, list):
            self.channel_nr = [self.channel_nr] if self.channel_nr is not None else []
        self.channel_nr = [v if isinstance(v, int) else int(v) for v in self.channel_nr]

        if not isinstance(self.nr_of_spots, list):
            self.nr_of_spots = [self.nr_of_spots] if self.nr_of_spots is not None else []
        self.nr_of_spots = [v if isinstance(v, int) else int(v) for v in self.nr_of_spots]

        if not isinstance(self.intensity_max_spot, list):
            self.intensity_max_spot = [self.intensity_max_spot] if self.intensity_max_spot is not None else []
        self.intensity_max_spot = [v if isinstance(v, float) else float(v) for v in self.intensity_max_spot]

        if not isinstance(self.intensity_max_spot_roi, list):
            self.intensity_max_spot_roi = [self.intensity_max_spot_roi] if self.intensity_max_spot_roi is not None else []
        self.intensity_max_spot_roi = [v if isinstance(v, int) else int(v) for v in self.intensity_max_spot_roi]

        if not isinstance(self.intensity_min_spot, list):
            self.intensity_min_spot = [self.intensity_min_spot] if self.intensity_min_spot is not None else []
        self.intensity_min_spot = [v if isinstance(v, float) else float(v) for v in self.intensity_min_spot]

        if not isinstance(self.intensity_min_spot_roi, list):
            self.intensity_min_spot_roi = [self.intensity_min_spot_roi] if self.intensity_min_spot_roi is not None else []
        self.intensity_min_spot_roi = [v if isinstance(v, int) else int(v) for v in self.intensity_min_spot_roi]

        if not isinstance(self.mean_intensity, list):
            self.mean_intensity = [self.mean_intensity] if self.mean_intensity is not None else []
        self.mean_intensity = [v if isinstance(v, float) else float(v) for v in self.mean_intensity]

        if not isinstance(self.median_intensity, list):
            self.median_intensity = [self.median_intensity] if self.median_intensity is not None else []
        self.median_intensity = [v if isinstance(v, float) else float(v) for v in self.median_intensity]

        if not isinstance(self.std_mean_intensity, list):
            self.std_mean_intensity = [self.std_mean_intensity] if self.std_mean_intensity is not None else []
        self.std_mean_intensity = [v if isinstance(v, float) else float(v) for v in self.std_mean_intensity]

        if not isinstance(self.mad_mean_intensity, list):
            self.mad_mean_intensity = [self.mad_mean_intensity] if self.mad_mean_intensity is not None else []
        self.mad_mean_intensity = [v if isinstance(v, float) else float(v) for v in self.mad_mean_intensity]

        if not isinstance(self.min_max_intensity_ratio, list):
            self.min_max_intensity_ratio = [self.min_max_intensity_ratio] if self.min_max_intensity_ratio is not None else []
        self.min_max_intensity_ratio = [v if isinstance(v, float) else float(v) for v in self.min_max_intensity_ratio]

        super().__post_init__(**kwargs)


@dataclass
class ArgolightBDistanceKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBDistanceKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBDistanceKeyValues"
    class_name: ClassVar[str] = "ArgolightBDistanceKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBDistanceKeyValues

    channel_A: Optional[Union[int, List[int]]] = empty_list()
    channel_B: Optional[Union[int, List[int]]] = empty_list()
    mean_3d_dist: Optional[Union[float, List[float]]] = empty_list()
    median_3d_dist: Optional[Union[float, List[float]]] = empty_list()
    std_3d_dist: Optional[Union[float, List[float]]] = empty_list()
    mad_3d_dist: Optional[Union[float, List[float]]] = empty_list()
    mean_z_dist: Optional[Union[float, List[float]]] = empty_list()
    median_z_dist: Optional[Union[float, List[float]]] = empty_list()
    std_z_dist: Optional[Union[float, List[float]]] = empty_list()
    mad_z_dist: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel_A, list):
            self.channel_A = [self.channel_A] if self.channel_A is not None else []
        self.channel_A = [v if isinstance(v, int) else int(v) for v in self.channel_A]

        if not isinstance(self.channel_B, list):
            self.channel_B = [self.channel_B] if self.channel_B is not None else []
        self.channel_B = [v if isinstance(v, int) else int(v) for v in self.channel_B]

        if not isinstance(self.mean_3d_dist, list):
            self.mean_3d_dist = [self.mean_3d_dist] if self.mean_3d_dist is not None else []
        self.mean_3d_dist = [v if isinstance(v, float) else float(v) for v in self.mean_3d_dist]

        if not isinstance(self.median_3d_dist, list):
            self.median_3d_dist = [self.median_3d_dist] if self.median_3d_dist is not None else []
        self.median_3d_dist = [v if isinstance(v, float) else float(v) for v in self.median_3d_dist]

        if not isinstance(self.std_3d_dist, list):
            self.std_3d_dist = [self.std_3d_dist] if self.std_3d_dist is not None else []
        self.std_3d_dist = [v if isinstance(v, float) else float(v) for v in self.std_3d_dist]

        if not isinstance(self.mad_3d_dist, list):
            self.mad_3d_dist = [self.mad_3d_dist] if self.mad_3d_dist is not None else []
        self.mad_3d_dist = [v if isinstance(v, float) else float(v) for v in self.mad_3d_dist]

        if not isinstance(self.mean_z_dist, list):
            self.mean_z_dist = [self.mean_z_dist] if self.mean_z_dist is not None else []
        self.mean_z_dist = [v if isinstance(v, float) else float(v) for v in self.mean_z_dist]

        if not isinstance(self.median_z_dist, list):
            self.median_z_dist = [self.median_z_dist] if self.median_z_dist is not None else []
        self.median_z_dist = [v if isinstance(v, float) else float(v) for v in self.median_z_dist]

        if not isinstance(self.std_z_dist, list):
            self.std_z_dist = [self.std_z_dist] if self.std_z_dist is not None else []
        self.std_z_dist = [v if isinstance(v, float) else float(v) for v in self.std_z_dist]

        if not isinstance(self.mad_z_dist, list):
            self.mad_z_dist = [self.mad_z_dist] if self.mad_z_dist is not None else []
        self.mad_z_dist = [v if isinstance(v, float) else float(v) for v in self.mad_z_dist]

        super().__post_init__(**kwargs)


@dataclass
class ArgolightEDataset(MetricsDataset):
    """
    An Argolight sample pattern E dataset.
    It contains resolution data on the axis indicated:
    - axis 1 = Y resolution = lines along X axis
    - axis 2 = X resolution = lines along Y axis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightEDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightEDataset"
    class_name: ClassVar[str] = "ArgolightEDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightEDataset

    microscope: Union[dict, Microscope] = None
    processed: Union[bool, Bool] = False
    input: Optional[Union[dict, "ArgolightEInput"]] = None
    output: Optional[Union[dict, "ArgolightEOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, ArgolightEInput):
            self.input = ArgolightEInput(**as_dict(self.input))

        if self.output is not None and not isinstance(self.output, ArgolightEOutput):
            self.output = ArgolightEOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


@dataclass
class ArgolightEInput(MetricsInput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightEInput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightEInput"
    class_name: ClassVar[str] = "ArgolightEInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightEInput

    argolight_e_image: Union[dict, Image] = None
    orientation_axis: int = None
    saturation_threshold: float = 0.01
    measured_band: float = 0.4
    prominence_threshold: float = 0.264
    bit_depth: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.argolight_e_image):
            self.MissingRequiredField("argolight_e_image")
        if not isinstance(self.argolight_e_image, Image):
            self.argolight_e_image = Image(**as_dict(self.argolight_e_image))

        if self._is_empty(self.saturation_threshold):
            self.MissingRequiredField("saturation_threshold")
        if not isinstance(self.saturation_threshold, float):
            self.saturation_threshold = float(self.saturation_threshold)

        if self._is_empty(self.orientation_axis):
            self.MissingRequiredField("orientation_axis")
        if not isinstance(self.orientation_axis, int):
            self.orientation_axis = int(self.orientation_axis)

        if self._is_empty(self.measured_band):
            self.MissingRequiredField("measured_band")
        if not isinstance(self.measured_band, float):
            self.measured_band = float(self.measured_band)

        if self._is_empty(self.prominence_threshold):
            self.MissingRequiredField("prominence_threshold")
        if not isinstance(self.prominence_threshold, float):
            self.prominence_threshold = float(self.prominence_threshold)

        if self.bit_depth is not None and not isinstance(self.bit_depth, int):
            self.bit_depth = int(self.bit_depth)

        super().__post_init__(**kwargs)


@dataclass
class ArgolightEOutput(MetricsOutput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightEOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightEOutput"
    class_name: ClassVar[str] = "ArgolightEOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightEOutput

    processing_application: Union[str, List[str]] = None
    processing_version: Union[str, List[str]] = None
    processing_datetime: Union[str, XSDDateTime] = None
    validated: Union[bool, Bool] = False
    peaks_rois: Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]] = empty_list()
    key_measurements: Optional[Union[dict, "ArgolightEKeyValues"]] = None
    intensity_profiles: Optional[Union[dict, Table]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.peaks_rois, list):
            self.peaks_rois = [self.peaks_rois] if self.peaks_rois is not None else []
        self.peaks_rois = [v if isinstance(v, Roi) else Roi(**as_dict(v)) for v in self.peaks_rois]

        if self.key_measurements is not None and not isinstance(self.key_measurements, ArgolightEKeyValues):
            self.key_measurements = ArgolightEKeyValues(**as_dict(self.key_measurements))

        if self.intensity_profiles is not None and not isinstance(self.intensity_profiles, Table):
            self.intensity_profiles = Table(**as_dict(self.intensity_profiles))

        super().__post_init__(**kwargs)


@dataclass
class ArgolightEKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightEKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightEKeyValues"
    class_name: ClassVar[str] = "ArgolightEKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightEKeyValues

    channel_nr: Optional[Union[int, List[int]]] = empty_list()
    focus_slice: Optional[Union[int, List[int]]] = empty_list()
    rayleigh_resolution_pixels: Optional[Union[float, List[float]]] = empty_list()
    rayleigh_resolution_microns: Optional[Union[float, List[float]]] = empty_list()
    peak_position_A: Optional[Union[float, List[float]]] = empty_list()
    peak_position_B: Optional[Union[float, List[float]]] = empty_list()
    peak_height_A: Optional[Union[float, List[float]]] = empty_list()
    peak_height_B: Optional[Union[float, List[float]]] = empty_list()
    peak_prominence_A: Optional[Union[float, List[float]]] = empty_list()
    peak_prominence_B: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel_nr, list):
            self.channel_nr = [self.channel_nr] if self.channel_nr is not None else []
        self.channel_nr = [v if isinstance(v, int) else int(v) for v in self.channel_nr]

        if not isinstance(self.focus_slice, list):
            self.focus_slice = [self.focus_slice] if self.focus_slice is not None else []
        self.focus_slice = [v if isinstance(v, int) else int(v) for v in self.focus_slice]

        if not isinstance(self.rayleigh_resolution_pixels, list):
            self.rayleigh_resolution_pixels = [self.rayleigh_resolution_pixels] if self.rayleigh_resolution_pixels is not None else []
        self.rayleigh_resolution_pixels = [v if isinstance(v, float) else float(v) for v in self.rayleigh_resolution_pixels]

        if not isinstance(self.rayleigh_resolution_microns, list):
            self.rayleigh_resolution_microns = [self.rayleigh_resolution_microns] if self.rayleigh_resolution_microns is not None else []
        self.rayleigh_resolution_microns = [v if isinstance(v, float) else float(v) for v in self.rayleigh_resolution_microns]

        if not isinstance(self.peak_position_A, list):
            self.peak_position_A = [self.peak_position_A] if self.peak_position_A is not None else []
        self.peak_position_A = [v if isinstance(v, float) else float(v) for v in self.peak_position_A]

        if not isinstance(self.peak_position_B, list):
            self.peak_position_B = [self.peak_position_B] if self.peak_position_B is not None else []
        self.peak_position_B = [v if isinstance(v, float) else float(v) for v in self.peak_position_B]

        if not isinstance(self.peak_height_A, list):
            self.peak_height_A = [self.peak_height_A] if self.peak_height_A is not None else []
        self.peak_height_A = [v if isinstance(v, float) else float(v) for v in self.peak_height_A]

        if not isinstance(self.peak_height_B, list):
            self.peak_height_B = [self.peak_height_B] if self.peak_height_B is not None else []
        self.peak_height_B = [v if isinstance(v, float) else float(v) for v in self.peak_height_B]

        if not isinstance(self.peak_prominence_A, list):
            self.peak_prominence_A = [self.peak_prominence_A] if self.peak_prominence_A is not None else []
        self.peak_prominence_A = [v if isinstance(v, float) else float(v) for v in self.peak_prominence_A]

        if not isinstance(self.peak_prominence_B, list):
            self.peak_prominence_B = [self.peak_prominence_B] if self.peak_prominence_B is not None else []
        self.peak_prominence_B = [v if isinstance(v, float) else float(v) for v in self.peak_prominence_B]

        super().__post_init__(**kwargs)


# Enumerations
class CommentTypesEnum(EnumDefinitionImpl):
    """
    The type of the comment
    """
    ACQUISITION = PermissibleValue(
        text="ACQUISITION",
        description="The comment is referring to the acquisition")
    PROCESSING = PermissibleValue(
        text="PROCESSING",
        description="The comment is referring to the processing")
    OTHER = PermissibleValue(
        text="OTHER",
        description="The comment is referring to something else")

    _defn = EnumDefinition(
        name="CommentTypesEnum",
        description="The type of the comment",
    )

class MicroscopeTypeEnum(EnumDefinitionImpl):
    """
    The type of the microscope
    """
    CONFOCAL = PermissibleValue(
        text="CONFOCAL",
        description="A confocal microscope")
    STED = PermissibleValue(
        text="STED",
        description="A STED microscope")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Another type of microscope")

    _defn = EnumDefinition(
        name="MicroscopeTypeEnum",
        description="The type of the microscope",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "WIDE-FIELD",
            PermissibleValue(
                text="WIDE-FIELD",
                description="A wide-field microscope"))
        setattr(cls, "3D-SIM",
            PermissibleValue(
                text="3D-SIM",
                description="A 3D-SIM microscope"))

class OMEROObjectTypeEnum(EnumDefinitionImpl):
    """
    The type of the OMERO object
    """
    IMAGE = PermissibleValue(
        text="IMAGE",
        description="An image")
    DATASET = PermissibleValue(
        text="DATASET",
        description="A dataset")
    PROJECT = PermissibleValue(
        text="PROJECT",
        description="A project")
    EXPERIMENTERGROUP = PermissibleValue(
        text="EXPERIMENTERGROUP",
        description="A group")
    EXPERIMENTER = PermissibleValue(
        text="EXPERIMENTER",
        description="An experimenter")
    TABLE = PermissibleValue(
        text="TABLE",
        description="A table")
    KEY_VALUES = PermissibleValue(
        text="KEY_VALUES",
        description="A set of key-value pairs")
    TAG = PermissibleValue(
        text="TAG",
        description="A tag")
    COMMENT = PermissibleValue(
        text="COMMENT",
        description="A comment")
    ROI = PermissibleValue(
        text="ROI",
        description="A region of interest")
    FILEANNOTATION = PermissibleValue(
        text="FILEANNOTATION",
        description="A file")

    _defn = EnumDefinition(
        name="OMEROObjectTypeEnum",
        description="The type of the OMERO object",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/name'], name="name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/description'], name="description", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/description'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.description, domain=None, range=Optional[str])

slots.excitation_wavelength_nm = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/excitation_wavelength_nm'], name="excitation_wavelength_nm", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/excitation_wavelength_nm'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.excitation_wavelength_nm, domain=None, range=Optional[float])

slots.emission_wavelength_nm = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/emission_wavelength_nm'], name="emission_wavelength_nm", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/emission_wavelength_nm'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.emission_wavelength_nm, domain=None, range=Optional[float])

slots.channel_nr = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channel_nr'], name="channel_nr", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channel_nr'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channel_nr, domain=None, range=Optional[Union[int, List[int]]])

slots.channel_name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channel_name'], name="channel_name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channel_name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channel_name, domain=None, range=Optional[Union[str, List[str]]])

slots.bit_depth = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/bit_depth'], name="bit_depth", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/bit_depth'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bit_depth, domain=None, range=Optional[int])

slots.saturation_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/saturation_threshold'], name="saturation_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/saturation_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.saturation_threshold, domain=None, range=Optional[float])

slots.sigma_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_z'], name="sigma_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sigma_z, domain=None, range=Optional[float])

slots.sigma_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_y'], name="sigma_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sigma_y, domain=None, range=Optional[float])

slots.sigma_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_x'], name="sigma_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sigma_x, domain=None, range=Optional[float])

slots.field_illumination_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/field_illumination_image'], name="field_illumination_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/field_illumination_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.field_illumination_image, domain=None, range=Union[Union[dict, Image], List[Union[dict, Image]]])

slots.corner_fraction = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/corner_fraction'], name="corner_fraction", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/corner_fraction'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.corner_fraction, domain=None, range=float)

slots.sigma = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/sigma'], name="sigma", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/sigma'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sigma, domain=None, range=float)

slots.center_region_intensity_fraction = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_region_intensity_fraction'], name="center_region_intensity_fraction", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_region_intensity_fraction'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_region_intensity_fraction, domain=None, range=Optional[Union[float, List[float]]])

slots.center_region_area_fraction = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_region_area_fraction'], name="center_region_area_fraction", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_region_area_fraction'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_region_area_fraction, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_y'], name="center_of_mass_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_y, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_y_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_y_relative'], name="center_of_mass_y_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_y_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_y_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_x'], name="center_of_mass_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_x, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_x_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_x_relative'], name="center_of_mass_x_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_x_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_x_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_distance_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_distance_relative'], name="center_of_mass_distance_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_distance_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_distance_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_geometric_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_geometric_y'], name="center_geometric_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_geometric_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_geometric_y, domain=None, range=Optional[Union[float, List[float]]])

slots.center_geometric_y_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_geometric_y_relative'], name="center_geometric_y_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_geometric_y_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_geometric_y_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_geometric_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_geometric_x'], name="center_geometric_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_geometric_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_geometric_x, domain=None, range=Optional[Union[float, List[float]]])

slots.center_geometric_x_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_geometric_x_relative'], name="center_geometric_x_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_geometric_x_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_geometric_x_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_geometric_distance_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_geometric_distance_relative'], name="center_geometric_distance_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_geometric_distance_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_geometric_distance_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_fitted_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_fitted_y'], name="center_fitted_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_fitted_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_fitted_y, domain=None, range=Optional[Union[float, List[float]]])

slots.center_fitted_y_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_fitted_y_relative'], name="center_fitted_y_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_fitted_y_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_fitted_y_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_fitted_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_fitted_x'], name="center_fitted_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_fitted_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_fitted_x, domain=None, range=Optional[Union[float, List[float]]])

slots.center_fitted_x_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_fitted_x_relative'], name="center_fitted_x_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_fitted_x_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_fitted_x_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.center_fitted_distance_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_fitted_distance_relative'], name="center_fitted_distance_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_fitted_distance_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_fitted_distance_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity'], name="max_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_y'], name="max_intensity_pos_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_y, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_y_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_y_relative'], name="max_intensity_pos_y_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_y_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_y_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_x'], name="max_intensity_pos_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_x, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_x_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_x_relative'], name="max_intensity_pos_x_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_x_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_x_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_distance_relative = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_distance_relative'], name="max_intensity_distance_relative", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_distance_relative'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_distance_relative, domain=None, range=Optional[Union[float, List[float]]])

slots.top_left_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_left_intensity_mean'], name="top_left_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_left_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_left_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.top_left_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_left_intensity_ratio'], name="top_left_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_left_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_left_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.top_center_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_center_intensity_mean'], name="top_center_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_center_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_center_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.top_center_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_center_intensity_ratio'], name="top_center_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_center_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_center_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.top_right_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_right_intensity_mean'], name="top_right_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_right_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_right_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.top_right_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/top_right_intensity_ratio'], name="top_right_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/top_right_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.top_right_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_left_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_left_intensity_mean'], name="middle_left_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_left_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_left_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_left_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_left_intensity_ratio'], name="middle_left_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_left_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_left_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_center_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_center_intensity_mean'], name="middle_center_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_center_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_center_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_center_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_center_intensity_ratio'], name="middle_center_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_center_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_center_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_right_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_right_intensity_mean'], name="middle_right_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_right_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_right_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.middle_right_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/middle_right_intensity_ratio'], name="middle_right_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/middle_right_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.middle_right_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_left_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_left_intensity_mean'], name="bottom_left_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_left_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_left_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_left_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_left_intensity_ratio'], name="bottom_left_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_left_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_left_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_center_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_center_intensity_mean'], name="bottom_center_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_center_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_center_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_center_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_center_intensity_ratio'], name="bottom_center_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_center_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_center_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_right_intensity_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_right_intensity_mean'], name="bottom_right_intensity_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_right_intensity_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_right_intensity_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.bottom_right_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/bottom_right_intensity_ratio'], name="bottom_right_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/bottom_right_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.bottom_right_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.psf_beads_images = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/psf_beads_images'], name="psf_beads_images", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/psf_beads_images'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.psf_beads_images, domain=None, range=Union[Union[dict, Image], List[Union[dict, Image]]])

slots.min_lateral_distance_factor = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/min_lateral_distance_factor'], name="min_lateral_distance_factor", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/min_lateral_distance_factor'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.min_lateral_distance_factor, domain=None, range=float)

slots.snr_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/snr_threshold'], name="snr_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/snr_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.snr_threshold, domain=None, range=float)

slots.fitting_r2_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fitting_r2_threshold'], name="fitting_r2_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fitting_r2_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fitting_r2_threshold, domain=None, range=float)

slots.intensity_robust_z_score_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_robust_z_score_threshold'], name="intensity_robust_z_score_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_robust_z_score_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_robust_z_score_threshold, domain=None, range=float)

slots.considered_valid_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_valid_count'], name="considered_valid_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_valid_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_valid_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_lateral_edge_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_lateral_edge_count'], name="considered_lateral_edge_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_lateral_edge_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_lateral_edge_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_self_proximity_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_self_proximity_count'], name="considered_self_proximity_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_self_proximity_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_self_proximity_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_axial_edge_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_axial_edge_count'], name="considered_axial_edge_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_axial_edge_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_axial_edge_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_intensity_outlier_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_intensity_outlier_count'], name="considered_intensity_outlier_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_intensity_outlier_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_intensity_outlier_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_bad_fit_z_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bad_fit_z_count'], name="considered_bad_fit_z_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bad_fit_z_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_bad_fit_z_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_bad_fit_y_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bad_fit_y_count'], name="considered_bad_fit_y_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bad_fit_y_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_bad_fit_y_count, domain=None, range=Optional[Union[int, List[int]]])

slots.considered_bad_fit_x_count = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bad_fit_x_count'], name="considered_bad_fit_x_count", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bad_fit_x_count'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.considered_bad_fit_x_count, domain=None, range=Optional[Union[int, List[int]]])

slots.intensity_max_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_max_mean'], name="intensity_max_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_max_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_max_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_max_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_max_median'], name="intensity_max_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_max_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_max_median, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_max_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_max_std'], name="intensity_max_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_max_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_max_std, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_min_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_min_mean'], name="intensity_min_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_min_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_min_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_min_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_min_median'], name="intensity_min_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_min_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_min_median, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_min_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_min_std'], name="intensity_min_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_min_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_min_std, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_std_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_std_mean'], name="intensity_std_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_std_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_std_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_std_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_std_median'], name="intensity_std_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_std_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_std_median, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_std_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/intensity_std_std'], name="intensity_std_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/intensity_std_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_std_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_z_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_z_mean'], name="fit_r2_z_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_z_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_z_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_z_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_z_median'], name="fit_r2_z_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_z_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_z_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_z_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_z_std'], name="fit_r2_z_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_z_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_z_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_y_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_y_mean'], name="fit_r2_y_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_y_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_y_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_y_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_y_median'], name="fit_r2_y_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_y_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_y_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_y_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_y_std'], name="fit_r2_y_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_y_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_y_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_x_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_x_mean'], name="fit_r2_x_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_x_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_x_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_x_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_x_median'], name="fit_r2_x_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_x_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_x_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_r2_x_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fit_r2_x_std'], name="fit_r2_x_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fit_r2_x_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_r2_x_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_z_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_z_mean'], name="fwhm_pixel_z_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_z_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_z_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_z_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_z_median'], name="fwhm_pixel_z_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_z_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_z_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_z_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_z_std'], name="fwhm_pixel_z_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_z_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_z_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_y_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_y_mean'], name="fwhm_pixel_y_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_y_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_y_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_y_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_y_median'], name="fwhm_pixel_y_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_y_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_y_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_y_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_y_std'], name="fwhm_pixel_y_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_y_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_y_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_x_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_x_mean'], name="fwhm_pixel_x_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_x_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_x_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_x_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_x_median'], name="fwhm_pixel_x_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_x_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_x_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_pixel_x_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_pixel_x_std'], name="fwhm_pixel_x_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_pixel_x_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_pixel_x_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_z_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_z_mean'], name="fwhm_micron_z_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_z_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_z_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_z_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_z_median'], name="fwhm_micron_z_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_z_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_z_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_z_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_z_std'], name="fwhm_micron_z_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_z_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_z_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_y_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_y_mean'], name="fwhm_micron_y_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_y_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_y_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_y_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_y_median'], name="fwhm_micron_y_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_y_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_y_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_y_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_y_std'], name="fwhm_micron_y_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_y_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_y_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_x_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_x_mean'], name="fwhm_micron_x_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_x_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_x_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_x_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_x_median'], name="fwhm_micron_x_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_x_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_x_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_micron_x_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_micron_x_std'], name="fwhm_micron_x_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_micron_x_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_micron_x_std, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_lateral_asymmetry_ratio_mean = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_mean'], name="fwhm_lateral_asymmetry_ratio_mean", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_mean'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_lateral_asymmetry_ratio_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_lateral_asymmetry_ratio_median = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_median'], name="fwhm_lateral_asymmetry_ratio_median", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_median'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_lateral_asymmetry_ratio_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fwhm_lateral_asymmetry_ratio_std = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_std'], name="fwhm_lateral_asymmetry_ratio_std", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/fwhm_lateral_asymmetry_ratio_std'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fwhm_lateral_asymmetry_ratio_std, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fit_r2_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fit_r2_z'], name="average_bead_fit_r2_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fit_r2_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fit_r2_z, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fit_r2_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fit_r2_y'], name="average_bead_fit_r2_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fit_r2_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fit_r2_y, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fit_r2_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fit_r2_x'], name="average_bead_fit_r2_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fit_r2_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fit_r2_x, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_pixel_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_pixel_z'], name="average_bead_fwhm_pixel_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_pixel_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_pixel_z, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_pixel_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_pixel_y'], name="average_bead_fwhm_pixel_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_pixel_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_pixel_y, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_pixel_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_pixel_x'], name="average_bead_fwhm_pixel_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_pixel_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_pixel_x, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_micron_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_micron_z'], name="average_bead_fwhm_micron_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_micron_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_micron_z, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_micron_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_micron_y'], name="average_bead_fwhm_micron_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_micron_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_micron_y, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_micron_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_micron_x'], name="average_bead_fwhm_micron_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_micron_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_micron_x, domain=None, range=Optional[Union[float, List[float]]])

slots.average_bead_fwhm_lateral_asymmetry_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead_fwhm_lateral_asymmetry_ratio'], name="average_bead_fwhm_lateral_asymmetry_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead_fwhm_lateral_asymmetry_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.average_bead_fwhm_lateral_asymmetry_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.argolight_b_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/argolight_b_image'], name="argolight_b_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/argolight_b_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolight_b_image, domain=None, range=Union[dict, Image])

slots.spots_distance = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_distance'], name="spots_distance", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_distance'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.spots_distance, domain=None, range=float)

slots.lower_threshold_correction_factors = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/lower_threshold_correction_factors'], name="lower_threshold_correction_factors", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/lower_threshold_correction_factors'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.lower_threshold_correction_factors, domain=None, range=Optional[Union[float, List[float]]])

slots.upper_threshold_correction_factors = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/upper_threshold_correction_factors'], name="upper_threshold_correction_factors", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/upper_threshold_correction_factors'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.upper_threshold_correction_factors, domain=None, range=Optional[Union[float, List[float]]])

slots.remove_center_cross = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/remove_center_cross'], name="remove_center_cross", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/remove_center_cross'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.remove_center_cross, domain=None, range=Optional[Union[bool, Bool]])

slots.nr_of_spots = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/nr_of_spots'], name="nr_of_spots", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/nr_of_spots'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_spots, domain=None, range=Optional[Union[int, List[int]]])

slots.intensity_max_spot = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_max_spot'], name="intensity_max_spot", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_max_spot'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_max_spot, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_max_spot_roi = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_max_spot_roi'], name="intensity_max_spot_roi", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_max_spot_roi'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_max_spot_roi, domain=None, range=Optional[Union[int, List[int]]])

slots.intensity_min_spot = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_min_spot'], name="intensity_min_spot", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_min_spot'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_min_spot, domain=None, range=Optional[Union[float, List[float]]])

slots.intensity_min_spot_roi = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_min_spot_roi'], name="intensity_min_spot_roi", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_min_spot_roi'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_min_spot_roi, domain=None, range=Optional[Union[int, List[int]]])

slots.mean_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mean_intensity'], name="mean_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mean_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mean_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.median_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/median_intensity'], name="median_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/median_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.median_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.std_mean_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/std_mean_intensity'], name="std_mean_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/std_mean_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.std_mean_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.mad_mean_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mad_mean_intensity'], name="mad_mean_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mad_mean_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mad_mean_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.min_max_intensity_ratio = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/min_max_intensity_ratio'], name="min_max_intensity_ratio", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/min_max_intensity_ratio'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.min_max_intensity_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.channel_A = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/channel_A'], name="channel_A", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/channel_A'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channel_A, domain=None, range=Optional[Union[int, List[int]]])

slots.channel_B = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/channel_B'], name="channel_B", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/channel_B'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channel_B, domain=None, range=Optional[Union[int, List[int]]])

slots.mean_3d_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mean_3d_dist'], name="mean_3d_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mean_3d_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mean_3d_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.median_3d_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/median_3d_dist'], name="median_3d_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/median_3d_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.median_3d_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.std_3d_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/std_3d_dist'], name="std_3d_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/std_3d_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.std_3d_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.mad_3d_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mad_3d_dist'], name="mad_3d_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mad_3d_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mad_3d_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.mean_z_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mean_z_dist'], name="mean_z_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mean_z_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mean_z_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.median_z_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/median_z_dist'], name="median_z_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/median_z_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.median_z_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.std_z_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/std_z_dist'], name="std_z_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/std_z_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.std_z_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.mad_z_dist = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/mad_z_dist'], name="mad_z_dist", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/mad_z_dist'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mad_z_dist, domain=None, range=Optional[Union[float, List[float]]])

slots.argolight_e_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/argolight_e_image'], name="argolight_e_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/argolight_e_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolight_e_image, domain=None, range=Union[dict, Image])

slots.orientation_axis = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/orientation_axis'], name="orientation_axis", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/orientation_axis'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.orientation_axis, domain=None, range=int)

slots.measured_band = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/measured_band'], name="measured_band", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/measured_band'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.measured_band, domain=None, range=float)

slots.prominence_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/prominence_threshold'], name="prominence_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/prominence_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.prominence_threshold, domain=None, range=float)

slots.focus_slice = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/focus_slice'], name="focus_slice", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/focus_slice'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.focus_slice, domain=None, range=Optional[Union[int, List[int]]])

slots.rayleigh_resolution_pixels = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/rayleigh_resolution_pixels'], name="rayleigh_resolution_pixels", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/rayleigh_resolution_pixels'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rayleigh_resolution_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.rayleigh_resolution_microns = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/rayleigh_resolution_microns'], name="rayleigh_resolution_microns", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/rayleigh_resolution_microns'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rayleigh_resolution_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_position_A = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_position_A'], name="peak_position_A", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_position_A'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_position_A, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_position_B = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_position_B'], name="peak_position_B", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_position_B'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_position_B, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_height_A = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_height_A'], name="peak_height_A", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_height_A'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_height_A, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_height_B = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_height_B'], name="peak_height_B", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_height_B'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_height_B, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_prominence_A = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_prominence_A'], name="peak_prominence_A", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_prominence_A'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_prominence_A, domain=None, range=Optional[Union[float, List[float]]])

slots.peak_prominence_B = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peak_prominence_B'], name="peak_prominence_B", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peak_prominence_B'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.peak_prominence_B, domain=None, range=Optional[Union[float, List[float]]])

slots.dataReference__data_uri = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data_uri'], name="dataReference__data_uri", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data_uri'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.dataReference__data_uri, domain=None, range=Optional[str])

slots.dataReference__omero_host = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/omero_host'], name="dataReference__omero_host", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/omero_host'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.dataReference__omero_host, domain=None, range=Optional[str])

slots.dataReference__omero_port = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/omero_port'], name="dataReference__omero_port", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/omero_port'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.dataReference__omero_port, domain=None, range=Optional[int])

slots.dataReference__omero_object_type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/omero_object_type'], name="dataReference__omero_object_type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/omero_object_type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.dataReference__omero_object_type, domain=None, range=Optional[Union[str, "OMEROObjectTypeEnum"]])

slots.dataReference__omero_object_id = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/omero_object_id'], name="dataReference__omero_object_id", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/omero_object_id'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.dataReference__omero_object_id, domain=None, range=Optional[int])

slots.metricsObject__data_reference = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data_reference'], name="metricsObject__data_reference", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data_reference'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsObject__data_reference, domain=None, range=Optional[Union[dict, DataReference]])

slots.metricsObject__linked_references = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/linked_references'], name="metricsObject__linked_references", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/linked_references'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsObject__linked_references, domain=None, range=Optional[Union[Union[dict, DataReference], List[Union[dict, DataReference]]]])

slots.microscopeCollection__microscopes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/microscopes'], name="microscopeCollection__microscopes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/microscopes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscopeCollection__microscopes, domain=None, range=Union[Union[dict, Microscope], List[Union[dict, Microscope]]])

slots.microscope__type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/type'], name="microscope__type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__type, domain=None, range=Optional[Union[str, "MicroscopeTypeEnum"]])

slots.microscope__manufacturer = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/manufacturer'], name="microscope__manufacturer", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/manufacturer'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__manufacturer, domain=None, range=Optional[str])

slots.microscope__model = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/model'], name="microscope__model", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/model'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__model, domain=None, range=Optional[str])

slots.microscope__serial_number = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/serial_number'], name="microscope__serial_number", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/serial_number'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__serial_number, domain=None, range=Optional[str])

slots.microscope__comments = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comments'], name="microscope__comments", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comments'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__comments, domain=None, range=Optional[Union[Union[dict, Comment], List[Union[dict, Comment]]]])

slots.sample__type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/type'], name="sample__type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sample__type, domain=None, range=str)

slots.sample__protocol = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/protocol'], name="sample__protocol", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/protocol'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sample__protocol, domain=None, range=Union[str, ProtocolUrl])

slots.protocol__version = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/version'], name="protocol__version", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/version'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.protocol__version, domain=None, range=str)

slots.protocol__authors = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/authors'], name="protocol__authors", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/authors'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.protocol__authors, domain=None, range=Optional[Union[Union[str, ExperimenterOrcid], List[Union[str, ExperimenterOrcid]]]])

slots.protocol__url = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/url'], name="protocol__url", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/url'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.protocol__url, domain=None, range=URIRef)

slots.experimenter__name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/name'], name="experimenter__name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.experimenter__name, domain=None, range=str)

slots.experimenter__orcid = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/orcid'], name="experimenter__orcid", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/orcid'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.experimenter__orcid, domain=None, range=URIRef)

slots.comment__datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/datetime'], name="comment__datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__datetime, domain=None, range=Union[str, XSDDateTime])

slots.comment__author = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/author'], name="comment__author", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/author'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__author, domain=None, range=Optional[Union[str, ExperimenterOrcid]])

slots.comment__comment_type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comment_type'], name="comment__comment_type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comment_type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__comment_type, domain=None, range=Union[str, "CommentTypesEnum"])

slots.comment__text = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/text'], name="comment__text", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/text'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__text, domain=None, range=str)

slots.metricsDatasetCollection__datasets = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/datasets'], name="metricsDatasetCollection__datasets", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/datasets'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDatasetCollection__datasets, domain=None, range=Optional[Union[Union[dict, MetricsDataset], List[Union[dict, MetricsDataset]]]])

slots.harmonizedMetricsDatasetCollection__dataset_class = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/dataset_class'], name="harmonizedMetricsDatasetCollection__dataset_class", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/dataset_class'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.harmonizedMetricsDatasetCollection__dataset_class, domain=None, range=str)

slots.metricsDataset__microscope = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/microscope'], name="metricsDataset__microscope", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/microscope'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__microscope, domain=None, range=Union[dict, Microscope])

slots.metricsDataset__sample = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sample'], name="metricsDataset__sample", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sample'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__sample, domain=None, range=Optional[Union[dict, Sample]])

slots.metricsDataset__experimenter = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/experimenter'], name="metricsDataset__experimenter", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/experimenter'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__experimenter, domain=None, range=Optional[Union[str, ExperimenterOrcid]])

slots.metricsDataset__acquisition_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/acquisition_datetime'], name="metricsDataset__acquisition_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/acquisition_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__acquisition_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metricsDataset__processed = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processed'], name="metricsDataset__processed", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processed'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__processed, domain=None, range=Union[bool, Bool])

slots.metricsDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/input'], name="metricsDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__input, domain=None, range=Union[dict, MetricsInput])

slots.metricsDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/output'], name="metricsDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__output, domain=None, range=Optional[Union[dict, MetricsOutput]])

slots.metricsOutput__processing_application = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_application'], name="metricsOutput__processing_application", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_application'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__processing_application, domain=None, range=Union[str, List[str]])

slots.metricsOutput__processing_version = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_version'], name="metricsOutput__processing_version", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_version'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__processing_version, domain=None, range=Union[str, List[str]])

slots.metricsOutput__processing_entity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_entity'], name="metricsOutput__processing_entity", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_entity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__processing_entity, domain=None, range=Optional[Union[str, List[str]]])

slots.metricsOutput__processing_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_datetime'], name="metricsOutput__processing_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__processing_datetime, domain=None, range=Union[str, XSDDateTime])

slots.metricsOutput__processing_log = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_log'], name="metricsOutput__processing_log", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_log'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__processing_log, domain=None, range=Optional[str])

slots.metricsOutput__warnings = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/warnings'], name="metricsOutput__warnings", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/warnings'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__warnings, domain=None, range=Optional[Union[str, List[str]]])

slots.metricsOutput__errors = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/errors'], name="metricsOutput__errors", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/errors'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__errors, domain=None, range=Optional[Union[str, List[str]]])

slots.metricsOutput__validated = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/validated'], name="metricsOutput__validated", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/validated'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__validated, domain=None, range=Union[bool, Bool])

slots.metricsOutput__validation_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/validation_datetime'], name="metricsOutput__validation_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/validation_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__validation_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metricsOutput__comment = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comment'], name="metricsOutput__comment", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comment'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsOutput__comment, domain=None, range=Optional[Union[dict, Comment]])

slots.image__voxel_size_x_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_x_micron'], name="image__voxel_size_x_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_x_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__voxel_size_x_micron, domain=None, range=Optional[float])

slots.image__voxel_size_y_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_y_micron'], name="image__voxel_size_y_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_y_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__voxel_size_y_micron, domain=None, range=Optional[float])

slots.image__voxel_size_z_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_z_micron'], name="image__voxel_size_z_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_z_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__voxel_size_z_micron, domain=None, range=Optional[float])

slots.image__shape_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_x'], name="image__shape_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__shape_x, domain=None, range=int)

slots.image__shape_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_y'], name="image__shape_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__shape_y, domain=None, range=int)

slots.image__shape_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_z'], name="image__shape_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__shape_z, domain=None, range=int)

slots.image__shape_c = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_c'], name="image__shape_c", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_c'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__shape_c, domain=None, range=int)

slots.image__shape_t = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_t'], name="image__shape_t", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_t'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__shape_t, domain=None, range=int)

slots.image__time_series = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/time_series'], name="image__time_series", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/time_series'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__time_series, domain=None, range=Optional[Union[dict, TimeSeries]])

slots.image__channel_series = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channel_series'], name="image__channel_series", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channel_series'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__channel_series, domain=None, range=Optional[Union[dict, ChannelSeries]])

slots.image__acquisition_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/acquisition_datetime'], name="image__acquisition_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/acquisition_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__acquisition_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.image__source_images = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/source_images'], name="image__source_images", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/source_images'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__source_images, domain=None, range=Optional[Union[Union[dict, DataReference], List[Union[dict, DataReference]]]])

slots.image__array_data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/array_data'], name="image__array_data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/array_data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image__array_data, domain=None, range=Optional[Union[dict, MetaObject]])

slots.channelSeries__channels = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channels'], name="channelSeries__channels", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channels'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channelSeries__channels, domain=None, range=Union[Union[dict, Channel], List[Union[dict, Channel]]])

slots.timeSeries__values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/values'], name="timeSeries__values", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.timeSeries__values, domain=None, range=Union[float, List[float]])

slots.column__source_reference = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/source_reference'], name="column__source_reference", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/source_reference'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__source_reference, domain=None, range=Optional[Union[dict, DataReference]])

slots.column__data_type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data_type'], name="column__data_type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data_type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__data_type, domain=None, range=str)

slots.column__values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/values'], name="column__values", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__values, domain=None, range=Optional[Union[str, List[str]]])

slots.roi__points = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/points'], name="roi__points", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/points'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__points, domain=None, range=Optional[Union[Union[dict, Point], List[Union[dict, Point]]]])

slots.roi__lines = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/lines'], name="roi__lines", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/lines'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__lines, domain=None, range=Optional[Union[Union[dict, Line], List[Union[dict, Line]]]])

slots.roi__rectangles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/rectangles'], name="roi__rectangles", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/rectangles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__rectangles, domain=None, range=Optional[Union[Union[dict, Rectangle], List[Union[dict, Rectangle]]]])

slots.roi__ellipses = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/ellipses'], name="roi__ellipses", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/ellipses'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__ellipses, domain=None, range=Optional[Union[Union[dict, Ellipse], List[Union[dict, Ellipse]]]])

slots.roi__polygons = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/polygons'], name="roi__polygons", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/polygons'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__polygons, domain=None, range=Optional[Union[Union[dict, Polygon], List[Union[dict, Polygon]]]])

slots.roi__masks = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/masks'], name="roi__masks", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/masks'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__masks, domain=None, range=Optional[Union[Union[dict, Mask], List[Union[dict, Mask]]]])

slots.shape__z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/z'], name="shape__z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__z, domain=None, range=Optional[float])

slots.shape__c = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/c'], name="shape__c", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/c'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__c, domain=None, range=Optional[int])

slots.shape__t = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/t'], name="shape__t", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/t'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__t, domain=None, range=Optional[int])

slots.shape__fill_color = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/fill_color'], name="shape__fill_color", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/fill_color'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__fill_color, domain=None, range=Optional[Union[dict, Color]])

slots.shape__stroke_color = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/stroke_color'], name="shape__stroke_color", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/stroke_color'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__stroke_color, domain=None, range=Optional[Union[dict, Color]])

slots.shape__stroke_width = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/stroke_width'], name="shape__stroke_width", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/stroke_width'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__stroke_width, domain=None, range=Optional[int])

slots.point__y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y'], name="point__y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.point__y, domain=None, range=float)

slots.point__x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x'], name="point__x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.point__x, domain=None, range=float)

slots.line__x1 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x1'], name="line__x1", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x1'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.line__x1, domain=None, range=float)

slots.line__y1 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y1'], name="line__y1", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y1'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.line__y1, domain=None, range=float)

slots.line__x2 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x2'], name="line__x2", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x2'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.line__x2, domain=None, range=float)

slots.line__y2 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y2'], name="line__y2", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y2'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.line__y2, domain=None, range=float)

slots.rectangle__x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x'], name="rectangle__x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rectangle__x, domain=None, range=float)

slots.rectangle__y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y'], name="rectangle__y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rectangle__y, domain=None, range=float)

slots.rectangle__w = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/w'], name="rectangle__w", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/w'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rectangle__w, domain=None, range=float)

slots.rectangle__h = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/h'], name="rectangle__h", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/h'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.rectangle__h, domain=None, range=float)

slots.ellipse__x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x'], name="ellipse__x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ellipse__x, domain=None, range=float)

slots.ellipse__y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y'], name="ellipse__y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ellipse__y, domain=None, range=float)

slots.ellipse__x_rad = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x_rad'], name="ellipse__x_rad", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x_rad'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ellipse__x_rad, domain=None, range=float)

slots.ellipse__y_rad = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y_rad'], name="ellipse__y_rad", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y_rad'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ellipse__y_rad, domain=None, range=float)

slots.polygon__vertexes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/vertexes'], name="polygon__vertexes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/vertexes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.polygon__vertexes, domain=None, range=Union[Union[dict, Vertex], List[Union[dict, Vertex]]])

slots.polygon__is_open = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/is_open'], name="polygon__is_open", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/is_open'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.polygon__is_open, domain=None, range=Union[bool, Bool])

slots.vertex__x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x'], name="vertex__x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.vertex__x, domain=None, range=float)

slots.vertex__y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y'], name="vertex__y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.vertex__y, domain=None, range=float)

slots.mask__y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/y'], name="mask__y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mask__y, domain=None, range=int)

slots.mask__x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/x'], name="mask__x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mask__x, domain=None, range=int)

slots.mask__mask = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/mask'], name="mask__mask", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/mask'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.mask__mask, domain=None, range=Optional[Union[dict, ImageMask]])

slots.color__r = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/r'], name="color__r", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/r'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.color__r, domain=None, range=int)

slots.color__g = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/g'], name="color__g", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/g'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.color__g, domain=None, range=int)

slots.color__b = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/b'], name="color__b", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/b'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.color__b, domain=None, range=int)

slots.color__alpha = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/alpha'], name="color__alpha", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/alpha'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.color__alpha, domain=None, range=Optional[int])

slots.profilesIntensity__intensity_profiles_table = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/intensity_profiles_table'], name="profilesIntensity__intensity_profiles_table", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/intensity_profiles_table'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.profilesIntensity__intensity_profiles_table, domain=None, range=Optional[Union[dict, Table]])

slots.roiMeasurements__measurements_table = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/measurements_table'], name="roiMeasurements__measurements_table", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/measurements_table'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roiMeasurements__measurements_table, domain=None, range=Optional[Union[dict, Table]])

slots.tag__description = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/description'], name="tag__description", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/description'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tag__description, domain=None, range=Optional[str])

slots.table__columns = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/columns'], name="table__columns", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/columns'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.table__columns, domain=None, range=Union[Union[dict, Column], List[Union[dict, Column]]])

slots.table__table_data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/table_data'], name="table__table_data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/table_data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.table__table_data, domain=None, range=Optional[Union[dict, MetaObject]])

slots.fieldIlluminationDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/input'], name="fieldIlluminationDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationDataset__input, domain=None, range=Optional[Union[dict, FieldIlluminationInput]])

slots.fieldIlluminationDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/output'], name="fieldIlluminationDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationDataset__output, domain=None, range=Optional[Union[dict, FieldIlluminationOutput]])

slots.fieldIlluminationOutput__key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/key_values'], name="fieldIlluminationOutput__key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__key_values, domain=None, range=Optional[Union[dict, FieldIlluminationKeyValues]])

slots.fieldIlluminationOutput__intensity_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/intensity_profiles'], name="fieldIlluminationOutput__intensity_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/intensity_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__intensity_profiles, domain=None, range=Optional[Union[Union[dict, Table], List[Union[dict, Table]]]])

slots.fieldIlluminationOutput__roi_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_profiles'], name="fieldIlluminationOutput__roi_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_profiles, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.fieldIlluminationOutput__roi_corners = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_corners'], name="fieldIlluminationOutput__roi_corners", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_corners'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_corners, domain=None, range=Optional[Union[dict, Roi]])

slots.fieldIlluminationOutput__roi_centers_of_mass = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_centers_of_mass'], name="fieldIlluminationOutput__roi_centers_of_mass", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_centers_of_mass'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_centers_of_mass, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.fieldIlluminationOutput__roi_centers_geometric = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_centers_geometric'], name="fieldIlluminationOutput__roi_centers_geometric", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_centers_geometric'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_centers_geometric, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.fieldIlluminationOutput__roi_centers_fitted = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_centers_fitted'], name="fieldIlluminationOutput__roi_centers_fitted", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_centers_fitted'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_centers_fitted, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.fieldIlluminationOutput__roi_centers_max_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_centers_max_intensity'], name="fieldIlluminationOutput__roi_centers_max_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_centers_max_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_centers_max_intensity, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.fieldIlluminationOutput__roi_center_region = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/roi_center_region'], name="fieldIlluminationOutput__roi_center_region", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/roi_center_region'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__roi_center_region, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/input'], name="pSFBeadsDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsDataset__input, domain=None, range=Optional[Union[dict, PSFBeadsInput]])

slots.pSFBeadsDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/output'], name="pSFBeadsDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsDataset__output, domain=None, range=Optional[Union[dict, PSFBeadsOutput]])

slots.pSFBeadsOutput__analyzed_bead_centers = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/analyzed_bead_centers'], name="pSFBeadsOutput__analyzed_bead_centers", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/analyzed_bead_centers'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__analyzed_bead_centers, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_lateral_edge = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_lateral_edge'], name="pSFBeadsOutput__considered_bead_centers_lateral_edge", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_lateral_edge'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_lateral_edge, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_self_proximity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_self_proximity'], name="pSFBeadsOutput__considered_bead_centers_self_proximity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_self_proximity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_self_proximity, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_axial_edge = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_axial_edge'], name="pSFBeadsOutput__considered_bead_centers_axial_edge", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_axial_edge'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_axial_edge, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_intensity_outlier = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_intensity_outlier'], name="pSFBeadsOutput__considered_bead_centers_intensity_outlier", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_intensity_outlier'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_intensity_outlier, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_z_fit_quality = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_z_fit_quality'], name="pSFBeadsOutput__considered_bead_centers_z_fit_quality", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_z_fit_quality'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_z_fit_quality, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_y_fit_quality = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_y_fit_quality'], name="pSFBeadsOutput__considered_bead_centers_y_fit_quality", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_y_fit_quality'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_y_fit_quality, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__considered_bead_centers_x_fit_quality = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/considered_bead_centers_x_fit_quality'], name="pSFBeadsOutput__considered_bead_centers_x_fit_quality", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/considered_bead_centers_x_fit_quality'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centers_x_fit_quality, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.pSFBeadsOutput__key_measurements = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/key_measurements'], name="pSFBeadsOutput__key_measurements", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/key_measurements'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__key_measurements, domain=None, range=Optional[Union[dict, PSFBeadsKeyMeasurements]])

slots.pSFBeadsOutput__bead_properties = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/bead_properties'], name="pSFBeadsOutput__bead_properties", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/bead_properties'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_properties, domain=None, range=Optional[Union[dict, Table]])

slots.pSFBeadsOutput__bead_z_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/bead_z_profiles'], name="pSFBeadsOutput__bead_z_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/bead_z_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_z_profiles, domain=None, range=Optional[Union[dict, Table]])

slots.pSFBeadsOutput__bead_y_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/bead_y_profiles'], name="pSFBeadsOutput__bead_y_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/bead_y_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_y_profiles, domain=None, range=Optional[Union[dict, Table]])

slots.pSFBeadsOutput__bead_x_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/bead_x_profiles'], name="pSFBeadsOutput__bead_x_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/bead_x_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_x_profiles, domain=None, range=Optional[Union[dict, Table]])

slots.pSFBeadsOutput__average_bead = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/psf_beads_schema/average_bead'], name="pSFBeadsOutput__average_bead", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/psf_beads_schema/average_bead'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__average_bead, domain=None, range=Optional[Union[dict, Image]])

slots.argolightBDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/input'], name="argolightBDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBDataset__input, domain=None, range=Optional[Union[dict, ArgolightBInput]])

slots.argolightBDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/output'], name="argolightBDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBDataset__output, domain=None, range=Optional[Union[dict, ArgolightBOutput]])

slots.argolightBOutput__spots_labels_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_labels_image'], name="argolightBOutput__spots_labels_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_labels_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_labels_image, domain=None, range=Optional[Union[dict, ImageMask]])

slots.argolightBOutput__spots_centers_of_mass = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_centers_of_mass'], name="argolightBOutput__spots_centers_of_mass", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_centers_of_mass'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_centers_of_mass, domain=None, range=Optional[Union[Union[dict, ArgolightBCentersOfMass], List[Union[dict, ArgolightBCentersOfMass]]]])

slots.argolightBOutput__intensity_key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_key_values'], name="argolightBOutput__intensity_key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__intensity_key_values, domain=None, range=Optional[Union[dict, ArgolightBIntensityKeyValues]])

slots.argolightBOutput__distance_key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/distance_key_values'], name="argolightBOutput__distance_key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/distance_key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__distance_key_values, domain=None, range=Optional[Union[dict, ArgolightBDistanceKeyValues]])

slots.argolightBOutput__spots_properties = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_properties'], name="argolightBOutput__spots_properties", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_properties'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_properties, domain=None, range=Optional[Union[dict, Table]])

slots.argolightBOutput__spots_distances = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_distances'], name="argolightBOutput__spots_distances", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_distances'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_distances, domain=None, range=Optional[Union[dict, Table]])

slots.argolightEDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/input'], name="argolightEDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEDataset__input, domain=None, range=Optional[Union[dict, ArgolightEInput]])

slots.argolightEDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/output'], name="argolightEDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEDataset__output, domain=None, range=Optional[Union[dict, ArgolightEOutput]])

slots.argolightEOutput__peaks_rois = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peaks_rois'], name="argolightEOutput__peaks_rois", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peaks_rois'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__peaks_rois, domain=None, range=Optional[Union[Union[dict, Roi], List[Union[dict, Roi]]]])

slots.argolightEOutput__key_measurements = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/key_measurements'], name="argolightEOutput__key_measurements", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/key_measurements'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__key_measurements, domain=None, range=Optional[Union[dict, ArgolightEKeyValues]])

slots.argolightEOutput__intensity_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_profiles'], name="argolightEOutput__intensity_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__intensity_profiles, domain=None, range=Optional[Union[dict, Table]])

slots.Tag_name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/name'], name="Tag_name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.Tag_name, domain=Tag, range=str)

slots.FieldIlluminationInput_saturation_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/saturation_threshold'], name="FieldIlluminationInput_saturation_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/saturation_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.FieldIlluminationInput_saturation_threshold, domain=FieldIlluminationInput, range=float)

slots.PSFBeadsInput_sigma_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_z'], name="PSFBeadsInput_sigma_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.PSFBeadsInput_sigma_z, domain=PSFBeadsInput, range=float)

slots.PSFBeadsInput_sigma_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_y'], name="PSFBeadsInput_sigma_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.PSFBeadsInput_sigma_y, domain=PSFBeadsInput, range=float)

slots.PSFBeadsInput_sigma_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_x'], name="PSFBeadsInput_sigma_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.PSFBeadsInput_sigma_x, domain=PSFBeadsInput, range=float)

slots.ArgolightBInput_saturation_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/saturation_threshold'], name="ArgolightBInput_saturation_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/saturation_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ArgolightBInput_saturation_threshold, domain=ArgolightBInput, range=float)

slots.ArgolightBInput_sigma_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_z'], name="ArgolightBInput_sigma_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ArgolightBInput_sigma_z, domain=ArgolightBInput, range=float)

slots.ArgolightBInput_sigma_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_y'], name="ArgolightBInput_sigma_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ArgolightBInput_sigma_y, domain=ArgolightBInput, range=float)

slots.ArgolightBInput_sigma_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sigma_x'], name="ArgolightBInput_sigma_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sigma_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ArgolightBInput_sigma_x, domain=ArgolightBInput, range=float)

slots.ArgolightEInput_saturation_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/saturation_threshold'], name="ArgolightEInput_saturation_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/saturation_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.ArgolightEInput_saturation_threshold, domain=ArgolightEInput, range=float)