from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_slide_1_focused(base_img_path, output_path):
    img = Image.open(base_img_path)
    w, h = img.size
    
    # In slide 1: Crop the left 65% of width, then crop vertically or scale to 3:4 portrait
    # Left character is centered around x in [50, 500], y in [250, 1000]
    crop_w = int(w * 0.70)
    crop_h = int(crop_w * (h / w))
    # Let's crop bounding box: x0=0, y0=int(h*0.05), x1=crop_w, y1=int(h*0.05)+crop_h
    cropped = img.crop((0, 0, int(w * 0.72), h))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.027))
    
    lines = [
        "apa yang kamu rasakan",
        "setelah ibumu sudah tiada ??"
    ]
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    line_h = int(h * 0.038)
    start_y = int(h * 0.50)
    
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        shadow_draw.text((x, y), line, font=font_text, fill=(0, 0, 0, 255))
        text_draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    shadow_blur_1 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=6))
    shadow_blur_2 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2))
    
    res = Image.alpha_composite(slide1_base, shadow_blur_1)
    res = Image.alpha_composite(res, shadow_blur_1)
    res = Image.alpha_composite(res, shadow_blur_2)
    res = Image.alpha_composite(res, shadow_blur_2)
    res = Image.alpha_composite(res, text_layer)
    
    res.convert("RGB").save(output_path, quality=98)
    print(f"Slide 1 created: {output_path}")

def create_slide_2_full(base_img_path, output_path):
    img = Image.open(base_img_path).convert("RGBA")
    w, h = img.size
    
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0265))
    
    lines = [
        "tidak ada lagi keluarga yang peduli",
        "kepadaku, dan semua saudara",
        "hanyalah nama."
    ]
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    line_h = int(h * 0.038)
    start_y = int(h * 0.60)
    
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        # Position centered or slightly to the right
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        shadow_draw.text((x, y), line, font=font_text, fill=(0, 0, 0, 255))
        text_draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    shadow_blur_1 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=6))
    shadow_blur_2 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2))
    
    res = Image.alpha_composite(img, shadow_blur_1)
    res = Image.alpha_composite(res, shadow_blur_1)
    res = Image.alpha_composite(res, shadow_blur_2)
    res = Image.alpha_composite(res, shadow_blur_2)
    res = Image.alpha_composite(res, text_layer)
    
    res.convert("RGB").save(output_path, quality=98)
    print(f"Slide 2 created: {output_path}")

create_slide_1_focused('/home/user/two_men_candlelight.jpg', '/home/user/slide1_obrolan_ibu.jpg')
create_slide_2_full('/home/user/two_men_candlelight.jpg', '/home/user/slide2_obrolan_ibu.jpg')
