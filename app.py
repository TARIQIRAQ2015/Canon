import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta
import pytz

# تعيين إعدادات الصفحة مع دعم اللغة العربية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إضافة الأنماط الأساسية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    * {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
    }

    /* إخفاء العناصر غير المطلوبة */
    #MainMenu, header, footer {display: none !important;}
    
    .main {
        padding: 2rem;
    }
    
    .stApp {
        background-color: #1a1a2e;
    }

    /* تنسيق البطاقات */
    .card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* تنسيق العناوين */
    .title {
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* تنسيق النتائج */
    .result-item {
        display: flex;
        justify-content: space-between;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .result-value {
        color: #64ffda;
        font-weight: bold;
    }

    .result-card {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }

    .result-title {
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .result-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        color: white;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .final-cost {
        color: #4CAF50 !important;
        font-size: 1.2rem;
    }

    .copy-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
    }

    .timestamp {
        color: #64ffda;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }

    .section-title {
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .detail-row {
        display: flex;
        justify-content: space-between;
        padding: 12px 0;
        color: white;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .main-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .card-header {
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #64ffda;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .info-label {
        color: rgba(255,255,255,0.9);
    }

    .info-value {
        color: #64ffda;
        font-weight: bold;
    }

    .final-value {
        color: #4CAF50 !important;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

def round_to_nearest_currency(amount):
    """تقريب المبلغ لأقرب فئة عملة متداولة"""
    currency_denominations = [250, 500, 1000]
    min_diff = float('inf')
    rounded_amount = amount
    
    for denom in currency_denominations:
        quotient = round(amount / denom)
        rounded = quotient * denom
        diff = abs(amount - rounded)
        if diff < min_diff:
            min_diff = diff
            rounded_amount = rounded
    
    return rounded_amount

def get_iraq_time():
    """الحصول على الوقت في العراق"""
    iraq_tz = pytz.timezone('Asia/Baghdad')
    return datetime.now(iraq_tz).strftime("%Y-%m-%d %I:%M %p")

def calculate_cost(colored_pages, bw_pages):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50
    bw_cost = bw_pages * 35
    total = colored_cost + bw_cost
    return total

def main():
    # العنوان الرئيسي
    st.markdown("""
        <div class="card">
            <h1 style="color: white; text-align: center; font-size: 2rem; margin-bottom: 1rem;">
                🖨️ حاسبة تكلفة الطباعة
            </h1>
            <p style="color: rgba(255,255,255,0.8); text-align: center;">
                حاسبة متطورة لتقدير تكاليف الطباعة بدقة عالية
            </p>
        </div>
    """, unsafe_allow_html=True)

    # قسم الإدخال
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # عدد الصفحات
        colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
        
        # الإضافات
        st.markdown('<div class="title">✨ الإضافات</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            cover = st.checkbox("تصميم غلاف")
            carton = st.checkbox("كرتون فاخر")
        with col2:
            nylon = st.checkbox("تغليف نايلون")
            ruler = st.checkbox("مسطرة خاصة")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # حساب وعرض النتائج
    if st.button("حساب التكلفة", type="primary"):
        total_cost = calculate_cost(colored_pages, bw_pages)
        rounded_cost = round_to_nearest_currency(total_cost)
        current_time = get_iraq_time()
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
                <div class="main-card">
                    <div class="timestamp">⏰ {current_time}</div>
                    <div class="card-header">📊 ملخص الطلب والتكلفة</div>
                    
                    <div class="info-row">
                        <span class="info-label">عدد الصفحات الملونة</span>
                        <span class="info-value">{colored_pages} صفحة</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">تكلفة الصفحات الملونة</span>
                        <span class="info-value">{colored_pages * 50:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">عدد الصفحات بالأبيض والأسود</span>
                        <span class="info-value">{bw_pages} صفحة</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">تكلفة الصفحات بالأبيض والأسود</span>
                        <span class="info-value">{bw_pages * 35:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">التكلفة قبل التقريب</span>
                        <span class="info-value">{total_cost:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">التكلفة النهائية</span>
                        <span class="final-value">{rounded_cost:,} دينار</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # نص النسخ
        copy_text = f"""
تفاصيل الطلب:
=============
⏰ {current_time}
عدد الصفحات الملونة: {colored_pages} صفحة
عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة
التكلفة قبل التقريب: {total_cost:,} دينار
التكلفة النهائية: {rounded_cost:,} دينار"""

        if st.button("نسخ النتائج 📋"):
            st.code(copy_text)
            st.success("تم نسخ النتائج بنجاح! يمكنك لصقها في أي مكان.")

if __name__ == "__main__":
    main()
