from PIL import Image, ImageDraw, ImageFont

def render_karma_slide1(base_path, output_path, crop_left=0.55):
    img = Image.open(base_path)
    w, h = img.size
    
    # Crop to left side to focus on the speaker
    crop_w = int(w * crop_left)
    cropped = img.crop((0, 0, crop_w, h))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.024))
    
    text = "karma itu tidak ada"
    
    pad_x = int(w * 0.05)
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
    
    # Semi-transparent dark rounded box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=14, fill=(0, 0, 0, 185))
    
    # Quote mark at top-left
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Text centered
    draw.text((box_x0 + pad_x, box_y0 + pad_y), text, font=font_text, fill=(255, 255, 255, 255))
    
    res = Image.alpha_composite(slide1_base, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 1 saved: {output_path}")

def render_karma_slide2(base_path, output_path):
    img = Image.open(base_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0215))
    
    lines = [
        "itu hanyalah konsep untuk menghibur",
        "korban yang tertindas, orang yang jahat",
        "padamu tidak selalu akan mendapat",
        "ganjarannya, bisa jadi dia hidup",
        "bahagia tanpa merasa bersalah, maka",
        "bertindaklah jangan diam saja!"
    ]
    
    line_h = int(h * 0.032)
    pad_x = int(w * 0.055)
    pad_y = int(h * 0.020)
    
    max_txt_w = max(draw.textbbox((0, 0), line, font=font_text)[2] - draw.textbbox((0, 0), line, font=font_text)[0] for line in lines)
    box_w = max_txt_w + (pad_x * 2)
    box_h = (len(lines) * line_h) + (pad_y * 2)
    
    box_x0 = (w - box_w) // 2
    box_y0 = int(h * 0.58)
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    # Semi-transparent dark rounded box
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=16, fill=(0, 0, 0, 185))
    
    # Quote mark at top-left
    draw.text((box_x0 + int(w * 0.03), box_y0 - int(h * 0.022)), "“", font=font_quote, fill=(255, 255, 255, 255))
    
    # Text left-aligned
    start_y = box_y0 + pad_y
    for i, line in enumerate(lines):
        x = box_x0 + pad_x
        y = start_y + i * line_h
        draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    res = Image.alpha_composite(img, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Slide 2 saved: {output_path}")

# Option 1: Demon Provoker & Wounded Man (Dark Fantasy)
render_karma_slide1('/home/user/concept_demon_provoker.jpg', '/home/user/slide1_karma_demon.jpg', crop_left=0.55)
render_karma_slide2('/home/user/concept_demon_provoker.jpg', '/home/user/slide2_karma_demon.jpg')

# Option 2: Gritty Noir Realism (Mentor & Battered Man)
render_karma_slide1('/home/user/concept_cynical_noir.jpg', '/home/user/slide1_karma_noir.jpg', crop_left=0.55)
render_karma_slide2('/home/user/concept_cynical_noir.jpg', '/home/user/slide2_karma_noir.jpg')
