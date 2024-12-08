import os
import subprocess
from typing import List


class PdfToImages:
    """
    A utility class for converting PDF files into images using pdftoppm.
    """

    def __init__(self, pdf_path: str, output_dir: str):
        self.pdf_path = pdf_path
        self.output_dir = output_dir

    def convert(self) -> List[str]:
        """
        Convert the PDF into images and return a list of generated image paths.

        Returns:
            List[str]: A list of paths to the generated images.

        Raises:
            FileNotFoundError: If the PDF file does not exist.
            RuntimeError: If the pdftoppm command fails.
        """
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Run the pdftoppm command
        command = [
            "pdftoppm",
            "-png",
            self.pdf_path,
            os.path.join(self.output_dir, "page")
        ]
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if process.returncode != 0:
            raise RuntimeError(f"Failed to convert PDF to images: {process.stderr.decode()}")

        # Return the generated image paths
        return [
            os.path.join(self.output_dir, file)
            for file in os.listdir(self.output_dir)
            if file.endswith(".png")
        ]
