# Table Data Extractor

Table Data Extractor is a Python package designed for extracting tables from images and PDFs using OCR (Optical Character Recognition). It supports automatic rotation detection, image preprocessing, and conversion of extracted tables into pandas DataFrames.

## Features

- Extract tables from images and PDFs.
- Automatically detect and correct image orientation.
- Enhance OCR results with preprocessing techniques (grayscale conversion, contrast enhancement, thresholding).
- Convert extracted tables into pandas DataFrames for easy data manipulation and analysis.

## Installation

You can install Table Data Extractor via pip:

```bash

pip install table_data_extractor

```

## Usage

### Image Table Extraction

``` python
from table_data_extractor import image_to_table_extract

# Example: Extract tables from an image
extracted_tables_image = image_to_table_extract("path_to_your_image.jpg", auto_rotation=True)
print(extracted_tables_image)

```


### PDF Table Extraction

```python
from table_data_extractor import pdf_to_table_extract

# Example: Extract tables from a PDF
extracted_tables_pdf = pdf_to_table_extract("path_to_your_pdf.pdf", page_number=1, auto_rotation=True)
print(extracted_tables_pdf)

```