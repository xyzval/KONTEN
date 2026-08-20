from PIL import Image, ImageDraw, ImageFont

def render_scary_slide1(base_path, output_path):
    img = Image.open(base_path)
    w, h = img.size
    
    # Proper crop preserving 3:4 aspect ratio focusing on the Demon on the left
    zoom_factor = 0.72
    crop_w = int(w * zoom_factor)
    crop_h = int(h * zoom_factor)
    
    crop_x0 = 0
    crop_y0 = int(h * 0.05)
    crop_x1 = crop_x0 + crop_w
    crop_y1 = crop_y0 + crop_h
    
    cropped = img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.024))
    
    lines = [
        "berikan aku jawaban untuk",
        "pertanyaan ini"
    ]
    
    line_h = int(h * 0.033)
    pad_x = int(w * 0.055)
    pad_y = int(h * 0.020)
    
    max_txt_w = max(draw.textbbox((0, 0), line, font=font_text)[2] - draw.textbbox((0, 0), line, font=font_text)[0] for line in lines)
    box_w = max_txt_w + (pad_x * 2)
    box_h = (len(lines) * line_h) + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.48)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 190))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(slide1_base, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Scary Slide 1 saved: {output_path}")

def render_scary_slide2(base_path, output_path):
    img = Image.open(base_path)
    w, h = img.size
    
    # Proper crop preserving 3:4 aspect ratio focusing on the Priest on the right
    zoom_factor = 0.72
    crop_w = int(w * zoom_factor)
    crop_h = int(h * zoom_factor)
    
    crop_x0 = w - crop_w
    crop_y0 = int(h * 0.20)
    crop_x1 = w
    crop_y1 = crop_y0 + crop_h
    
    cropped = img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    slide2_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.024))
    
    text = "katakanlah"
    
    pad_x = int(w * 0.065)
    pad_y = int(h * 0.018)
    
    bbox = draw.textbbox((0, 0), text, font=font_text)
    txt_w = bbox[2] - bbox[0]
    txt_h = bbox[3] - bbox[1]
    
    box_w = txt_w + (pad_x * 2)
    box_h = txt_h + (pad_y * 2) + int(h * 0.005)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.54)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 190))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    draw.text((box_x0 + pad_x, box_y0 + pad_y), text, font=font_text, fill=(255, 255, 255, 255))
    
    res = Image.alpha_composite(slide2_base, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Scary Slide 2 saved: {output_path}")

def render_scary_slide3(base_path, output_path):
    img = Image.open(base_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0235))
    
    lines = [
        "jika takdir sudah diatur oleh tuhan",
        "lantas mengapa kamu berdoa ?"
    ]
    
    line_h = int(h * 0.034)
    pad_x = int(w * 0.055)
    pad_y = int(h * 0.020)
    
    max_txt_w = max(draw.textbbox((0, 0), line, font=font_text)[2] - draw.textbbox((0, 0), line, font=font_text)[0] for line in lines)
    box_w = max_txt_w + (pad_x * 2)
    box_h = (len(lines) * line_h) + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.58)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=16, fill=(0, 0, 0, 190))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        x = box_x0 + pad_x
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Scary Slide 3 saved: {output_path}")

render_scary_slide1('/home/user/scary_demon_takdir.jpg', '/home/user/slide1_takdir_seram.jpg')
render_scary_slide2('/home/user/scary_demon_takdir.jpg', '/home/user/slide2_takdir_seram.jpg')
render_scary_slide3('/home/user/scary_demon_takdir.jpg', '/home/user/slide3_takdir_seram.jpg')
