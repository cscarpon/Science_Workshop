library(R6)
library(fs) # The 'pathlib' of R

#' @title DataProcessor Class
#' @description A class to batch process CSV files by converting content to uppercase.
#'
#' @field input_dir Path. The directory containing raw CSV files.
#' @field output_dir Path. The directory where processed files will be saved.
#' @export
DataProcessor <- R6Class("DataProcessor",
  public = list(
  input_dir = NULL,
  output_dir = NULL,

#' @description 
#' The Constructor: Initializes paths and creates the output folder.
#' @param input_dir Character or Path. Directory containing raw data.
#' @param output_dir Character or Path. Directory for processed results.
  initialize = function(input_dir, output_dir) {
    # Use fs::path() for cross-platform safety (like Path())
    self$input_dir <- path(input_dir)
    self$output_dir <- path(output_dir)
    
    # Action: Create the folder if it doesn't exist
    dir_create(self$output_dir)
  },

  #' @description
  #' Logic for a single file: reads a CSV and converts content to uppercase.
  #' @param file_path Character or Path. The specific file to process.
  #' @return A data frame with all character columns converted to uppercase.
  process_file = function(file_path) {
    data <- read.csv(file_path)
    # Note: toupper() on a whole dataframe converts it to a character vector.
    # For a workshop, this logic is usually applied to specific columns.
    return(toupper(data)) 
  },

  #' @description
  #' The main 'Engine': Orchestrates the batch processing across the input directory.
  #' @return None. Writes files to the output directory and prints messages.
  run = function() {
    # dir_ls with a glob pattern finds the files
    files <- dir_ls(self$input_dir, glob = "*.csv")
    
    for (f in files) {
      result <- self$process_file(f)
      
      # path_file/path_ext_remove are like .name and .stem in pathlib
      file_stem <- path_ext_remove(path_file(f))
      out_path <- path(self$output_dir, paste0(file_stem, "_processed.csv"))
      
      write.csv(result, out_path, row.names = FALSE)
      message(paste("Done:", path_file(f), "->", path_file(out_path)))
    }
  })
)


### --- How to use it --- ###

### The input directories
data_dir <- path("data")
out_dir  <- path("outputs")

processor <- DataProcessor$new(input_dir = data_dir, output_dir = out_dir)
processor$run()

## Diagnostic tools for the processor class
str(processor)
ls(processor)

# Viewing the input variables that have been selected.
processor$input_dir
