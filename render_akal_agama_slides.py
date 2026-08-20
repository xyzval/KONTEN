from PIL import Image, ImageDraw, ImageFont

def render_slide_1(bg_path, output_path):
    img = Image.open(bg_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.024))
    
    text = "Jika syarat beragama adalah berakal..."
    
    pad_x = int(w * 0.055)
    pad_y = int(h * 0.018)
    
    bbox = draw.textbbox((0, 0), text, font=font_text)
    txt_w = bbox[2] - bbox[0]
    txt_h = bbox[3] - bbox[1]
    
    box_w = txt_w + (pad_x * 2)
    box_h = txt_h + (pad_y * 2) + int(h * 0.005)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.52)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 185))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    draw.text((box_x0 + pad_x, box_y0 + pad_y), text, font=font_text, fill=(255, 255, 255, 255))
    
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 1 saved: {output_path}")

def render_slide_2(bg_path, output_path):
    img = Image.open(bg_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0235))
    
    lines = [
        "Tapi kenapa yang berakal kebanyakan",
        "tidak beragama?."
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
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 185))
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        x = box_x0 + pad_x
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 2 saved: {output_path}")

render_slide_1('/home/user/scholar_intellect_faith.jpg', '/home/user/slide1_akal_agama.jpg')
render_slide_2('/home/user/demon_skeptic_intellect.jpg', '/home/user/slide2_akal_agama.jpg')
