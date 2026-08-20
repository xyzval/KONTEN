from PIL import Image, ImageDraw, ImageFont, ImageFilter

def render_gothic_slide1(base_path, output_path):
    img = Image.open(base_path)
    w, h = img.size
    
    # Crop the left side focusing on the demon
    # Crop box: left=0, top=0, right=int(w * 0.65), bottom=h
    cropped = img.crop((0, 0, int(w * 0.65), h))
    slide1_base = cropped.resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0265))
    
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
    print(f"Gothic Slide 1 created: {output_path}")

def render_gothic_slide2(base_path, output_path):
    img = Image.open(base_path).convert("RGBA")
    w, h = img.size
    
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.0255))
    
    lines = [
        "tidak ada lagi keluarga yang peduli",
        "kepadaku, dan semua saudara",
        "hanyalah nama."
    ]
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    line_h = int(h * 0.036)
    start_y = int(h * 0.62)
    
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
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
    print(f"Gothic Slide 2 created: {output_path}")

render_gothic_slide1('/home/user/demon_skeleton_gothic.jpg', '/home/user/slide1_iblis_tengkorak_baru.jpg')
render_gothic_slide2('/home/user/demon_skeleton_gothic.jpg', '/home/user/slide2_iblis_tengkorak_baru.jpg')
