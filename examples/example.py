import os
from src.pdf_to_images import PdfToImages

if __name__ == "__main__":
    # Input PDF file
    pdf_path = os.path.join(os.path.dirname(__file__), "sample.pdf")

    # Output directory for images
    output_dir = os.path.join(os.path.dirname(__file__), "output")

    try:
        # Initialize PdfToImages
        converter = PdfToImages(pdf_path, output_dir)

        # Convert PDF to images
        images = converter.convert()

        print("Conversion successful! Generated images:")
        for img in images:
            print(img)
    except Exception as e:
        print(f"Error: {e}")
