import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math
from datetime import datetime, timedelta
import pytz

# تكوين الصفحة يجب أن يكون أول شيء
st.set_page_config(page_title="حاسبة تكلفة الطباعة", page_icon="🖨️", layout="wide")

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
        color: white;
    }

    /* تنسيق البطاقات */
    .card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
    }

    /* تنسيق العناوين */
    .card-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px solid #64ffda;
        padding-bottom: 10px;
        color: #64ffda;
    }

    .info {
        margin: 12px 0;
        font-size: 1.1rem;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .highlight {
        color: #64ffda;
        font-weight: bold;
    }

    .final-cost {
        color: #4CAF50;
        font-size: 1.4rem;
        font-weight: bold;
    }

    .copy-button {
        position: fixed;
        top: 70px;
        left: 20px;
        padding: 10px 20px;
        background: #64ffda;
        color: #1a1a2e;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        z-index: 999;
    }

    .copy-button:hover {
        background: #4CAF50;
        color: white;
    }

    .extras-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }

    .section-title {
        color: #64ffda;
        font-size: 1.2rem;
        margin-bottom: 10px;
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

def calculate_cost(colored_pages, bw_pages, extras):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50
    bw_cost = bw_pages * 35
    extras_cost = sum(250 for x in extras if x)  # كل إضافة بـ 250 دينار
    return colored_cost + bw_cost + extras_cost

def main():
    st.title("🖨️ حاسبة تكلفة الطباعة")
    
    # إدخال البيانات
    col1, col2 = st.columns(2)
    
    with col1:
        colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    with col2:
        st.markdown('<div class="extras-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎁 الإضافات</div>', unsafe_allow_html=True)
        carton = st.checkbox("كرتون ملون (250 دينار)")
        holder = st.checkbox("حاملة كتب (250 دينار)")
        nylon = st.checkbox("نايلون شفاف (250 دينار)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if colored_pages > 0 or bw_pages > 0:
        # حساب التكاليف
        extras = [carton, holder, nylon]
        colored_cost = colored_pages * 50
        bw_cost = bw_pages * 35
        extras_cost = sum(250 for x in extras if x)
        total_cost = colored_cost + bw_cost + extras_cost
        rounded_cost = round_to_nearest_250(total_cost)
        current_time = get_iraq_time()

        # إنشاء نص النسخ
        copy_text = f"""
ملخص الطباعة:
=============
⏰ وقت الحساب: {current_time}

تفاصيل الطلب:
- عدد الصفحات الملونة: {colored_pages:,} صفحة ({colored_cost:,} دينار)
- عدد الصفحات بالأبيض والأسود: {bw_pages:,} صفحة ({bw_cost:,} دينار)

الإضافات المختارة:
{' - كرتون ملون (250 دينار)' if carton else ''}
{' - حاملة كتب (250 دينار)' if holder else ''}
{' - نايلون شفاف (250 دينار)' if nylon else ''}
تكلفة الإضافات: {extras_cost:,} دينار

التكاليف:
- المبلغ الإجمالي: {total_cost:,} دينار
- المبلغ النهائي (مقرب): {rounded_cost:,} دينار"""

        # زر النسخ
        st.markdown(
            f'<button class="copy-button" onclick="navigator.clipboard.writeText(`{copy_text}`)">'
            '📋 نسخ النتائج</button>',
            unsafe_allow_html=True
        )

        # عرض النتائج
        st.markdown(f"""
            <div class="card">
                <div class="card-header">📝 ملخص الطباعة</div>
                <div class="info">⏰ وقت الحساب: <span class="highlight">{current_time}</span></div>
                <div class="info">عدد الصفحات الملونة: <span class="highlight">{colored_pages:,} صفحة</span></div>
                <div class="info">تكلفة الصفحات الملونة: <span class="highlight">{colored_cost:,} دينار</span></div>
                <div class="info">عدد الصفحات بالأبيض والأسود: <span class="highlight">{bw_pages:,} صفحة</span></div>
                <div class="info">تكلفة الصفحات بالأبيض والأسود: <span class="highlight">{bw_cost:,} دينار</span></div>
                <div class="info">تكلفة الإضافات: <span class="highlight">{extras_cost:,} دينار</span></div>
                <div class="info">المبلغ الإجمالي: <span class="highlight">{total_cost:,} دينار</span></div>
                <div class="info">المبلغ النهائي (مقرب لأقرب 250 دينار): <span class="final-cost">{rounded_cost:,} دينار</span></div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
