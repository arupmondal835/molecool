"""
molecool
a python package for analysing anf visualizing pdb and xyz file.
"""

# Add imports here
from .functions import *
#import molecool.functions

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

