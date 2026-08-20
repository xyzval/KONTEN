import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def render_arabic_lines(draw, lines, font_ar, right_x, start_y, line_height, fill=(255, 255, 255, 255)):
    cur_y = start_y
    for line in lines:
        draw.text((right_x, cur_y), line, font=font_ar, fill=fill, direction='rtl', language='ara', anchor='ra')
        cur_y += line_height
    return cur_y

def render_latin_lines(draw, lines, font_lat, left_x, start_y, line_height, fill=(250, 250, 250, 255)):
    cur_y = start_y
    for line in lines:
        draw.text((left_x, cur_y), line, font=font_lat, fill=fill)
        cur_y += line_height
    return cur_y

def create_slide_1(bg_path, output_path, question_text="apa penyebab laki-laki\nberumur pendek ??"):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.024))
    
    lines = question_text.split("\n")
    box_w = int(w * 0.58)
    box_h = int(h * 0.10)
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.49)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Semi-transparent dark pill box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 190))
    
    # Quote mark at top-left
    draw.text((box_x0 + int(w * 0.035), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Question text centered
    line_h = int(h * 0.030)
    start_y = box_y0 + (box_h - len(lines) * line_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    result = Image.alpha_composite(bg, overlay).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Slide 1 generated: {output_path}")

def create_slide_2(bg_path, output_path):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.042))
    font_ar = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.024))
    font_id = ImageFont.truetype("/home/user/fonts/Roboto-Regular.ttf", int(h * 0.019))
    font_src = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.020))
    
    ar_lines = [
        "صلى الله عليه وسلم و يأتى على الناس زمان يكون هلاك",
        "الرجل على يد زوجته وأبويه وولده يعيرونه بالفقر ويكلفونه ما",
        "لا يطيق ، فيدخل المداخل التي يذهب فيها دينه فيهلك (۳) ،",
        "وفي الخبر ( قلة العيال"
    ]
    
    indo_raw = 'Akan datang suatu masa, dimana kerusakan (karena penuh tekanan, yang bisa saja hingga berujung kematian) seorang laki-laki berada di tangan istrinya, kedua orang tuanya, dan anaknya. Mereka mencelanya dengan kemiskinan dan memaksanya bekerja di luar kemampuannya. Akhirnya (karena tertekan)ia masuki banyak pekerjaan /melakukan pekerjaan apa saja (yang bahkan) dapat menghilangkan agamanya. (Karena tenaga terforsir dan penuh tekanan) maka ia akan rusak (secara mental/ secara agama/ bahkan secara jasad {mati})."'
    
    id_lines = textwrap.wrap(indo_raw, width=44)
    src_raw = "-Ihya' Ulumudin, juz 2, bab nikah"
    
    box_w = int(w * 0.88)
    pad_x = int(w * 0.045)
    pad_y = int(h * 0.022)
    
    ar_line_h = int(h * 0.034)
    id_line_h = int(h * 0.027)
    
    total_content_h = (len(ar_lines) * ar_line_h) + int(h * 0.015) + (len(id_lines) * id_line_h) + int(h * 0.025) + int(h * 0.03)
    box_h = total_content_h + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.40)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Draw rounded dark box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=16, fill=(0, 0, 0, 190))
    
    # Quote mark at top-left
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Render Arabic lines (right aligned)
    right_x = box_x1 - pad_x
    start_ar_y = box_y0 + pad_y + int(h * 0.005)
    cur_y = render_arabic_lines(draw, ar_lines, font_ar, right_x, start_ar_y, ar_line_h)
    
    cur_y += int(h * 0.012)
    
    # Render Indonesian lines (left aligned)
    left_x = box_x0 + pad_x
    cur_y = render_latin_lines(draw, id_lines, font_id, left_x, cur_y, id_line_h)
    
    cur_y += int(h * 0.015)
    
    # Render source citation
    draw.text((left_x, cur_y), src_raw, font=font_src, fill=(225, 225, 225, 255))
    
    result = Image.alpha_composite(bg, overlay).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Slide 2 generated: {output_path}")

if __name__ == '__main__':
    # Concept 1: Shrouded Figure (Sosok Bayangan Bertudung Hitam / Malakul Maut Allegory)
    create_slide_1('/home/user/concept_shrouded_figure.jpg', '/home/user/slide1_konsep_tudung_bayangan.jpg')
    create_slide_2('/home/user/concept_shrouded_figure.jpg', '/home/user/slide2_konsep_tudung_bayangan.jpg')
    
    # Concept 2: Exhausted Alone (Kelelahan & Keputusasaan Sendiri / Solo Exhaustion)
    create_slide_1('/home/user/concept_exhausted_portrait.jpg', '/home/user/slide1_konsep_kelelahan_sendiri.jpg')
    create_slide_2('/home/user/concept_exhausted_portrait.jpg', '/home/user/slide2_konsep_kelelahan_sendiri.jpg')
