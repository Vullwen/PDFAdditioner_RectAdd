import os
import PyPDF2

# Set the directory containing the PDF files
inputDirectory = 'C://Users//cpinquier//Documents//taf//input'
# Set the directory where the output PDF files will be saved
outputDirectory = 'C://Users//cpinquier//Documents//taf//output'
# Set the filename of the PDF to add
additionalPdf = open('C://Users//cpinquier//Documents//taf//CARENE-FLYER-HD.pdf', 'rb')
additionalPdfReader = PyPDF2.PdfFileReader(additionalPdf)

# Get a list of all of the PDF filenames in the input directory
pdfFilenames = [f for f in os.listdir(inputDirectory) if f.endswith('.pdf')]
act = len(pdfFilenames)

# Iterate over the PDF filenames
for filename in pdfFilenames:
    # Construct the full path to the input PDF file
    inputFilepath = os.path.join(inputDirectory, filename)
    
    # Open the input PDF file
    with open(inputFilepath, 'rb') as f:
        # Create a PDF reader object
        pdfReader = PyPDF2.PdfFileReader(f)
        # Create a new PDF object
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # Add the first page of the current PDF to the output PDF
        pdfWriter.addPage(pdfReader.getPage(0))
        # Add the first page of the additional PDF to the output PDF
        pdfWriter.addPage(additionalPdfReader.getPage(0))

        # Construct the full path to the output PDF file
        outputFilepath = os.path.join(outputDirectory, filename)
        
        # Save the output PDF to a file with the same name as the input file
        with open(outputFilepath, 'wb') as out:
            pdfWriter.write(out)
    
    # Print the progress
    print('Progress: {}/{} - {}%'.format(pdfFilenames.index(filename) + 1, act, round((pdfFilenames.index(filename) + 1)/act*100, 2)))

# Close the additional PDF file
additionalPdf.close()
print('Done!') 