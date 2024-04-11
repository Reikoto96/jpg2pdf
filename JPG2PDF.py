from fpdf import FPDF
from tqdm import tqdm
import os


def convert_images_to_pdf():
    # Get the source folder path from the user
    folder_path = input("Enter the path to the folder containing JPG files: ")

    # Get the destination PDF file name from the user
    output_file = input("Enter the name of the output PDF file: ")

    pdf = FPDF()

    # Get the list of JPG files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

    # Sort the files numerically based on the filename
    image_files.sort(key=lambda x: int(x.split(".")[0]))

    # Add each image to the PDF
    for image_file in tqdm(image_files, desc="Converting images to PDF", unit="image"):
        image_path = os.path.join(folder_path, image_file)
        pdf.add_page()
        pdf.image(image_path, 0, 0, pdf.w, pdf.h)

    # Save the PDF file
    pdf.output(output_file, "F")
    print("PDF file created successfully!")


# Convert the images to PDF
convert_images_to_pdf()
