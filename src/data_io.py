"""
Simplified data loading functions for raster and vector data.
"""

import rasterio
import geopandas as gpd
from pathlib import Path
from typing import Union, Tuple
import numpy as np


def load_raster(filepath: Union[str, Path]) -> Tuple[np.ndarray, dict]:
    """
    Read a raster file and return data array and metadata.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the raster file (GeoTIFF, etc.)
        
    Returns
    -------
    data : np.ndarray
        Raster data array (bands, height, width)
    metadata : dict
        Raster metadata (transform, CRS, bounds, etc.)
    """
    with rasterio.open(filepath) as src:
        data = src.read()
        metadata = {
            'transform': src.transform,
            'crs': src.crs,
            'bounds': src.bounds,
            'width': src.width,
            'height': src.height,
            'count': src.count,
            'dtype': src.dtypes[0],
            'nodata': src.nodata,
        }
    
    return data, metadata


def load_vector(filepath: Union[str, Path]) -> gpd.GeoDataFrame:
    """
    Read a vector file into a GeoDataFrame.
    
    Parameters
    ----------
    filepath : str or Path
        Path to vector file (Shapefile, GeoJSON, GeoPackage, etc.)
        
    Returns
    -------
    gpd.GeoDataFrame
        Vector data
    """
    return gpd.read_file(filepath)


def save_raster(
    filepath: Union[str, Path],
    data: np.ndarray,
    metadata: dict
) -> None:
    """
    Save raster data to file.
    
    Parameters
    ----------
    filepath : str or Path
        Output file path
    data : np.ndarray
        Raster data array
    metadata : dict
        Raster metadata
    """
    with rasterio.open(
        filepath,
        'w',
        driver='GTiff',
        height=data.shape[-2],
        width=data.shape[-1],
        count=data.shape[0] if data.ndim == 3 else 1,
        dtype=data.dtype,
        crs=metadata['crs'],
        transform=metadata['transform'],
        nodata=metadata.get('nodata')
    ) as dst:
        if data.ndim == 2:
            dst.write(data, 1)
        else:
            dst.write(data)


def save_vector(
    filepath: Union[str, Path],
    gdf: gpd.GeoDataFrame
) -> None:
    """
    Save GeoDataFrame to file.
    
    Parameters
    ----------
    filepath : str or Path
        Output file path
    gdf : gpd.GeoDataFrame
        Vector data to save
    """
    gdf.to_file(filepath)
