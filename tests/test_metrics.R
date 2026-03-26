library(testthat)
library(sf)
library(here)

test_that("addition works correctly", {
  result <- 2 + 3
  expect_equal(result, 5)
})

test_that("mount_roads10m.geojson is present and geographically valid", {
  
  # 1. Check if the file exists (Reproducibility Check)
  # R uses relative paths from the project root/working directory
  path <- here("data", "mount_roads10m.geojson")
  expect_true(file.exists(path), info = paste("Critical Error:", path, "is missing!"))
  
  # 2. Try loading the file
  # st_read is the 'sf' equivalent of gpd.read_file
  # quiet = TRUE prevents the metadata from cluttering your test output
  gdf <- st_read(path, quiet = TRUE)
  
  # 3. Check for data corruption or empty files
  expect_gt(nrow(gdf), 0)
  
  # 4. Check for geometry type
  # st_geometry_type returns a factor; we convert to character to compare
  geom_types <- as.character(unique(st_geometry_type(gdf)))
  
  # Define what we are willing to accept (R types are usually UPPERCASE)
  allowed_types <- c("POLYGON", "MULTIPOLYGON", "LINESTRING", "MULTILINESTRING")
  
  # Check if there is any intersection between found types and allowed types
  expect_true(any(geom_types %in% allowed_types), 
              info = paste("Unexpected geometry types found:", paste(geom_types, collapse = ", ")))
  
  # 5. Scientific Check (Bonus): Ensure a Coordinate Reference System is present
  expect_false(is.na(st_crs(gdf)), info = "Spatial data is missing a CRS!")
})