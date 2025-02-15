from interfaces.converter import Converter
from io import BytesIO
from fpdf import FPDF

class ImageService(Converter):
    def to_pdf(self, image_file) -> BytesIO:
        pdf = FPDF()
        pdf.add_page()
        pdf.image(image_file, x=10, y=10, w=100)
        output = BytesIO()
        pdf.output(output)
        output.seek(0)
        return output