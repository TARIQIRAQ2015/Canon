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

    .summary-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .summary-header {
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #64ffda;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .summary-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .summary-label {
        color: rgba(255,255,255,0.9);
    }

    .summary-value {
        color: #64ffda;
        font-weight: bold;
    }

    .timestamp {
        color: #64ffda;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def round_to_nearest_250(amount):
    """تقريب المبلغ لأقرب 250 دينار"""
    return round(amount / 250) * 250

def get_iraq_time():
    """الحصول على الوقت في العراق"""
    iraq_tz = pytz.timezone('Asia/Baghdad')
    return datetime.now(iraq_tz).strftime("%Y-%m-%d %I:%M %p")

def calculate_cost(colored_pages, bw_pages):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50
    bw_cost = bw_pages * 35
    return colored_cost + bw_cost

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
        rounded_cost = round_to_nearest_250(total_cost)
        current_time = get_iraq_time()
        
        # عرض النتائج
        st.markdown(f"""
            <div class="summary-card">
                <div class="timestamp">⏰ {current_time}</div>
                <div class="summary-header">
                    <span>📝 ملخص الطباعة</span>
                </div>
                
                <div class="summary-row">
                    <span class="summary-label">عدد الصفحات الملونة</span>
                    <span class="summary-value">{colored_pages:,} صفحة</span>
                </div>
                <div class="summary-row">
                    <span class="summary-label">تكلفة الصفحات الملونة</span>
                    <span class="summary-value">{colored_pages * 50:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span class="summary-label">عدد الصفحات بالأبيض والأسود</span>
                    <span class="summary-value">{bw_pages:,} صفحة</span>
                </div>
                <div class="summary-row">
                    <span class="summary-label">تكلفة الصفحات بالأبيض والأسود</span>
                    <span class="summary-value">{bw_pages * 35:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span class="summary-label">المبلغ الإجمالي</span>
                    <span class="summary-value">{total_cost:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span class="summary-label">المبلغ النهائي (مقرب لأقرب 250 دينار)</span>
                    <span class="final-cost">{rounded_cost:,} دينار</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # نص النسخ
        copy_text = f"""
ملخص الطباعة:
=============
⏰ وقت الحساب: {current_time}

تفاصيل الطلب:
- عدد الصفحات الملونة: {colored_pages:,} صفحة ({colored_pages * 50:,} دينار)
- عدد الصفحات بالأبيض والأسود: {bw_pages:,} صفحة ({bw_pages * 35:,} دينار)

التكاليف:
- المبلغ الإجمالي: {total_cost:,} دينار
- المبلغ النهائي (مقرب): {rounded_cost:,} دينار"""

        if st.button("نسخ النتائج 📋"):
            st.code(copy_text)
            st.success("تم نسخ النتائج! يمكنك لصقها في أي مكان.")

if __name__ == "__main__":
    main()
