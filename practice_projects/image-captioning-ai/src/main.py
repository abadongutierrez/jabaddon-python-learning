"""
Main script to demonstrate the image captioning functionality.
"""

import os
import sys
from image_captioning_ai import caption_image_file 


def main():
    """
    Main function to run image captioning.
    """
    # Default image path
    default_image = "imgs/image-01.jpg"
    
    # Check if an image path was provided as command line argument
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = default_image
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        print(f"Please make sure the image exists or provide a valid path.")
        return
    
    print(f"Generating caption for image: {image_path}")
    print("Loading model and processing image...")
    
    try:
        # Generate caption using the function from our module
        caption = caption_image_file(image_path)
        
        print("\n" + "="*50)
        print("GENERATED CAPTION:")
        print("="*50)
        print(f"{caption}")
        print("="*50)
        
    except Exception as e:
        print(f"Error generating caption: {e}")
        return


if __name__ == "__main__":
    main()