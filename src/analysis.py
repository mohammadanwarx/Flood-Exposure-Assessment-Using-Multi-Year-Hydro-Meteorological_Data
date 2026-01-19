"""
Simplified flood exposure analysis for mini project.
Combines zonal statistics, exposure metrics, and basic analysis.
"""

import numpy as np
import pandas as pd
import geopandas as gpd
from rasterstats import zonal_stats
from typing import Union, List, Dict, Optional
from pathlib import Path


def compute_zonal_statistics(
    raster_path: Union[str, Path],
    zones_gdf: gpd.GeoDataFrame,
    stats: List[str] = ['min', 'max', 'mean', 'median', 'std', 'sum', 'count']
) -> gpd.GeoDataFrame:
    """
    Calculate zonal statistics for raster data within vector zones.
    
    Parameters
    ----------
    raster_path : str or Path
        Path to raster file
    zones_gdf : gpd.GeoDataFrame
        GeoDataFrame with zone polygons
    stats : list
        Statistics to calculate
        
    Returns
    -------
    gpd.GeoDataFrame
        Input GeoDataFrame with statistics columns added
    """
    zs = zonal_stats(
        zones_gdf,
        str(raster_path),
        stats=stats,
        geojson_out=False
    )
    
    stats_df = pd.DataFrame(zs)
    result = zones_gdf.copy()
    result = pd.concat([result, stats_df], axis=1)
    
    return result


def calculate_exposure_index(
    flood_depth: np.ndarray,
    population_density: np.ndarray,
    weights: Dict[str, float] = None
) -> np.ndarray:
    """
    Calculate a composite flood exposure index.
    
    Parameters
    ----------
    flood_depth : np.ndarray
        Flood depth raster
    population_density : np.ndarray
        Population density raster
    weights : dict, optional
        Weights for each component (default: equal weights)
        
    Returns
    -------
    np.ndarray
        Exposure index raster
    """
    if weights is None:
        weights = {'depth': 0.5, 'population': 0.5}
    
    # Normalize inputs to 0-1 range
    depth_norm = (flood_depth - np.nanmin(flood_depth)) / (np.nanmax(flood_depth) - np.nanmin(flood_depth))
    pop_norm = (population_density - np.nanmin(population_density)) / (np.nanmax(population_density) - np.nanmin(population_density))
    
    # Calculate weighted index
    exposure_index = (
        weights['depth'] * depth_norm +
        weights['population'] * pop_norm
    )
    
    return exposure_index


def calculate_risk_categories(
    exposure_values: np.ndarray,
    thresholds: Dict[str, float] = None
) -> np.ndarray:
    """
    Categorize exposure values into risk levels.
    
    Parameters
    ----------
    exposure_values : np.ndarray
        Exposure values
    thresholds : dict, optional
        Risk category thresholds
        
    Returns
    -------
    np.ndarray
        Risk category labels
    """
    if thresholds is None:
        thresholds = {'low': 0.33, 'medium': 0.66, 'high': 1.0}
    
    categories = np.full(exposure_values.shape, 'low', dtype=object)
    categories[exposure_values > thresholds['low']] = 'medium'
    categories[exposure_values > thresholds['medium']] = 'high'
    
    return categories
