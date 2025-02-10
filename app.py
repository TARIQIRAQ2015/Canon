import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
import requests
import json
import math

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة الذكية",
    page_icon="🎨",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Cairo', sans-serif !important;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #ffffff;
        direction: rtl;
        text-align: right;
    }

    /* إخفاء العناصر غير المرغوب فيها */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* تنسيق مربع الحاسبة */
    .calculator-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin: 2rem auto;
        max-width: 800px;
    }

    /* تنسيق العنوان */
    .title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #00ffff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    /* تنسيق النتيجة */
    .result {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 700;
        color: #00ffff;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    /* تنسيق عناصر الإدخال */
    .stNumberInput, .stCheckbox {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #ffffff !important;
    }

    .stNumberInput:hover, .stCheckbox:hover {
        border-color: #00ffff !important;
        transition: all 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

def calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler):
    total_cost = 0
    total_cost += colored_pages * 50
    total_cost += bw_pages * 35
    if cover: total_cost += 250
    if carton: total_cost += 250
    if nylon: total_cost += 250
    if ruler: total_cost += 250
    return total_cost

def round_to_nearest_currency(amount):
    remainder = amount % 250
    if remainder == 0:
        return amount
    elif remainder >= 125:
        return amount + (250 - remainder)
    else:
        return amount - remainder

def main():
    st.markdown("<div class='calculator-box'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>✨ حاسبة تكلفة الطباعة المتطورة ✨</h1>", unsafe_allow_html=True)

    # المدخلات
    colored_pages = st.number_input("🎨 عدد الصفحات الملونة", min_value=0, value=0)
    bw_pages = st.number_input("📄 عدد الصفحات السوداء", min_value=0, value=0)
    
    # الإضافات
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("🎯 تصميم غلاف احترافي")
        carton = st.checkbox("📦 كرتون فاخر")
    with col2:
        nylon = st.checkbox("✨ تغليف نايلون")
        ruler = st.checkbox("📏 مسطرة خاصة")

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
    rounded_cost = round_to_nearest_currency(total_cost)

    # عرض النتيجة
    st.markdown(f"""
        <div class='result'>
            💎 التكلفة الإجمالية: {rounded_cost} دينار 💎
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
