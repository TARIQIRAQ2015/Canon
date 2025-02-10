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

# إضافة الأنماط المحسنة
st.markdown("""
    <style>
    /* إعادة تعيين كامل للصفحة */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* إخفاء جميع العناصر غير المرغوبة */
    #MainMenu, header, footer, [data-testid="stToolbar"],
    .css-1544g2n.e1fqkh3o4, [data-testid="stSidebar"],
    .css-r698ls.e8zbici2, .css-18e3th9.egzxvld2,
    .css-1dp5vir.e8zbici1, .css-14xtw13.e8zbici0 {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        visibility: hidden !important;
        z-index: -1 !important;
    }
    
    /* تحسين المحتوى الرئيسي */
    .main .block-container {
        max-width: 100% !important;
        width: 100% !important;
        padding: 2rem !important;
        margin: 0 !important;
    }
    
    /* تحسين الخلفية */
    .stApp {
        background: linear-gradient(135deg, 
            #1a1a2e,
            #16213e,
            #0f3460,
            #162447
        ) !important;
        background-size: 400% 400% !important;
        animation: gradient 15s ease infinite !important;
        min-height: 100vh !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden !important;
    }
    
    /* تحسين العناصر التفاعلية */
    .stButton > button {
        width: 100% !important;
        padding: 0.75rem !important;
        border-radius: 10px !important;
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    /* تحسين حقول الإدخال */
    .stTextInput > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 0.5rem !important;
        color: white !important;
    }
    
    /* تحسين النصوص */
    .stMarkdown {
        color: white !important;
    }
    
    /* تأثير الخلفية المتحركة */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }
        
        .stButton > button {
            padding: 0.5rem !important;
        }
    }
    
    /* تحسين الجداول */
    .stTable {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }
    
    .stTable td {
        background: transparent !important;
        border: none !important;
        color: white !important;
    }
    
    /* تحسين التحديد */
    ::selection {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
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
