# Auto generated from microscopemetrics_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-02-07T12:12:49
# Schema: microscopemetrics-schema
#
# id: https://w3id.org/MontpellierRessourcesImagerie/microscopemetrics-schema
# description: A schema for microscope-metrics, a python package for microscope QC
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
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
MICROSCOPEMETRICS_SCHEMA = CurieNamespace('microscopemetrics_schema', 'https://w3id.org/MontpellierRessourcesImagerie/microscopemetrics-schema/')
DEFAULT_ = MICROSCOPEMETRICS_SCHEMA


# Types

# Class references
class MicroscopeId(extended_str):
    pass


class SampleType(extended_str):
    pass


class ProtocolUrl(extended_str):
    pass


class ExperimenterOrcid(extended_str):
    pass


class ImageImageUrl(extended_str):
    pass


class ImageAsNumpyImageUrl(ImageImageUrl):
    pass


class ImageInlineImageUrl(ImageImageUrl):
    pass


class ImageMaskImageUrl(ImageInlineImageUrl):
    pass


class Image2DImageUrl(ImageInlineImageUrl):
    pass


class Image5DImageUrl(ImageInlineImageUrl):
    pass


class RoiLabel(extended_str):
    pass


class ShapeLabel(extended_str):
    pass


class PointLabel(ShapeLabel):
    pass


class LineLabel(ShapeLabel):
    pass


class RectangleLabel(ShapeLabel):
    pass


class EllipseLabel(ShapeLabel):
    pass


class PolygonLabel(ShapeLabel):
    pass


class MaskLabel(ShapeLabel):
    pass


class RoiMassCentersLabel(RoiLabel):
    pass


class RoiGeometricCentersLabel(RoiLabel):
    pass


class RoiProfilesLabel(RoiLabel):
    pass


class RoiMeasurementsLabel(RoiLabel):
    pass


class TagId(extended_int):
    pass


class ColumnName(extended_str):
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


class MetricsObject(NamedObject):
    """
    A base object for all microscope-metrics objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsObject"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsObject"
    class_name: ClassVar[str] = "MetricsObject"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsObject


class Device(MetricsObject):
    """
    A base object for all microscope-metrics devices
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Device"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Device


@dataclass
class Microscope(Device):
    """
    A microscope
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Microscope"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Microscope"
    class_name: ClassVar[str] = "Microscope"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Microscope

    id: Union[str, MicroscopeId] = None
    type: Optional[Union[str, "MicroscopeType"]] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    url: Optional[str] = None
    comment: Optional[Union[Union[dict, "Comment"], List[Union[dict, "Comment"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicroscopeId):
            self.id = MicroscopeId(self.id)

        if self.type is not None and not isinstance(self.type, MicroscopeType):
            self.type = MicroscopeType(self.type)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        self._normalize_inlined_as_dict(slot_name="comment", slot_type=Comment, key_name="datetime", keyed=False)

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

    type: Union[str, SampleType] = None
    protocol: Union[str, ProtocolUrl] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SampleType):
            self.type = SampleType(self.type)

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
    text: str = None
    comment_type: Optional[Union[str, "CommentTypes"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datetime):
            self.MissingRequiredField("datetime")
        if not isinstance(self.datetime, XSDDateTime):
            self.datetime = XSDDateTime(self.datetime)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.comment_type is not None and not isinstance(self.comment_type, CommentTypes):
            self.comment_type = CommentTypes(self.comment_type)

        super().__post_init__(**kwargs)


@dataclass
class MetricsDataset(NamedObject):
    """
    A base object on which microscope-metrics runs the analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsDataset"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsDataset"
    class_name: ClassVar[str] = "MetricsDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsDataset

    microscope: Union[str, MicroscopeId] = None
    processed: Union[bool, Bool] = False
    sample: Optional[Union[str, SampleType]] = None
    experimenter: Optional[Union[Union[str, ExperimenterOrcid], List[Union[str, ExperimenterOrcid]]]] = empty_list()
    acquisition_datetime: Optional[Union[str, XSDDateTime]] = None
    processing_datetime: Optional[Union[str, XSDDateTime]] = None
    processing_log: Optional[str] = None
    comment: Optional[Union[Union[dict, Comment], List[Union[dict, Comment]]]] = empty_list()
    input: Optional[Union[dict, "MetricsInput"]] = None
    output: Optional[Union[dict, "MetricsOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.microscope):
            self.MissingRequiredField("microscope")
        if not isinstance(self.microscope, MicroscopeId):
            self.microscope = MicroscopeId(self.microscope)

        if self._is_empty(self.processed):
            self.MissingRequiredField("processed")
        if not isinstance(self.processed, Bool):
            self.processed = Bool(self.processed)

        if self.sample is not None and not isinstance(self.sample, SampleType):
            self.sample = SampleType(self.sample)

        if not isinstance(self.experimenter, list):
            self.experimenter = [self.experimenter] if self.experimenter is not None else []
        self.experimenter = [v if isinstance(v, ExperimenterOrcid) else ExperimenterOrcid(v) for v in self.experimenter]

        if self.acquisition_datetime is not None and not isinstance(self.acquisition_datetime, XSDDateTime):
            self.acquisition_datetime = XSDDateTime(self.acquisition_datetime)

        if self.processing_datetime is not None and not isinstance(self.processing_datetime, XSDDateTime):
            self.processing_datetime = XSDDateTime(self.processing_datetime)

        if self.processing_log is not None and not isinstance(self.processing_log, str):
            self.processing_log = str(self.processing_log)

        self._normalize_inlined_as_dict(slot_name="comment", slot_type=Comment, key_name="datetime", keyed=False)

        if self.input is not None and not isinstance(self.input, MetricsInput):
            self.input = MetricsInput()

        if self.output is not None and not isinstance(self.output, MetricsOutput):
            self.output = MetricsOutput()

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


class MetricsOutput(YAMLRoot):
    """
    An abstract class for analysis outputs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/MetricsOutput"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/MetricsOutput"
    class_name: ClassVar[str] = "MetricsOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.MetricsOutput


@dataclass
class Image(MetricsObject):
    """
    A base object for all microscope-metrics images
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Image"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Image

    image_url: Union[str, ImageImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1
    source_image_url: Optional[Union[str, List[str]]] = empty_list()
    voxel_size_x_micron: Optional[float] = None
    voxel_size_y_micron: Optional[float] = None
    voxel_size_z_micron: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image_url):
            self.MissingRequiredField("image_url")
        if not isinstance(self.image_url, ImageImageUrl):
            self.image_url = ImageImageUrl(self.image_url)

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

        if not isinstance(self.source_image_url, list):
            self.source_image_url = [self.source_image_url] if self.source_image_url is not None else []
        self.source_image_url = [v if isinstance(v, str) else str(v) for v in self.source_image_url]

        if self.voxel_size_x_micron is not None and not isinstance(self.voxel_size_x_micron, float):
            self.voxel_size_x_micron = float(self.voxel_size_x_micron)

        if self.voxel_size_y_micron is not None and not isinstance(self.voxel_size_y_micron, float):
            self.voxel_size_y_micron = float(self.voxel_size_y_micron)

        if self.voxel_size_z_micron is not None and not isinstance(self.voxel_size_z_micron, float):
            self.voxel_size_z_micron = float(self.voxel_size_z_micron)

        super().__post_init__(**kwargs)


@dataclass
class ImageAsNumpy(Image):
    """
    An image as a numpy array in TZYXC order
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ImageAsNumpy"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ImageAsNumpy"
    class_name: ClassVar[str] = "ImageAsNumpy"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ImageAsNumpy

    image_url: Union[str, ImageAsNumpyImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1
    data: Optional[Union[dict, MetaObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image_url):
            self.MissingRequiredField("image_url")
        if not isinstance(self.image_url, ImageAsNumpyImageUrl):
            self.image_url = ImageAsNumpyImageUrl(self.image_url)

        super().__post_init__(**kwargs)


@dataclass
class ImageInline(Image):
    """
    A base object for all microscope-metrics images that are stored as arrays in line
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ImageInline"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ImageInline"
    class_name: ClassVar[str] = "ImageInline"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ImageInline

    image_url: Union[str, ImageInlineImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1

@dataclass
class ImageMask(ImageInline):
    """
    A base object for all microscope-metrics masks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ImageMask"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ImageMask"
    class_name: ClassVar[str] = "ImageMask"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ImageMask

    image_url: Union[str, ImageMaskImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    data: Union[Union[bool, Bool], List[Union[bool, Bool]]] = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image_url):
            self.MissingRequiredField("image_url")
        if not isinstance(self.image_url, ImageMaskImageUrl):
            self.image_url = ImageMaskImageUrl(self.image_url)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, list):
            self.data = [self.data] if self.data is not None else []
        self.data = [v if isinstance(v, Bool) else Bool(v) for v in self.data]

        super().__post_init__(**kwargs)


@dataclass
class Image2D(ImageInline):
    """
    A 2D image in YX order
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Image2D"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Image2D"
    class_name: ClassVar[str] = "Image2D"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Image2D

    image_url: Union[str, Image2DImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    data: Union[float, List[float]] = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image_url):
            self.MissingRequiredField("image_url")
        if not isinstance(self.image_url, Image2DImageUrl):
            self.image_url = Image2DImageUrl(self.image_url)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, list):
            self.data = [self.data] if self.data is not None else []
        self.data = [v if isinstance(v, float) else float(v) for v in self.data]

        super().__post_init__(**kwargs)


@dataclass
class Image5D(ImageInline):
    """
    A 5D image in TZYXC order
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Image5D"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Image5D"
    class_name: ClassVar[str] = "Image5D"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Image5D

    image_url: Union[str, Image5DImageUrl] = None
    shape_x: int = None
    shape_y: int = None
    data: Union[float, List[float]] = None
    shape_z: int = 1
    shape_c: int = 1
    shape_t: int = 1
    time_series: Optional[Union[dict, "TimeSeries"]] = None
    channel_series: Optional[Union[dict, "ChannelSeries"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image_url):
            self.MissingRequiredField("image_url")
        if not isinstance(self.image_url, Image5DImageUrl):
            self.image_url = Image5DImageUrl(self.image_url)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, list):
            self.data = [self.data] if self.data is not None else []
        self.data = [v if isinstance(v, float) else float(v) for v in self.data]

        if self.time_series is not None and not isinstance(self.time_series, TimeSeries):
            self.time_series = TimeSeries(**as_dict(self.time_series))

        if self.channel_series is not None and not isinstance(self.channel_series, ChannelSeries):
            self.channel_series = ChannelSeries(**as_dict(self.channel_series))

        super().__post_init__(**kwargs)


@dataclass
class ChannelSeries(YAMLRoot):
    """
    A series whose values represent channel
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/ChannelSeries"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/ChannelSeries"
    class_name: ClassVar[str] = "ChannelSeries"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ChannelSeries

    values: Union[Union[dict, "Channel"], List[Union[dict, "Channel"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, Channel) else Channel(**as_dict(v)) for v in self.values]

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
class Roi(YAMLRoot):
    """
    A ROI (Region Of Interest). Collection of shapes and an image to which they are applied
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Roi"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Roi"
    class_name: ClassVar[str] = "Roi"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Roi

    label: Union[str, RoiLabel] = None
    description: Optional[str] = None
    image: Optional[Union[Union[str, ImageImageUrl], List[Union[str, ImageImageUrl]]]] = empty_list()
    shapes: Optional[Union[Dict[Union[str, ShapeLabel], Union[dict, "Shape"]], List[Union[dict, "Shape"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RoiLabel):
            self.label = RoiLabel(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.image, list):
            self.image = [self.image] if self.image is not None else []
        self.image = [v if isinstance(v, ImageImageUrl) else ImageImageUrl(v) for v in self.image]

        self._normalize_inlined_as_dict(slot_name="shapes", slot_type=Shape, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Shape(YAMLRoot):
    """
    A shape
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Shape"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Shape

    label: Union[str, ShapeLabel] = None
    z: Optional[float] = None
    c: Optional[int] = None
    t: Optional[int] = None
    fill_color: Optional[Union[dict, "Color"]] = None
    stroke_color: Optional[Union[dict, "Color"]] = None
    stroke_width: Optional[int] = 1

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, ShapeLabel):
            self.label = ShapeLabel(self.label)

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

    label: Union[str, PointLabel] = None
    y: float = None
    x: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, PointLabel):
            self.label = PointLabel(self.label)

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

    label: Union[str, LineLabel] = None
    x1: float = None
    y1: float = None
    x2: float = None
    y2: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, LineLabel):
            self.label = LineLabel(self.label)

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

    label: Union[str, RectangleLabel] = None
    x: float = None
    y: float = None
    w: float = None
    h: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RectangleLabel):
            self.label = RectangleLabel(self.label)

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

    label: Union[str, EllipseLabel] = None
    x: float = None
    y: float = None
    x_rad: float = None
    y_rad: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, EllipseLabel):
            self.label = EllipseLabel(self.label)

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

    label: Union[str, PolygonLabel] = None
    vertexes: Union[Union[dict, "Vertex"], List[Union[dict, "Vertex"]]] = None
    is_open: Union[bool, Bool] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, PolygonLabel):
            self.label = PolygonLabel(self.label)

        if self._is_empty(self.vertexes):
            self.MissingRequiredField("vertexes")
        if not isinstance(self.vertexes, list):
            self.vertexes = [self.vertexes] if self.vertexes is not None else []
        self.vertexes = [v if isinstance(v, Vertex) else Vertex(**as_dict(v)) for v in self.vertexes]

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

    label: Union[str, MaskLabel] = None
    y: int = 0
    x: int = 0
    mask: Optional[Union[dict, ImageMask]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, MaskLabel):
            self.label = MaskLabel(self.label)

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


