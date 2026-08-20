from PIL import Image, ImageDraw, ImageFont

def render_proper_slide1(base_path, output_path):
    img = Image.open(base_path)
    w, h = img.size
    
    # Target aspect ratio is w : h
    # We want to zoom into the left top portion (the demon)
    # Let's crop with same aspect ratio:
    zoom_factor = 0.75  # 75% of full dimensions
    crop_w = int(w * zoom_factor)
    crop_h = int(h * zoom_factor)
    
    # Position crop at left-top: x0=0, y0=int(h * 0.05)
    crop_x0 = 0
    crop_y0 = int(h * 0.04)
    crop_x1 = crop_x0 + crop_w
    crop_y1 = crop_y0 + crop_h
    
    cropped = img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.038))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.024))
    
    text = "karma itu tidak ada"
    
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
    
    res = Image.alpha_composite(slide1_base, overlay).convert("RGB")
    res.save(output_path, quality=98)
    print(f"Fixed Slide 1 saved: {output_path}")

render_proper_slide1('/home/user/concept_demon_provoker.jpg', '/home/user/slide1_karma_demon_fixed.jpg')
render_proper_slide1('/home/user/concept_cynical_noir.jpg', '/home/user/slide1_karma_noir_fixed.jpg')
