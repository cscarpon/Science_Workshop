from pathlib import Path
import os

class DataProcessor:
    """
    A tool to batch process CSV files by converting content to uppercase.

    This class provides a structured way to handle directory-level file 
    transformations, ensuring that the output folder is prepared and
    files are handled using modern Pathlib logic.

    Attributes:
        input_dir (Path): Source directory containing the raw .csv files.
        output_dir (Path): Target directory where processed results are saved.
    """

    def __init__(self, input_dir, output_dir):
        """
        Initializes the DataProcessor with input and output paths.

        Args:
            input_dir (str or Path): The directory containing files to process.
            output_dir (str or Path): The directory where output files will be written.
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        
        # Action: Create the folder if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_file(self, file_path):
        """
        Reads a single file and converts its text content to uppercase.

        Args:
            file_path (Path): The Path object representing the file to be read.

        Returns:
            str: The entire content of the file converted to uppercase strings.
        """
        # .read_text() is a modern 'pathlib' way to open and read in one go
        data = file_path.read_text()
        return data.upper()

    def run(self):
        """
        Orchestrates the batch processing of all CSV files in the input directory.

        This method identifies all files ending in .csv, applies the transformation 
        logic via process_file(), and writes the new content to the output directory 
        with a '_processed' suffix.

        Returns:
            None
        """
        # .glob("*.csv") finds all matching files in the folder
        for path in self.input_dir.glob("*.csv"):
            result = self.process_file(path)
            
            # Use / operator (pathlib magic) to join paths safely
            # .stem gets the filename without the .csv extension
            out_path = self.output_dir / f"{path.stem}_processed.csv"
            
            out_path.write_text(result)
            print(f"Done: {path.name} -> {out_path.name}")
            
            
#### Running the processor 

data_dir = os.path.join("..", "data")
out_dir = os.path.join("..", "outputs")

if __name__ == "__main__":
    # Example usage
    processor = DataProcessor(input_dir="data", output_dir="outputs")
    processor.run()