import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
import requests
import json
import math

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة الذكية",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@200;300;400;500;700;800;900&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Tajawal', sans-serif !important;
        background: linear-gradient(120deg, #2E3192 0%, #1BFFFF 100%);
        color: #ffffff;
        direction: rtl;
        text-align: right;
        padding: 2rem;
    }

    /* إخفاء العناصر غير المرغوب فيها */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* تنسيق مربع الحاسبة */
    .calculator-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.2);
        margin: 1rem auto;
        max-width: 900px;
    }

    /* تنسيق العنوان */
    .title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #FFFFFF, #1BFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 3rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    }

    /* تنسيق النتيجة */
    .result {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        padding: 2.5rem;
        border-radius: 20px;
        margin-top: 2.5rem;
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        color: #FFFFFF;
        border: 2px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }

    .sub-result {
        font-size: 1.2rem;
        color: rgba(255,255,255,0.8);
        margin-top: 1rem;
    }

    /* تنسيق عناصر الإدخال */
    .stNumberInput input, .stCheckbox {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 15px !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        padding: 1rem !important;
    }

    .stNumberInput input:hover, .stCheckbox:hover {
        border-color: #1BFFFF !important;
        box-shadow: 0 0 15px rgba(27, 255, 255, 0.3) !important;
        transition: all 0.3s ease;
    }

    /* تنسيق العناوين */
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 1.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    /* تنسيق الأقسام */
    .section {
        background: rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        border: 1px solid rgba(255,255,255,0.2);
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
    st.markdown("<h1 class='title'>🖨️ حاسبة تكلفة الطباعة الاحترافية 🖨️</h1>", unsafe_allow_html=True)

    # قسم الصفحات
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>📑 تفاصيل الصفحات</h2>", unsafe_allow_html=True)
    colored_pages = st.number_input("🎨 عدد الصفحات الملونة", min_value=0, value=0, help="ادخل عدد الصفحات الملونة المطلوبة")
    bw_pages = st.number_input("⚫ عدد الصفحات بالأبيض والأسود", min_value=0, value=0, help="ادخل عدد الصفحات بالأبيض والأسود")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # قسم الإضافات
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>✨ الإضافات المميزة</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("🎯 تصميم غلاف احترافي", help="إضافة غلاف مصمم باحترافية")
        carton = st.checkbox("📦 كرتون فاخر", help="تغليف بكرتون عالي الجودة")
    with col2:
        nylon = st.checkbox("✨ تغليف نايلون", help="تغليف إضافي بالنايلون للحماية")
        ruler = st.checkbox("📏 مسطرة خاصة", help="إضافة مسطرة خاصة للقياس")
    st.markdown("</div>", unsafe_allow_html=True)

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
    rounded_cost = round_to_nearest_currency(total_cost)

    # عرض النتيجة
    st.markdown(f"""
        <div class='result'>
            💫 التكلفة الإجمالية (بعد التقريب): {rounded_cost:,} دينار 💫
            <div class='sub-result'>
                التكلفة قبل التقريب: {total_cost:,} دينار
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
