import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
import pyperclip

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Tajawal', sans-serif !important;
        background: #1A1A1A;
        color: #FFFFFF;
        direction: rtl;
        text-align: right;
        padding: 2rem;
    }

    /* إخفاء العناصر غير المرغوب فيها */
    header[data-testid="stHeader"], footer, #MainMenu {
        display: none !important;
    }

    /* تنسيق مربع الحاسبة */
    .calculator-box {
        background: #2D2D2D;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin: 0 auto;
        max-width: 800px;
    }

    /* تنسيق العنوان */
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* تنسيق النتيجة */
    .result {
        background: #363636;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 700;
        color: #FFFFFF;
    }

    .sub-result {
        font-size: 1.1rem;
        color: #B0B0B0;
        margin-top: 0.5rem;
    }

    /* تنسيق عناصر الإدخال */
    .stNumberInput input {
        background: #363636 !important;
        border: 1px solid #4A4A4A !important;
        border-radius: 8px !important;
        color: #FFFFFF !important;
        font-size: 1rem !important;
        padding: 0.5rem !important;
    }

    .stCheckbox {
        background: #363636 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
    }

    /* تنسيق العناوين */
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 1rem 0;
    }

    /* تنسيق الأقسام */
    .section {
        background: #363636;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }

    /* تنسيق زر النسخ */
    .copy-button {
        background: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        margin-top: 1rem;
        font-family: 'Tajawal', sans-serif;
    }

    .copy-button:hover {
        background: #45a049;
    }

    /* تنسيق ملخص الطلب */
    .summary {
        background: #404040;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
        text-align: right;
        font-size: 1.1rem;
        line-height: 1.6;
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

def generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost):
    extras = []
    if cover: extras.append("تصميم غلاف")
    if carton: extras.append("كرتون فاخر")
    if nylon: extras.append("تغليف نايلون")
    if ruler: extras.append("مسطرة خاصة")
    
    summary = f"""خلاصة الطلب:
• عدد الصفحات الملونة: {colored_pages} صفحة
• عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة"""

    if extras:
        summary += f"\n• الإضافات المطلوبة: {' + '.join(extras)}"
    
    summary += f"""
• التكلفة قبل التقريب: {total_cost:,} دينار
• التكلفة النهائية بعد التقريب: {rounded_cost:,} دينار"""
    
    return summary

def main():
    st.markdown("<div class='calculator-box'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>حاسبة تكلفة الطباعة 🖨️</h1>", unsafe_allow_html=True)

    # قسم الصفحات
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>تفاصيل الصفحات</h2>", unsafe_allow_html=True)
    colored_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود", min_value=0, value=0)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # قسم الإضافات
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>الإضافات</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("تصميم غلاف")
        carton = st.checkbox("كرتون فاخر")
    with col2:
        nylon = st.checkbox("تغليف نايلون")
        ruler = st.checkbox("مسطرة خاصة")
    st.markdown("</div>", unsafe_allow_html=True)

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
    rounded_cost = round_to_nearest_currency(total_cost)

    # عرض النتيجة والملخص
    st.markdown(f"""
        <div class='result'>
            التكلفة الإجمالية: {rounded_cost:,} دينار
            <div class='sub-result'>
                التكلفة قبل التقريب: {total_cost:,} دينار
            </div>
        </div>
    """, unsafe_allow_html=True)

    # إنشاء وعرض الملخص
    summary = generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)
    st.markdown(f"<div class='summary'>{summary.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
    
    # زر نسخ الملخص
    if st.button("نسخ الملخص", key="copy_button"):
        st.session_state.clipboard = summary
        st.success("تم نسخ الملخص بنجاح!")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
