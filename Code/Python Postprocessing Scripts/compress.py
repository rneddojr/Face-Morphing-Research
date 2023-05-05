import PIL
from PIL import Image

def compress_image_tokb(input_path, output_path, target_size):
    # Open the image
    im = Image.open(input_path)

    # Compress the image
    im.save(output_path, quality=85, optimize=True, progressive=True)

    # Check the size of the image
    image_size = im.size

    # If the image is larger than the target size, compress it further
    while image_size > target_size:
        # Reduce the quality of the image
        im.save(output_path, quality=quality-5, optimize=True, progressive=True)

        # Check the size of the image again
        image_size = im.size

    # Save the compressed image
    im.save(output_path)