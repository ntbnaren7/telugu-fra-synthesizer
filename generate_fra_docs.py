import os, random, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ===== CONFIG =====
NUM_DOCS = 200
OUTPUT_DIR = "fra_telugu_docs"
ZIP_NAME = "fra_telugu_docs.zip"

# ===== FONTS =====
# Put your Telugu font files (NotoSansTelugu-Regular.ttf and NotoSansTelugu_Condensed-Bold.ttf)
# in the same folder as this script
regular_path = "NotoSansTelugu-Regular.ttf"
bold_path = "NotoSansTelugu_Condensed-Bold.ttf"

try:
    font_reg = ImageFont.truetype(regular_path, 26)
    font_small = ImageFont.truetype(regular_path, 20)
    font_bold = ImageFont.truetype(bold_path, 38)
except:
    print("⚠️ Could not load Telugu fonts. Using default.")
    font_reg = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_bold = ImageFont.load_default()

# ===== DATA SOURCES =====
headers = [
    "అటవీ హక్కుల చట్టం 2006 కింద పత్రం",
    "అనెక్సర్ - II (గ్రామ సభ నిర్ణయం)",
    "అనెక్సర్ - III (డీఎల్సీ ఆమోదం)",
    "అనెక్సర్ - IV (వ్యక్తిగత పత్తా)",
    "అనెక్సర్ - V (సామూహిక పత్తా)"
]
fields = [
    "హక్కుదారుని పేరు", "తండ్రి పేరు", "గ్రామం పేరు",
    "మండలం", "జిల్లా", "హక్కు రకం",
    "సర్వే నెంబర్", "విస్తీర్ణం", "స్థితి", "తేదీ"
]
statuses = ["ఆమోదించబడింది", "పెండింగ్", "తిరస్కరించబడింది", "అంశికంగా ఆమోదించబడింది"]
rights = ["వ్యక్తిగత హక్కు (IFR)", "సామూహిక హక్కు (CFR)", "సమాజ హక్కు (CR)"]
villages = ["అనంతగిరి", "ఎతూరునాగారం", "మంగపేట", "తాడ్వాయి", "భూపాలపల్లి", "ములుగు", "కొండపల్లి", "పామవరపు", "పరస్నగరం"]

# ===== EFFECT =====
def apply_yellow_old_effect(img):
    w,h = img.size
    yellow_layer = Image.new("RGB",(w,h),(240,220,140))
    img = Image.blend(img,yellow_layer,alpha=0.35)
    img = img.point(lambda p: p*random.uniform(0.75,0.9))
    if random.random()<0.9:
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.4,1.0)))
    # stains
    stain = Image.new("RGBA", img.size,(255,255,255,0))
    sd = ImageDraw.Draw(stain)
    for _ in range(random.randint(40,100)):
        rx,ry = random.randint(0,w-1), random.randint(0,h-1)
        rsize = random.randint(5,35)
        color=(random.randint(200,240),random.randint(180,210),random.randint(90,130),random.randint(60,120))
        sd.ellipse((rx,ry,rx+rsize,ry+rsize), fill=color)
    img = Image.alpha_composite(img.convert("RGBA"),stain).convert("RGB")
    return img

# ===== GENERATION =====
os.makedirs(OUTPUT_DIR, exist_ok=True)

for i in range(1, NUM_DOCS+1):
    W,H = 1000,1400
    img = Image.new("RGB",(W,H),(250,245,200))
    draw = ImageDraw.Draw(img)

    header = random.choice(headers)
    draw.text((W//2-220,60), header, font=font_bold, fill=(40,40,40))
    draw.line((60,130,W-60,130), fill=(60,60,60), width=2)

    y = 160
    for field in fields:
        if "పేరు" in field:
            value = f"శ్రీ {random.choice(['రాములు','కృష్ణ','వెంకటేశ్','లక్ష్మణ్','సాయిలు','శేషు','బాబురావు','రాజు','శంకర్','నరసింహం','మధు','హనుమంతు','శివ','గోపాల్'])}"
        elif "గ్రామం" in field:
            value = random.choice(villages)
        elif "హక్కు రకం" in field:
            value = random.choice(rights)
        elif "స్థితి" in field:
            value = random.choice(statuses)
        elif "విస్తీర్ణం" in field:
            value = f"{random.randint(1,40)} ఎకరాలు"
        elif "సర్వే" in field:
            value = f"{random.randint(100,999)}/{random.randint(1,9)}"
        elif "తేదీ" in field:
            value = f"{random.randint(1,28)}-{random.randint(1,12)}-19{random.randint(40,99)}"
        else:
            value = f"సూచన {random.randint(1000,9999)}"
        draw.text((80,y), f"{field}:", font=font_reg, fill=(30,30,30))
        draw.text((400,y), value, font=font_reg, fill=(30,30,30))
        y += 65

    draw.rectangle((60, H-220, W-60, H-120), outline=(60,60,60), width=2)
    draw.text((80,H-200), "జిల్లా అధికారుల సంతకం: ____________________", font=font_reg, fill=(30,30,30))

    if random.random()<0.85:
        sx,sy = random.randint(W-300,W-140), random.randint(H-400,H-280)
        draw.ellipse((sx-65,sy-65,sx+65,sy+65), outline=(100,0,0), width=5)
        draw.text((sx-50,sy-10),"జిల్లా ముద్ర",font=font_small,fill=(120,0,0))

    img = apply_yellow_old_effect(img)
    img.save(os.path.join(OUTPUT_DIR,f"fra_telugu_yellow_{i:03d}.png"), format="PNG", optimize=True)

# ===== ZIP =====
with zipfile.ZipFile(ZIP_NAME,'w') as zf:
    for f in sorted(os.listdir(OUTPUT_DIR)):
        zf.write(os.path.join(OUTPUT_DIR,f), arcname=f)

print(f"✅ Done! Generated {NUM_DOCS} documents.")
print(f"📂 PNGs saved in: {OUTPUT_DIR}")
print(f"📦 ZIP file created: {ZIP_NAME}")