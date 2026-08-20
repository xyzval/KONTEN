from PIL import Image, ImageDraw, ImageFont

def create_slide_1_box(base_path, output_path):
    img = Image.open(base_path)
    w, h = img.size
    
    # Left crop 53% for demon focus
    crop_w = int(w * 0.53)
    cropped = img.crop((0, 0, crop_w, h))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.024))
    
    lines = [
        "apa yang kamu rasakan",
        "setelah ibumu sudah tiada ??"
    ]
    
    line_h = int(h * 0.033)
    pad_x = int(w * 0.05)
    pad_y = int(h * 0.022)
    
    # Calculate box size based on text width
    max_txt_w = max(draw.textbbox((0, 0), line, font=font_text)[2] - draw.textbbox((0, 0), line, font=font_text)[0] for line in lines)
    box_w = max_txt_w + (pad_x * 2)
    box_h = (len(lines) * line_h) + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.48)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Draw rounded transparent black box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 185))
    
    # Quote mark at top-left of the box
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Text centered in box
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(slide1_base, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 1 with box saved: {output_path}")

def create_slide_2_box(base_path, output_path):
    img = Image.open(base_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Medium.ttf", int(h * 0.0235))
    
    lines = [
        "tidak ada lagi keluarga yang peduli",
        "kepadaku, dan semua saudara",
        "hanyalah nama."
    ]
    
    line_h = int(h * 0.033)
    pad_x = int(w * 0.055)
    pad_y = int(h * 0.022)
    
    max_txt_w = max(draw.textbbox((0, 0), line, font=font_text)[2] - draw.textbbox((0, 0), line, font=font_text)[0] for line in lines)
    box_w = max_txt_w + (pad_x * 2)
    box_h = (len(lines) * line_h) + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.58)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Draw rounded transparent black box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 185))
    
    # Quote mark at top-left of the box
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Text left-aligned or centered in box
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        x = box_x0 + pad_x
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 2 with box saved: {output_path}")

create_slide_1_box('/home/user/demon_skeleton_gothic.jpg', '/home/user/slide1_iblis_tengkorak_kotak.jpg')
create_slide_2_box('/home/user/demon_skeleton_gothic.jpg', '/home/user/slide2_iblis_tengkorak_kotak.jpg')
