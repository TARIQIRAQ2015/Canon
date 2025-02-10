import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta

# تعيين إعدادات الصفحة مع إخفاء كامل للقائمة الجانبية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تحسين الأنماط مع دعم كامل للغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

    /* إعدادات عامة للغة العربية */
    * {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* تحسين محاذاة العناصر */
    .stTextInput, .stNumberInput, .stSelectbox, .stMultiselect {
        direction: rtl !important;
    }
    
    .stTextInput > div > div > input {
        text-align: right !important;
        direction: rtl !important;
    }
    
    .stNumberInput > div > div > input {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* تحسين محاذاة العناوين */
    h1, h2, h3, p {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* تحسين محاذاة مربعات الاختيار */
    .stCheckbox > label {
        direction: rtl !important;
        text-align: right !important;
        display: flex !important;
        justify-content: flex-end !important;
        flex-direction: row-reverse !important;
    }
    
    .stCheckbox > label > div {
        margin-left: 0.5rem !important;
        margin-right: 0 !important;
    }
    
    /* تحسين بطاقة النتائج */
    .result-card {
        direction: rtl !important;
        text-align: right !important;
        padding: 2rem !important;
    }
    
    /* تحسين القوائم */
    .details-list {
        padding-right: 0 !important;
        padding-left: 0 !important;
    }
    
    .details-list li {
        text-align: right !important;
        padding-right: 0 !important;
    }
    
    /* تحسين صفوف الأسعار */
    .price-row {
        flex-direction: row-reverse !important;
    }
    
    /* تحسين العناوين الرئيسية */
    .main-title {
        text-align: right !important;
        margin-right: 0 !important;
        padding-right: 0 !important;
    }
    
    .section-title {
        text-align: right !important;
        padding-right: 1rem !important;
        margin-right: 0 !important;
    }
    
    /* تحسين الأزرار */
    .stButton {
        text-align: right !important;
    }
    
    /* تحسين النصوص */
    .stMarkdown {
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* تحسين المدخلات الرقمية */
    input[type="number"] {
        direction: ltr !important;
        text-align: left !important;
    }
    
    /* تحسين التذييل */
    .element-container {
        direction: rtl !important;
    }
    
    /* تحسين الهوامش */
    .block-container {
        padding-right: 5% !important;
        padding-left: 5% !important;
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .block-container {
            padding-right: 2% !important;
            padding-left: 2% !important;
        }
        
        .result-card {
            padding: 1rem !important;
        }
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
    
    current_time = datetime.now() + timedelta(hours=3)
    
    result_html = f"""
        <div class="result-card">
            <div class="section-title">📄 تفاصيل الصفحات</div>
            <div class="section-content">
                <ul class="details-list">
                    {"<li>• " + str(colored_pages) + " صفحة ملونة</li>" if colored_pages > 0 else ""}
                    {"<li>• " + str(bw_pages) + " صفحة أبيض وأسود</li>" if bw_pages > 0 else ""}
                </ul>
            </div>
            
            {f'''
            <div class="section-title">✨ الإضافات المطلوبة</div>
            <div class="section-content">
                <ul class="details-list">
                    {"".join(f"<li>• {extra}</li>" for extra in extras)}
                </ul>
            </div>
            ''' if extras else ""}
            
            <div class="section-title">💰 التفاصيل المالية</div>
            <div class="section-content">
                <div class="price-row">
                    <span>التكلفة قبل التقريب:</span>
                    <span class="price">{total_cost:,} دينار</span>
                </div>
                <div class="price-row final-price">
                    <span>التكلفة النهائية:</span>
                    <span class="price">{rounded_cost:,} دينار</span>
                </div>
            </div>
        </div>
    """
    
    st.markdown(result_html, unsafe_allow_html=True)

def main():
    # عرض العنوان الرئيسي
    st.markdown("""
        <div class="main-title">
            حاسبة تكلفة الطباعة
            <div class="subtitle">
                احسب تكلفة طباعتك بسهولة وسرعة
            </div>
        </div>
    """, unsafe_allow_html=True)

    # استخدام الأعمدة لتخطيط أفضل
    col1, col2 = st.columns(2)

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

    # عرض النتائج
    generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)

    # زر النسخ
    st.markdown(f"""
        <div class="copy-button-container">
            <button class="modern-copy-button" onclick="copyToClipboard()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18">
                    <path fill="currentColor" d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                </svg>
                نسخ النتائج
            </button>
            <textarea id="summary-text" style="position: absolute; left: -9999px;">{generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)}</textarea>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
