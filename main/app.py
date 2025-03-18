from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image, UnidentifiedImageError
from rembg import remove
import io
import base64
import logging
import numpy as np

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def home():

    processed_image_data = None
    original_filename = ""
    is_valid = False

    if request.method == "POST":
        file = request.files["image_file"]
        is_valid  = is_valid_image(file)

        if not is_valid:
            print("image not valid")
            return

        original_filename = file.filename.split('.')[0]
        print(original_filename)
        with Image.open(file) as input_image:
            input_array = np.array(input_image)

            output_array = remove(input_array)
            output_image = Image.fromarray(output_array)
            output_image = output_image.convert("RGBA")

            img_byte_arr = io.BytesIO()
            output_image.save(img_byte_arr, format="PNG") 
            img_byte_arr.seek(0)

            processed_image_data = base64.b64encode(img_byte_arr.read()).decode('utf-8')

    return render_template(
        "index.html",
        processed_image_data=processed_image_data,
        original_filename=original_filename
        )


def is_valid_image(image):

    try:
        with Image.open(image) as img:
            img.verify()
        return True

    except UnidentifiedImageError as e:
        logging.debug(f"Cannot identify: {e}")
        return False
    
    except ValueError as e:
        logging.debug(f"Invalid operation: {e}")
        return False
    
    except Exception as e:
        logging.warning(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    app.run(debug=True)