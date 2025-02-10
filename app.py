import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta

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
    </style>
""", unsafe_allow_html=True)

def calculate_cost(colored_pages, bw_pages, cover, carton, nylon, ruler):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50  # 50 دينار للصفحة الملونة
    bw_cost = bw_pages * 35  # 35 دينار للصفحة الأبيض والأسود
    total = colored_cost + bw_cost
    if cover: total += 1000
    if carton: total += 500
    if nylon: total += 250
    if ruler: total += 150
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
        total_cost = calculate_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
        rounded_cost = round(total_cost / 100) * 100
        
        # عرض النتائج
        st.markdown("""
            <div class="result-card">
                <div class="result-title">📋 تفاصيل الطلب</div>
                <div class="result-row">
                    <span>عدد الصفحات الملونة:</span>
                    <span class="result-value">{} صفحة</span>
                </div>
                <div class="result-row">
                    <span>عدد الصفحات بالأبيض والأسود:</span>
                    <span class="result-value">{} صفحة</span>
                </div>
            </div>

            <div class="result-card">
                <div class="result-title">💰 التفاصيل المالية</div>
                <div class="result-row">
                    <span>تكلفة الصفحات الملونة:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>تكلفة الصفحات بالأبيض والأسود:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>التكلفة قبل التقريب:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>التكلفة النهائية:</span>
                    <span class="result-value final-cost">{:,} دينار</span>
                </div>
            </div>
        """.format(
            colored_pages,
            bw_pages,
            colored_pages * 50,
            bw_pages * 35,
            total_cost,
            rounded_cost
        ), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
