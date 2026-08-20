import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def test_render(bg_path, output_path, ar_align_mode="center_over_text"):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    font_ar = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.0245))
    font_id = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0195))
    font_src = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.020))
    
    ar_lines = [
        "صلى الله عليه وسلم و يأتى على الناس زمان يكون هلاك",
        "الرجل على يد زوجته وأبويه وولده يعيرونه بالفقر ويكلفونه ما",
        "لا يطيق ، فيدخل المداخل التي يذهب فيها دينه فيهلك (۳) ،",
        "وفي الخبر ( قلة العيال"
    ]
    
    indo_raw = 'Akan datang suatu masa, dimana kerusakan (karena penuh tekanan, yang bisa saja hingga berujung kematian) seorang laki-laki berada di tangan istrinya, kedua orang tuanya, dan anaknya. Mereka mencelanya dengan kemiskinan dan memaksanya bekerja di luar kemampuannya. Akhirnya (karena tertekan)ia masuki banyak pekerjaan /melakukan pekerjaan apa saja (yang bahkan) dapat menghilangkan agamanya. (Karena tenaga terforsir dan penuh tekanan) maka ia akan rusak (secara mental/ secara agama/ bahkan secara jasad {mati})."'
    
    id_lines = textwrap.wrap(indo_raw, width=44)
    src_raw = "-Ihya' Ulumudin, juz 2, bab nikah"
    
    left_x = int(w * 0.07)
    start_y = int(h * 0.44)
    
    ar_line_h = int(h * 0.034)
    id_line_h = int(h * 0.0265)
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    # Calculate width of indonesian block
    max_id_w = max(text_draw.textbbox((0, 0), line, font=font_id)[2] for line in id_lines)
    id_right_x = left_x + max_id_w
    
    cur_y = start_y
    for line in ar_lines:
        if ar_align_mode == "align_with_indo_right":
            # Right aligned with the right boundary of Indonesian text
            rx = id_right_x + int(w * 0.08)
            shadow_draw.text((rx, cur_y), line, font=font_ar, fill=(0, 0, 0, 255), direction='rtl', language='ara', anchor='ra')
            text_draw.text((rx, cur_y), line, font=font_ar, fill=(255, 255, 255, 255), direction='rtl', language='ara', anchor='ra')
        elif ar_align_mode == "left_anchor":
            # Placed starting from left_x
            shadow_draw.text((left_x, cur_y), line, font=font_ar, fill=(0, 0, 0, 255), direction='rtl', language='ara', anchor='la')
            text_draw.text((left_x, cur_y), line, font=font_ar, fill=(255, 255, 255, 255), direction='rtl', language='ara', anchor='la')
        elif ar_align_mode == "shifted_left":
            # Shifted to left: right anchor at w * 0.80 instead of 0.93
            rx = int(w * 0.78)
            shadow_draw.text((rx, cur_y), line, font=font_ar, fill=(0, 0, 0, 255), direction='rtl', language='ara', anchor='ra')
            text_draw.text((rx, cur_y), line, font=font_ar, fill=(255, 255, 255, 255), direction='rtl', language='ara', anchor='ra')
        cur_y += ar_line_h
        
    cur_y += int(h * 0.015)
    
    for line in id_lines:
        shadow_draw.text((left_x, cur_y), line, font=font_id, fill=(0, 0, 0, 255))
        text_draw.text((left_x, cur_y), line, font=font_id, fill=(255, 255, 255, 255))
        cur_y += id_line_h
        
    cur_y += int(h * 0.016)
    
    shadow_draw.text((left_x, cur_y), src_raw, font=font_src, fill=(0, 0, 0, 255))
    text_draw.text((left_x, cur_y), src_raw, font=font_src, fill=(240, 240, 240, 255))
    
    shadow_blur_1 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=5))
    shadow_blur_2 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2))
    
    bg = Image.alpha_composite(bg, shadow_blur_1)
    bg = Image.alpha_composite(bg, shadow_blur_1)
    bg = Image.alpha_composite(bg, shadow_blur_2)
    bg = Image.alpha_composite(bg, shadow_blur_2)
    bg = Image.alpha_composite(bg, text_layer)
    
    result = bg.convert("RGB")
    result.save(output_path, quality=98)
    print(f"Rendered: {output_path}")

test_render('/home/user/concept_shrouded_figure.jpg', '/home/user/test_left_anchor.jpg', 'left_anchor')
test_render('/home/user/concept_shrouded_figure.jpg', '/home/user/test_shifted_left.jpg', 'shifted_left')
test_render('/home/user/concept_shrouded_figure.jpg', '/home/user/test_align_right_indo.jpg', 'align_with_indo_right')