@dataclass
class RoiMassCenters(Roi):
    """
    Point ROIs marking the center of mass of detected objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/RoiMassCenters"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/RoiMassCenters"
    class_name: ClassVar[str] = "RoiMassCenters"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.RoiMassCenters

    label: Union[str, RoiMassCentersLabel] = None
    shapes: Optional[Union[Dict[Union[str, PointLabel], Union[dict, Point]], List[Union[dict, Point]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RoiMassCentersLabel):
            self.label = RoiMassCentersLabel(self.label)

        self._normalize_inlined_as_dict(slot_name="shapes", slot_type=Point, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class RoiGeometricCenters(Roi):
    """
    Point ROIs marking the geometric center of detected objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/RoiGeometricCenters"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/RoiGeometricCenters"
    class_name: ClassVar[str] = "RoiGeometricCenters"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.RoiGeometricCenters

    label: Union[str, RoiGeometricCentersLabel] = None
    shapes: Optional[Union[Dict[Union[str, PointLabel], Union[dict, Point]], List[Union[dict, Point]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RoiGeometricCentersLabel):
            self.label = RoiGeometricCentersLabel(self.label)

        self._normalize_inlined_as_dict(slot_name="shapes", slot_type=Point, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class RoiProfiles(Roi):
    """
    line ROIs where profiles were computed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/RoiProfiles"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/RoiProfiles"
    class_name: ClassVar[str] = "RoiProfiles"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.RoiProfiles

    label: Union[str, RoiProfilesLabel] = None
    shapes: Optional[Union[Dict[Union[str, LineLabel], Union[dict, Line]], List[Union[dict, Line]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RoiProfilesLabel):
            self.label = RoiProfilesLabel(self.label)

        self._normalize_inlined_as_dict(slot_name="shapes", slot_type=Line, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class RoiMeasurements(Roi):
    """
    ROIs delimiting where measurements were performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/RoiMeasurements"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/RoiMeasurements"
    class_name: ClassVar[str] = "RoiMeasurements"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.RoiMeasurements

    label: Union[str, RoiMeasurementsLabel] = None
    shapes: Optional[Union[Dict[Union[str, RectangleLabel], Union[dict, Rectangle]], List[Union[dict, Rectangle]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, RoiMeasurementsLabel):
            self.label = RoiMeasurementsLabel(self.label)

        self._normalize_inlined_as_dict(slot_name="shapes", slot_type=Rectangle, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


class KeyValues(YAMLRoot):
    """
    A collection of key-value pairs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/KeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/KeyValues"
    class_name: ClassVar[str] = "KeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.KeyValues


@dataclass
class Tag(YAMLRoot):
    """
    A tag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Tag"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Tag"
    class_name: ClassVar[str] = "Tag"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Tag

    id: Union[int, TagId] = None
    text: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TagId):
            self.id = TagId(self.id)

        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Table(MetricsObject):
    """
    A table
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Table"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Table"
    class_name: ClassVar[str] = "Table"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Table

    table_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.table_url is not None and not isinstance(self.table_url, str):
            self.table_url = str(self.table_url)

        super().__post_init__(**kwargs)


@dataclass
class TableAsPandasDF(Table):
    """
    A table as a Pandas DataFrame
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/TableAsPandasDF"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/TableAsPandasDF"
    class_name: ClassVar[str] = "TableAsPandasDF"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.TableAsPandasDF

    df: Union[dict, MetaObject] = None

@dataclass
class TableAsDict(Table):
    """
    A table inlined in a metrics dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/TableAsDict"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/TableAsDict"
    class_name: ClassVar[str] = "TableAsDict"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.TableAsDict

    columns: Union[Dict[Union[str, ColumnName], Union[dict, "Column"]], List[Union[dict, "Column"]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.columns):
            self.MissingRequiredField("columns")
        self._normalize_inlined_as_dict(slot_name="columns", slot_type=Column, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Column(YAMLRoot):
    """
    A column
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["core_schema/Column"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:core_schema/Column"
    class_name: ClassVar[str] = "Column"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.Column

    name: Union[str, ColumnName] = None
    values: Union[str, List[str]] = None
    source_uri: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ColumnName):
            self.name = ColumnName(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.source_uri is not None and not isinstance(self.source_uri, str):
            self.source_uri = str(self.source_uri)

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

    microscope: Union[str, MicroscopeId] = None
    input: Union[dict, "FieldIlluminationInput"] = None
    processed: Union[bool, Bool] = False
    output: Optional[Union[dict, "FieldIlluminationOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, FieldIlluminationInput):
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

    field_illumination_image: Union[dict, ImageAsNumpy] = None
    saturation_threshold: float = 0.01
    center_threshold: float = 0.9
    corner_fraction: float = 0.1
    sigma: float = 5.0
    intensity_map_size: int = 64
    bit_depth: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.field_illumination_image):
            self.MissingRequiredField("field_illumination_image")
        if not isinstance(self.field_illumination_image, ImageAsNumpy):
            self.field_illumination_image = ImageAsNumpy(**as_dict(self.field_illumination_image))

        if self._is_empty(self.saturation_threshold):
            self.MissingRequiredField("saturation_threshold")
        if not isinstance(self.saturation_threshold, float):
            self.saturation_threshold = float(self.saturation_threshold)

        if self._is_empty(self.center_threshold):
            self.MissingRequiredField("center_threshold")
        if not isinstance(self.center_threshold, float):
            self.center_threshold = float(self.center_threshold)

        if self._is_empty(self.corner_fraction):
            self.MissingRequiredField("corner_fraction")
        if not isinstance(self.corner_fraction, float):
            self.corner_fraction = float(self.corner_fraction)

        if self._is_empty(self.sigma):
            self.MissingRequiredField("sigma")
        if not isinstance(self.sigma, float):
            self.sigma = float(self.sigma)

        if self._is_empty(self.intensity_map_size):
            self.MissingRequiredField("intensity_map_size")
        if not isinstance(self.intensity_map_size, int):
            self.intensity_map_size = int(self.intensity_map_size)

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

    key_values: Optional[Union[dict, "FieldIlluminationKeyValues"]] = None
    intensity_profiles: Optional[Union[dict, TableAsDict]] = None
    intensity_map: Optional[Union[dict, Image5D]] = None
    profile_rois: Optional[Union[dict, RoiProfiles]] = None
    corner_rois: Optional[Union[dict, RoiMeasurements]] = None
    center_of_illumination: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key_values is not None and not isinstance(self.key_values, FieldIlluminationKeyValues):
            self.key_values = FieldIlluminationKeyValues(**as_dict(self.key_values))

        if self.intensity_profiles is not None and not isinstance(self.intensity_profiles, TableAsDict):
            self.intensity_profiles = TableAsDict(**as_dict(self.intensity_profiles))

        if self.intensity_map is not None and not isinstance(self.intensity_map, Image5D):
            self.intensity_map = Image5D(**as_dict(self.intensity_map))

        if self.profile_rois is not None and not isinstance(self.profile_rois, RoiProfiles):
            self.profile_rois = RoiProfiles(**as_dict(self.profile_rois))

        if self.corner_rois is not None and not isinstance(self.corner_rois, RoiMeasurements):
            self.corner_rois = RoiMeasurements(**as_dict(self.corner_rois))

        self._normalize_inlined_as_dict(slot_name="center_of_illumination", slot_type=RoiMassCenters, key_name="label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class FieldIlluminationKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/field_illumination_schema/FieldIlluminationKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/field_illumination_schema/FieldIlluminationKeyValues"
    class_name: ClassVar[str] = "FieldIlluminationKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.FieldIlluminationKeyValues

    channel: Optional[Union[int, List[int]]] = empty_list()
    nb_pixels_center: Optional[Union[int, List[int]]] = empty_list()
    center_of_mass_x: Optional[Union[float, List[float]]] = empty_list()
    center_of_mass_y: Optional[Union[float, List[float]]] = empty_list()
    max_intensity: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_x: Optional[Union[float, List[float]]] = empty_list()
    max_intensity_pos_y: Optional[Union[float, List[float]]] = empty_list()
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
    decile_0: Optional[Union[float, List[float]]] = empty_list()
    decile_1: Optional[Union[float, List[float]]] = empty_list()
    decile_2: Optional[Union[float, List[float]]] = empty_list()
    decile_3: Optional[Union[float, List[float]]] = empty_list()
    decile_4: Optional[Union[float, List[float]]] = empty_list()
    decile_5: Optional[Union[float, List[float]]] = empty_list()
    decile_6: Optional[Union[float, List[float]]] = empty_list()
    decile_7: Optional[Union[float, List[float]]] = empty_list()
    decile_8: Optional[Union[float, List[float]]] = empty_list()
    decile_9: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.channel, list):
            self.channel = [self.channel] if self.channel is not None else []
        self.channel = [v if isinstance(v, int) else int(v) for v in self.channel]

        if not isinstance(self.nb_pixels_center, list):
            self.nb_pixels_center = [self.nb_pixels_center] if self.nb_pixels_center is not None else []
        self.nb_pixels_center = [v if isinstance(v, int) else int(v) for v in self.nb_pixels_center]

        if not isinstance(self.center_of_mass_x, list):
            self.center_of_mass_x = [self.center_of_mass_x] if self.center_of_mass_x is not None else []
        self.center_of_mass_x = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_x]

        if not isinstance(self.center_of_mass_y, list):
            self.center_of_mass_y = [self.center_of_mass_y] if self.center_of_mass_y is not None else []
        self.center_of_mass_y = [v if isinstance(v, float) else float(v) for v in self.center_of_mass_y]

        if not isinstance(self.max_intensity, list):
            self.max_intensity = [self.max_intensity] if self.max_intensity is not None else []
        self.max_intensity = [v if isinstance(v, float) else float(v) for v in self.max_intensity]

        if not isinstance(self.max_intensity_pos_x, list):
            self.max_intensity_pos_x = [self.max_intensity_pos_x] if self.max_intensity_pos_x is not None else []
        self.max_intensity_pos_x = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_x]

        if not isinstance(self.max_intensity_pos_y, list):
            self.max_intensity_pos_y = [self.max_intensity_pos_y] if self.max_intensity_pos_y is not None else []
        self.max_intensity_pos_y = [v if isinstance(v, float) else float(v) for v in self.max_intensity_pos_y]

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

        if not isinstance(self.decile_0, list):
            self.decile_0 = [self.decile_0] if self.decile_0 is not None else []
        self.decile_0 = [v if isinstance(v, float) else float(v) for v in self.decile_0]

        if not isinstance(self.decile_1, list):
            self.decile_1 = [self.decile_1] if self.decile_1 is not None else []
        self.decile_1 = [v if isinstance(v, float) else float(v) for v in self.decile_1]

        if not isinstance(self.decile_2, list):
            self.decile_2 = [self.decile_2] if self.decile_2 is not None else []
        self.decile_2 = [v if isinstance(v, float) else float(v) for v in self.decile_2]

        if not isinstance(self.decile_3, list):
            self.decile_3 = [self.decile_3] if self.decile_3 is not None else []
        self.decile_3 = [v if isinstance(v, float) else float(v) for v in self.decile_3]

        if not isinstance(self.decile_4, list):
            self.decile_4 = [self.decile_4] if self.decile_4 is not None else []
        self.decile_4 = [v if isinstance(v, float) else float(v) for v in self.decile_4]

        if not isinstance(self.decile_5, list):
            self.decile_5 = [self.decile_5] if self.decile_5 is not None else []
        self.decile_5 = [v if isinstance(v, float) else float(v) for v in self.decile_5]

        if not isinstance(self.decile_6, list):
            self.decile_6 = [self.decile_6] if self.decile_6 is not None else []
        self.decile_6 = [v if isinstance(v, float) else float(v) for v in self.decile_6]

        if not isinstance(self.decile_7, list):
            self.decile_7 = [self.decile_7] if self.decile_7 is not None else []
        self.decile_7 = [v if isinstance(v, float) else float(v) for v in self.decile_7]

        if not isinstance(self.decile_8, list):
            self.decile_8 = [self.decile_8] if self.decile_8 is not None else []
        self.decile_8 = [v if isinstance(v, float) else float(v) for v in self.decile_8]

        if not isinstance(self.decile_9, list):
            self.decile_9 = [self.decile_9] if self.decile_9 is not None else []
        self.decile_9 = [v if isinstance(v, float) else float(v) for v in self.decile_9]

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsDataset(MetricsDataset):
    """
    A PSF beads dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/MontpellierRessourcesImagerie/microscope-metrics/blob/main/src/microscopemetrics/data_schema/samples/argolight_schema.yaml/PSFBeadsDataset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PSFBeadsDataset"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsDataset

    microscope: Union[str, MicroscopeId] = None
    input: Union[dict, "PSFBeadsInput"] = None
    processed: Union[bool, Bool] = False
    output: Optional[Union[dict, "PSFBeadsOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, PSFBeadsInput):
            self.input = PSFBeadsInput(**as_dict(self.input))

        if self.output is not None and not isinstance(self.output, PSFBeadsOutput):
            self.output = PSFBeadsOutput(**as_dict(self.output))

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsInput(MetricsInput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/MontpellierRessourcesImagerie/microscope-metrics/blob/main/src/microscopemetrics/data_schema/samples/argolight_schema.yaml/PSFBeadsInput")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PSFBeadsInput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsInput

    psf_beads_images: Union[Dict[Union[str, ImageAsNumpyImageUrl], Union[dict, ImageAsNumpy]], List[Union[dict, ImageAsNumpy]]] = empty_dict()
    min_lateral_distance_factor: float = 20.0
    sigma_z: float = 1.0
    sigma_y: float = 1.0
    sigma_x: float = 1.0
    snr_threshold: float = 10.0
    fitting_rss_threshold: float = 0.1
    intensity_zscore_threshold: float = 3.0

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.psf_beads_images):
            self.MissingRequiredField("psf_beads_images")
        self._normalize_inlined_as_dict(slot_name="psf_beads_images", slot_type=ImageAsNumpy, key_name="image_url", keyed=True)

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

        if self._is_empty(self.fitting_rss_threshold):
            self.MissingRequiredField("fitting_rss_threshold")
        if not isinstance(self.fitting_rss_threshold, float):
            self.fitting_rss_threshold = float(self.fitting_rss_threshold)

        if self._is_empty(self.intensity_zscore_threshold):
            self.MissingRequiredField("intensity_zscore_threshold")
        if not isinstance(self.intensity_zscore_threshold, float):
            self.intensity_zscore_threshold = float(self.intensity_zscore_threshold)

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsOutput(MetricsOutput):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/MontpellierRessourcesImagerie/microscope-metrics/blob/main/src/microscopemetrics/data_schema/samples/argolight_schema.yaml/PSFBeadsOutput")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PSFBeadsOutput"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsOutput

    bead_crops: Optional[Union[Dict[Union[str, ImageAsNumpyImageUrl], Union[dict, ImageAsNumpy]], List[Union[dict, ImageAsNumpy]]]] = empty_dict()
    analyzed_bead_centroids: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    discarded_bead_centroids_lateral_edge: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    discarded_bead_centroids_self_proximity: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    considered_bead_centroids_axial_edge: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    considered_bead_centroids_cluster: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    considered_bead_centroids_fit_quality: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    key_values: Optional[Union[dict, "PSFBeadsKeyMeasurements"]] = None
    bead_properties: Optional[Union[dict, TableAsDict]] = None
    bead_z_profiles: Optional[Union[dict, TableAsDict]] = None
    bead_y_profiles: Optional[Union[dict, TableAsDict]] = None
    bead_x_profiles: Optional[Union[dict, TableAsDict]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="bead_crops", slot_type=ImageAsNumpy, key_name="image_url", keyed=True)

        self._normalize_inlined_as_dict(slot_name="analyzed_bead_centroids", slot_type=RoiMassCenters, key_name="label", keyed=True)

        self._normalize_inlined_as_dict(slot_name="discarded_bead_centroids_lateral_edge", slot_type=RoiMassCenters, key_name="label", keyed=True)

        self._normalize_inlined_as_dict(slot_name="discarded_bead_centroids_self_proximity", slot_type=RoiMassCenters, key_name="label", keyed=True)

        self._normalize_inlined_as_dict(slot_name="considered_bead_centroids_axial_edge", slot_type=RoiMassCenters, key_name="label", keyed=True)

        self._normalize_inlined_as_dict(slot_name="considered_bead_centroids_cluster", slot_type=RoiMassCenters, key_name="label", keyed=True)

        self._normalize_inlined_as_dict(slot_name="considered_bead_centroids_fit_quality", slot_type=RoiMassCenters, key_name="label", keyed=True)

        if self.key_values is not None and not isinstance(self.key_values, PSFBeadsKeyMeasurements):
            self.key_values = PSFBeadsKeyMeasurements(**as_dict(self.key_values))

        if self.bead_properties is not None and not isinstance(self.bead_properties, TableAsDict):
            self.bead_properties = TableAsDict(**as_dict(self.bead_properties))

        if self.bead_z_profiles is not None and not isinstance(self.bead_z_profiles, TableAsDict):
            self.bead_z_profiles = TableAsDict(**as_dict(self.bead_z_profiles))

        if self.bead_y_profiles is not None and not isinstance(self.bead_y_profiles, TableAsDict):
            self.bead_y_profiles = TableAsDict(**as_dict(self.bead_y_profiles))

        if self.bead_x_profiles is not None and not isinstance(self.bead_x_profiles, TableAsDict):
            self.bead_x_profiles = TableAsDict(**as_dict(self.bead_x_profiles))

        super().__post_init__(**kwargs)


@dataclass
class PSFBeadsKeyMeasurements(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/MontpellierRessourcesImagerie/microscope-metrics/blob/main/src/microscopemetrics/data_schema/samples/argolight_schema.yaml/PSFBeadsKeyMeasurements")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PSFBeadsKeyMeasurements"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.PSFBeadsKeyMeasurements

    nr_of_beads_analyzed: Optional[Union[int, List[int]]] = empty_list()
    nr_of_beads_discarded_lateral_edge: Optional[Union[int, List[int]]] = empty_list()
    nr_of_beads_discarded_axial_edge: Optional[Union[int, List[int]]] = empty_list()
    nr_of_beads_discarded_self_proximity: Optional[Union[int, List[int]]] = empty_list()
    nr_of_beads_discarded_cluster: Optional[Union[int, List[int]]] = empty_list()
    nr_of_beads_discarded_fit_quality: Optional[Union[int, List[int]]] = empty_list()
    fit_quality_z_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_z_median: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_z_stdev: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_y_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_y_median: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_y_stdev: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_x_mean: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_x_median: Optional[Union[float, List[float]]] = empty_list()
    fit_quality_x_stdev: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_z_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_z_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_z_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_y_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_y_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_y_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_x_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_x_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_x_pixels: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_z_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_z_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_z_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_y_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_y_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_y_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_x_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_x_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_x_microns: Optional[Union[float, List[float]]] = empty_list()
    resolution_mean_fwhm_lateral_asymmetry_ratio: Optional[Union[float, List[float]]] = empty_list()
    resolution_median_fwhm_lateral_asymmetry_ratio: Optional[Union[float, List[float]]] = empty_list()
    resolution_stdev_fwhm_lateral_asymmetry_ratio: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.nr_of_beads_analyzed, list):
            self.nr_of_beads_analyzed = [self.nr_of_beads_analyzed] if self.nr_of_beads_analyzed is not None else []
        self.nr_of_beads_analyzed = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_analyzed]

        if not isinstance(self.nr_of_beads_discarded_lateral_edge, list):
            self.nr_of_beads_discarded_lateral_edge = [self.nr_of_beads_discarded_lateral_edge] if self.nr_of_beads_discarded_lateral_edge is not None else []
        self.nr_of_beads_discarded_lateral_edge = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_discarded_lateral_edge]

        if not isinstance(self.nr_of_beads_discarded_axial_edge, list):
            self.nr_of_beads_discarded_axial_edge = [self.nr_of_beads_discarded_axial_edge] if self.nr_of_beads_discarded_axial_edge is not None else []
        self.nr_of_beads_discarded_axial_edge = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_discarded_axial_edge]

        if not isinstance(self.nr_of_beads_discarded_self_proximity, list):
            self.nr_of_beads_discarded_self_proximity = [self.nr_of_beads_discarded_self_proximity] if self.nr_of_beads_discarded_self_proximity is not None else []
        self.nr_of_beads_discarded_self_proximity = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_discarded_self_proximity]

        if not isinstance(self.nr_of_beads_discarded_cluster, list):
            self.nr_of_beads_discarded_cluster = [self.nr_of_beads_discarded_cluster] if self.nr_of_beads_discarded_cluster is not None else []
        self.nr_of_beads_discarded_cluster = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_discarded_cluster]

        if not isinstance(self.nr_of_beads_discarded_fit_quality, list):
            self.nr_of_beads_discarded_fit_quality = [self.nr_of_beads_discarded_fit_quality] if self.nr_of_beads_discarded_fit_quality is not None else []
        self.nr_of_beads_discarded_fit_quality = [v if isinstance(v, int) else int(v) for v in self.nr_of_beads_discarded_fit_quality]

        if not isinstance(self.fit_quality_z_mean, list):
            self.fit_quality_z_mean = [self.fit_quality_z_mean] if self.fit_quality_z_mean is not None else []
        self.fit_quality_z_mean = [v if isinstance(v, float) else float(v) for v in self.fit_quality_z_mean]

        if not isinstance(self.fit_quality_z_median, list):
            self.fit_quality_z_median = [self.fit_quality_z_median] if self.fit_quality_z_median is not None else []
        self.fit_quality_z_median = [v if isinstance(v, float) else float(v) for v in self.fit_quality_z_median]

        if not isinstance(self.fit_quality_z_stdev, list):
            self.fit_quality_z_stdev = [self.fit_quality_z_stdev] if self.fit_quality_z_stdev is not None else []
        self.fit_quality_z_stdev = [v if isinstance(v, float) else float(v) for v in self.fit_quality_z_stdev]

        if not isinstance(self.fit_quality_y_mean, list):
            self.fit_quality_y_mean = [self.fit_quality_y_mean] if self.fit_quality_y_mean is not None else []
        self.fit_quality_y_mean = [v if isinstance(v, float) else float(v) for v in self.fit_quality_y_mean]

        if not isinstance(self.fit_quality_y_median, list):
            self.fit_quality_y_median = [self.fit_quality_y_median] if self.fit_quality_y_median is not None else []
        self.fit_quality_y_median = [v if isinstance(v, float) else float(v) for v in self.fit_quality_y_median]

        if not isinstance(self.fit_quality_y_stdev, list):
            self.fit_quality_y_stdev = [self.fit_quality_y_stdev] if self.fit_quality_y_stdev is not None else []
        self.fit_quality_y_stdev = [v if isinstance(v, float) else float(v) for v in self.fit_quality_y_stdev]

        if not isinstance(self.fit_quality_x_mean, list):
            self.fit_quality_x_mean = [self.fit_quality_x_mean] if self.fit_quality_x_mean is not None else []
        self.fit_quality_x_mean = [v if isinstance(v, float) else float(v) for v in self.fit_quality_x_mean]

        if not isinstance(self.fit_quality_x_median, list):
            self.fit_quality_x_median = [self.fit_quality_x_median] if self.fit_quality_x_median is not None else []
        self.fit_quality_x_median = [v if isinstance(v, float) else float(v) for v in self.fit_quality_x_median]

        if not isinstance(self.fit_quality_x_stdev, list):
            self.fit_quality_x_stdev = [self.fit_quality_x_stdev] if self.fit_quality_x_stdev is not None else []
        self.fit_quality_x_stdev = [v if isinstance(v, float) else float(v) for v in self.fit_quality_x_stdev]

        if not isinstance(self.resolution_mean_fwhm_z_pixels, list):
            self.resolution_mean_fwhm_z_pixels = [self.resolution_mean_fwhm_z_pixels] if self.resolution_mean_fwhm_z_pixels is not None else []
        self.resolution_mean_fwhm_z_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_z_pixels]

        if not isinstance(self.resolution_median_fwhm_z_pixels, list):
            self.resolution_median_fwhm_z_pixels = [self.resolution_median_fwhm_z_pixels] if self.resolution_median_fwhm_z_pixels is not None else []
        self.resolution_median_fwhm_z_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_z_pixels]

        if not isinstance(self.resolution_stdev_fwhm_z_pixels, list):
            self.resolution_stdev_fwhm_z_pixels = [self.resolution_stdev_fwhm_z_pixels] if self.resolution_stdev_fwhm_z_pixels is not None else []
        self.resolution_stdev_fwhm_z_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_z_pixels]

        if not isinstance(self.resolution_mean_fwhm_y_pixels, list):
            self.resolution_mean_fwhm_y_pixels = [self.resolution_mean_fwhm_y_pixels] if self.resolution_mean_fwhm_y_pixels is not None else []
        self.resolution_mean_fwhm_y_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_y_pixels]

        if not isinstance(self.resolution_median_fwhm_y_pixels, list):
            self.resolution_median_fwhm_y_pixels = [self.resolution_median_fwhm_y_pixels] if self.resolution_median_fwhm_y_pixels is not None else []
        self.resolution_median_fwhm_y_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_y_pixels]

        if not isinstance(self.resolution_stdev_fwhm_y_pixels, list):
            self.resolution_stdev_fwhm_y_pixels = [self.resolution_stdev_fwhm_y_pixels] if self.resolution_stdev_fwhm_y_pixels is not None else []
        self.resolution_stdev_fwhm_y_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_y_pixels]

        if not isinstance(self.resolution_mean_fwhm_x_pixels, list):
            self.resolution_mean_fwhm_x_pixels = [self.resolution_mean_fwhm_x_pixels] if self.resolution_mean_fwhm_x_pixels is not None else []
        self.resolution_mean_fwhm_x_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_x_pixels]

        if not isinstance(self.resolution_median_fwhm_x_pixels, list):
            self.resolution_median_fwhm_x_pixels = [self.resolution_median_fwhm_x_pixels] if self.resolution_median_fwhm_x_pixels is not None else []
        self.resolution_median_fwhm_x_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_x_pixels]

        if not isinstance(self.resolution_stdev_fwhm_x_pixels, list):
            self.resolution_stdev_fwhm_x_pixels = [self.resolution_stdev_fwhm_x_pixels] if self.resolution_stdev_fwhm_x_pixels is not None else []
        self.resolution_stdev_fwhm_x_pixels = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_x_pixels]

        if not isinstance(self.resolution_mean_fwhm_z_microns, list):
            self.resolution_mean_fwhm_z_microns = [self.resolution_mean_fwhm_z_microns] if self.resolution_mean_fwhm_z_microns is not None else []
        self.resolution_mean_fwhm_z_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_z_microns]

        if not isinstance(self.resolution_median_fwhm_z_microns, list):
            self.resolution_median_fwhm_z_microns = [self.resolution_median_fwhm_z_microns] if self.resolution_median_fwhm_z_microns is not None else []
        self.resolution_median_fwhm_z_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_z_microns]

        if not isinstance(self.resolution_stdev_fwhm_z_microns, list):
            self.resolution_stdev_fwhm_z_microns = [self.resolution_stdev_fwhm_z_microns] if self.resolution_stdev_fwhm_z_microns is not None else []
        self.resolution_stdev_fwhm_z_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_z_microns]

        if not isinstance(self.resolution_mean_fwhm_y_microns, list):
            self.resolution_mean_fwhm_y_microns = [self.resolution_mean_fwhm_y_microns] if self.resolution_mean_fwhm_y_microns is not None else []
        self.resolution_mean_fwhm_y_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_y_microns]

        if not isinstance(self.resolution_median_fwhm_y_microns, list):
            self.resolution_median_fwhm_y_microns = [self.resolution_median_fwhm_y_microns] if self.resolution_median_fwhm_y_microns is not None else []
        self.resolution_median_fwhm_y_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_y_microns]

        if not isinstance(self.resolution_stdev_fwhm_y_microns, list):
            self.resolution_stdev_fwhm_y_microns = [self.resolution_stdev_fwhm_y_microns] if self.resolution_stdev_fwhm_y_microns is not None else []
        self.resolution_stdev_fwhm_y_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_y_microns]

        if not isinstance(self.resolution_mean_fwhm_x_microns, list):
            self.resolution_mean_fwhm_x_microns = [self.resolution_mean_fwhm_x_microns] if self.resolution_mean_fwhm_x_microns is not None else []
        self.resolution_mean_fwhm_x_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_x_microns]

        if not isinstance(self.resolution_median_fwhm_x_microns, list):
            self.resolution_median_fwhm_x_microns = [self.resolution_median_fwhm_x_microns] if self.resolution_median_fwhm_x_microns is not None else []
        self.resolution_median_fwhm_x_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_x_microns]

        if not isinstance(self.resolution_stdev_fwhm_x_microns, list):
            self.resolution_stdev_fwhm_x_microns = [self.resolution_stdev_fwhm_x_microns] if self.resolution_stdev_fwhm_x_microns is not None else []
        self.resolution_stdev_fwhm_x_microns = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_x_microns]

        if not isinstance(self.resolution_mean_fwhm_lateral_asymmetry_ratio, list):
            self.resolution_mean_fwhm_lateral_asymmetry_ratio = [self.resolution_mean_fwhm_lateral_asymmetry_ratio] if self.resolution_mean_fwhm_lateral_asymmetry_ratio is not None else []
        self.resolution_mean_fwhm_lateral_asymmetry_ratio = [v if isinstance(v, float) else float(v) for v in self.resolution_mean_fwhm_lateral_asymmetry_ratio]

        if not isinstance(self.resolution_median_fwhm_lateral_asymmetry_ratio, list):
            self.resolution_median_fwhm_lateral_asymmetry_ratio = [self.resolution_median_fwhm_lateral_asymmetry_ratio] if self.resolution_median_fwhm_lateral_asymmetry_ratio is not None else []
        self.resolution_median_fwhm_lateral_asymmetry_ratio = [v if isinstance(v, float) else float(v) for v in self.resolution_median_fwhm_lateral_asymmetry_ratio]

        if not isinstance(self.resolution_stdev_fwhm_lateral_asymmetry_ratio, list):
            self.resolution_stdev_fwhm_lateral_asymmetry_ratio = [self.resolution_stdev_fwhm_lateral_asymmetry_ratio] if self.resolution_stdev_fwhm_lateral_asymmetry_ratio is not None else []
        self.resolution_stdev_fwhm_lateral_asymmetry_ratio = [v if isinstance(v, float) else float(v) for v in self.resolution_stdev_fwhm_lateral_asymmetry_ratio]

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

    microscope: Union[str, MicroscopeId] = None
    input: Union[dict, "ArgolightBInput"] = None
    processed: Union[bool, Bool] = False
    output: Optional[Union[dict, "ArgolightBOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, ArgolightBInput):
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

    argolight_b_image: Union[dict, ImageAsNumpy] = None
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
        if not isinstance(self.argolight_b_image, ImageAsNumpy):
            self.argolight_b_image = ImageAsNumpy(**as_dict(self.argolight_b_image))

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

    spots_labels_image: Optional[Union[str, ImageAsNumpyImageUrl]] = None
    spots_centroids: Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]] = empty_dict()
    intensity_key_values: Optional[Union[dict, "ArgolightBIntensityKeyValues"]] = None
    distance_key_values: Optional[Union[dict, "ArgolightBDistanceKeyValues"]] = None
    spots_properties: Optional[Union[dict, TableAsDict]] = None
    spots_distances: Optional[Union[dict, TableAsDict]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.spots_labels_image is not None and not isinstance(self.spots_labels_image, ImageAsNumpyImageUrl):
            self.spots_labels_image = ImageAsNumpyImageUrl(self.spots_labels_image)

        self._normalize_inlined_as_dict(slot_name="spots_centroids", slot_type=RoiMassCenters, key_name="label", keyed=True)

        if self.intensity_key_values is not None and not isinstance(self.intensity_key_values, ArgolightBIntensityKeyValues):
            self.intensity_key_values = ArgolightBIntensityKeyValues(**as_dict(self.intensity_key_values))

        if self.distance_key_values is not None and not isinstance(self.distance_key_values, ArgolightBDistanceKeyValues):
            self.distance_key_values = ArgolightBDistanceKeyValues(**as_dict(self.distance_key_values))

        if self.spots_properties is not None and not isinstance(self.spots_properties, TableAsDict):
            self.spots_properties = TableAsDict(**as_dict(self.spots_properties))

        if self.spots_distances is not None and not isinstance(self.spots_distances, TableAsDict):
            self.spots_distances = TableAsDict(**as_dict(self.spots_distances))

        super().__post_init__(**kwargs)


@dataclass
class ArgolightBIntensityKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightBIntensityKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightBIntensityKeyValues"
    class_name: ClassVar[str] = "ArgolightBIntensityKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightBIntensityKeyValues

    channel: Optional[Union[int, List[int]]] = empty_list()
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
        if not isinstance(self.channel, list):
            self.channel = [self.channel] if self.channel is not None else []
        self.channel = [v if isinstance(v, int) else int(v) for v in self.channel]

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

    microscope: Union[str, MicroscopeId] = None
    input: Union[dict, "ArgolightEInput"] = None
    processed: Union[bool, Bool] = False
    output: Optional[Union[dict, "ArgolightEOutput"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, ArgolightEInput):
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

    argolight_e_image: Union[dict, ImageAsNumpy] = None
    orientation_axis: int = None
    saturation_threshold: float = 0.01
    measured_band: float = 0.4
    prominence_threshold: float = 0.264
    bit_depth: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.argolight_e_image):
            self.MissingRequiredField("argolight_e_image")
        if not isinstance(self.argolight_e_image, ImageAsNumpy):
            self.argolight_e_image = ImageAsNumpy(**as_dict(self.argolight_e_image))

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

    peaks_rois: Optional[Union[Dict[Union[str, RoiLabel], Union[dict, Roi]], List[Union[dict, Roi]]]] = empty_dict()
    key_measurements: Optional[Union[dict, "ArgolightEKeyValues"]] = None
    intensity_profiles: Optional[Union[dict, TableAsDict]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="peaks_rois", slot_type=Roi, key_name="label", keyed=True)

        if self.key_measurements is not None and not isinstance(self.key_measurements, ArgolightEKeyValues):
            self.key_measurements = ArgolightEKeyValues(**as_dict(self.key_measurements))

        if self.intensity_profiles is not None and not isinstance(self.intensity_profiles, TableAsDict):
            self.intensity_profiles = TableAsDict(**as_dict(self.intensity_profiles))

        super().__post_init__(**kwargs)


@dataclass
class ArgolightEKeyValues(KeyValues):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA["samples/argolight_schema/ArgolightEKeyValues"]
    class_class_curie: ClassVar[str] = "microscopemetrics_schema:samples/argolight_schema/ArgolightEKeyValues"
    class_name: ClassVar[str] = "ArgolightEKeyValues"
    class_model_uri: ClassVar[URIRef] = MICROSCOPEMETRICS_SCHEMA.ArgolightEKeyValues

    channel: Optional[Union[int, List[int]]] = empty_list()
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
        if not isinstance(self.channel, list):
            self.channel = [self.channel] if self.channel is not None else []
        self.channel = [v if isinstance(v, int) else int(v) for v in self.channel]

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
class CommentTypes(EnumDefinitionImpl):
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
        name="CommentTypes",
        description="The type of the comment",
    )

class MicroscopeType(EnumDefinitionImpl):
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
        name="MicroscopeType",
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

# Slots
class slots:
    pass

slots.id = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/id'], name="id", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/id'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/name'], name="name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/description'], name="description", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/description'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.description, domain=None, range=Optional[str])

slots.image_url = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/image_url'], name="image_url", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/image_url'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image_url, domain=None, range=URIRef)

slots.source_image_url = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/source_image_url'], name="source_image_url", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/source_image_url'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.source_image_url, domain=None, range=Optional[Union[str, List[str]]])

slots.table_url = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/table_url'], name="table_url", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/table_url'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.table_url, domain=None, range=Optional[str])

slots.shape_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_x'], name="shape_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape_x, domain=None, range=int)

slots.shape_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_y'], name="shape_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape_y, domain=None, range=int)

slots.shape_z = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_z'], name="shape_z", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_z'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape_z, domain=None, range=int)

slots.shape_c = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_c'], name="shape_c", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_c'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape_c, domain=None, range=int)

slots.shape_t = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shape_t'], name="shape_t", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shape_t'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape_t, domain=None, range=int)

slots.voxel_size_x_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_x_micron'], name="voxel_size_x_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_x_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.voxel_size_x_micron, domain=None, range=Optional[float])

slots.voxel_size_y_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_y_micron'], name="voxel_size_y_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_y_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.voxel_size_y_micron, domain=None, range=Optional[float])

slots.voxel_size_z_micron = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/voxel_size_z_micron'], name="voxel_size_z_micron", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/voxel_size_z_micron'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.voxel_size_z_micron, domain=None, range=Optional[float])

slots.excitation_wavelength_nm = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/excitation_wavelength_nm'], name="excitation_wavelength_nm", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/excitation_wavelength_nm'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.excitation_wavelength_nm, domain=None, range=Optional[float])

slots.emission_wavelength_nm = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/emission_wavelength_nm'], name="emission_wavelength_nm", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/emission_wavelength_nm'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.emission_wavelength_nm, domain=None, range=Optional[float])

slots.channel = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channel'], name="channel", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channel'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channel, domain=None, range=Optional[Union[int, List[int]]])

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
                   model_uri=MICROSCOPEMETRICS_SCHEMA.field_illumination_image, domain=None, range=Union[dict, ImageAsNumpy])

slots.center_threshold = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_threshold'], name="center_threshold", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_threshold'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_threshold, domain=None, range=float)

slots.corner_fraction = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/corner_fraction'], name="corner_fraction", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/corner_fraction'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.corner_fraction, domain=None, range=float)

slots.sigma = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/sigma'], name="sigma", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/sigma'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sigma, domain=None, range=float)

slots.intensity_map_size = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/intensity_map_size'], name="intensity_map_size", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/intensity_map_size'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_map_size, domain=None, range=int)

slots.nb_pixels_center = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/nb_pixels_center'], name="nb_pixels_center", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/nb_pixels_center'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nb_pixels_center, domain=None, range=Optional[Union[int, List[int]]])

slots.center_of_mass_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_x'], name="center_of_mass_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_x, domain=None, range=Optional[Union[float, List[float]]])

slots.center_of_mass_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_mass_y'], name="center_of_mass_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_mass_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.center_of_mass_y, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity'], name="max_intensity", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_x = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_x'], name="max_intensity_pos_x", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_x'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_x, domain=None, range=Optional[Union[float, List[float]]])

slots.max_intensity_pos_y = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/max_intensity_pos_y'], name="max_intensity_pos_y", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/max_intensity_pos_y'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.max_intensity_pos_y, domain=None, range=Optional[Union[float, List[float]]])

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

slots.decile_0 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_0'], name="decile_0", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_0'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_0, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_1 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_1'], name="decile_1", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_1'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_1, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_2 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_2'], name="decile_2", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_2'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_2, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_3 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_3'], name="decile_3", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_3'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_3, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_4 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_4'], name="decile_4", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_4'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_4, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_5 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_5'], name="decile_5", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_5'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_5, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_6 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_6'], name="decile_6", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_6'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_6, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_7 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_7'], name="decile_7", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_7'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_7, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_8 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_8'], name="decile_8", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_8'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_8, domain=None, range=Optional[Union[float, List[float]]])

slots.decile_9 = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/decile_9'], name="decile_9", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/decile_9'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.decile_9, domain=None, range=Optional[Union[float, List[float]]])

slots.psf_beads_images = Slot(uri="str(uriorcurie)", name="psf_beads_images", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.psf_beads_images, domain=None, range=Union[Dict[Union[str, ImageAsNumpyImageUrl], Union[dict, ImageAsNumpy]], List[Union[dict, ImageAsNumpy]]])

slots.min_lateral_distance_factor = Slot(uri="str(uriorcurie)", name="min_lateral_distance_factor", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.min_lateral_distance_factor, domain=None, range=float)

slots.snr_threshold = Slot(uri="str(uriorcurie)", name="snr_threshold", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.snr_threshold, domain=None, range=float)

slots.fitting_rss_threshold = Slot(uri="str(uriorcurie)", name="fitting_rss_threshold", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fitting_rss_threshold, domain=None, range=float)

slots.intensity_zscore_threshold = Slot(uri="str(uriorcurie)", name="intensity_zscore_threshold", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.intensity_zscore_threshold, domain=None, range=float)

slots.nr_of_beads_analyzed = Slot(uri="str(uriorcurie)", name="nr_of_beads_analyzed", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_analyzed, domain=None, range=Optional[Union[int, List[int]]])

slots.nr_of_beads_discarded_lateral_edge = Slot(uri="str(uriorcurie)", name="nr_of_beads_discarded_lateral_edge", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_discarded_lateral_edge, domain=None, range=Optional[Union[int, List[int]]])

slots.nr_of_beads_discarded_axial_edge = Slot(uri="str(uriorcurie)", name="nr_of_beads_discarded_axial_edge", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_discarded_axial_edge, domain=None, range=Optional[Union[int, List[int]]])

slots.nr_of_beads_discarded_self_proximity = Slot(uri="str(uriorcurie)", name="nr_of_beads_discarded_self_proximity", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_discarded_self_proximity, domain=None, range=Optional[Union[int, List[int]]])

slots.nr_of_beads_discarded_cluster = Slot(uri="str(uriorcurie)", name="nr_of_beads_discarded_cluster", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_discarded_cluster, domain=None, range=Optional[Union[int, List[int]]])

slots.nr_of_beads_discarded_fit_quality = Slot(uri="str(uriorcurie)", name="nr_of_beads_discarded_fit_quality", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.nr_of_beads_discarded_fit_quality, domain=None, range=Optional[Union[int, List[int]]])

slots.fit_quality_z_mean = Slot(uri="str(uriorcurie)", name="fit_quality_z_mean", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_z_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_z_median = Slot(uri="str(uriorcurie)", name="fit_quality_z_median", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_z_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_z_stdev = Slot(uri="str(uriorcurie)", name="fit_quality_z_stdev", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_z_stdev, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_y_mean = Slot(uri="str(uriorcurie)", name="fit_quality_y_mean", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_y_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_y_median = Slot(uri="str(uriorcurie)", name="fit_quality_y_median", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_y_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_y_stdev = Slot(uri="str(uriorcurie)", name="fit_quality_y_stdev", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_y_stdev, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_x_mean = Slot(uri="str(uriorcurie)", name="fit_quality_x_mean", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_x_mean, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_x_median = Slot(uri="str(uriorcurie)", name="fit_quality_x_median", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_x_median, domain=None, range=Optional[Union[float, List[float]]])

slots.fit_quality_x_stdev = Slot(uri="str(uriorcurie)", name="fit_quality_x_stdev", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fit_quality_x_stdev, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_z_pixels = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_z_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_z_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_z_pixels = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_z_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_z_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_z_pixels = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_z_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_z_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_y_pixels = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_y_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_y_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_y_pixels = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_y_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_y_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_y_pixels = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_y_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_y_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_x_pixels = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_x_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_x_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_x_pixels = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_x_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_x_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_x_pixels = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_x_pixels", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_x_pixels, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_z_microns = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_z_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_z_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_z_microns = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_z_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_z_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_z_microns = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_z_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_z_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_y_microns = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_y_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_y_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_y_microns = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_y_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_y_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_y_microns = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_y_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_y_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_x_microns = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_x_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_x_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_x_microns = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_x_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_x_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_x_microns = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_x_microns", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_x_microns, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_mean_fwhm_lateral_asymmetry_ratio = Slot(uri="str(uriorcurie)", name="resolution_mean_fwhm_lateral_asymmetry_ratio", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_mean_fwhm_lateral_asymmetry_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_median_fwhm_lateral_asymmetry_ratio = Slot(uri="str(uriorcurie)", name="resolution_median_fwhm_lateral_asymmetry_ratio", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_median_fwhm_lateral_asymmetry_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.resolution_stdev_fwhm_lateral_asymmetry_ratio = Slot(uri="str(uriorcurie)", name="resolution_stdev_fwhm_lateral_asymmetry_ratio", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.resolution_stdev_fwhm_lateral_asymmetry_ratio, domain=None, range=Optional[Union[float, List[float]]])

slots.argolight_b_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/argolight_b_image'], name="argolight_b_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/argolight_b_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolight_b_image, domain=None, range=Union[dict, ImageAsNumpy])

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
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolight_e_image, domain=None, range=Union[dict, ImageAsNumpy])

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

slots.microscope__type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/type'], name="microscope__type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__type, domain=None, range=Optional[Union[str, "MicroscopeType"]])

slots.microscope__manufacturer = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/manufacturer'], name="microscope__manufacturer", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/manufacturer'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__manufacturer, domain=None, range=Optional[str])

slots.microscope__model = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/model'], name="microscope__model", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/model'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__model, domain=None, range=Optional[str])

slots.microscope__serial_number = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/serial_number'], name="microscope__serial_number", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/serial_number'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__serial_number, domain=None, range=Optional[str])

slots.microscope__url = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/url'], name="microscope__url", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/url'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__url, domain=None, range=Optional[str])

slots.microscope__comment = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comment'], name="microscope__comment", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comment'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.microscope__comment, domain=None, range=Optional[Union[Union[dict, Comment], List[Union[dict, Comment]]]])

slots.sample__type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/type'], name="sample__type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.sample__type, domain=None, range=URIRef)

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

slots.comment__comment_type = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comment_type'], name="comment__comment_type", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comment_type'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__comment_type, domain=None, range=Optional[Union[str, "CommentTypes"]])

slots.comment__text = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/text'], name="comment__text", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/text'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.comment__text, domain=None, range=str)

slots.metricsDataset__microscope = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/microscope'], name="metricsDataset__microscope", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/microscope'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__microscope, domain=None, range=Union[str, MicroscopeId])

slots.metricsDataset__sample = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/sample'], name="metricsDataset__sample", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/sample'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__sample, domain=None, range=Optional[Union[str, SampleType]])

slots.metricsDataset__experimenter = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/experimenter'], name="metricsDataset__experimenter", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/experimenter'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__experimenter, domain=None, range=Optional[Union[Union[str, ExperimenterOrcid], List[Union[str, ExperimenterOrcid]]]])

slots.metricsDataset__acquisition_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/acquisition_datetime'], name="metricsDataset__acquisition_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/acquisition_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__acquisition_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metricsDataset__processed = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processed'], name="metricsDataset__processed", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processed'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__processed, domain=None, range=Union[bool, Bool])

slots.metricsDataset__processing_datetime = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_datetime'], name="metricsDataset__processing_datetime", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_datetime'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__processing_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metricsDataset__processing_log = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/processing_log'], name="metricsDataset__processing_log", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/processing_log'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__processing_log, domain=None, range=Optional[str])

slots.metricsDataset__comment = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/comment'], name="metricsDataset__comment", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/comment'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__comment, domain=None, range=Optional[Union[Union[dict, Comment], List[Union[dict, Comment]]]])

slots.metricsDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/input'], name="metricsDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__input, domain=None, range=Optional[Union[dict, MetricsInput]])

slots.metricsDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/output'], name="metricsDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.metricsDataset__output, domain=None, range=Optional[Union[dict, MetricsOutput]])

slots.imageAsNumpy__data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data'], name="imageAsNumpy__data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.imageAsNumpy__data, domain=None, range=Optional[Union[dict, MetaObject]])

slots.imageMask__data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data'], name="imageMask__data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.imageMask__data, domain=None, range=Union[Union[bool, Bool], List[Union[bool, Bool]]])

slots.image2D__data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data'], name="image2D__data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image2D__data, domain=None, range=Union[float, List[float]])

slots.image5D__time_series = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/time_series'], name="image5D__time_series", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/time_series'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image5D__time_series, domain=None, range=Optional[Union[dict, TimeSeries]])

slots.image5D__channel_series = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/channel_series'], name="image5D__channel_series", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/channel_series'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image5D__channel_series, domain=None, range=Optional[Union[dict, ChannelSeries]])

slots.image5D__data = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/data'], name="image5D__data", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/data'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.image5D__data, domain=None, range=Union[float, List[float]])

slots.channelSeries__values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/values'], name="channelSeries__values", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.channelSeries__values, domain=None, range=Union[Union[dict, Channel], List[Union[dict, Channel]]])

slots.timeSeries__values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/values'], name="timeSeries__values", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.timeSeries__values, domain=None, range=Union[float, List[float]])

slots.roi__label = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/label'], name="roi__label", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/label'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__label, domain=None, range=URIRef)

slots.roi__description = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/description'], name="roi__description", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/description'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__description, domain=None, range=Optional[str])

slots.roi__image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/image'], name="roi__image", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__image, domain=None, range=Optional[Union[Union[str, ImageImageUrl], List[Union[str, ImageImageUrl]]]])

slots.roi__shapes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shapes'], name="roi__shapes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shapes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roi__shapes, domain=None, range=Optional[Union[Dict[Union[str, ShapeLabel], Union[dict, Shape]], List[Union[dict, Shape]]]])

slots.shape__label = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/label'], name="shape__label", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/label'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.shape__label, domain=None, range=URIRef)

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

slots.roiMassCenters__shapes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shapes'], name="roiMassCenters__shapes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shapes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roiMassCenters__shapes, domain=None, range=Optional[Union[Dict[Union[str, PointLabel], Union[dict, Point]], List[Union[dict, Point]]]])

slots.roiGeometricCenters__shapes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shapes'], name="roiGeometricCenters__shapes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shapes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roiGeometricCenters__shapes, domain=None, range=Optional[Union[Dict[Union[str, PointLabel], Union[dict, Point]], List[Union[dict, Point]]]])

slots.roiProfiles__shapes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shapes'], name="roiProfiles__shapes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shapes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roiProfiles__shapes, domain=None, range=Optional[Union[Dict[Union[str, LineLabel], Union[dict, Line]], List[Union[dict, Line]]]])

slots.roiMeasurements__shapes = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/shapes'], name="roiMeasurements__shapes", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/shapes'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.roiMeasurements__shapes, domain=None, range=Optional[Union[Dict[Union[str, RectangleLabel], Union[dict, Rectangle]], List[Union[dict, Rectangle]]]])

slots.tag__id = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/id'], name="tag__id", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/id'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tag__id, domain=None, range=URIRef)

slots.tag__text = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/text'], name="tag__text", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/text'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tag__text, domain=None, range=str)

slots.tag__description = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/description'], name="tag__description", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/description'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tag__description, domain=None, range=Optional[str])

slots.tableAsPandasDF__df = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/df'], name="tableAsPandasDF__df", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/df'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tableAsPandasDF__df, domain=None, range=Union[dict, MetaObject])

slots.tableAsDict__columns = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/columns'], name="tableAsDict__columns", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/columns'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.tableAsDict__columns, domain=None, range=Union[Dict[Union[str, ColumnName], Union[dict, Column]], List[Union[dict, Column]]])

slots.column__name = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/name'], name="column__name", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/name'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__name, domain=None, range=URIRef)

slots.column__source_uri = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/source_uri'], name="column__source_uri", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/source_uri'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__source_uri, domain=None, range=Optional[str])

slots.column__values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['core_schema/values'], name="column__values", curie=MICROSCOPEMETRICS_SCHEMA.curie('core_schema/values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.column__values, domain=None, range=Union[str, List[str]])

slots.fieldIlluminationDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/input'], name="fieldIlluminationDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationDataset__input, domain=None, range=Union[dict, FieldIlluminationInput])

slots.fieldIlluminationDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/output'], name="fieldIlluminationDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationDataset__output, domain=None, range=Optional[Union[dict, FieldIlluminationOutput]])

slots.fieldIlluminationOutput__key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/key_values'], name="fieldIlluminationOutput__key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__key_values, domain=None, range=Optional[Union[dict, FieldIlluminationKeyValues]])

slots.fieldIlluminationOutput__intensity_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/intensity_profiles'], name="fieldIlluminationOutput__intensity_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/intensity_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__intensity_profiles, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.fieldIlluminationOutput__intensity_map = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/intensity_map'], name="fieldIlluminationOutput__intensity_map", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/intensity_map'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__intensity_map, domain=None, range=Optional[Union[dict, Image5D]])

slots.fieldIlluminationOutput__profile_rois = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/profile_rois'], name="fieldIlluminationOutput__profile_rois", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/profile_rois'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__profile_rois, domain=None, range=Optional[Union[dict, RoiProfiles]])

slots.fieldIlluminationOutput__corner_rois = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/corner_rois'], name="fieldIlluminationOutput__corner_rois", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/corner_rois'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__corner_rois, domain=None, range=Optional[Union[dict, RoiMeasurements]])

slots.fieldIlluminationOutput__center_of_illumination = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/field_illumination_schema/center_of_illumination'], name="fieldIlluminationOutput__center_of_illumination", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/field_illumination_schema/center_of_illumination'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.fieldIlluminationOutput__center_of_illumination, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsDataset__input = Slot(uri="str(uriorcurie)", name="pSFBeadsDataset__input", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsDataset__input, domain=None, range=Union[dict, PSFBeadsInput])

slots.pSFBeadsDataset__output = Slot(uri="str(uriorcurie)", name="pSFBeadsDataset__output", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsDataset__output, domain=None, range=Optional[Union[dict, PSFBeadsOutput]])

slots.pSFBeadsOutput__bead_crops = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__bead_crops", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_crops, domain=None, range=Optional[Union[Dict[Union[str, ImageAsNumpyImageUrl], Union[dict, ImageAsNumpy]], List[Union[dict, ImageAsNumpy]]]])

slots.pSFBeadsOutput__analyzed_bead_centroids = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__analyzed_bead_centroids", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__analyzed_bead_centroids, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__discarded_bead_centroids_lateral_edge = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__discarded_bead_centroids_lateral_edge", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__discarded_bead_centroids_lateral_edge, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__discarded_bead_centroids_self_proximity = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__discarded_bead_centroids_self_proximity", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__discarded_bead_centroids_self_proximity, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__considered_bead_centroids_axial_edge = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__considered_bead_centroids_axial_edge", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centroids_axial_edge, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__considered_bead_centroids_cluster = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__considered_bead_centroids_cluster", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centroids_cluster, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__considered_bead_centroids_fit_quality = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__considered_bead_centroids_fit_quality", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__considered_bead_centroids_fit_quality, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.pSFBeadsOutput__key_values = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__key_values", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__key_values, domain=None, range=Optional[Union[dict, PSFBeadsKeyMeasurements]])

slots.pSFBeadsOutput__bead_properties = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__bead_properties", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_properties, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.pSFBeadsOutput__bead_z_profiles = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__bead_z_profiles", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_z_profiles, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.pSFBeadsOutput__bead_y_profiles = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__bead_y_profiles", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_y_profiles, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.pSFBeadsOutput__bead_x_profiles = Slot(uri="str(uriorcurie)", name="pSFBeadsOutput__bead_x_profiles", curie=None,
                   model_uri=MICROSCOPEMETRICS_SCHEMA.pSFBeadsOutput__bead_x_profiles, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.argolightBDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/input'], name="argolightBDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBDataset__input, domain=None, range=Union[dict, ArgolightBInput])

slots.argolightBDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/output'], name="argolightBDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBDataset__output, domain=None, range=Optional[Union[dict, ArgolightBOutput]])

slots.argolightBOutput__spots_labels_image = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_labels_image'], name="argolightBOutput__spots_labels_image", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_labels_image'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_labels_image, domain=None, range=Optional[Union[str, ImageAsNumpyImageUrl]])

slots.argolightBOutput__spots_centroids = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_centroids'], name="argolightBOutput__spots_centroids", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_centroids'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_centroids, domain=None, range=Optional[Union[Dict[Union[str, RoiMassCentersLabel], Union[dict, RoiMassCenters]], List[Union[dict, RoiMassCenters]]]])

slots.argolightBOutput__intensity_key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_key_values'], name="argolightBOutput__intensity_key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__intensity_key_values, domain=None, range=Optional[Union[dict, ArgolightBIntensityKeyValues]])

slots.argolightBOutput__distance_key_values = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/distance_key_values'], name="argolightBOutput__distance_key_values", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/distance_key_values'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__distance_key_values, domain=None, range=Optional[Union[dict, ArgolightBDistanceKeyValues]])

slots.argolightBOutput__spots_properties = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_properties'], name="argolightBOutput__spots_properties", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_properties'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_properties, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.argolightBOutput__spots_distances = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/spots_distances'], name="argolightBOutput__spots_distances", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/spots_distances'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightBOutput__spots_distances, domain=None, range=Optional[Union[dict, TableAsDict]])

slots.argolightEDataset__input = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/input'], name="argolightEDataset__input", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/input'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEDataset__input, domain=None, range=Union[dict, ArgolightEInput])

slots.argolightEDataset__output = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/output'], name="argolightEDataset__output", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/output'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEDataset__output, domain=None, range=Optional[Union[dict, ArgolightEOutput]])

slots.argolightEOutput__peaks_rois = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/peaks_rois'], name="argolightEOutput__peaks_rois", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/peaks_rois'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__peaks_rois, domain=None, range=Optional[Union[Dict[Union[str, RoiLabel], Union[dict, Roi]], List[Union[dict, Roi]]]])

slots.argolightEOutput__key_measurements = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/key_measurements'], name="argolightEOutput__key_measurements", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/key_measurements'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__key_measurements, domain=None, range=Optional[Union[dict, ArgolightEKeyValues]])

slots.argolightEOutput__intensity_profiles = Slot(uri=MICROSCOPEMETRICS_SCHEMA['samples/argolight_schema/intensity_profiles'], name="argolightEOutput__intensity_profiles", curie=MICROSCOPEMETRICS_SCHEMA.curie('samples/argolight_schema/intensity_profiles'),
                   model_uri=MICROSCOPEMETRICS_SCHEMA.argolightEOutput__intensity_profiles, domain=None, range=Optional[Union[dict, TableAsDict]])

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