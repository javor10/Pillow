from PIL import Image

def apply_mosaic_filter(image, block_size=10):
    """
    Apply a mosaic filter to the given image.

    Parameters:
    - image (PIL.Image.Image): The input image.
    - block_size (int): The size of the mosaic blocks.

    Returns:
    - PIL.Image.Image: The filtered image.
    """
    width, height = image.size

    # Create a new image with the same mode and size as the input image
    filtered_image = Image.new(image.mode, image.size)

    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            # Crop a block from the original image
            box = (x, y, x + block_size, y + block_size)
            block = image.crop(box)

            # Calculate the average color of the block
            average_color = (
                sum(p[0] for p in block.getdata()) // block_size**2,
                sum(p[1] for p in block.getdata()) // block_size**2,
                sum(p[2] for p in block.getdata()) // block_size**2
            )

            # Create a new image with the average color and paste it onto the filtered image
            filtered_block = Image.new(image.mode, block.size, average_color)
            filtered_image.paste(filtered_block, box)

    return filtered_image