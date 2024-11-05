from pdf2docx import Converter

pdf_file = 'check.pdf'
docx_file = 'check.docx'  # Use the correct variable name

# Create a Converter object
cv = Converter(pdf_file)

# Convert the PDF to DOCX
cv.convert(docx_file)

# Close the Converter object
cv.close()
print("This is completed")
