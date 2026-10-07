from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input, output, r):
    """
    Rotate a specific page of a PDF file.

    Args:
        input (str): The PDF file to be rotated.
        output (str): The output file name after rotation.
        r (int): The specific page to get rotated (enter as 1-index based).

    Returns:
        str: Message for successful output.
    """
    reader = PdfReader(input)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i == r - 1:
            page.rotate(180)
        writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)

    return("Rotation successful")
