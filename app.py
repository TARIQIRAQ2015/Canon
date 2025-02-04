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

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700&display=swap');
    
    /* تعيين الخط والخلفية الأساسية */
    .main {
        font-family: 'Cairo', sans-serif;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #e9ecef;
    }
    
    /* تنسيق العنوان الرئيسي */
    h1 {
        background: linear-gradient(120deg, #CBA135 0%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    /* تأثير التوهج للعنوان */
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #CBA135, 0 0 20px #CBA135;
        }
        to {
            text-shadow: 0 0 15px #FFD700, 0 0 25px #FFD700;
        }
    }
    
    /* تنسيق الأزرار */
    .stButton>button {
        background: linear-gradient(135deg, #CBA135 0%, #FFD700 100%);
        color: #1a1a2e;
        border: none;
        border-radius: 15px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(203, 161, 53, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(203, 161, 53, 0.3);
        background: linear-gradient(135deg, #FFD700 0%, #CBA135 100%);
    }
    
    /* تنسيق حقول الإدخال */
    .stNumberInput>div>div>input {
        background: rgba(45, 45, 68, 0.9);
        border: 2px solid rgba(203, 161, 53, 0.3);
        border-radius: 10px;
        color: #e9ecef;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .stNumberInput>div>div>input:focus {
        border-color: #CBA135;
        box-shadow: 0 0 15px rgba(203, 161, 53, 0.3);
    }
    
    /* تنسيق مربعات الاختيار */
    .stCheckbox>label {
        color: #e9ecef !important;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .stCheckbox>label>span {
        background: rgba(45, 45, 68, 0.9);
        border: 2px solid rgba(203, 161, 53, 0.3);
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .stCheckbox>label>span:hover {
        border-color: #CBA135;
        box-shadow: 0 0 10px rgba(203, 161, 53, 0.2);
    }
    
    /* تنسيق القائمة المنسدلة */
    .stSelectbox>div>div {
        background: rgba(45, 45, 68, 0.9);
        border: 2px solid rgba(203, 161, 53, 0.3);
        border-radius: 10px;
        color: #e9ecef;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .stSelectbox>div>div:hover {
        border-color: #CBA135;
        box-shadow: 0 0 15px rgba(203, 161, 53, 0.3);
    }
    
    /* تنسيق عرض النتيجة */
    .result-container {
        background: rgba(45, 45, 68, 0.9);
        border: 2px solid #CBA135;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(203, 161, 53, 0.2);
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* تنسيق متجاوب */
    @media screen and (max-width: 768px) {
        h1 {
            font-size: 2.5rem !important;
        }
        
        .stButton>button {
            width: 100%;
            padding: 0.6rem 1.5rem;
        }
        
        .result-container {
            padding: 1.5rem;
        }
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
            <div class='result-container'>
                <h3 style='color: #CBA135; margin: 0; font-size: 1.8rem; text-align: center;'>التكلفة الإجمالية</h3>
                <p style='color: #e9ecef; font-size: 2.5rem; margin: 1rem 0; text-align: center; font-weight: bold;'>{total_cost} دينار</p>
                <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
                    <div style='background: rgba(203, 161, 53, 0.1); padding: 1rem; border-radius: 10px; text-align: center;'>
                        <p style='margin: 0; color: #CBA135;'>عدد الصفحات الكلي</p>
                        <p style='margin: 0; font-size: 1.2rem;'>{colored_pages + bw_color_pages + bw_pages}</p>
                    </div>
                    <div style='background: rgba(203, 161, 53, 0.1); padding: 1rem; border-radius: 10px; text-align: center;'>
                        <p style='margin: 0; color: #CBA135;'>الإضافات</p>
                        <p style='margin: 0; font-size: 1.2rem;'>{sum([cover, carton, nylon])}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    if st.button("💰 Calculate Total Cost"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        st.markdown(f"""
            <div class='result-container'>
                <h3 style='color: #CBA135; margin: 0; font-size: 1.8rem; text-align: center;'>Total Cost</h3>
                <p style='color: #e9ecef; font-size: 2.5rem; margin: 1rem 0; text-align: center; font-weight: bold;'>{total_cost} Dinar</p>
                <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
                    <div style='background: rgba(203, 161, 53, 0.1); padding: 1rem; border-radius: 10px; text-align: center;'>
                        <p style='margin: 0; color: #CBA135;'>Total Pages</p>
                        <p style='margin: 0; font-size: 1.2rem;'>{colored_pages + bw_color_pages + bw_pages}</p>
                    </div>
                    <div style='background: rgba(203, 161, 53, 0.1); padding: 1rem; border-radius: 10px; text-align: center;'>
                        <p style='margin: 0; color: #CBA135;'>Add-ons</p>
                        <p style='margin: 0; font-size: 1.2rem;'>{sum([cover, carton, nylon])}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# زر إعادة التعيين مع تصميم محسن
if language == "العربية":
    if st.button("🔄 إعادة تعيين"):
        st.experimental_rerun()
else:
    if st.button("🔄 Reset"):
        st.experimental_rerun()
