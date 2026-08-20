import os
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def render_text_with_shadow(base_draw, shadow_draw, x, y, text, font, text_color=(255, 255, 255, 255), shadow_color=(0, 0, 0, 220), is_arabic=False, anchor=None):
    # Draw shadow first on shadow layer
    if is_arabic:
        shadow_draw.text((x, y), text, font=font, fill=shadow_color, direction='rtl', language='ara', anchor=anchor)
        base_draw.text((x, y), text, font=font, fill=text_color, direction='rtl', language='ara', anchor=anchor)
    else:
        shadow_draw.text((x, y), text, font=font, fill=shadow_color)
        base_draw.text((x, y), text, font=font, fill=text_color)

def create_slide_2_nobg(bg_path, output_path, with_subtle_shadow=True):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    # Shadow layer and text layer
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.045))
    font_ar = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.0245))
    font_id = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.0195))
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
    
    left_x = int(w * 0.08)
    right_x = int(w * 0.92)
    start_y = int(h * 0.42)
    
    ar_line_h = int(h * 0.034)
    id_line_h = int(h * 0.027)
    
    # Draw Quote icon
    render_text_with_shadow(text_draw, shadow_draw, left_x, start_y - int(h * 0.035), "“", font_quote)
    
    # Draw Arabic text lines
    cur_y = start_y
    for line in ar_lines:
        render_text_with_shadow(text_draw, shadow_draw, right_x, cur_y, line, font_ar, is_arabic=True, anchor='ra')
        cur_y += ar_line_h
        
    cur_y += int(h * 0.014)
    
    # Draw Indonesian translation lines
    for line in id_lines:
        render_text_with_shadow(text_draw, shadow_draw, left_x, cur_y, line, font_id)
        cur_y += id_line_h
        
    cur_y += int(h * 0.016)
    
    # Draw Source citation
    render_text_with_shadow(text_draw, shadow_draw, left_x, cur_y, src_raw, font_src)
    
    if with_subtle_shadow:
        # Blur shadow layer slightly for soft readable contrast on painting
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=3))
        # Draw shadow multiple times for deep clean contrast
        bg = Image.alpha_composite(bg, shadow_layer)
        bg = Image.alpha_composite(bg, shadow_layer)
    
    result = Image.alpha_composite(bg, text_layer).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Generated no-bg slide 2: {output_path}")

def create_slide_1_nobg(bg_path, output_path, question_text="apa penyebab laki-laki\nberumur pendek ??"):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.040))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.027))
    
    lines = question_text.split("\n")
    line_h = int(h * 0.035)
    start_y = int(h * 0.50)
    
    # Center lines
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        if i == 0:
            # Quote mark
            render_text_with_shadow(text_draw, shadow_draw, x - int(w * 0.05), y - int(h * 0.02), "“", font_quote)
        render_text_with_shadow(text_draw, shadow_draw, x, y, line, font_text)
        
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=4))
    bg = Image.alpha_composite(bg, shadow_layer)
    bg = Image.alpha_composite(bg, shadow_layer)
    result = Image.alpha_composite(bg, text_layer).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Generated no-bg slide 1: {output_path}")

create_slide_2_nobg('/home/user/concept_shrouded_figure.jpg', '/home/user/slide2_tudung_tanpa_background.jpg')
create_slide_1_nobg('/home/user/concept_shrouded_figure.jpg', '/home/user/slide1_tudung_tanpa_background.jpg')

# Also for concept 2 (Solo exhaustion)
create_slide_2_nobg('/home/user/concept_exhausted_portrait.jpg', '/home/user/slide2_kelelahan_tanpa_background.jpg')
create_slide_1_nobg('/home/user/concept_exhausted_portrait.jpg', '/home/user/slide1_kelelahan_tanpa_background.jpg')
