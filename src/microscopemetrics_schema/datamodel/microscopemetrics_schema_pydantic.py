from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'microscopemetrics_schema',
     'default_range': 'string',
     'description': 'A schema for microscope-metrics, a python package for '
                    'microscope QC',
     'id': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema',
     'imports': ['linkml:types',
                 'core',
                 'analyses/field_illumination',
                 'analyses/psf_beads',
                 'analyses/light_source_power',
                 'analyses/user_experiment',
                 'samples/homogeneous_field',
                 'samples/beads',
                 'samples/light_source_power',
                 'samples/user_sample'],
     'license': 'GNU GPL v3.0',
     'name': 'microscopemetrics-schema',
     'prefixes': {'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'http://www.example.org/rdf#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'microscopemetrics_schema': {'prefix_prefix': 'microscopemetrics_schema',
                                               'prefix_reference': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/'}},
     'see_also': ['https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema'],
     'source_file': 'src/microscopemetrics_schema/schema/microscopemetrics_schema.yaml',
     'title': 'microscopemetrics-schema'} )

class PlaneAxisEnum(str, Enum):
    """
    The axis of the plane
    """
    XY = "XY"
    """
    The XY plane
    """
    XZ = "XZ"
    """
    The XZ plane
    """
    YZ = "YZ"
    """
    The YZ plane
    """


class AxisEnum(str, Enum):
    """
    The axis of the image
    """
    X = "X"
    """
    The X axis
    """
    Y = "Y"
    """
    The Y axis
    """
    Z = "Z"
    """
    The Z axis
    """
    C = "C"
    """
    The C axis
    """
    T = "T"
    """
    The T axis
    """


class CommentTypesEnum(str, Enum):
    """
    The type of the comment
    """
    ACQUISITION = "ACQUISITION"
    """
    The comment is referring to the acquisition
    """
    PROCESSING = "PROCESSING"
    """
    The comment is referring to the processing
    """
    OTHER = "OTHER"
    """
    The comment is referring to something else
    """


class MicroscopeTypeEnum(str, Enum):
    """
    The type of the microscope
    """
    WIDEFIELD = "WIDEFIELD"
    """
    A wide-field microscope
    """
    CONFOCAL = "CONFOCAL"
    """
    A confocal microscope
    """
    STED = "STED"
    """
    A STED microscope
    """
    SIM3D = "SIM3D"
    """
    A 3D-SIM microscope
    """
    OTHER = "OTHER"
    """
    Another type of microscope
    """


class OMEROObjectTypeEnum(str, Enum):
    """
    The type of the OMERO object
    """
    IMAGE = "IMAGE"
    """
    An image
    """
    CHANNEL = "CHANNEL"
    """
    A channel
    """
    DATASET = "DATASET"
    """
    A dataset
    """
    PROJECT = "PROJECT"
    """
    A project
    """
    EXPERIMENTERGROUP = "EXPERIMENTERGROUP"
    """
    A group
    """
    EXPERIMENTER = "EXPERIMENTER"
    """
    An experimenter
    """
    TABLE = "TABLE"
    """
    A table
    """
    KEY_VALUES = "KEY_VALUES"
    """
    A set of key-value pairs
    """
    TAG = "TAG"
    """
    A tag
    """
    COMMENT = "COMMENT"
    """
    A comment
    """
    ROI = "ROI"
    """
    A region of interest
    """
    FILEANNOTATION = "FILEANNOTATION"
    """
    A file
    """


class MeasuringLocationEnum(str, Enum):
    """
    The location at which the measurement was taken.
    """
    SOURCE_EXIT = "SOURCE_EXIT"
    """
    Power at the exit of the light source
    """
    FIBER_EXIT = "FIBER_EXIT"
    """
    Power at the exit of the fiber
    """
    OBJECTIVE_BACKFOCAL = "OBJECTIVE_BACKFOCAL"
    """
    Power at the back focal plane of the objective
    """
    OBJECTIVE_EXIT = "OBJECTIVE_EXIT"
    """
    Power at the exit of the objective
    """
    OBJECTIVE_FOCAL = "OBJECTIVE_FOCAL"
    """
    Power at the focal plane of the objective
    """
    OTHER = "OTHER"
    """
    Other location
    """



