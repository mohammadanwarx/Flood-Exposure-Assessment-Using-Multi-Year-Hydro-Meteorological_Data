"""
Simple preprocessing functions for raster and vector data.
"""

import numpy as np
import geopandas as gpd
import rasterio
from rasterio.mask import mask
from rasterio.warp import calculate_default_transform, reproject, Resampling
from typing import Union, Tuple
from pathlib import Path


def reproject_raster(
    src_path: Union[str, Path],
    dst_path: Union[str, Path],
    dst_crs: str
) -> None:
    """
    Reproject a raster to a new CRS.
    
    Parameters
    ----------
    src_path : str or Path
        Source raster file
    dst_path : str or Path
        Output raster file
    dst_crs : str
        Target CRS (e.g., 'EPSG:4326')
    """
    with rasterio.open(src_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds
        )
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': dst_crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        with rasterio.open(dst_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=dst_crs,
                    resampling=Resampling.nearest
                )


def mask_raster_by_geometry(
    raster_path: Union[str, Path],
    geometries: gpd.GeoDataFrame,
    output_path: Union[str, Path] = None
) -> Tuple[np.ndarray, dict]:
    """
    Mask/clip a raster by vector geometries.
    
    Parameters
    ----------
    raster_path : str or Path
        Input raster file
    geometries : gpd.GeoDataFrame
        Geometries to mask by
    output_path : str or Path, optional
        Output file path (if None, returns arrays only)
        
    Returns
    -------
    masked_data : np.ndarray
        Masked raster data
    metadata : dict
        Updated metadata
    """
    with rasterio.open(raster_path) as src:
        # Ensure same CRS
        if geometries.crs != src.crs:
            geometries = geometries.to_crs(src.crs)
        
        # Mask raster
        masked_data, masked_transform = mask(
            src, geometries.geometry, crop=True, nodata=src.nodata
        )
        
        metadata = src.meta.copy()
        metadata.update({
            'height': masked_data.shape[1],
            'width': masked_data.shape[2],
            'transform': masked_transform
        })
        
        if output_path:
            with rasterio.open(output_path, 'w', **metadata) as dst:
                dst.write(masked_data)
    
    return masked_data, metadata


def reproject_vector(
    gdf: gpd.GeoDataFrame,
    target_crs: str
) -> gpd.GeoDataFrame:
    """
    Reproject a GeoDataFrame to a new CRS.
    
    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame
    target_crs : str
        Target CRS (e.g., 'EPSG:4326')
        
    Returns
    -------
    gpd.GeoDataFrame
        Reprojected GeoDataFrame
    """
    return gdf.to_crs(target_crs)
