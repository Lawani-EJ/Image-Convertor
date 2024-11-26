import streamlit as st 
from imgconvrtr import convert_img_format
from PIL import Image

# setting up the webpage structure 
st.set_page_config(page_title="Image Convrtr 😗👌")
st.title("Image Convertor")
st.write("Convert all your images in one click")

# File uploader 
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["png", "jpg", "jpeg", "jfif", "bmp"]
)

if uploaded_file is not None:
    # this is going to show the uploaded image 
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploade image", use_column_width=True)

    # show the original image format 
    st.write(f"Original format : {img.format}")

    # Output format selection 
    format_options = ["PNG","JPEG","JFIF","BMP"]
    output_format = st.selectbox("Choose the output format", format_options)

    # convert the image 
    if img.format != output_format:
        if st.button("Convert 📸"):
            converted_img = convert_img_format(uploaded_file, output_format.lower())
            st.write(f"Image converted to {output_format}")

            # the download button 
            st.download_button(
                label=f"Download as {output_format}",
                data = converted_img,
                file_name=f"image.{output_format.lower()}",
                mime = f"image/{output_format.lower()}"
            )
        else:
            st.write("Please click the convert button to download the converted image")