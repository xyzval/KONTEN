from PIL import Image, ImageDraw, ImageFont

def render_slide_2_fixed(bg_path, output_path):
    img = Image.open(bg_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_head = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.022))
    font_saw = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.026))
    font_ar = ImageFont.truetype("/home/user/fonts/Amiri-Bold.ttf", int(h * 0.024))
    font_id = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.0195))
    font_src = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0195))
    
    arabic_text = "إِيَّاكُمْ وَالْغُلُوَّ فِي الدِّينِ فَإِنَّمَا أَهْلَكَ مَنْ كَانَ قَبْلَكُمُ الْغُلُوُّ فِي الدِّينِ"
    
    indo_lines = [
        "Hati-hatilah kalian dari berlebihan dalam agama,",
        "karena yang membinasakan umat sebelum kalian",
        "adalah sikap berlebihan dalam agama."
    ]
    source_text = "HR. Ibnu Majah"
    
    box_w = int(w * 0.88)
    pad_x = int(w * 0.05)
    pad_y = int(h * 0.022)
    
    head_h = int(h * 0.030)
    ar_h = int(h * 0.036)
    id_line_h = int(h * 0.027)
    
    total_h = head_h + int(h * 0.01) + ar_h + int(h * 0.015) + (len(indo_lines) * id_line_h) + int(h * 0.012) + int(h * 0.026)
    box_h = total_h + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.42)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=16, fill=(0, 0, 0, 185))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    cur_y = box_y0 + pad_y
    
    # Header: "Dari Rasulullah " + ﷺ + " :"
    t1 = "Dari Rasulullah "
    t1_bbox = draw.textbbox((0, 0), t1, font=font_head)
    t1_w = t1_bbox[2] - t1_bbox[0]
    draw.text((box_x0 + pad_x, cur_y), t1, font=font_head, fill=(255, 255, 255, 255))
    
    # Render ﷺ with Amiri font
    saw_str = "ﷺ"
    saw_bbox = draw.textbbox((0, 0), saw_str, font=font_saw, direction='rtl', language='ara')
    saw_w = saw_bbox[2] - saw_bbox[0]
    draw.text((box_x0 + pad_x + t1_w, cur_y - int(h * 0.003)), saw_str, font=font_saw, fill=(255, 255, 255, 255), direction='rtl', language='ara')
    
    # Render " :"
    draw.text((box_x0 + pad_x + t1_w + saw_w + int(w * 0.01), cur_y), " :", font=font_head, fill=(255, 255, 255, 255))
    cur_y += head_h + int(h * 0.008)
    
    # Arabic text (right aligned inside box)
    ar_rx = box_x1 - pad_x
    draw.text((ar_rx, cur_y), arabic_text, font=font_ar, fill=(255, 255, 255, 255), direction='rtl', language='ara', anchor='ra')
    cur_y += ar_h + int(h * 0.012)
    
    # Indonesian lines
    for line in indo_lines:
        draw.text((box_x0 + pad_x, cur_y), line, font=font_id, fill=(245, 245, 245, 255))
        cur_y += id_line_h
        
    cur_y += int(h * 0.012)
    
    # Source
    draw.text((box_x0 + pad_x, cur_y), source_text, font=font_src, fill=(225, 225, 225, 255))
    
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 2 fixed saved: {output_path}")

render_slide_2_fixed('/home/user/prophet_wisdom_mosque.jpg', '/home/user/slide2_ghuluw_hadits_final.jpg')
