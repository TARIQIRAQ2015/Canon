import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from streamlit_option_menu import option_menu
import streamlit_toggle as tog

# تحميل الرسوم المتحركة
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# تعريف الألوان والأنماط
primary_color = "#1E1E2E"
secondary_color = "#CBA135"
text_color = "#FFFFFF"

# تطبيق الأنماط
st.markdown("""
    <style>
    .main {
        background-color: #1E1E2E;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #CBA135;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(203, 161, 53, 0.5);
    }
    .stNumberInput>div>div>input {
        background-color: #2D2D44;
        color: white;
        border: 1px solid #CBA135;
    }
    .stSelectbox>div>div {
        background-color: #2D2D44;
        color: white;
    }
    .stCheckbox>label {
        color: white !important;
    }
    h1 {
        color: #CBA135 !important;
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .success {
        background-color: #2D2D44 !important;
        border: 2px solid #CBA135 !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(203, 161, 53, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# تحميل الرسوم المتحركة
lottie_printer = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_sjcbakkb.json')

# عنوان التطبيق مع الرسوم المتحركة
st.title("🖨️ حساب تكلفة الطباعة")
st_lottie(lottie_printer, height=200)

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

# زر لحساب التكلفة
if language == "العربية":
    if st.button("💰 حساب التكلفة"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        st.markdown(f"""
            <div style='background-color: #2D2D44; padding: 20px; border-radius: 10px; border: 2px solid #CBA135; margin: 20px 0;'>
                <h3 style='color: #CBA135; margin: 0;'>التكلفة الإجمالية</h3>
                <p style='color: white; font-size: 24px; margin: 10px 0;'>{total_cost} دينار</p>
            </div>
        """, unsafe_allow_html=True)
else:
    if st.button("💰 Calculate Total Cost"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        st.markdown(f"""
            <div style='background-color: #2D2D44; padding: 20px; border-radius: 10px; border: 2px solid #CBA135; margin: 20px 0;'>
                <h3 style='color: #CBA135; margin: 0;'>Total Cost</h3>
                <p style='color: white; font-size: 24px; margin: 10px 0;'>{total_cost} Dinar</p>
            </div>
        """, unsafe_allow_html=True)

# زر إعادة التعيين مع تصميم محسن
if language == "العربية":
    if st.button("🔄 إعادة تعيين"):
        st.experimental_rerun()
else:
    if st.button("🔄 Reset"):
        st.experimental_rerun()