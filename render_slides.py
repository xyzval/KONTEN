import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

def wrap_arabic(text, max_chars_per_line=45):
    # Split text into words and wrap
    words = text.split()
    lines = []
    current_line = []
    current_len = 0
    for w in words:
        if current_len + len(w) + 1 <= max_chars_per_line:
            current_line.append(w)
            current_len += len(w) + 1
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [w]
            current_len = len(w)
    if current_line:
        lines.append(" ".join(current_line))
    
    reshaped_lines = []
    for line in lines:
        reshaped = arabic_reshaper.reshape(line)
        bidi = get_display(reshaped)
        reshaped_lines.append(bidi)
    return reshaped_lines

def wrap_indonesian(text, max_chars_per_line=50):
    lines = textwrap.wrap(text, width=max_chars_per_line)
    return lines

def create_slide_1(bg_path, output_path, question_text="apa penyebab laki-laki\nberumur pendek ??"):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Fonts
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.035))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.024))
    
    # Box dimensions
    lines = question_text.split("\n")
    box_w = int(w * 0.58)
    box_h = int(h * 0.11)
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.48)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Draw rounded dark box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=16, fill=(0, 0, 0, 175))
    
    # Quote mark at top left of box
    draw.text((box_x0 + int(w * 0.04), box_y0 - int(h * 0.025)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Draw question text centered
    line_h = int(h * 0.032)
    start_y = box_y0 + (box_h - len(lines) * line_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    result = Image.alpha_composite(bg, overlay).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Created Slide 1: {output_path}")

def create_slide_2(bg_path, output_path):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Fonts
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.04))
    font_ar = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.023))
    font_id = ImageFont.truetype("/home/user/fonts/Roboto-Regular.ttf", int(h * 0.020))
    font_src = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.021))
    
    arabic_raw = "صلى الله عليه وسلم و يأتى على الناس زمان يكون هلاك الرجل على يد زوجته وأبويه وولده يعيرونه بالفقر ويكلفونه ما لا يطيق ، فيدخل المداخل التي يذهب فيها دينه فيهلك (٣) ، وفي الخبر ( قلة العيال"
    
    indo_raw = 'Akan datang suatu masa, dimana kerusakan (karena penuh tekanan, yang bisa saja hingga berujung kematian) seorang laki-laki berada di tangan istrinya, kedua orang tuanya, dan anaknya. Mereka mencelanya dengan kemiskinan dan memaksanya bekerja di luar kemampuannya. Akhirnya (karena tertekan)ia masuki banyak pekerjaan /melakukan pekerjaan apa saja (yang bahkan) dapat menghilangkan agamanya. (Karena tenaga terforsir dan penuh tekanan) maka ia akan rusak (secara mental/ secara agama/ bahkan secara jasad {mati})."'
    
    src_raw = "-Ihya' Ulumudin, juz 2, bab nikah"
    
    ar_lines = wrap_arabic(arabic_raw, max_chars_per_line=48)
    id_lines = wrap_indonesian(indo_raw, max_chars_per_line=44)
    
    # Box dimensions
    box_w = int(w * 0.88)
    pad_x = int(w * 0.045)
    pad_y = int(h * 0.025)
    
    ar_line_h = int(h * 0.034)
    id_line_h = int(h * 0.028)
    
    content_h = (len(ar_lines) * ar_line_h) + int(h * 0.02) + (len(id_lines) * id_line_h) + int(h * 0.035) + int(h * 0.03)
    box_h = content_h + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.38)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Ensure box fits image
    if box_y1 > h - int(h * 0.03):
        box_y0 = h - box_h - int(h * 0.03)
        box_y1 = box_y0 + box_h
        
    # Draw rounded dark box with subtle transparency
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=20, fill=(0, 0, 0, 185))
    
    # Quote mark at top left
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.025)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Draw Arabic text (right-aligned or centered within box)
    cur_y = box_y0 + pad_y + int(h * 0.005)
    for line in ar_lines:
        bbox = draw.textbbox((0, 0), line, font=font_ar)
        txt_w = bbox[2] - bbox[0]
        # Align right
        x = box_x1 - pad_x - txt_w
        draw.text((x, cur_y), line, font=font_ar, fill=(255, 255, 255, 255))
        cur_y += ar_line_h
        
    cur_y += int(h * 0.015)
    
    # Draw Indonesian text (left-aligned)
    for line in id_lines:
        x = box_x0 + pad_x
        draw.text((x, cur_y), line, font=font_id, fill=(250, 250, 250, 255))
        cur_y += id_line_h
        
    cur_y += int(h * 0.018)
    
    # Draw source citation
    draw.text((box_x0 + pad_x, cur_y), src_raw, font=font_src, fill=(225, 225, 225, 255))
    
    result = Image.alpha_composite(bg, overlay).convert("RGB")
    result.save(output_path, quality=95)
    print(f"Created Slide 2: {output_path}")

if __name__ == '__main__':
    # Option 1: Shrouded Figure
    create_slide_1('/home/user/concept_shrouded_figure.jpg', '/home/user/desain_opsi1_slide1.jpg')
    create_slide_2('/home/user/concept_shrouded_figure.jpg', '/home/user/desain_opsi1_slide2.jpg')
    
    # Option 2: Exhausted Alone
    create_slide_1('/home/user/concept_exhausted_portrait.jpg', '/home/user/desain_opsi2_slide1.jpg')
    create_slide_2('/home/user/concept_exhausted_portrait.jpg', '/home/user/desain_opsi2_slide2.jpg')
