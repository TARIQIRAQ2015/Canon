import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta

# تحسين إعدادات الصفحة
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تحسين الأنماط مع دعم اللغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    /* الإعدادات الأساسية */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* إخفاء العناصر غير المرغوبة */
    #MainMenu, header, footer, [data-testid="stToolbar"],
    .css-1544g2n.e1fqkh3o4, [data-testid="stSidebar"],
    .css-r698ls.e8zbici2, .css-18e3th9.egzxvld2,
    .css-1dp5vir.e8zbici1, .css-14xtw13.e8zbici0,
    .css-eh5xgm.e1ewe7hr3, .viewerBadge_container__1QSob,
    .css-1aehpvj.euu6i2w0, .css-qrbaxs {
        display: none !important;
    }
    
    /* تحسين المحتوى الرئيسي */
    .main .block-container {
        padding: 2rem 3rem !important;
        max-width: 100% !important;
    }
    
    /* تنسيق بطاقة النتائج */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        direction: rtl;
        text-align: right;
    }
    
    /* تنسيق العناوين */
    .section-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #fff;
        margin-bottom: 1rem;
        border-right: 4px solid #64ffda;
        padding-right: 1rem;
    }
    
    /* تنسيق المحتوى */
    .section-content {
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    /* تنسيق الأسعار */
    .price-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .price {
        font-weight: bold;
        color: #64ffda;
        font-size: 1.1rem;
    }
    
    .final-price .price {
        font-size: 1.3rem;
        color: #4CAF50;
    }
    
    /* تحسين حقول الإدخال */
    .stNumberInput > div > div {
        direction: rtl !important;
        text-align: right !important;
    }
    
    .stSelectbox > div > div {
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* تحسين التفاصيل */
    .details-list {
        list-style: none;
        padding: 0;
    }
    
    .details-list li {
        padding: 0.5rem 0;
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }
        
        .result-card {
            padding: 1rem;
        }
        
        .price-row {
            flex-direction: column;
            align-items: flex-start;
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
    return ""

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
