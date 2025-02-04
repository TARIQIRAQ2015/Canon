import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
from streamlit_particles import particles

# تحميل الرسوم المتحركة
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# تكوين خلفية الجزيئات المتحركة
particles_config = {
    "particles": {
        "number": {
            "value": 50,
            "density": {
                "enable": True,
                "value_area": 800
            }
        },
        "color": {
            "value": "#CBA135"
        },
        "shape": {
            "type": "circle"
        },
        "opacity": {
            "value": 0.5,
            "random": True
        },
        "size": {
            "value": 3,
            "random": True
        },
        "line_linked": {
            "enable": True,
            "distance": 150,
            "color": "#CBA135",
            "opacity": 0.2,
            "width": 1
        },
        "move": {
            "enable": True,
            "speed": 2,
            "direction": "none",
            "random": True,
            "straight": False,
            "out_mode": "out",
            "bounce": False,
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": True,
                "mode": "repulse"
            },
            "onclick": {
                "enable": True,
                "mode": "push"
            },
            "resize": True
        }
    }
}

# تطبيق الأنماط
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0F0F1F 0%, #1E1E2E 100%);
        color: #FFFFFF;
    }
    .stButton>button {
        background: linear-gradient(135deg, #CBA135 0%, #E5B94E 100%);
        color: white;
        border-radius: 15px;
        padding: 0.7rem 2.5rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(203, 161, 53, 0.3);
        backdrop-filter: blur(10px);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(203, 161, 53, 0.5);
    }
    .stNumberInput>div>div>input {
        background: rgba(45, 45, 68, 0.7);
        color: white;
        border: 2px solid #CBA135;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    .stSelectbox>div>div {
        background: rgba(45, 45, 68, 0.7);
        color: white;
        border: 2px solid #CBA135;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    .stCheckbox>label {
        color: white !important;
        background: rgba(45, 45, 68, 0.7);
        padding: 10px 15px;
        border-radius: 10px;
        border: 1px solid #CBA135;
        backdrop-filter: blur(10px);
    }
    h1 {
        background: linear-gradient(135deg, #CBA135 0%, #E5B94E 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem !important;
        margin-bottom: 2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-weight: bold !important;
        letter-spacing: 2px;
    }
    .result-card {
        background: rgba(45, 45, 68, 0.7);
        border: 2px solid #CBA135;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    .section-title {
        color: #CBA135;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# تطبيق خلفية الجزيئات
particles(particles_config, key="particles")

# تحميل الرسوم المتحركة للطابعة
lottie_printer = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_rlzitsqx.json')

# عنوان التطبيق مع الرسوم المتحركة
st.markdown('<div style="text-align: center; padding: 20px;">', unsafe_allow_html=True)
st.title("🖨️ نظام حساب تكلفة الطباعة المتطور")
st_lottie(lottie_printer, height=250, key="printer")
st.markdown('</div>', unsafe_allow_html=True)

# تعريف الألوان والأنماط
primary_color = "#1E1E2E"
secondary_color = "#CBA135"
text_color = "#FFFFFF"

# دالة لحساب التكلفة الإجمالية
def calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon):
    total_cost = 0
    
    # حساب تكلفة الصفحات الملونة
    total_cost += colored_pages * 50
    
    # حساب تكلفة الصفحات الأبيض والأسود مع ألوان قليلة
    total_cost += bw_color_pages * 40
    
    # حساب تكلفة الصفحات الأبيض والأسود فقط
    total_cost += bw_pages * 35
    
    # حساب تكلفة الصفحة الأخيرة إذا كانت فارغة
    if last_page_empty:
        total_cost += 25
    
    # حساب تكلفة الغلاف إذا تم اختياره
    if cover:
        total_cost += 250
    
    # حساب تكلفة الكارتونة إذا تم اختيارها
    if carton:
        total_cost += 250
    
    # حساب تكلفة النايلون إذا تم اختياره
    if nylon:
        total_cost += 250
    
    return total_cost

# اختيار اللغة
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# إدخال عدد الصفحات
if language == "العربية":
    colored_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
    bw_color_pages = st.number_input("عدد الصفحات الأبيض والأسود مع ألوان قليلة", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات الأبيض والأسود فقط", min_value=0, value=0)
else:
    colored_pages = st.number_input("Number of Colored Pages", min_value=0, value=0)
    bw_color_pages = st.number_input("Number of Black & White Pages with Few Colors", min_value=0, value=0)
    bw_pages = st.number_input("Number of Black & White Pages Only", min_value=0, value=0)

# خيارات إضافية
if language == "العربية":
    last_page_empty = st.checkbox("الصفحة الأخيرة فارغة")
    cover = st.checkbox("إضافة غلاف ملون")
    carton = st.checkbox("إضافة كارتونة")
    nylon = st.checkbox("إضافة نايلون")
else:
    last_page_empty = st.checkbox("Last Page is Empty")
    cover = st.checkbox("Add Colored Cover")
    carton = st.checkbox("Add Carton")
    nylon = st.checkbox("Add Nylon")

# تحسين عرض النتيجة
if language == "العربية":
    if st.button("💰 حساب التكلفة", key="calc_ar"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        st.markdown(f"""
            <div class="result-card">
                <h3 class="section-title">التكلفة الإجمالية</h3>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <p style="color: #E5B94E; font-size: 36px; margin: 0; font-weight: bold;">
                        {total_cost} دينار
                    </p>
                </div>
                <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(203, 161, 53, 0.3);">
                    <p style="color: #CBA135; margin: 5px 0;">تفاصيل التكلفة:</p>
                    <p style="color: white; margin: 5px 0;">• صفحات ملونة: {colored_pages * 50} دينار</p>
                    <p style="color: white; margin: 5px 0;">• صفحات أبيض وأسود مع ألوان: {bw_color_pages * 40} دينار</p>
                    <p style="color: white; margin: 5px 0;">• صفحات أبيض وأسود: {bw_pages * 35} دينار</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    if st.button("💰 Calculate Total Cost", key="calc_en"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        st.markdown(f"""
            <div class="result-card">
                <h3 class="section-title">Total Cost</h3>
                <div style="display: flex; justify-content: center; align-items: center;">
                    <p style="color: #E5B94E; font-size: 36px; margin: 0; font-weight: bold;">
                        {total_cost} Dinar
                    </p>
                </div>
                <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(203, 161, 53, 0.3);">
                    <p style="color: #CBA135; margin: 5px 0;">Cost Details:</p>
                    <p style="color: white; margin: 5px 0;">• Colored Pages: {colored_pages * 50} Dinar</p>
                    <p style="color: white; margin: 5px 0;">• B&W with Colors: {bw_color_pages * 40} Dinar</p>
                    <p style="color: white; margin: 5px 0;">• B&W Pages: {bw_pages * 35} Dinar</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# أزرار إعادة التعيين مع تصميم محسن
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if language == "العربية":
        if st.button("🔄 إعادة تعيين", key="reset_ar"):
            st.experimental_rerun()
    else:
        if st.button("🔄 Reset", key="reset_en"):
            st.experimental_rerun()
