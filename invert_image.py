from PIL import Image
import sys
import os

def invert_image(input_path, output_path=None):
    """
    Invert an image (make white black and vice versa)
    
    Args:
        input_path (str): Path to the input image
        output_path (str, optional): Path to save the inverted image. If not provided,
                                   will append '_inverted' to the input filename
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert image to RGB if it's not
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Invert the image
            inverted_img = Image.eval(img, lambda x: 255 - x)
            
            # Generate output path if not provided
            if output_path is None:
                filename, ext = os.path.splitext(input_path)
                output_path = f"{filename}_inverted{ext}"
            
            # Save the inverted image with maximum quality
            if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
                inverted_img.save(output_path, 'JPEG', quality=100)
            else:
                inverted_img.save(output_path)
                
            print(f"Inverted image saved to: {output_path}")
            
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python invert_image.py <input_image_path> [output_image_path]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    invert_image(input_path, output_path) 
