from table_data_extractor import pdf_to_table_extract
def main():
    
    pdf_path="/Users/ainiton/Downloads/deep_edge_review.pdf"
    result=pdf_to_table_extract(pdf_path, page_number=9  , auto_rotation=True)
    print("Result: " , result)
if __name__ == "__main__":
    main()