"""
Simple visualization functions for maps and plots.
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from typing import Optional, Union
from pathlib import Path


def plot_raster(
    data: np.ndarray,
    title: str = "Raster Data",
    cmap: str = "viridis",
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot a single-band raster.
    
    Parameters
    ----------
    data : np.ndarray
        2D raster array
    title : str
        Plot title
    cmap : str
        Colormap name
    save_path : str or Path, optional
        Path to save figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    if data.ndim == 3:
        data = data[0]
    
    im = ax.imshow(data, cmap=cmap)
    ax.set_title(title)
    plt.colorbar(im, ax=ax, label="Value")
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_vector(
    gdf: gpd.GeoDataFrame,
    column: Optional[str] = None,
    title: str = "Vector Data",
    cmap: str = "viridis",
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot a GeoDataFrame.
    
    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Vector data to plot
    column : str, optional
        Column to use for coloring
    title : str
        Plot title
    cmap : str
        Colormap name
    save_path : str or Path, optional
        Path to save figure
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    
    if column:
        gdf.plot(column=column, ax=ax, legend=True, cmap=cmap)
    else:
        gdf.plot(ax=ax, color='blue', edgecolor='black')
    
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_zonal_statistics(
    gdf: gpd.GeoDataFrame,
    stat_column: str,
    title: str = "Zonal Statistics",
    cmap: str = "YlOrRd",
    save_path: Optional[Union[str, Path]] = None
) -> None:
    """
    Plot zonal statistics results.
    
    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        GeoDataFrame with statistics
    stat_column : str
        Column containing statistics to plot
    title : str
        Plot title
    cmap : str
        Colormap name
    save_path : str or Path, optional
        Path to save figure
    """
    plot_vector(gdf, column=stat_column, title=title, cmap=cmap, save_path=save_path)
