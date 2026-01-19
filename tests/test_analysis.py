"""Tests for analysis module."""

import pytest
import numpy as np
import pandas as pd
import geopandas as gpd
from src.analysis import compute_zonal_statistics, calculate_exposure_index, calculate_risk_categories


def test_compute_zonal_statistics():
    """Test computing zonal statistics."""
    # This is a placeholder - requires actual test data
    # raster_path = "tests/data/test_raster.tif"
    # zones = gpd.read_file("tests/data/test_zones.shp")
    # result = compute_zonal_statistics(raster_path, zones, stats=['mean', 'max'])
    # assert isinstance(result, gpd.GeoDataFrame)
    # assert 'mean' in result.columns
    # assert 'max' in result.columns
    pass


def test_calculate_exposure_index():
    """Test calculating exposure index."""
    # Create dummy data
    flood_depth = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    population = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], dtype=float)
    
    # Calculate exposure index
    exposure = calculate_exposure_index(flood_depth, population)
    
    assert isinstance(exposure, np.ndarray)
    assert exposure.shape == flood_depth.shape
    assert np.all(exposure >= 0) and np.all(exposure <= 1)


def test_calculate_exposure_index_with_weights():
    """Test calculating exposure index with custom weights."""
    flood_depth = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    population = np.array([[10, 20, 30], [40, 50, 60]], dtype=float)
    weights = {'depth': 0.7, 'population': 0.3}
    
    exposure = calculate_exposure_index(flood_depth, population, weights)
    
    assert isinstance(exposure, np.ndarray)
    assert exposure.shape == flood_depth.shape


def test_calculate_risk_categories():
    """Test categorizing exposure values into risk levels."""
    exposure_values = np.array([0.1, 0.4, 0.7, 0.9])
    
    categories = calculate_risk_categories(exposure_values)
    
    assert isinstance(categories, np.ndarray)
    assert len(categories) == len(exposure_values)
    assert set(categories) <= {'low', 'medium', 'high'}
    assert categories[0] == 'low'
    assert categories[-1] == 'high'


def test_calculate_risk_categories_custom_thresholds():
    """Test risk categories with custom thresholds."""
    exposure_values = np.array([0.2, 0.5, 0.8])
    thresholds = {'low': 0.4, 'medium': 0.7, 'high': 1.0}
    
    categories = calculate_risk_categories(exposure_values, thresholds)
    
    assert categories[0] == 'low'
    assert categories[1] == 'medium'
    assert categories[2] == 'high'
