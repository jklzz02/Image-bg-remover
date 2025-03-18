
# Flask Image Background Remover

This project is a simple Flask web application that allows users to upload an image, process it by removing its background using the `rembg` library, and then download the processed image.

## Features

- **Image Upload**: Upload an image in SVG, PNG, JPG, or GIF formats.
- **Background Removal**: The app uses the `rembg` library to remove the background from the uploaded image.
- **Image Display**: Once the background is removed, the processed image is displayed.
- **Image Download**: Users can download the processed image in PNG format.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Pillow
- `rembg`
- `numpy`

To install the required dependencies, you can run the following command:

```bash
pip install Flask Pillow rembg numpy
```

## Project Structure

The project is structured with two main components:

1. **Flask Application** (`app.py`): 
   - The backend code for handling the image processing logic.
   - Users upload an image via a form, and the backend processes it using the `rembg` library.
   - After processing, the app generates a base64-encoded version of the processed image and sends it to the frontend for display.

2. **HTML Template** (`templates/index.html`): 
   - The frontend of the app, where users can upload their image.
   - After the image is processed, the HTML page displays the processed image and provides a download link.
   - The page uses TailwindCSS for styling.

## How It Works

1. **User Upload**: The user uploads an image via the form on the homepage. The image file is sent to the Flask backend.
2. **Background Removal**: In the backend, the `rembg` library removes the background from the uploaded image. The image is then saved as a PNG.
3. **Base64 Encoding**: The processed image is converted to a base64 string, which allows it to be embedded directly into the HTML for immediate display.
4. **Image Display**: The frontend receives the base64-encoded image and displays it on the page. A download link is also provided for the user to save the processed image.

## Running the Application

To run the application locally, follow these steps:

1. Clone the repository or download the project files.
2. Install the required dependencies by running:

   ```bash
   pip install Flask Pillow rembg numpy
   ```

3. Start the Flask development server:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to [http://localhost:5000](http://localhost:5000).
5. Upload an image and the app will process it by removing the background. Once processed, you can view and download the image.