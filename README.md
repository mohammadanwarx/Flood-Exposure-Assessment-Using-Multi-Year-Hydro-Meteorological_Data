# Flood Exposure Geospatial Pipeline

A simplified geospatial analysis pipeline for assessing flood exposure using raster and vector data.

## Features

- **Data I/O**: Load and save raster (GeoTIFF) and vector (Shapefile, GeoJSON) data
- **Preprocessing**: Reprojection, masking, and clipping operations
- **Zonal Statistics**: Calculate exposure metrics within administrative boundaries
- **Visualization**: Generate maps and plots for results

## Project Structure

```
flood-exposure-geospatial-pipeline/
├── data/
│   └── raw/           # Input raster and vector data
├── src/               # Source code (4 simple modules)
│   ├── data_io.py         # Load/save raster and vector data
│   ├── preprocessing.py   # Reproject, mask, clip operations
│   ├── analysis.py        # Zonal statistics and exposure metrics
│   └── visualization.py   # Maps and plots
├── notebooks/         # Jupyter notebooks for analysis
└── outputs/          # All analysis outputs (figures, results)
```

## Installation

### Using pip

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.data_io import load_raster, load_vector
from src.analysis import compute_zonal_statistics
from src.visualization import plot_zonal_statistics

# Load flood depth raster
flood_data, metadata = load_raster("data/raw/raster/flood_depth.tif")

# Load administrative boundaries
admin_boundaries = load_vector("data/raw/vector/boundaries.shp")

# Calculate exposure metrics
results = compute_zonal_statistics(
    "data/raw/raster/flood_depth.tif",
    admin_boundaries,
    stats=['mean', 'max', 'sum']
)

# Visualize results
plot_zonal_statistics(results, 'mean', title='Mean Flood Depth by Region')
```

## Usage

See the `notebooks/` directory for detailed examples and tutorials.

## License

MIT License
