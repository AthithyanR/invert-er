# Image Inverter

A simple Python script to invert images (make white black and vice versa).

## Setup

1. Make sure you have Python installed on your system
2. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Unix/MacOS
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with an input image path:

```bash
python invert_image.py <input_image_path> [output_image_path]
```

- `input_image_path`: Path to the image you want to invert (required)
- `output_image_path`: Path where you want to save the inverted image (optional)
  - If not provided, the inverted image will be saved with '_inverted' appended to the original filename

## Example

```bash
python invert_image.py input.jpg output.jpg
```

This will create an inverted version of `input.jpg` and save it as `output.jpg`. 