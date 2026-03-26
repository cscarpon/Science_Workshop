# Science Workshop: Reproducibility in Science

## Purpose of this Workshop

This repository serves as a template for Reproducible Science.

- Environment Control using conda or renv
- Package management with `roxygen2` and `docstring`
- Validation of packages using `pytest` or `testthat`
- Object oriented programming and class structures
- Simple `readme` styling

---

## Setup

Use this in powershell
`conda env create -f environment.yml`  

`conda activate research_env`  

Use this in R

```R
# Inside an R session:
install.packages("renv")
renv::restore()
```

---

## How to run R and Python Tests

In the terminal / powershell

```
pytest scripts/test_metrics.py -v
```

```
# Run from the terminal:
Rscript -e "library(testthat); test_file('scripts/test_metrics.R')"
```


---

## Running the class functions:

```Python
# For Python
from scripts.DataProcessor import DataProcessor
processor = DataProcessor(input_dir="data", output_dir="outputs")
processor.run()
```

```R
#For R
source("scripts/DataProcessor.R")
processor <- DataProcessor$new(input_dir = "data", output_dir = "outputs")
processor$run()
```

