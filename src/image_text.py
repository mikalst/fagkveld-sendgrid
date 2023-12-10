from PIL import Image, ImageDraw, ImageFont
 
# Image Configs
font_size = 36
text_color = "black"
line_spacing = 1.3 

def put_text_on_image(input_image_path: str, text_content, output_image_path, font_path):
    # Open an Image
    original_image = Image.open(input_image_path)
    image_width, image_height = original_image.size

    # Create a drawing object and font object
    draw = ImageDraw.Draw(original_image)
    font = ImageFont.truetype(font_path, font_size)

    # get max width of image
    max_width = int(image_width * 0.9)

    # create list of nice lengths of text to fit the image
    wrapped_text = wrap_text(text_content, max_width, font)

    y = (image_height - int(font_size * len(wrapped_text) * line_spacing)) // 2
    
    for line in wrapped_text:
        line_width = font.getlength(line)
        draw.text(
            ((image_width - line_width) // 2, y), 
            line, 
            text_color, 
            font=font, 
        )
        y += int(font_size * line_spacing)

    # Save the modified image
    original_image.save(output_image_path)

    return original_image


def wrap_text(text, max_width, font: ImageFont.FreeTypeFont):
    lines = []
    paragraphs = text.split('\n')
    for paragraph in paragraphs:
        words = paragraph.split(' ')
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            line_width = font.getlength(test_line)
            if line_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line[:-1])
                current_line = word + ' '
    
        lines.append(current_line[:-1])
    
    return lines