"""Tests for preprocessing module."""

import pytest
import numpy as np
import geopandas as gpd
from pathlib import Path
from src.preprocessing import reproject_raster, mask_raster_by_geometry, reproject_vector


def test_reproject_raster(tmp_path):
    """Test reprojecting a raster to a new CRS."""
    # This is a placeholder - requires actual test data
    # src_path = "tests/data/test_raster.tif"
    # dst_path = tmp_path / "reprojected.tif"
    # reproject_raster(src_path, dst_path, 'EPSG:3857')
    # assert dst_path.exists()
    pass


def test_mask_raster_by_geometry():
    """Test masking a raster by vector geometries."""
    # This is a placeholder - requires actual test data
    # raster_path = "tests/data/test_raster.tif"
    # geometries = gpd.read_file("tests/data/test_vector.shp")
    # masked_data, metadata = mask_raster_by_geometry(raster_path, geometries)
    # assert isinstance(masked_data, np.ndarray)
    # assert masked_data.shape[1] <= original_height
    # assert masked_data.shape[2] <= original_width
    pass


def test_reproject_vector():
    """Test reprojecting a GeoDataFrame to a new CRS."""
    # Create dummy GeoDataFrame
    from shapely.geometry import Point
    gdf = gpd.GeoDataFrame(
        {'id': [1, 2]},
        geometry=[Point(0, 0), Point(1, 1)],
        crs='EPSG:4326'
    )
    
    # Reproject to Web Mercator
    reprojected = reproject_vector(gdf, 'EPSG:3857')
    
    assert reprojected.crs.to_string() == 'EPSG:3857'
    assert len(reprojected) == len(gdf)
