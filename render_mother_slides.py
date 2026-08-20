import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def render_slide_1(base_img_path, output_path):
    img = Image.open(base_img_path)
    w, h = img.size
    
    # For Slide 1: Crop / focus on the left character (the speaker asking)
    # Original aspect ratio is 1086 x 1448
    # Let's crop from left 0 to ~900 and scale to full height
    crop_w = int(w * 0.82)
    crop_box = (0, 0, crop_w, h)
    slide1_base = img.crop(crop_box).resize((w, h), Image.Resampling.LANCZOS).convert("RGBA")
    
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
    start_y = int(h * 0.48)
    
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

def render_slide_2(base_img_path, output_path):
    img = Image.open(base_img_path).convert("RGBA")
    w, h = img.size
    
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.026))
    
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
    start_y = int(h * 0.58)
    
    # Position text nicely centered or slightly to the right above the table
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        # Center horizontally
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

render_slide_1('/home/user/two_men_candlelight.jpg', '/home/user/slide1_ibu_baru.jpg')
render_slide_2('/home/user/two_men_candlelight.jpg', '/home/user/slide2_ibu_baru.jpg')
