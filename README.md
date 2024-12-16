# PDF to Images Conversion (Python)

A lightweight Python service for converting PDF files into images using `pdftoppm`. It generates one PNG image per page in the PDF.

---

## Features

- Converts PDF files to PNG images.
- Outputs one image per page in the PDF.
- Lightweight and easy to use.

## Requirements

- Python 3.7 or higher.
- `pdftoppm` installed on the system (part of `poppler-utils`).

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/marwan-ahmed-23/PDF-to-Images-Conversion-python.git
    ```

2. Install `pdftoppm` (if not already installed):

    ```
    sudo apt install poppler-utils
    ```

## Usage

### Example

Use the provided example script in the `examples/` directory:

```
from src.pdf_to_images import PdfToImages

pdf_path = "sample.pdf"
output_dir = "output"

converter = PdfToImages(pdf_path, output_dir)
images = converter.convert()

print(images)
```

Place a sample PDF in the `examples/` folder and run the script:

```
python examples/example.py
```

## Directory Structure

PDF-to-Images-Conversion-python/
├── examples/
│   └── example.py         # Example usage for PDF to images conversion
├── src/
│   └── pdf_to_images.py   # Core logic for PDF to images conversion
├── .gitignore             # Git ignore file
└── README.md              # Project documentation

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to report bugs or suggest features.

