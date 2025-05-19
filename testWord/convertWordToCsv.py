import docx
import csv
print("Conversion started ")
# Load the Word document
doc = docx.Document('Book1.docx')

# Open CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Loop through tables in the document
    
    for para in doc.paragraphs:
        print(" loop")
        text = para.text.strip()
        writer.writerow([text])

print("Conversion complete: 'output.csv' created.")