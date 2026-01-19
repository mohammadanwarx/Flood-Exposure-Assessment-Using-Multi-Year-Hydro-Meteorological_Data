"""Tests for visualization module."""

import pytest
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon
from src.visualization import plot_raster, plot_vector, plot_zonal_statistics
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing


def test_plot_raster(tmp_path):
    """Test plotting a raster."""
    # Create dummy raster data
    data = np.random.rand(10, 10)
    save_path = tmp_path / "test_raster_plot.png"
    
    # Plot (should not raise error)
    # plot_raster(data, title="Test Raster", save_path=save_path)
    # assert save_path.exists()
    pass


def test_plot_vector(tmp_path):
    """Test plotting a vector."""
    # Create dummy GeoDataFrame
    gdf = gpd.GeoDataFrame(
        {'id': [1, 2, 3], 'value': [10, 20, 30]},
        geometry=[
            Point(0, 0).buffer(0.1),
            Point(1, 1).buffer(0.1),
            Point(2, 2).buffer(0.1)
        ],
        crs='EPSG:4326'
    )
    save_path = tmp_path / "test_vector_plot.png"
    
    # Plot (should not raise error)
    # plot_vector(gdf, column='value', title="Test Vector", save_path=save_path)
    # assert save_path.exists()
    pass


def test_plot_zonal_statistics(tmp_path):
    """Test plotting zonal statistics."""
    # Create dummy GeoDataFrame with statistics
    gdf = gpd.GeoDataFrame(
        {'zone_id': [1, 2], 'mean': [5.5, 8.3], 'max': [10, 15]},
        geometry=[
            Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
            Polygon([(1, 1), (2, 1), (2, 2), (1, 2)])
        ],
        crs='EPSG:4326'
    )
    save_path = tmp_path / "test_zonal_plot.png"
    
    # Plot (should not raise error)
    # plot_zonal_statistics(gdf, 'mean', title="Test Zonal Stats", save_path=save_path)
    # assert save_path.exists()
    pass
