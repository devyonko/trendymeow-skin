import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="K13 Skin Studio // Summer",
    layout="wide",
    page_icon="🎐"
)

# --- 2. ANIME THEME ENGINE (CSS) ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Potta+One&family=M+PLUS+Rounded+1c:wght@400;700&family=Noto+Sans+JP:wght@500&display=swap" rel="stylesheet">
<style>
    /* === 1. BACKGROUND: Anime Sky === */
    .stApp {
        /* Main area: Bright Summer Sky */
        background: linear-gradient(160deg, #89f7fe 0%, #66a6ff 50%, #ff9a9e 100%);
        background-attachment: fixed;
    }

    /* === 2. TYPOGRAPHY === */
    
    /* Global Fonts */
    h1, h2, h3, .brush-font {
        font-family: 'Potta One', cursive !important;
        letter-spacing: 1px;
    }
    p, label, .stMarkdown, .stSlider, div {
        font-family: 'M PLUS Rounded 1c', sans-serif !important;
    }

    /* --- SIDEBAR SPECIFIC STYLING (DARK MODE) --- */
    
    /* Sidebar Background: Deep Night Blue Glass */
    section[data-testid="stSidebar"] {
        background-color: rgba(20, 30, 48, 0.9) !important;
        border-right: 2px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
    }

    /* Sidebar Text: ALL LIGHT COLORS */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #ff9a9e !important; /* Neon Pink Headers */
        text-shadow: 0 0 10px rgba(255, 154, 158, 0.5);
    }
    
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] li, 
    [data-testid="stSidebar"] .stMarkdown {
        color: #ecf0f1 !important; /* White/Light Grey Body */
    }

    [data-testid="stSidebar"] label {
        color: #ffffff !important; /* Pure White Labels */
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    [data-testid="stSidebar"] .stCaption {
        color: #bdc3c7 !important; /* Light Grey Captions */
    }

    /* --- MAIN AREA STYLING (LIGHT MODE) --- */
    
    /* Main Headers */
    .main h1 {
        color: #fff !important;
        text-shadow: 3px 3px 0px #2980b9, 5px 5px 10px rgba(0,0,0,0.2);
    }
    
    /* Main Blocks (Glass White) */
    div[data-testid="stBlock"] {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 2px solid white;
    }
    
    /* Dark Text inside the white main blocks */
    div[data-testid="stBlock"] p, 
    div[data-testid="stBlock"] h3 {
        color: #2c3e50 !important;
    }

    /* === 3. BUTTONS === */
    .stButton>button {
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        border: none;
        color: white !important;
        font-family: 'Potta One', cursive !important;
        border-radius: 50px;
        padding: 12px 30px;
        font-size: 1.1em;
        transition: transform 0.2s;
        box-shadow: 0 5px 15px rgba(255, 118, 136, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }

    /* === 4. ANIMATIONS === */
    .sakura {
        position: fixed; top: -10%; z-index: 9999;
        user-select: none; pointer-events: none;
        animation-name: fall; animation-timing-function: linear; animation-iteration-count: infinite;
    }
    @keyframes fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 0.8;}
        100% { top: 110%; transform: translateX(100px) rotate(360deg); opacity: 0;}
    }
</style>

<div style="position:fixed; width:100%; height:100%; top:0; left:0; pointer-events:none;">
    <div class="sakura" style="left:10%; animation-duration:10s; font-size: 20px;">🌸</div>
    <div class="sakura" style="left:30%; animation-duration:15s; animation-delay:2s; font-size: 15px;">🌸</div>
    <div class="sakura" style="left:70%; animation-duration:12s; animation-delay:1s; font-size: 24px;">🌸</div>
    <div class="sakura" style="left:50%; animation-duration:18s; animation-delay:4s; font-size: 18px;">🌸</div>
    <div class="sakura" style="left:90%; animation-duration:14s; animation-delay:3s; font-size: 22px;">🌸</div>
