from PIL import Image, ImageDraw, ImageFont, ImageFilter

def render_slide1(bg_path, output_path, question_text="apa penyebab laki-laki\nberumur pendek ??"):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    
    font_quote = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.045))
    font_text = ImageFont.truetype("/home/user/fonts/Roboto-Bold.ttf", int(h * 0.028))
    
    lines = question_text.split("\n")
    line_h = int(h * 0.036)
    start_y = int(h * 0.52)
    
    shadow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    shadow_draw = ImageDraw.Draw(shadow_layer)
    text_draw = ImageDraw.Draw(text_layer)
    
    for i, line in enumerate(lines):
        bbox = text_draw.textbbox((0, 0), line, font=font_text)
        txt_w = bbox[2] - bbox[0]
        x = (w - txt_w) // 2
        y = start_y + i * line_h
        if i == 0:
            shadow_draw.text((x - int(w * 0.045), y - int(h * 0.015)), "“", font=font_quote, fill=(0, 0, 0, 255))
            text_draw.text((x - int(w * 0.045), y - int(h * 0.015)), "“", font=font_quote, fill=(255, 255, 255, 255))
        shadow_draw.text((x, y), line, font=font_text, fill=(0, 0, 0, 255))
        text_draw.text((x, y), line, font=font_text, fill=(255, 255, 255, 255))
        
    shadow_blur_1 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=5))
    shadow_blur_2 = shadow_layer.filter(ImageFilter.GaussianBlur(radius=2))
    
    bg = Image.alpha_composite(bg, shadow_blur_1)
    bg = Image.alpha_composite(bg, shadow_blur_1)
    bg = Image.alpha_composite(bg, shadow_blur_2)
    bg = Image.alpha_composite(bg, text_layer)
    
    result = bg.convert("RGB")
    result.save(output_path, quality=98)
    print(f"Slide 1 Rendered: {output_path}")

render_slide1('/home/user/concept_shrouded_figure.jpg', '/home/user/slide1_tanpa_background_bersih.jpg')
