import pytest
import geopandas as gpd
import os

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
    # Define the path relative to the root of your repo
    path = os.path.join("data", "mount_roads10m.geojson")
    
    # 1. Check if the file exists (Reproducibility Check)
    assert os.path.exists(path), f"Critical Error: {path} is missing from the repository!"
    
    # 2. Try loading the file
    gdf = gpd.read_file(path)
    
    # 3. Check for data corruption or empty files
    assert len(gdf) > 0, "The roads GeoJSON loaded but contains zero rows."
    
    # 4. Check for geometry type (Ensuring it's actually a network of lines)
    # Most roads should be LineString or MultiLineString
    geom_types = gdf.geometry.type.unique()
    assert 'LineString' in geom_types or 'MultiLineString' in geom_types, \
        f"Unexpected geometry types found: {geom_types}"

    # 5. Scientific Check: Is the CRS defined?
    assert gdf.crs is not None, "Spatial data is missing a Coordinate Reference System (CRS)."