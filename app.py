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
    
    /* إخفاء الشريط الجانبي والعناصر غير المرغوب فيها */
    .css-1d391kg, .css-1p05t8e, .css-r698ls, .css-18e3th9 {
        padding: 0 1rem !important;
    }
    
    /* إخفاء زر فتح الشريط الجانبي */
    .css-14xtw13 {
        display: none !important;
    }
    
    /* إخفاء الشريط الجانبي نفسه */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* إخفاء جميع العناصر غير المرغوب فيها */
    #MainMenu, header, footer, [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* الأنماط الأساسية مع الخلفية المتحركة */
    .stApp {
        background: linear-gradient(135deg, 
            #1a1a2e,
            #16213e,
            #0f3460,
            #162447
        );
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        color: #e2e2e2;
    }
    
    /* تأثير الخلفية المتحركة */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* العنوان الرئيسي */
    .main-title {
        font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
        font-weight: bold !important;
        text-align: center !important;
        margin: 1rem 0 !important;
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    
    .subtitle {
        font-size: 0.7em;
        text-align: center;
        margin-top: 0.5em;
        color: #e2e2e2;
        opacity: 0.9;
    }
    
    /* تحسين عناصر الإدخال مع تأثيرات الشفافية */
    .stSelectbox > div > div,
    .stNumberInput > div > div {
        background: rgba(30, 37, 48, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    /* تأثيرات التحويم */
    .stSelectbox > div > div:hover,
    .stNumberInput > div > div:hover {
        background: rgba(22, 27, 37, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* تحسين الجداول */
    .stTable th, .stTable td {
        text-align: right !important;
        direction: rtl !important;
        padding: 0.5rem !important;
    }
    
    /* تحسين ملخص النتائج مع تأثير الشفافية */
    pre {
        background: rgba(20, 30, 60, 0.8) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease;
    }
    
    pre:hover {
        border-color: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    /* تحسين الأزرار مع تأثيرات الشفافية */
    .stButton > button {
        background: linear-gradient(135deg, 
            rgba(255,255,255,0.1),
            rgba(255,255,255,0.05)
        ) !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, 
            rgba(255,255,255,0.15),
            rgba(255,255,255,0.1)
        ) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* تحسين الروابط الاجتماعية */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin: 30px 0;
    }
    
    .social-links img {
        width: 36px;
        height: 36px;
        transition: all 0.3s ease;
    }
    
    .social-links img:hover {
        transform: translateY(-3px);
        filter: brightness(1.2);
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main-title {
            font-size: 1.5rem !important;
        }
        
        .stSelectbox > div > div,
        .stNumberInput > div > div {
            padding: 0.6rem !important;
        }
        
        .social-links img {
            width: 28px;
            height: 28px;
        }
    }
    
    /* تصميم بطاقة النتائج */
    .result-card {
        background: rgba(20, 30, 60, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* رأس البطاقة */
    .result-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .result-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #fff;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    
    .result-datetime {
        display: flex;
        gap: 1rem;
        color: rgba(255, 255, 255, 0.8);
    }
    
    /* أقسام النتائج */
    .result-section {
        margin: 1rem 0;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .result-section:hover {
        background: rgba(255, 255, 255, 0.08);
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #fff;
        margin-bottom: 0.5rem;
    }
    
    .section-content {
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
    }
    
    /* تنسيق الأسعار */
    .price-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0.5rem 0;
    }
    
    .price {
        font-weight: bold;
        color: #4CAF50;
    }
    
    .final-price .price {
        font-size: 1.2rem;
        color: #64ffda;
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .result-header {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
        }
        
        .result-datetime {
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .price-row {
            flex-direction: column;
            text-align: center;
            gap: 0.5rem;
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

    # تجميع الإضافات المطلوبة
    extras = []
    if cover: extras.append("تصميم غلاف")
    if carton: extras.append("كرتون فاخر")
    if nylon: extras.append("تغليف نايلون")
    if ruler: extras.append("مسطرة خاصة")

    # إنشاء نص النتائج بتنسيق جديد
    st.markdown(f"""
        <div class="result-card">
            <div class="result-header">
                <div class="result-title">ملخص الطلب</div>
                <div class="result-datetime">
                    <span>📅 {date_str}</span>
                    <span>🕒 {time_str}</span>
                </div>
            </div>
            
            <div class="result-section">
                <div class="section-title">📄 تفاصيل الصفحات</div>
                <div class="section-content">
                    {f"• {colored_pages} صفحة ملونة" if colored_pages else ""}
                    {f"• {bw_pages} صفحة أبيض وأسود" if bw_pages else ""}
                </div>
            </div>
            
            {f'''
            <div class="result-section">
                <div class="section-title">✨ الإضافات المطلوبة</div>
                <div class="section-content">
                    • {' + '.join(extras)}
                </div>
            </div>
            ''' if extras else ''}
            
            <div class="result-section">
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
        </div>
    """, unsafe_allow_html=True)

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
