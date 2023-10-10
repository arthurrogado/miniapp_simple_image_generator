from PIL import ImageFont, ImageDraw, Image

def make_telegram_lover_card(text, user_image = None, basecard = "basecard.png"):

    image = Image.open("App/Core/draw_card/basecard.png")
    image_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("App/Utils/arial.ttf", 18)


    left, top, right, bottom = font.getbbox(text)
    print(left, top, right, bottom)
    # this values are the size of the text relative to the top left corner of the image
    # left = 220: distance from left to start writing
    # top = 170: distance from top to start writing
    # right = 280: distance from left to end writing
    # bottom = 450: distance from top to end writing

    width = right - left
    height = bottom - top
    print("Width:", width, "Height:", height)

    # top left to start writing: 220, 170
    # top right to end writing: 280, 450

    y_start = 140

    # wrap text to be between 220 and 450
    # split text by spaces (with split), and make a loop adding the words until it reaches the limit between 220 and 450 (450 - 220)
    # if it gets bigger, remove the last word, increase y and continue from the initial x (220)
    # if it gets smaller, keep adding words until you reach the limit between 220 and 450 (450 - 220)

    words = text.split(" ")
    x_start = 220
    x_end = 420
    limit = x_end - x_start

    space_length = image_draw.textlength(" ", font=font)

    row_lenght = 0
    words_in_row = []
    for word in words:
        word_lenght = image_draw.textlength(word, font=font) # retorna o tamanho da word

        if row_lenght + word_lenght + space_length < limit:
            row_lenght += word_lenght + space_length
            words_in_row.append(word)

        else:
            # write the row
            image_draw.text( (x_start, y_start), " ".join(words_in_row), font=font, fill=(0, 0, 0))
            # reset row
            row_lenght = 0
            words_in_row = []
            y_start += height
            # add word to row
            row_lenght += word_lenght
            words_in_row.append(word)

    # write the last row
    image_draw.text( (x_start, y_start), " ".join(words_in_row), font=font, fill=(0, 0, 0))

    # write company name
    company_name = "Company: Durov's Heart"
    company_font = ImageFont.truetype("App/Utils/arial.ttf", 12)
    c_left, c_top, c_right, c_bottom = company_font.getbbox(company_name)
    company_width = c_right - c_left
    company_height = c_bottom - c_top

    company_x = x_start
    company_y = y_start + company_height + height
    image_draw.text( (company_x, company_y), company_name, font=company_font, fill=(0, 0, 0))

    # mask
    mask = Image.open("App/Core/draw_card/round_mask.png").resize((160,160)).convert("L")

    if not user_image:
        # null_user_image
        image_to_paste = Image.open("App/Core/draw_card/null_user_image.jpg").resize(mask.size)
    else:
        image_to_paste = user_image.resize(mask.size)

    image.paste(image_to_paste, (50, 128), mask=mask)

    return image

if __name__ == "__main__":
    image = make_telegram_lover_card("Arthur Rogado")
    image.show()