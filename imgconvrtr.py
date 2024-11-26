from PIL import Image
import io
def convert_img_format(image_file, frmat):
    # Open the image file
    with Image.open(image_file) as img:
        output_img = io.BytesIO()
        img.save(output_img, format=frmat.upper())
        output_img.seek(0)
        return output_img