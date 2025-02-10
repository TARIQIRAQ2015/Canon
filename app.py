import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta

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
    
    /* إخفاء العناصر غير المرغوب فيها بشكل صحيح */
    #MainMenu, header, footer, [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* تحسين الاتجاه والمحاذاة للغة العربية */
    .stApp, .main, [data-testid="stMarkdownContainer"], .element-container {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* تحسين تنسيق العنوان والنصوص */
    .main-title {
        font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
        text-align: center !important;
        margin: 1rem 0 !important;
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    
    /* تحسين القوائم المنسدلة */
    .stSelectbox > div > div {
        background: rgba(30, 37, 48, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px);
        padding: 0.8rem !important;
        font-size: 1rem !important;
    }
    
    /* تحسين حقول الإدخال */
    .stNumberInput > div > div > input {
        text-align: right !important;
        direction: rtl !important;
        font-size: 1rem !important;
    }
    
    /* تحسين الجداول */
    .stTable th, .stTable td {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* تحسين ملخص النتائج */
    pre {
        direction: ltr !important;
        font-family: 'Courier New', monospace !important;
        background: rgba(20, 30, 60, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main-title {
            font-size: 1.5rem !important;
        }
        .stSelectbox > div > div {
            padding: 0.6rem !important;
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
    # تنسيق التاريخ والوقت حسب توقيت بغداد
    current_time = datetime.now() + timedelta(hours=3)
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%I:%M %p")
    
    extras = []
    if cover: extras.append("تصميم غلاف")
    if carton: extras.append("كرتون فاخر")
    if nylon: extras.append("تغليف نايلون")
    if ruler: extras.append("مسطرة خاصة")
    
    summary = f"""╔══════════════════════════════════════════════════════════════════╗
║                         ملخص النتائج ✨                         ║
╠══════════════════════════════════════════════════════════════════╣
║ 📅 التاريخ: {date_str}
║ ⏰ الوقت: {time_str}
╟──────────────────────────────────────────────────────────────────
║ 📄 تفاصيل الصفحات:
║ • عدد الصفحات الملونة: {colored_pages} صفحة
║ • عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة
"""

    if extras:
        summary += f"""╟──────────────────────────────────────────────────────────────────
║ ✨ الإضافات المطلوبة:
║ • {' + '.join(extras)}
"""
    
    summary += f"""╟──────────────────────────────────────────────────────────────────
║ 💰 التفاصيل المالية:
║ • التكلفة قبل التقريب: {total_cost:,} دينار
║ • التكلفة النهائية: {rounded_cost:,} دينار
╚══════════════════════════════════════════════════════════════════╝"""
    
    return summary

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
    summary = generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)
    st.markdown(f'<div class="summary">{summary}</div>', unsafe_allow_html=True)

    # زر النسخ
    st.markdown(f"""
        <div class="copy-button-container">
            <button class="modern-copy-button" onclick="copyToClipboard()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18">
                    <path fill="currentColor" d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                </svg>
                نسخ النتائج
            </button>
            <textarea id="summary-text" style="position: absolute; left: -9999px;">{summary}</textarea>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