class NamedObject(ConfiguredBaseModel):
    """
    An object with a name and a description
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class DataReference(ConfiguredBaseModel):
    """
    A reference to a data resource
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'unique_keys': {'omero_reference': {'description': 'A metrics object is '
                                                            'uniquely identified by a '
                                                            'combination of its OMERO '
                                                            'attributes',
                                             'unique_key_name': 'omero_reference',
                                             'unique_key_slots': ['omero_host',
                                                                  'omero_object_type',
                                                                  'omero_object_id']}}})

    data_uri: Optional[str] = Field(default=None, description="""The URI of the object data""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataReference']} })
    omero_host: Optional[str] = Field(default=None, description="""The host of the OMERO server""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataReference']} })
    omero_port: Optional[int] = Field(default=None, description="""The port of the OMERO server""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataReference']} })
    omero_object_type: Optional[OMEROObjectTypeEnum] = Field(default=None, description="""The type of the OMERO object""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataReference']} })
    omero_object_id: Optional[int] = Field(default=None, description="""The ID of the OMERO object""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataReference']} })


class MetricsObject(NamedObject):
    """
    A base object for all microscope-metrics objects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class MicroscopeCollection(ConfiguredBaseModel):
    """
    A collection of microscopes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    microscope_collection: list[Microscope] = Field(default=..., description="""The microscopes of the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroscopeCollection']} })


class Microscope(MetricsObject):
    """
    A microscope
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    microscope_type: Optional[MicroscopeTypeEnum] = Field(default=None, description="""The type of the microscope""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    model: Optional[str] = Field(default=None, description="""The model of a device""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'PowerMeter']} })
    serial_number: Optional[str] = Field(default=None, description="""The serial number of a device""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope']} })
    comment_collection: Optional[list[Comment]] = Field(default=None, description="""A collection of comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Sample(NamedObject):
    """
    A sample is a standard physical object that is imaged by a microscope
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Protocol(NamedObject):
    """
    Set of instructions for preparing a sample or acquiring data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    version: str = Field(default=..., description="""The version of the protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    authors: Optional[list[Experimenter]] = Field(default=None, description="""The authors of the protocol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    url: str = Field(default=..., description="""The URL where the protocol can be found""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Experimenter(MetricsObject):
    """
    The person that performed the experiment or developed the protocol
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    orcid: Optional[str] = Field(default=None, description="""The ORCID of the experimenter""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experimenter']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Comment(MetricsObject):
    """
    A comment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    comment_datetime: datetime  = Field(default=..., description="""The datetime to which the comment is referring""", json_schema_extra = { "linkml_meta": {'domain_of': ['Comment']} })
    author: Optional[Experimenter] = Field(default=None, description="""The author of the comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Comment']} })
    comment_type: CommentTypesEnum = Field(default=..., description="""The type of the comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Comment']} })
    text: str = Field(default=..., description="""The text of the comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Comment']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class MetricsDatasetCollection(MetricsObject):
    """
    A collection of microscope-metrics datasets
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    dataset_collection: Optional[list[MetricsDataset]] = Field(default=None, description="""The datasets of the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDatasetCollection']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class HarmonizedMetricsDatasetCollection(MetricsDatasetCollection):
    """
    A collection of harmonized microscope-metrics datasets. All of the datasets in the collection share the same analysis and processing parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    dataset_class: str = Field(default=..., description="""The class of the datasets in the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['HarmonizedMetricsDatasetCollection']} })
    dataset_collection: Optional[list[MetricsDataset]] = Field(default=None, description="""The datasets of the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDatasetCollection']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class MetricsDataset(MetricsObject):
    """
    A base object on which microscope-metrics runs the analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'tree_root': True})

    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    input_data: MetricsInputData = Field(default=..., description="""The input data for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    output: Optional[MetricsOutput] = Field(default=None, description="""The output of the analysis""", json_schema_extra = { "linkml_meta": {'abstract': True, 'domain_of': ['MetricsDataset']} })
    microscope: Microscope = Field(default=..., description="""The microscope that was used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    experimenter: Optional[Experimenter] = Field(default=None, description="""The experimenter that performed the imaging experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    acquisition_protocol: Optional[Protocol] = Field(default=None, description="""The protocol used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    processed: bool = Field(default=False, description="""Has the dataset been processed by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset'], 'ifabsent': 'False'} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class HasSampleMixin(ConfiguredBaseModel):
    """
    A mixin for objects that have a sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    sample: Optional[Sample] = Field(default=None, description="""The physical sample that was imaged""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSampleMixin']} })


class HasInputParametersMixin(ConfiguredBaseModel):
    """
    A mixin for objects that have input parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    input_parameters: Optional[MetricsInputParameters] = Field(default=None, description="""The input parameters for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasInputParametersMixin']} })


class MetricsInputData(ConfiguredBaseModel):
    """
    An abstract class for analysis input data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    pass


class MetricsInputParameters(ConfiguredBaseModel):
    """
    An abstract class for analysis inputs parameters
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    pass


class MetricsOutput(ConfiguredBaseModel):
    """
    An abstract class for analysis outputs
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    key_measurements: list[KeyMeasurement] = Field(default=..., description="""A list of KeyMeasurement subclasses summarizing the most important measurements as a function of, for example, channels""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    comment: Optional[Comment] = Field(default=None, description="""A human readable comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_application: list[str] = Field(default=..., description="""The application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_version: list[str] = Field(default=..., description="""The version of the application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_entity: Optional[list[str]] = Field(default=None, description="""The entity that processed the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_datetime: datetime  = Field(default=..., description="""The datetime of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_log: Optional[str] = Field(default=None, description="""The log of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    warnings: Optional[list[str]] = Field(default=None, description="""The warnings of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    errors: Optional[list[str]] = Field(default=None, description="""The errors of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    validated: bool = Field(default=False, description="""Has the dataset been validated by a human""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput'], 'ifabsent': 'False'} })
    validation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the validation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })


class Image(MetricsObject):
    """
    A microscope-metrics image
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    voxel_size_x_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the x dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_y_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the y dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_z_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the z dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_x: int = Field(default=..., description="""The shape of an image in the x dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_y: int = Field(default=..., description="""The shape of an image in the y dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_z: int = Field(default=1, description="""The shape of an image in the z dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_c: int = Field(default=1, description="""The shape of an image in the c dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_t: int = Field(default=1, description="""The shape of an image in the t dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    time_series: Optional[TimeSeries] = Field(default=None, description="""A series representing time for time-lapse images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis0']} })
    channel_series: Optional[ChannelSeries] = Field(default=None, description="""A series representing channels for multi-channel images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis4']} })
    source_images: Optional[list[DataReference]] = Field(default=None, description="""A list of references linking to the images that were used as a source""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    array_data: Optional[Any] = Field(default=None, description="""A non-required slot for non-serializable array data object""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class ImageMask(Image):
    """
    A mask image. Either a binary image or a label image
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    voxel_size_x_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the x dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_y_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the y dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_z_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the z dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_x: int = Field(default=..., description="""The shape of an image in the x dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_y: int = Field(default=..., description="""The shape of an image in the y dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_z: int = Field(default=1, description="""The shape of an image in the z dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_c: int = Field(default=1, description="""The shape of an image in the c dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_t: int = Field(default=1, description="""The shape of an image in the t dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    time_series: Optional[TimeSeries] = Field(default=None, description="""A series representing time for time-lapse images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis0']} })
    channel_series: Optional[ChannelSeries] = Field(default=None, description="""A series representing channels for multi-channel images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis4']} })
    source_images: Optional[list[DataReference]] = Field(default=None, description="""A list of references linking to the images that were used as a source""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    array_data: Optional[Any] = Field(default=None, description="""A non-required slot for non-serializable array data object""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class OrthogonalImage(Image):
    """
    An image that is orthogonal to the main image
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    source_roi: Roi = Field(default=..., description="""The source ROI of the orthogonal image. The ROI has to contain a single point shape.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OrthogonalImage']} })
    axis: PlaneAxisEnum = Field(default=..., description="""The axis of the orthogonal image""", json_schema_extra = { "linkml_meta": {'domain_of': ['OrthogonalImage']} })
    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    voxel_size_x_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the x dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_y_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the y dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    voxel_size_z_micron: Optional[float] = Field(default=None, description="""The physical size in the voxel in the z dimension in microns""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_x: int = Field(default=..., description="""The shape of an image in the x dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_y: int = Field(default=..., description="""The shape of an image in the y dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    shape_z: int = Field(default=1, description="""The shape of an image in the z dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_c: int = Field(default=1, description="""The shape of an image in the c dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    shape_t: int = Field(default=1, description="""The shape of an image in the t dimension""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'ifabsent': 'int(1)'} })
    time_series: Optional[TimeSeries] = Field(default=None, description="""A series representing time for time-lapse images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis0']} })
    channel_series: Optional[ChannelSeries] = Field(default=None, description="""A series representing channels for multi-channel images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image'], 'implements': ['linkml:axis4']} })
    source_images: Optional[list[DataReference]] = Field(default=None, description="""A list of references linking to the images that were used as a source""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    array_data: Optional[Any] = Field(default=None, description="""A non-required slot for non-serializable array data object""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class ChannelSeries(ConfiguredBaseModel):
    """
    A series representing channels
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'implements': ['linkml:OneDimensionalSeries']})

    channels: list[Channel] = Field(default=..., description="""The channels of the ChannelSeries""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChannelSeries'], 'implements': ['linkml:elements']} })


class Channel(MetricsObject):
    """
    A image channel
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    excitation_wavelength_nm: Optional[float] = Field(default=None, description="""The excitation wavelength in nm""", json_schema_extra = { "linkml_meta": {'domain_of': ['Channel']} })
    emission_wavelength_nm: Optional[float] = Field(default=None, description="""The emission wavelength in nm""", json_schema_extra = { "linkml_meta": {'domain_of': ['Channel']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class TimeSeries(ConfiguredBaseModel):
    """
    A series whose values represent time
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'implements': ['linkml:OneDimensionalSeries']})

    time_points_sec: list[float] = Field(default=..., description="""The relative times at which the time series were acquired in seconds""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries'], 'implements': ['linkml:elements']} })


class Column(NamedObject):
    """
    Attributes of a column
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    source_reference: Optional[DataReference] = Field(default=None, description="""The source object of the column""", json_schema_extra = { "linkml_meta": {'domain_of': ['Column']} })
    data_type: str = Field(default="str", description="""The data type of the column""", json_schema_extra = { "linkml_meta": {'domain_of': ['Column'], 'ifabsent': 'string(str)'} })
    values: Optional[list[str]] = Field(default=None, description="""An optional container for the values of the column""", json_schema_extra = { "linkml_meta": {'domain_of': ['Column']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Roi(MetricsObject):
    """
    A ROI (Region Of Interest). Collection of shapes and an image to which they are applied
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    points: Optional[list[Point]] = Field(default=None, description="""A list of points included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    lines: Optional[list[Line]] = Field(default=None, description="""A list of lines included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    rectangles: Optional[list[Rectangle]] = Field(default=None, description="""A list of rectangles included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    ellipses: Optional[list[Ellipse]] = Field(default=None, description="""A list of ellipses included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    polygons: Optional[list[Polygon]] = Field(default=None, description="""A list of polygons included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    masks: Optional[list[Mask]] = Field(default=None, description="""A list of masks included in the ROI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Roi']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Shape(NamedObject):
    """
    A shape
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Point(Shape):
    """
    A point as defined by x and y coordinates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x: float = Field(default=..., description="""The x coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    y: float = Field(default=..., description="""The y coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Line(Shape):
    """
    A line as defined by x1, y1, x2, y2 coordinates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x1: float = Field(default=..., description="""The x coordinate of the first point of the line""", json_schema_extra = { "linkml_meta": {'domain_of': ['Line']} })
    y1: float = Field(default=..., description="""The y coordinate of the first point of the line""", json_schema_extra = { "linkml_meta": {'domain_of': ['Line']} })
    x2: float = Field(default=..., description="""The x coordinate of the second point of the line""", json_schema_extra = { "linkml_meta": {'domain_of': ['Line']} })
    y2: float = Field(default=..., description="""The y coordinate of the second point of the line""", json_schema_extra = { "linkml_meta": {'domain_of': ['Line']} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Rectangle(Shape):
    """
    A rectangle as defined by x, y coordinates and width, height
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x: float = Field(default=..., description="""The x coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    y: float = Field(default=..., description="""The y coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    w: float = Field(default=..., description="""The width""", json_schema_extra = { "linkml_meta": {'domain_of': ['Rectangle', 'Ellipse']} })
    h: float = Field(default=..., description="""The height""", json_schema_extra = { "linkml_meta": {'domain_of': ['Rectangle', 'Ellipse']} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Ellipse(Shape):
    """
    An ellipse as defined by x, y coordinates and x and y radii
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x: float = Field(default=..., description="""The x coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    y: float = Field(default=..., description="""The y coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    w: float = Field(default=..., description="""The width""", json_schema_extra = { "linkml_meta": {'domain_of': ['Rectangle', 'Ellipse']} })
    h: float = Field(default=..., description="""The height""", json_schema_extra = { "linkml_meta": {'domain_of': ['Rectangle', 'Ellipse']} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Polygon(Shape):
    """
    A polygon as defined by a series of vertexes and a boolean to indicate if closed or not
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    vertexes: list[Vertex] = Field(default=..., description="""A list of vertexes defining the polygon""", json_schema_extra = { "linkml_meta": {'domain_of': ['Polygon']} })
    is_open: bool = Field(default=False, description="""Is the polygon open. By default, it is closed (false)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Polygon'], 'ifabsent': 'False'} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Vertex(ConfiguredBaseModel):
    """
    A vertex as defined by x and y coordinates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x: float = Field(default=..., description="""The x coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    y: float = Field(default=..., description="""The y coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })


class Mask(Shape):
    """
    A mask as defined by a boolean image
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    x: float = Field(default=..., description="""The x coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    y: float = Field(default=..., description="""The y coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Point', 'Rectangle', 'Ellipse', 'Vertex', 'Mask']} })
    mask: Optional[ImageMask] = Field(default=None, description="""The mask image""", json_schema_extra = { "linkml_meta": {'domain_of': ['Mask']} })
    z: Optional[float] = Field(default=None, description="""The z coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    c: Optional[int] = Field(default=None, description="""The c coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    t: Optional[int] = Field(default=None, description="""The t coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    fill_color: Optional[Color] = Field(default=None, description="""The fill color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_color: Optional[Color] = Field(default=None, description="""The stroke color of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape']} })
    stroke_width: Optional[int] = Field(default=1, description="""The stroke width of the shape""", json_schema_extra = { "linkml_meta": {'domain_of': ['Shape'], 'ifabsent': 'int(1)'} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class Color(ConfiguredBaseModel):
    """
    A color as defined by RGB values and an optional alpha value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    r: int = Field(default=128, description="""The red value of the color""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['Color'], 'ifabsent': 'int(128)'} })
    g: int = Field(default=128, description="""The green value of the color""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['Color'], 'ifabsent': 'int(128)'} })
    b: int = Field(default=128, description="""The blue value of the color""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['Color'], 'ifabsent': 'int(128)'} })
    alpha: Optional[int] = Field(default=255, description="""The alpha value of the color (optional)""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['Color'], 'ifabsent': 'int(255)'} })


class CentersOfMass(ConfiguredBaseModel):
    """
    The center of mass of detected objects. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    pass


class CentersGeometric(ConfiguredBaseModel):
    """
    The geometric center of detected objects. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    pass


class CentersFitted(ConfiguredBaseModel):
    """
    The fitted center of detected objects. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    pass


class CentersMaxIntensity(ConfiguredBaseModel):
    """
    The position of maximum intensity of detected objects. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    pass


class ProfilesIntensity(ConfiguredBaseModel):
    """
    Profiles computed on the image. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    intensity_profiles_table: Optional[Table] = Field(default=None, description="""Linked table of profiles""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProfilesIntensity']} })


class RoiMeasurements(ConfiguredBaseModel):
    """
    Measurements computed on the ROIs of an image. Intended to be used with ROIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core',
         'mixin': True})

    measurements_table: Optional[Table] = Field(default=None, description="""Linked table of measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['RoiMeasurements']} })


class KeyMeasurement(ConfiguredBaseModel):
    """
    A dict-like of key measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    pass


class Table(MetricsObject):
    """
    A microscope-metrics table
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/core'})

    table_data: Optional[Any] = Field(default=None, description="""A non-required slot for non-serializable table data object""", json_schema_extra = { "linkml_meta": {'domain_of': ['Table']} })
    columns: list[Column] = Field(default=..., description="""The columns of the table""", json_schema_extra = { "linkml_meta": {'domain_of': ['Table'], 'implements': ['linkml:elements']} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class HomogeneousField(Sample):
    """
    An homogeneous field.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/homogeneous_field'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class FluorescentHomogeneousThickField(HomogeneousField):
    """
    An homogeneous field with a fluorescent thick sample. Similar to the Chroma slides.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/homogeneous_field'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class FluorescentHomogeneousThinField(HomogeneousField):
    """
    An homogeneous field with a fluorescent thin sample. Similar to a dye thin layer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/homogeneous_field'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class FieldIlluminationDataset(HasInputParametersMixin, HasSampleMixin, MetricsDataset):
    """
    A field illumination dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/field_illumination',
         'mixins': ['HasSampleMixin', 'HasInputParametersMixin'],
         'slot_usage': {'input_data': {'name': 'input_data',
                                       'range': 'FieldIlluminationInputData'},
                        'input_parameters': {'name': 'input_parameters',
                                             'range': 'FieldIlluminationInputParameters'},
                        'output': {'name': 'output',
                                   'range': 'FieldIlluminationOutput'},
                        'sample': {'name': 'sample', 'range': 'HomogeneousField'}}})

    sample: Optional[HomogeneousField] = Field(default=None, description="""The physical sample that was imaged""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSampleMixin']} })
    input_parameters: Optional[FieldIlluminationInputParameters] = Field(default=None, description="""The input parameters for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasInputParametersMixin']} })
    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    input_data: FieldIlluminationInputData = Field(default=..., description="""The input data for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    output: Optional[FieldIlluminationOutput] = Field(default=None, description="""The output of the analysis""", json_schema_extra = { "linkml_meta": {'abstract': True, 'domain_of': ['MetricsDataset']} })
    microscope: Microscope = Field(default=..., description="""The microscope that was used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    experimenter: Optional[Experimenter] = Field(default=None, description="""The experimenter that performed the imaging experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    acquisition_protocol: Optional[Protocol] = Field(default=None, description="""The protocol used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    processed: bool = Field(default=False, description="""Has the dataset been processed by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset'], 'ifabsent': 'False'} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class FieldIlluminationInputData(MetricsInputData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/field_illumination'})

    field_illumination_images: list[Image] = Field(default=..., description="""Input parameter: homogeneity image provided in the order TZYXC. While the analysis accepts multiple channels, the T and Z dimensions are expected to be 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputData']} })


class FieldIlluminationInputParameters(MetricsInputParameters):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/field_illumination',
         'slot_usage': {'saturation_threshold': {'name': 'saturation_threshold',
                                                 'required': True}}})

    bit_depth: Optional[int] = Field(default=None, description="""Detector bit depth""", ge=1, le=64, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters']} })
    saturation_threshold: float = Field(default=0.01, description="""Tolerated saturation threshold. If the amount of saturated pixels is above this threshold, the image is considered as saturated and the analysis is not performed.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters'],
         'ifabsent': 'float(0.01)'} })
    corner_fraction: float = Field(default=0.1, description="""Input parameter: the proportion of the image to be considered as corner or center""", ge=0.01, le=0.49, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters'], 'ifabsent': 'float(0.1)'} })
    sigma: float = Field(default=5.0, description="""Input parameter: the sigma for the smoothing gaussian filter to be applied prior to analysis""", ge=2.0, le=8.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters'], 'ifabsent': 'float(5.0)'} })


class FieldIlluminationOutput(MetricsOutput):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/field_illumination',
         'slot_usage': {'intensity_profiles': {'description': 'Intensity profiles for '
                                                              'the field illumination '
                                                              'analysis in the '
                                                              'different directions',
                                               'name': 'intensity_profiles'},
                        'key_measurements': {'name': 'key_measurements',
                                             'range': 'FieldIlluminationKeyMeasurement'}}})

    intensity_profiles: Optional[list[Table]] = Field(default=None, description="""Intensity profiles for the field illumination analysis in the different directions""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput', 'UserExperimentOutput']} })
    roi_profiles: Optional[list[Roi]] = Field(default=None, description="""line ROIs used to compute the intensity profiles""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_corners: Optional[list[Roi]] = Field(default=None, description="""Rectangular ROIs used to compute the corner intensities. The sama ROI is assigned to multiple images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_centers_of_mass: Optional[list[Roi]] = Field(default=None, description="""Point ROIs marking the center of mass of the area of maximum illumination. When the image is very flat, the 99 percentile is used instead. One point per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_centers_geometric: Optional[list[Roi]] = Field(default=None, description="""Point ROIs marking the geometric center of the area of maximum illumination. One point per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_centers_fitted: Optional[list[Roi]] = Field(default=None, description="""Point ROIs marking the fitted center of the area of maximum illumination. One point per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_centers_max_intensity: Optional[list[Roi]] = Field(default=None, description="""Point ROIs marking the maximum intensity of the area of maximum illumination. One point per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    roi_center_region: Optional[list[Roi]] = Field(default=None, description="""Mask ROIs marking the area of maximum illumination. One mask per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput']} })
    key_measurements: list[FieldIlluminationKeyMeasurement] = Field(default=..., description="""A list of KeyMeasurement subclasses summarizing the most important measurements as a function of, for example, channels""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    comment: Optional[Comment] = Field(default=None, description="""A human readable comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_application: list[str] = Field(default=..., description="""The application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_version: list[str] = Field(default=..., description="""The version of the application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_entity: Optional[list[str]] = Field(default=None, description="""The entity that processed the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_datetime: datetime  = Field(default=..., description="""The datetime of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_log: Optional[str] = Field(default=None, description="""The log of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    warnings: Optional[list[str]] = Field(default=None, description="""The warnings of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    errors: Optional[list[str]] = Field(default=None, description="""The errors of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    validated: bool = Field(default=False, description="""Has the dataset been validated by a human""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput'], 'ifabsent': 'False'} })
    validation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the validation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })


class FieldIlluminationKeyMeasurement(KeyMeasurement):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/field_illumination'})

    image_name: Optional[str] = Field(default=None, description="""The name of the image where the measurement was taken""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    image_id: Optional[str] = Field(default=None, description="""The id of the image where the measurement was taken. If images are originary in OMERO this is the image_id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    channel_name: Optional[str] = Field(default=None, description="""The channel name to which the measurements apply""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    channel_nr: Optional[int] = Field(default=None, description="""The channel number to which the measurements apply""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    channel_id: Optional[str] = Field(default=None, description="""The channel id to which the measurements apply""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_region_intensity_fraction: Optional[float] = Field(default=None, description="""The fraction of the upper intensity range occupied by the center of illumination region. That is, a value of 0.1 means that the center of illumination occupies the top 10% of the intensity range. microscope-metrics tries to adapt the threshold of this intensity so that the area occupied is not too large. One value per channel.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_region_area_fraction: Optional[float] = Field(default=None, description="""The fraction of the area occupied by the center of illumination region. If the centre upper intensity fraction is 0.1, that means that the center of illumination occupies 10% of the area of the image. One value per channel.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_of_mass_y: Optional[float] = Field(default=None, description="""The y coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_of_mass_y_relative: Optional[float] = Field(default=None, description="""The relative y position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_of_mass_x: Optional[float] = Field(default=None, description="""The x coordinate of the center of mass of the center of illumination region. In pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_of_mass_x_relative: Optional[float] = Field(default=None, description="""The relative x position of the center of mass of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge. One value per channel.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_of_mass_distance_relative: Optional[float] = Field(default=None, description="""The relative distance of the centers of mass to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image. One value per channel.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_geometric_y: Optional[float] = Field(default=None, description="""The y coordinate of the geometric center of the center of illumination region. In pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_geometric_y_relative: Optional[float] = Field(default=None, description="""The relative y position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge. One value per channel.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_geometric_x: Optional[float] = Field(default=None, description="""The x coordinate of the geometric center of the center of illumination region. In pixels""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_geometric_x_relative: Optional[float] = Field(default=None, description="""The relative x position of the geometric center of the center of illumination region.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_geometric_distance_relative: Optional[float] = Field(default=None, description="""The relative distance of the geometric center to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_fitted_y: Optional[float] = Field(default=None, description="""The y coordinate of the fitted center of illumination. In pixels""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_fitted_y_relative: Optional[float] = Field(default=None, description="""The relative y position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_fitted_x: Optional[float] = Field(default=None, description="""The x coordinate of the fitted center of illumination. In pixels""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_fitted_x_relative: Optional[float] = Field(default=None, description="""The relative x position of the fitted center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    center_fitted_distance_relative: Optional[float] = Field(default=None, description="""The relative distance of the fitted center of illumination to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity: Optional[float] = Field(default=None, description="""The maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity_pos_y: Optional[float] = Field(default=None, description="""The y coordinate of the maximum intensity of the center of illumination. In pixels""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity_pos_y_relative: Optional[float] = Field(default=None, description="""The relative y position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is upper edge, 0.0 is center and 1.0 is lower edge.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity_pos_x: Optional[float] = Field(default=None, description="""The x coordinate of the maximum intensity of the center of illumination. In pixels""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity_pos_x_relative: Optional[float] = Field(default=None, description="""The relative x position of the maximum intensity of the center of illumination.  Relative to the image size along that axis. -1.0 is left edge, 0.0 is center and 1.0 is right edge.""", ge=-1.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    max_intensity_distance_relative: Optional[float] = Field(default=None, description="""The relative distance of the maximum intensity to the center of the image. Relative to the distance to  an image corner. 0.0 is centered and 1.0 at a distance equal to the the corner of the image.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_left_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the top-left corner of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_left_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the top-left corner of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_center_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the top-center of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_center_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the top-center of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_right_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the top-right corner of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    top_right_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the top-right corner of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_left_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the middle-left of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_left_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the middle-left of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_center_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the middle-center of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_center_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the middle-center of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_right_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the middle-right of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    middle_right_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the middle-right of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_left_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-left of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_left_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-left of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_center_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-center of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_center_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-center of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_right_intensity_mean: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-right of the image""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })
    bottom_right_intensity_ratio: Optional[float] = Field(default=None, description="""The mean intensity of the bottom-right of the image  divided by the maximum intensity of the center of illumination""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement']} })


class FLuorescentBeads(Sample):
    """
    A sample of fluorescent beads.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/beads'})

    bead_diameter_micron: float = Field(default=..., description="""The diameter of the beads in the sample measured in microns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    excitation_wavelengths_nm: list[float] = Field(default=..., description="""The excitation wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    emission_wavelengths_nm: list[float] = Field(default=..., description="""The emission wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class MultiWavelengthBeads(FLuorescentBeads):
    """
    A sample of beads fluorescent in different wavelengths.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/beads'})

    bead_diameter_micron: float = Field(default=..., description="""The diameter of the beads in the sample measured in microns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    excitation_wavelengths_nm: list[float] = Field(default=..., description="""The excitation wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    emission_wavelengths_nm: list[float] = Field(default=..., description="""The emission wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class PSFBeads(FLuorescentBeads):
    """
    A sample of beads with subresolution size used for PSF estimation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/beads'})

    bead_diameter_micron: float = Field(default=..., description="""The diameter of the beads in the sample measured in microns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    excitation_wavelengths_nm: list[float] = Field(default=..., description="""The excitation wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    emission_wavelengths_nm: list[float] = Field(default=..., description="""The emission wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class NonPSFBeads(FLuorescentBeads):
    """
    A sample of beads without subresolution size.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/beads'})

    bead_diameter_micron: float = Field(default=..., description="""The diameter of the beads in the sample measured in microns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    excitation_wavelengths_nm: list[float] = Field(default=..., description="""The excitation wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    emission_wavelengths_nm: list[float] = Field(default=..., description="""The emission wavelength of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FLuorescentBeads']} })
    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class PSFBeadsDataset(HasInputParametersMixin, HasSampleMixin, MetricsDataset):
    """
    A PSF beads dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/psf_beads',
         'mixins': ['HasSampleMixin', 'HasInputParametersMixin'],
         'slot_usage': {'input_data': {'name': 'input_data',
                                       'range': 'PSFBeadsInputData'},
                        'input_parameters': {'name': 'input_parameters',
                                             'range': 'PSFBeadsInputParameters'},
                        'output': {'name': 'output', 'range': 'PSFBeadsOutput'},
                        'sample': {'name': 'sample', 'range': 'PSFBeads'}}})

    sample: Optional[PSFBeads] = Field(default=None, description="""The physical sample that was imaged""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSampleMixin']} })
    input_parameters: Optional[PSFBeadsInputParameters] = Field(default=None, description="""The input parameters for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasInputParametersMixin']} })
    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    input_data: PSFBeadsInputData = Field(default=..., description="""The input data for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    output: Optional[PSFBeadsOutput] = Field(default=None, description="""The output of the analysis""", json_schema_extra = { "linkml_meta": {'abstract': True, 'domain_of': ['MetricsDataset']} })
    microscope: Microscope = Field(default=..., description="""The microscope that was used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    experimenter: Optional[Experimenter] = Field(default=None, description="""The experimenter that performed the imaging experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    acquisition_protocol: Optional[Protocol] = Field(default=None, description="""The protocol used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    processed: bool = Field(default=False, description="""Has the dataset been processed by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset'], 'ifabsent': 'False'} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class PSFBeadsInputData(MetricsInputData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/psf_beads'})

    psf_beads_images: list[Image] = Field(default=..., description="""The image containing the beads provided in the order TZYXC. More than one image can be provided if the image conditions are the same.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputData']} })


class PSFBeadsInputParameters(MetricsInputParameters):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/psf_beads'})

    bit_depth: Optional[int] = Field(default=None, description="""Detector bit depth""", ge=1, le=64, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters']} })
    saturation_threshold: Optional[float] = Field(default=0.01, description="""Tolerated saturation threshold. If the amount of saturated pixels is above this threshold, the image is considered as saturated and the analysis is not performed.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters'],
         'ifabsent': 'float(0.01)'} })
    min_lateral_distance_factor: float = Field(default=20, description="""Minimal distance that has to separate laterally the beads represented as the  number of times the expected FWHM of the beads.""", ge=10.0, le=30.0, json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(20)'} })
    sigma_min: float = Field(default=1.0, description="""Min value for the range of sigmas used in for the detection of the beads. Lower values will tend to include  noisy pixels as beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(1.0)'} })
    sigma_max: float = Field(default=5.0, description="""Max value for the range of sigmas used in for the detection of the beads. Higher values will tend to detect  larger objects as beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(5.0)'} })
    snr_threshold: float = Field(default=10.0, description="""Signal to noise ratio threshold to be used for bead detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(10.0)'} })
    fitting_gaussian_r2_threshold: float = Field(default=0.95, description="""Threshold for the coefficient of determination (R^2) of the gaussian fit to be considered good.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(0.95)'} })
    fitting_airy_r2_threshold: float = Field(default=0.5, description="""Threshold for the coefficient of determination (R^2) of the airy fit to be considered good.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(0.5)'} })
    intensity_robust_z_score_threshold: float = Field(default=2.0, description="""Threshold for the robust z-score of the intensity of the bead to be considered good.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsInputParameters'], 'ifabsent': 'float(2.0)'} })


class PSFBeadsOutput(MetricsOutput):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/psf_beads',
         'slot_usage': {'key_measurements': {'name': 'key_measurements',
                                             'range': 'PSFBeadsKeyMeasurement'}}})

    analyzed_bead_centers: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads that have been analyzed. One point shape will be provided per bead correctly detected. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_lateral_edge: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as too close to the edge of the image. Measurements on these bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_self_proximity: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as too close to another bead. Measurements on these bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_axial_edge: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as too close to the top and or bottom of the image. Measurements on these bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_intensity_outlier: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as being too intense and potentially represent a cluster of beads. Intensity robust z-score over requested threshold. Measurements on these bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_z_fit_airy_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the airy fit quality in z was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in z for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_y_fit_airy_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the airy fit quality in y was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in y for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_x_fit_airy_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the airy fit quality in x was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in x for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_z_fit_gaussian_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the gaussian fit quality in z was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in z for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_y_fit_gaussian_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the gaussian fit quality in y was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in y for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    considered_bead_centers_x_fit_gaussian_quality: Optional[list[Roi]] = Field(default=None, description="""The centers of the beads detected but considered as the airy gaussian quality in x was not good enough.  coefficient of determination (R^2) (R^2) over requested threshold. Measurements in x for this bead not considered for the dataset analysis. One point will be provided per bead. One ROI per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    bead_properties: Optional[Table] = Field(default=None, description="""Properties associated with the analysis of the beads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    bead_profiles_z: Optional[Table] = Field(default=None, description="""The intensity profiles along the z axis of the analyzed beads as well as the fits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    bead_profiles_y: Optional[Table] = Field(default=None, description="""The intensity profiles along the y axis of the analyzed beads as well as the fits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    bead_profiles_x: Optional[Table] = Field(default=None, description="""The intensity profiles along the x axis of the analyzed beads as well as the fits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    average_bead: Optional[Image] = Field(default=None, description="""The average bead image created from all the beads considered valid. The average bead is calculated after aligning the beads in all three axes. This one image contains all the channels. If the analysis does not detect at least two beads in a channel, the average bead for this channel is not calculated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsOutput']} })
    key_measurements: list[PSFBeadsKeyMeasurement] = Field(default=..., description="""A list of KeyMeasurement subclasses summarizing the most important measurements as a function of, for example, channels""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    comment: Optional[Comment] = Field(default=None, description="""A human readable comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_application: list[str] = Field(default=..., description="""The application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_version: list[str] = Field(default=..., description="""The version of the application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_entity: Optional[list[str]] = Field(default=None, description="""The entity that processed the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_datetime: datetime  = Field(default=..., description="""The datetime of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_log: Optional[str] = Field(default=None, description="""The log of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    warnings: Optional[list[str]] = Field(default=None, description="""The warnings of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    errors: Optional[list[str]] = Field(default=None, description="""The errors of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    validated: bool = Field(default=False, description="""Has the dataset been validated by a human""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput'], 'ifabsent': 'False'} })
    validation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the validation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })


class PSFBeadsKeyMeasurement(KeyMeasurement):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/psf_beads'})

    channel_name: Optional[str] = Field(default=None, description="""The channel name to which the measurements apply""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    channel_nr: Optional[int] = Field(default=None, description="""The channel number to which the measurements apply""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    total_bead_count: Optional[int] = Field(default=None, description="""Total number of beads detected in the image. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_valid_count: Optional[int] = Field(default=None, description="""Number of beads analyzed. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_self_proximity_count: Optional[int] = Field(default=None, description="""Number of beads considered for being too close to another bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_lateral_edge_count: Optional[int] = Field(default=None, description="""Number of beads considered for being too close to the edge of the image. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_axial_edge_count: Optional[int] = Field(default=None, description="""Number of beads considered as being too close to the top and or bottom of the image. These beads are not considered for the z axis FWHM measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_intensity_outlier_count: Optional[int] = Field(default=None, description="""Number of beads considered as being too intense and potentially represent a cluster of beads. These beads have a robust z-score over the requested threshold. Measurements on these beads are not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_airy_z_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad airy fit quality in the z axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_airy_y_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad airy fit quality in the y axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_airy_x_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad airy fit quality in the x axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_gaussian_z_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad gaussian fit quality in the z axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_gaussian_y_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad gaussian fit quality in the y axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    considered_bad_fit_gaussian_x_count: Optional[int] = Field(default=None, description="""Number of beads considered as having a bad gaussian fit quality in the x axis. The fitting measurements are  not averaged into the key measurements. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_integrated_mean: Optional[float] = Field(default=None, description="""Mean integrated intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_integrated_median: Optional[float] = Field(default=None, description="""Median integrated intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_integrated_std: Optional[float] = Field(default=None, description="""Standard deviation of the integrated intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_max_mean: Optional[float] = Field(default=None, description="""Mean maximum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_max_median: Optional[float] = Field(default=None, description="""Median maximum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_max_std: Optional[float] = Field(default=None, description="""Standard deviation of the maximum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_min_mean: Optional[float] = Field(default=None, description="""Mean minimum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_min_median: Optional[float] = Field(default=None, description="""Median minimum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_min_std: Optional[float] = Field(default=None, description="""Standard deviation of the minimum intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_std_mean: Optional[float] = Field(default=None, description="""Mean standard deviation of the intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_std_median: Optional[float] = Field(default=None, description="""Median standard deviation of the intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    intensity_std_std: Optional[float] = Field(default=None, description="""Standard deviation of the standard deviation of the intensity of the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_z_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the airy fit in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_z_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the airy fit  in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_z_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the airy fit  in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_y_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the airy fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_y_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the airy fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_y_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the airy fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_x_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the airy fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_x_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the airy fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_airy_r2_x_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the airy fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_z_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the gaussian fit  in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_z_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the gaussian fit  in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_z_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the gaussian fit  in the z axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_y_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the gaussian fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_y_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the gaussian fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_y_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the gaussian fit  in the y axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_x_mean: Optional[float] = Field(default=None, description="""Mean coefficient of determination (R^2) for the gaussian fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_x_median: Optional[float] = Field(default=None, description="""Median coefficient of determination (R^2) for the gaussian fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fit_gaussian_r2_x_std: Optional[float] = Field(default=None, description="""Standard deviation of the coefficient of determination (R^2) for the gaussian fit  in the x axis for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_z_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the Z axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_z_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the Z axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_z_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the Z axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_y_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the Y axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_y_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the Y axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_y_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the Y axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_x_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the X axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_x_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the X axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_pixel_x_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the X axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_z_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the Z axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_z_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the Z axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_z_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the Z axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_y_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the Y axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_y_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the Y axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_y_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the Y axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_x_mean: Optional[float] = Field(default=None, description="""Mean FWHM for the analyzed beads in the X axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_x_median: Optional[float] = Field(default=None, description="""Median FWHM for the analyzed beads in the X axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_micron_x_std: Optional[float] = Field(default=None, description="""Standard deviation of the FWHM for the analyzed beads in the X axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_lateral_asymmetry_ratio_mean: Optional[float] = Field(default=None, description="""Mean lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_lateral_asymmetry_ratio_median: Optional[float] = Field(default=None, description="""Median lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    fwhm_lateral_asymmetry_ratio_std: Optional[float] = Field(default=None, description="""Standard deviation of the lateral FWHM asymmetry ratio for the analyzed beads. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_airy_r2_z: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the airy fit in the Z axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_airy_r2_y: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the airy fit in the Y axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_airy_r2_x: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the airy fit in the X axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_gaussian_r2_z: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the gaussian fit in the Z axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_gaussian_r2_y: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the gaussian fit in the Y axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fit_gaussian_r2_x: Optional[float] = Field(default=None, description="""Coefficient of determination (R^2) for the gaussian fit in the X axis of the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_pixel_z: Optional[float] = Field(default=None, description="""FWHM for the average bead in the Z axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_pixel_y: Optional[float] = Field(default=None, description="""FWHM for the average bead in the Y axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_pixel_x: Optional[float] = Field(default=None, description="""FWHM for the average bead in the X axis in pixels. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_micron_z: Optional[float] = Field(default=None, description="""Average FWHM for the beads in the Z axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_micron_y: Optional[float] = Field(default=None, description="""FWHM for the average bead in the Y axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_micron_x: Optional[float] = Field(default=None, description="""FWHM for the average bead in the X axis in microns. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_fwhm_lateral_asymmetry_ratio: Optional[float] = Field(default=None, description="""Lateral FWHM asymmetry ratio for the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_intensity_integrated: Optional[float] = Field(default=None, description="""Integrated intensity for the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_intensity_max: Optional[float] = Field(default=None, description="""Maximum intensity for the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_intensity_min: Optional[float] = Field(default=None, description="""Minimum intensity for the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })
    average_bead_intensity_std: Optional[float] = Field(default=None, description="""Standard deviation of the intensity for the average bead. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PSFBeadsKeyMeasurement']} })


class LightSourcePowerDataset(MetricsDataset):
    """
    Power measurements dataset. A collection of power measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power',
         'slot_usage': {'input_data': {'name': 'input_data',
                                       'range': 'LightSourcePowerInputData'},
                        'input_parameters': {'name': 'input_parameters',
                                             'range': 'LightSourcePowerInputParameters'},
                        'output': {'name': 'output',
                                   'range': 'LightSourcePowerOutput'}}})

    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    input_data: LightSourcePowerInputData = Field(default=..., description="""The input data for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    output: Optional[LightSourcePowerOutput] = Field(default=None, description="""The output of the analysis""", json_schema_extra = { "linkml_meta": {'abstract': True, 'domain_of': ['MetricsDataset']} })
    microscope: Microscope = Field(default=..., description="""The microscope that was used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    experimenter: Optional[Experimenter] = Field(default=None, description="""The experimenter that performed the imaging experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    acquisition_protocol: Optional[Protocol] = Field(default=None, description="""The protocol used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    processed: bool = Field(default=False, description="""Has the dataset been processed by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset'], 'ifabsent': 'False'} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class LightSourcePowerInputData(MetricsInputData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power'})

    power_measurements: list[PowerMeasurement] = Field(default=..., description="""This is a collection of power measurements for different light sources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputData']} })


class LightSourcePowerInputParameters(MetricsInputParameters):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power'})

    linearity_required_measurements: Optional[int] = Field(default=10, description="""The minimum number of measurements required to calculate power linearity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'int(10)'} })
    short_term_stability_measurement_interval_seconds: Optional[float] = Field(default=1.0, description="""The measurement interval, in seconds, used to calculate short term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'float(1.0)'} })
    short_term_stability_required_measurements: Optional[int] = Field(default=300, description="""The minimum number of measurements required to calculate short term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'int(300)'} })
    short_term_stability_required_integration_time_seconds: Optional[float] = Field(default=0.1, description="""The minimum integration time, in seconds, required to calculate short term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'float(0.1)'} })
    long_term_stability_measurement_interval_seconds: Optional[float] = Field(default=30.0, description="""The measurement interval, in seconds, used to calculate long term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'float(30.0)'} })
    long_term_stability_required_measurements: Optional[int] = Field(default=240, description="""The minimum number of measurements required to calculate long term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'int(240)'} })
    long_term_stability_required_integration_time_seconds: Optional[float] = Field(default=1.0, description="""The minimum integration time, in seconds, required to calculate long term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerInputParameters'], 'ifabsent': 'float(1.0)'} })


class LightSourcePowerOutput(MetricsOutput):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power',
         'slot_usage': {'key_measurements': {'name': 'key_measurements',
                                             'range': 'LightSourcePowerKeyMeasurement'}}})

    key_measurements: list[LightSourcePowerKeyMeasurement] = Field(default=..., description="""A list of KeyMeasurement subclasses summarizing the most important measurements as a function of, for example, channels""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    comment: Optional[Comment] = Field(default=None, description="""A human readable comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_application: list[str] = Field(default=..., description="""The application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_version: list[str] = Field(default=..., description="""The version of the application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_entity: Optional[list[str]] = Field(default=None, description="""The entity that processed the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_datetime: datetime  = Field(default=..., description="""The datetime of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_log: Optional[str] = Field(default=None, description="""The log of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    warnings: Optional[list[str]] = Field(default=None, description="""The warnings of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    errors: Optional[list[str]] = Field(default=None, description="""The errors of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    validated: bool = Field(default=False, description="""Has the dataset been validated by a human""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput'], 'ifabsent': 'False'} })
    validation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the validation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })


class LightSourcePowerKeyMeasurement(KeyMeasurement):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power',
         'slot_usage': {'light_source': {'inlined': False, 'name': 'light_source'},
                        'power_meter': {'inlined': False, 'name': 'power_meter'}}})

    light_source: Optional[LightSource] = Field(default=None, description="""The light source under investigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    power_meter: Optional[PowerMeter] = Field(default=None, description="""The power meter used to measure the power.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    measuring_location: Optional[MeasuringLocationEnum] = Field(default=None, description="""The location at which the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    nr_of_measurements: Optional[int] = Field(default=None, description="""The number of power measurements taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_mean_mw: Optional[float] = Field(default=None, description="""The mean power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_median_mw: Optional[float] = Field(default=None, description="""The median power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_std_mw: Optional[float] = Field(default=None, description="""The standard deviation of the power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_min_mw: Optional[float] = Field(default=None, description="""The minimum power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_max_mw: Optional[float] = Field(default=None, description="""The maximum power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_start_datetime: Optional[datetime ] = Field(default=None, title="Linearity start datetime", description="""The datetime of the first measurement used to calculate power linearity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_end_datetime: Optional[datetime ] = Field(default=None, title="Linearity end datetime", description="""The datetime of the last measurement used to calculate power linearity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_slope: Optional[float] = Field(default=None, title="Linearity slope", description="""The slope of the linear regression model that fits output power as a function of the set point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_intercept: Optional[float] = Field(default=None, title="Linearity intercept", description="""The intercept of the linear regression model that fits output power as a function of the set point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_coefficient_of_determination: Optional[float] = Field(default=None, title="Linearity coefficient of determination", description="""The coefficient of determination a linear regression model fits output power as a function of the set point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_p_value: Optional[float] = Field(default=None, title="Linearity p-value", description="""The p-value of the linear regression model that fits output power as a function of the set point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    power_linearity_std_err: Optional[float] = Field(default=None, title="Linearity standard error", description="""The standard error of the linear regression model that fits output power as a function of the set point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    short_term_power_stability_start_datetime: Optional[datetime ] = Field(default=None, title="Short term stability start datetime", description="""The datetime of the first measurement used to calculate short term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    short_term_power_stability_end_datetime: Optional[datetime ] = Field(default=None, title="Short term stability end datetime", description="""The datetime of the last measurement used to calculate short term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    short_term_power_stability: Optional[float] = Field(default=None, title="Short term stability", description="""The short term stability of the light source""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    long_term_power_stability_start_datetime: Optional[datetime ] = Field(default=None, title="Long term stability start datetime", description="""The datetime of the first measurement used to calculate long term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    long_term_power_stability_end_datetime: Optional[datetime ] = Field(default=None, title="Long term stability end datetime", description="""The datetime of the last measurement used to calculate long term power stability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })
    long_term_power_stability: Optional[float] = Field(default=None, title="Long term stability", description="""The long term stability of the light source""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement']} })


class PowerMeasurement(ConfiguredBaseModel):
    """
    A single power measurement for a light source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power'})

    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    light_source: Optional[LightSource] = Field(default=None, description="""The light source under investigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    power_meter: Optional[PowerMeter] = Field(default=None, description="""The power meter used to measure the power.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    measuring_location: Optional[MeasuringLocationEnum] = Field(default=None, description="""The location at which the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSourcePowerKeyMeasurement', 'PowerMeasurement']} })
    power_set_point: Optional[float] = Field(default=None, description="""The power set point as a fraction of the nominal power of the light source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowerMeasurement']} })
    power_mw: Optional[float] = Field(default=None, description="""The power measured in milliwatts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowerMeasurement']} })
    integration_time_seconds: Optional[float] = Field(default=None, description="""The integration time in seconds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowerMeasurement']} })


class LightSource(NamedObject):
    """
    A light source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    wavelength_nm: Optional[float] = Field(default=None, description="""The wavelength of the light source in nanometers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LightSource']} })
    name: str = Field(default=..., description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class PowerMeter(NamedObject):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    manufacturer: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    model: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'PowerMeter']} })
    name: str = Field(default=..., description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class UserExperiment(Sample):
    """
    A non-standardized microscope sample produced during regular operation of a research project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/user_sample'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class UserExperimentDataset(HasInputParametersMixin, HasSampleMixin, MetricsDataset):
    """
    A dataset of non-standardized microscope samples produced during regular operation of a research project.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/user_experiment',
         'mixins': ['HasSampleMixin', 'HasInputParametersMixin'],
         'slot_usage': {'input_data': {'name': 'input_data',
                                       'range': 'UserExperimentInputData'},
                        'input_parameters': {'name': 'input_parameters',
                                             'range': 'UserExperimentInputParameters'},
                        'output': {'name': 'output', 'range': 'UserExperimentOutput'},
                        'sample': {'name': 'sample', 'range': 'UserExperiment'}}})

    sample: Optional[UserExperiment] = Field(default=None, description="""The physical sample that was imaged""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasSampleMixin']} })
    input_parameters: Optional[UserExperimentInputParameters] = Field(default=None, description="""The input parameters for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasInputParametersMixin']} })
    acquisition_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the acquisition""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset', 'Image', 'PowerMeasurement']} })
    input_data: UserExperimentInputData = Field(default=..., description="""The input data for the analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    output: Optional[UserExperimentOutput] = Field(default=None, description="""The output of the analysis""", json_schema_extra = { "linkml_meta": {'abstract': True, 'domain_of': ['MetricsDataset']} })
    microscope: Microscope = Field(default=..., description="""The microscope that was used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    experimenter: Optional[Experimenter] = Field(default=None, description="""The experimenter that performed the imaging experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    acquisition_protocol: Optional[Protocol] = Field(default=None, description="""The protocol used to acquire the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset']} })
    processed: bool = Field(default=False, description="""Has the dataset been processed by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsDataset'], 'ifabsent': 'False'} })
    data_reference: Optional[DataReference] = Field(default=None, description="""A reference to the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    linked_references: Optional[list[DataReference]] = Field(default=None, description="""A list of linked references""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsObject']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


class UserExperimentInputData(MetricsInputData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/user_experiment'})

    user_experiment_images: list[Image] = Field(default=..., description="""The user_experiment images provided in the order TZYXC. More than one image can be provided if the image conditions are the same.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentInputData']} })
    orthogonal_rois: Optional[list[Roi]] = Field(default=None, description="""Rois containing a point shape where the orthogonal views are to be taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentInputData']} })
    profile_rois: Optional[list[Roi]] = Field(default=None, description="""Rois containing a line shape where a intensity profile is to be calculated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentInputData']} })


class UserExperimentInputParameters(MetricsInputParameters):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/user_experiment'})

    bit_depth: Optional[int] = Field(default=None, description="""Detector bit depth""", ge=1, le=64, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters']} })
    saturation_threshold: Optional[float] = Field(default=0.01, description="""Tolerated saturation threshold. If the amount of saturated pixels is above this threshold, the image is considered as saturated and the analysis is not performed.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationInputParameters',
                       'PSFBeadsInputParameters',
                       'UserExperimentInputParameters'],
         'ifabsent': 'float(0.01)'} })


class UserExperimentOutput(MetricsOutput):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/user_experiment',
         'slot_usage': {'intensity_profiles': {'description': 'Intensity profiles '
                                                              'along the profile_rois '
                                                              'provided as input.',
                                               'name': 'intensity_profiles'},
                        'key_measurements': {'name': 'key_measurements',
                                             'range': 'UserExperimentKeyMeasurement'}}})

    intensity_profiles: Optional[list[Table]] = Field(default=None, description="""Intensity profiles along the profile_rois provided as input.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationOutput', 'UserExperimentOutput']} })
    orthogonal_images: Optional[list[OrthogonalImage]] = Field(default=None, description="""Orthogonal images created from the provided orthogonal_rois.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentOutput']} })
    fft_images: Optional[list[Image]] = Field(default=None, description="""Fourier space transforms of the input images.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentOutput']} })
    key_measurements: list[UserExperimentKeyMeasurement] = Field(default=..., description="""A list of KeyMeasurement subclasses summarizing the most important measurements as a function of, for example, channels""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    comment: Optional[Comment] = Field(default=None, description="""A human readable comment""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_application: list[str] = Field(default=..., description="""The application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_version: list[str] = Field(default=..., description="""The version of the application used to process the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_entity: Optional[list[str]] = Field(default=None, description="""The entity that processed the dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_datetime: datetime  = Field(default=..., description="""The datetime of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    processing_log: Optional[str] = Field(default=None, description="""The log of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    warnings: Optional[list[str]] = Field(default=None, description="""The warnings of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    errors: Optional[list[str]] = Field(default=None, description="""The errors of the processing by microscope-metrics""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })
    validated: bool = Field(default=False, description="""Has the dataset been validated by a human""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput'], 'ifabsent': 'False'} })
    validation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime of the validation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricsOutput']} })


class UserExperimentKeyMeasurement(KeyMeasurement):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/user_experiment'})

    channel_name: Optional[str] = Field(default=None, description="""The channel name to which the measurements apply""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    channel_nr: Optional[int] = Field(default=None, description="""The channel number to which the measurements apply""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['FieldIlluminationKeyMeasurement',
                       'PSFBeadsKeyMeasurement',
                       'UserExperimentKeyMeasurement']} })
    variation_coefficient: Optional[float] = Field(default=None, description="""The variation coefficient of the signal of the image. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentKeyMeasurement']} })
    saturated_channels: Optional[int] = Field(default=None, description="""The channels that are saturated in the image. One value per channel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UserExperimentKeyMeasurement']} })


class LightSourcePower(Sample):
    """
    A sample providing measurements on light source power.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/light_source_power'})

    preparation_protocol: Protocol = Field(default=..., description="""The protocol used to prepare a sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    preparation_datetime: Optional[datetime ] = Field(default=None, description="""The datetime when the sample was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    manufacturer: Optional[str] = Field(default=None, description="""A manufacturer""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microscope', 'Sample', 'PowerMeter']} })
    name: Optional[str] = Field(default=None, description="""The human readable name of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })
    description: Optional[str] = Field(default=None, description="""A human readable description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedObject']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedObject.model_rebuild()
DataReference.model_rebuild()
MetricsObject.model_rebuild()
MicroscopeCollection.model_rebuild()
Microscope.model_rebuild()
Sample.model_rebuild()
Protocol.model_rebuild()
Experimenter.model_rebuild()
Comment.model_rebuild()
MetricsDatasetCollection.model_rebuild()
HarmonizedMetricsDatasetCollection.model_rebuild()
MetricsDataset.model_rebuild()
HasSampleMixin.model_rebuild()
HasInputParametersMixin.model_rebuild()
MetricsInputData.model_rebuild()
MetricsInputParameters.model_rebuild()
MetricsOutput.model_rebuild()
Image.model_rebuild()
ImageMask.model_rebuild()
OrthogonalImage.model_rebuild()
ChannelSeries.model_rebuild()
Channel.model_rebuild()
TimeSeries.model_rebuild()
Column.model_rebuild()
Roi.model_rebuild()
Shape.model_rebuild()
Point.model_rebuild()
Line.model_rebuild()
Rectangle.model_rebuild()
Ellipse.model_rebuild()
Polygon.model_rebuild()
Vertex.model_rebuild()
Mask.model_rebuild()
Color.model_rebuild()
CentersOfMass.model_rebuild()
CentersGeometric.model_rebuild()
CentersFitted.model_rebuild()
CentersMaxIntensity.model_rebuild()
ProfilesIntensity.model_rebuild()
RoiMeasurements.model_rebuild()
KeyMeasurement.model_rebuild()
Table.model_rebuild()
HomogeneousField.model_rebuild()
FluorescentHomogeneousThickField.model_rebuild()
FluorescentHomogeneousThinField.model_rebuild()
FieldIlluminationDataset.model_rebuild()
FieldIlluminationInputData.model_rebuild()
FieldIlluminationInputParameters.model_rebuild()
FieldIlluminationOutput.model_rebuild()
FieldIlluminationKeyMeasurement.model_rebuild()
FLuorescentBeads.model_rebuild()
MultiWavelengthBeads.model_rebuild()
PSFBeads.model_rebuild()
NonPSFBeads.model_rebuild()
PSFBeadsDataset.model_rebuild()
PSFBeadsInputData.model_rebuild()
PSFBeadsInputParameters.model_rebuild()
PSFBeadsOutput.model_rebuild()
PSFBeadsKeyMeasurement.model_rebuild()
LightSourcePowerDataset.model_rebuild()
LightSourcePowerInputData.model_rebuild()
LightSourcePowerInputParameters.model_rebuild()
LightSourcePowerOutput.model_rebuild()
LightSourcePowerKeyMeasurement.model_rebuild()
PowerMeasurement.model_rebuild()
LightSource.model_rebuild()
PowerMeter.model_rebuild()
UserExperiment.model_rebuild()
UserExperimentDataset.model_rebuild()
UserExperimentInputData.model_rebuild()
UserExperimentInputParameters.model_rebuild()
UserExperimentOutput.model_rebuild()
UserExperimentKeyMeasurement.model_rebuild()
LightSourcePower.model_rebuild()
