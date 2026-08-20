from PIL import Image, ImageDraw, ImageFont, ImageFilter

def refine_slide1():
    img = Image.open('/home/user/demon_skeleton_gothic.jpg')
    w, h = img.size
    
    # Left crop 52% of image
    crop_w = int(w * 0.53)
    cropped = img.crop((0, 0, crop_w, h))
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
    
    res.convert("RGB").save('/home/user/slide1_iblis_tengkorak_final.jpg', quality=98)
    print("Refined Slide 1 saved!")

refine_slide1()
