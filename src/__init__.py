"""
Flood Exposure Geospatial Pipeline
===================================

A simplified pipeline for flood exposure analysis using geospatial data.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import main modules for easier access
from src import data_io
from src import preprocessing
from src import analysis
from src import visualization

__all__ = [
    "data_io",
    "preprocessing",
    "analysis",
    "visualization",
]
