from PIL import Image

def apply_mosaic_filter(image, block_size=100):
    """
    Apply a mosaic filter to the given image.

    Parameters:
    - image (PIL.Image.Image): The input image.
    - block_size (int): The size of the mosaic blocks.

    Returns:
    - PIL.Image.Image: The mosaic image.
    """
    width, height = image.size

    # Create a new image with the same mode and size as the input image
    # 입력받은 이미지와 동일한 모드와 크기로 새로운 이미지 객체 생성
    filtered_image = Image.new(image.mode, image.size)

    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            # Crop a block from the original image
            # 원본 이미지에서 블록을 잘라냄
            box = (x, y, x + block_size, y + block_size)
            block = image.crop(box)
            
            # Calculate the average color of the block
            # 블록의 평균 색상을 계산함
            average_color = (
                sum(p[0] for p in block.getdata()) // block_size**2,
                sum(p[1] for p in block.getdata()) // block_size**2,
                sum(p[2] for p in block.getdata()) // block_size**2
            )

            # Create a new image with the average color and paste it onto the filtered image
            # 평균 색상으로 새 이미지를 생성하여 필터링된 이미지에 붙여넣음
            filtered_block = Image.new(image.mode, block.size, average_color)
            filtered_image.paste(filtered_block, box)

    # return to created image
    # 만들어진 이미지로 반환
    return filtered_image