</div>
""", unsafe_allow_html=True)

# --- 3. CONSTANTS ---
DPI = 300 
MM_TO_INCH = 0.0393701
A4_WIDTH_MM = 210
A4_HEIGHT_MM = 297

def mm_to_px(mm):
    return int(mm * MM_TO_INCH * DPI)

PHONE_W_MM = 76.1
PHONE_H_MM = 163.2

SKIN_W_PX = mm_to_px(PHONE_W_MM)
SKIN_H_PX = mm_to_px(PHONE_H_MM)
A4_W_PX = mm_to_px(A4_WIDTH_MM)
A4_H_PX = mm_to_px(A4_HEIGHT_MM)

# --- 4. HEADER ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1>K13 Skin Studio <span style='font-size:0.6em; color:#fff;'>夏</span></h1>", unsafe_allow_html=True)
    st.markdown("**Create your anime aesthetic phone skin.**")

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("## Configuration")
    
    st.markdown("---")
    st.markdown("### 1. Upload (アップロード)")
    uploaded_file = st.file_uploader("Choose Wallpaper", type=["jpg", "png", "jpeg"])
    
    st.markdown("---")
    st.markdown("### 2. Calibration (調整)")
    st.caption("Adjust hole positions if needed:")
    offset_x_mm = st.slider("Horizontal (mm)", 0.0, 20.0, 4.0, 0.5)
    offset_y_mm = st.slider("Vertical (mm)", 0.0, 20.0, 4.0, 0.5)
    
    st.markdown("---")
    st.info("Tip: Use high-quality anime art for the best result!")

# --- 6. CORE LOGIC ---
R_BIG = 9.5
R_SMALL = 4.0
GAP_LEFT_VERT = 2.5
GAP_HORIZ = 6.0
GAP_RIGHT_VERT = 11.0

if uploaded_file is not None:
    # Load
    user_img = Image.open(uploaded_file).convert("RGBA")
    skin_canvas = Image.new("RGBA", (SKIN_W_PX, SKIN_H_PX), (255, 255, 255, 255))
    
    # Resize
    img_ratio = user_img.width / user_img.height
    skin_ratio = SKIN_W_PX / SKIN_H_PX
    
    if img_ratio > skin_ratio:
        new_h = SKIN_H_PX
        new_w = int(new_h * img_ratio)
    else:
        new_w = SKIN_W_PX
        new_h = int(new_w / img_ratio)
        
    user_img_resized = user_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    paste_x = (SKIN_W_PX - new_w) // 2
    paste_y = (SKIN_H_PX - new_h) // 2
    skin_canvas.paste(user_img_resized, (paste_x, paste_y))

    # Mask (Holes)
    mask = Image.new("L", (SKIN_W_PX, SKIN_H_PX), 255)
    draw_mask = ImageDraw.Draw(mask)

    c1_x = offset_x_mm + R_BIG
    c1_y = offset_y_mm + R_BIG
    c2_x = c1_x
    c2_y = c1_y + R_BIG + GAP_LEFT_VERT + R_BIG
    c3_x = c1_x + R_BIG + GAP_HORIZ + R_SMALL
    c3_y = (c1_y - R_BIG) + 6.75 + R_SMALL
    c4_x = c3_x
    c4_y = c3_y + R_SMALL + GAP_RIGHT_VERT + R_SMALL

    def punch(x, y, r, d):
        px, py, pr = mm_to_px(x), mm_to_px(y), mm_to_px(r)
        d.ellipse((px-pr, py-pr, px+pr, py+pr), fill=0)

    punch(c1_x, c1_y, R_BIG, draw_mask)
    punch(c2_x, c2_y, R_BIG, draw_mask)
    punch(c3_x, c3_y, R_SMALL, draw_mask)
    punch(c4_x, c4_y, R_SMALL, draw_mask)

    skin_final = skin_canvas.copy()
    skin_final.putalpha(mask)

    # A4 Page
    a4_page = Image.new("RGB", (A4_W_PX, A4_H_PX), (255, 255, 255))
    draw_a4 = ImageDraw.Draw(a4_page)

    center_x = (A4_W_PX - SKIN_W_PX) // 2
    center_y = (A4_H_PX - SKIN_H_PX) // 2
    a4_page.paste(skin_final, (center_x, center_y), skin_final)
    
    # Blue Outline for cutting
    draw_a4.rectangle([center_x, center_y, center_x + SKIN_W_PX, center_y + SKIN_H_PX], outline="#3498db", width=5)

    # Scale Line
    line_len_px = mm_to_px(50) 
    line_x_start = 100
    line_y_start = A4_H_PX - 200
    draw_a4.line([(line_x_start, line_y_start), (line_x_start + line_len_px, line_y_start)], fill="#3498db", width=8)
    
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    draw_a4.text((line_x_start, line_y_start - 60), "SCALE CHECK: 5 cm", fill="#3498db", font=font)

    # --- 7. OUTPUT ---
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("### Preview (プレビュー)")
        try:
             st.image(skin_final, use_container_width=True)
        except:
             st.image(skin_final, use_column_width=True)

    with c2:
        st.markdown("### Download (ダウンロード)")
        st.success("Ready to print!")
        
        pdf_buffer = io.BytesIO()
        a4_page.save(pdf_buffer, format="PDF", resolution=DPI)
        
        st.download_button(
            label="Download PDF Skin",
            data=pdf_buffer.getvalue(),
            file_name="K13_Summer_Skin.pdf",
            mime="application/pdf"
        )

else:
    st.markdown("""
    <div style="text-align: center; padding: 60px; background: rgba(255,255,255,0.6); border-radius: 20px;">
        <h3 style="color:#3498db !important; font-family:'Potta One' !important;">Waiting for Image...</h3>
        <p>Please upload your wallpaper in the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)