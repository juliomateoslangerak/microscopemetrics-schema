# microscopemetrics-schema

A schema for microscope-metrics, a python package for microscope QC

## Adding a new metrics dataset type

### Step 1: Add a new yaml file to the `analyses` directory
Probably the easiest way to do this is to copy an existing file and modify it. The file should contain the
following:

```yaml
id: https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/analyses/light_source_power
name: microscopemetrics_analyses_light_source_power
prefixes:
  linkml: https://w3id.org/linkml/
imports:
  - linkml:types
  - core_schema  # TODO: change to metrics:core_schema
  - samples/light_source_power

default_range: string


classes:
  YourClassName:
    xxx

slots:
  YourSlotName:
    xxx
```

### Step 2: If necessary, add a new yaml file to the `samples` directory

Similar to the above, but for the samples directory.

``` yaml
id: https://MontpellierRessourcesImagerie.github.io/microscopemetrics-schema/samples/homogeneous_field
name: microscopemetrics_samples_homogeneous_field
prefixes:
  linkml: https://w3id.org/linkml/
imports:
  - linkml:types
  - core_schema  # TODO: change to metrics:core_schema

default_range: string


classes:
  YourClassName:
    xxx

slots:
  YourSlotName:
    xxx
```

### Step 3: Add the new file imports to the microscopemetrics-schema.yaml file

This will ensure that the new files are included in the schema.

### Step 4: Generate the schema

```bash
make all
```

### Step 5: Add strategies to the `strategies` directory

You will have to create a series of hypothesis strategies to generate
instances of your new classes. These should be added to the `strategies' __init__.py file.
However, we will probably move this to separate files in the future.

### Step 6: Add tests to the `tests_strategies` module

These tests are going to test the strategies you have created.

### Step 7: Add tests to the `tests_data` module

If you have example datasets, you can add them here as well as adding the sample to the 
'src/data/examples' directory. There is a directory for invalid datasets as well. Place there
datasets that should not pass validation.