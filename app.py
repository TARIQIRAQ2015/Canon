import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
import requests
import json
import math

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="✨",
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
        background: #f0f2f6;
        color: #1f1f1f;
        direction: rtl;
        text-align: right;
    }

    /* إخفاء العناصر غير المرغوب فيها */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* تنسيق مربع الحاسبة */
    .calculator-box {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 800px;
    }

    /* تنسيق العنوان */
    .title {
        font-size: 2rem;
        font-weight: 700;
        color: #1f1f1f;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* تنسيق النتيجة */
    .result {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
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
    st.markdown("<h1 class='title'>حاسبة تكلفة الطباعة</h1>", unsafe_allow_html=True)

    # المدخلات
    colored_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات السوداء", min_value=0, value=0)
    
    # الإضافات
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("تصميم غلاف احترافي")
        carton = st.checkbox("كرتون فاخر")
    with col2:
        nylon = st.checkbox("تغليف نايلون")
        ruler = st.checkbox("مسطرة خاصة")

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
    rounded_cost = round_to_nearest_currency(total_cost)

    # عرض النتيجة
    st.markdown(f"""
        <div class='result'>
            التكلفة الإجمالية: {rounded_cost} دينار
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
