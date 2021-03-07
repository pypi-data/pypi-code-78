import setuptools
from pyapacheatlas import __version__

LONG_DESCRIPTION = """
# PyApacheAtlas: API Support for Azure Purview and Apache Atlas

A python package to work with the Apache Atlas API and support bulk loading, custom lineage, and more from a Pythonic set of classes and Excel templates. 

The package currently supports:
* Bulk upload of entities.
* Bulk upload of type definitions.
* Creating custom lineage between two existing entities.
* Creating custom table and complex column level lineage in the [Hive Bridge style](https://atlas.apache.org/0.8.3/Bridge-Hive.html).
  * Supports Azure Purview ColumnMapping Attributes.
* Creating a column lineage scaffolding as in the Hive Bridge Style .
* Performing "What-If" analysis to check if...
   * Your entities are valid types.
   * Your entities are missing required attributes.
   * Your entities are using undefined attributes.
* Working with the glossary.
  * Uploading terms.
  * Downloading individual or all terms.
* Working with classifications.
  * Classify one entity with multiple classifications.
  * Classify multiple entities with a single classification.
  * Remove classification ("declassify") from an entity.
* Working with relationships.
  * Able to create arbitrary relationships between entities.
  * e.g. associating a given column with a table.
  * Able to upload relationship definitions.
* Deleting types (by name) or entities (by guid).
* Search (only for Azure Purview advanced search).
* Authentication to Azure Purview via Service Principal.
* Authentication using basic authentication of username and password for open source Atlas.
"""

def setup_package():
    setuptools.setup(
        name="pyapacheatlas",
        version=__version__,
        author="Will Johnson",
        author_email="will@willj.com",
        description="A package to simplify working with the Apache Atlas REST APIs for Atlas and Azure Purview.",
        long_description_content_type="text/markdown",
        url="https://github.com/wjohnson/pyapacheatlas",
        packages=setuptools.find_packages(),
        install_requires=[
            'openpyxl>=3.0',
            'requests>=2.0'
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
        long_description=LONG_DESCRIPTION
    )

if __name__ == "__main__":
    setup_package()