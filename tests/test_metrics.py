import pytest
import geopandas as gpd
import os
from pathlib import Path

# Create a test file (must start with test_)
# File: test_metrics.py

def test_positive_values():
    values = [1, 2, 3]
    assert all(v > 0 for v in values)

# Example of validating scientific assumptions
def test_no_negative_heights():
    heights = [10.2, 5.4, 3.1]
    assert min(heights) >= 0


def test_load_roads_geojson():
    """Validates that the mountain roads data is present and geographically valid."""
    
    # 1. Get the path of THIS test file (root/scripts/test_file.py)
    this_file = Path(__file__).resolve()
    
    # 2. Go up one level to the root, then into the data folder
    root_dir = this_file.parent.parent
    path = root_dir / "data" / "mount_roads10m.geojson"

    # 3. Check if the file exists
    assert path.exists(), f"Critical Error: {path} is missing!"
    
    # 2. Try loading the file
    gdf = gpd.read_file(path)
    
    # 3. Check for data corruption or empty files
    assert len(gdf) > 0, "The roads GeoJSON loaded but contains zero rows."
    
    # 4. Check for geometry type
    geom_types = gdf.geometry.type.unique()
    
    # Define what we are willing to accept for this workshop
    allowed_types = ['Polygon', 'MultiPolygon', 'LineString', 'MultiLineString']
    
    # Check if the actual types in the file overlap with our allowed list
    assert any(t in allowed_types for t in geom_types), \
        f"Unexpected geometry types found: {geom_types}"