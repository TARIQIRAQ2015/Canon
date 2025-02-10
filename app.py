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

# تحسين الأنماط للغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

    /* إعدادات عامة */
    .stApp {
        font-family: 'Tajawal', sans-serif !important;
    }

    /* إخفاء العناصر غير المرغوبة */
    #MainMenu, header, footer, [data-testid="stToolbar"],
    .css-1544g2n.e1fqkh3o4, [data-testid="stSidebar"] {
        display: none !important;
    }

    /* تحسين المحتوى الرئيسي */
    .main .block-container {
        padding: 2rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        direction: rtl !important;
    }

    /* تحسين العناوين */
    h1, h2, h3, .stMarkdown p {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Tajawal', sans-serif !important;
    }

    /* تحسين حقول الإدخال */
    .stTextInput, .stNumberInput, .stSelectbox {
        direction: rtl !important;
    }

    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        text-align: right !important;
        padding-right: 1rem !important;
    }

    /* تحسين مربعات الاختيار */
    .stCheckbox {
        direction: rtl !important;
    }
    
    .stCheckbox > label {
        flex-direction: row-reverse !important;
        justify-content: flex-end !important;
    }

    /* تحسين بطاقة النتائج */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        direction: rtl !important;
        text-align: right !important;
    }

    /* تحسين صفوف الأسعار */
    .price-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        direction: rtl !important;
    }

    .price {
        font-weight: bold;
        color: #64ffda;
        font-family: 'Tajawal', sans-serif !important;
    }

    /* تحسين القوائم */
    .details-list {
        list-style-position: inside;
        padding-right: 0 !important;
    }

    .details-list li {
        text-align: right !important;
        margin: 0.5rem 0;
    }

    /* تحسين الأزرار */
    .stButton > button {
        width: 100% !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 500 !important;
    }

    /* تحسين التذييل */
    .footer {
        direction: rtl !important;
        text-align: center !important;
        margin-top: 2rem !important;
    }

    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }
        
        .result-card {
            padding: 1rem !important;
        }
        
        .price-row {
            flex-direction: column !important;
            align-items: flex-start !important;
        }
    }

    /* تنسيق العنوان الرئيسي */
    .main-header {
        background: linear-gradient(to left, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: right;
        direction: rtl;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, 
            rgba(100,255,218,0.1) 0%,
            rgba(0,0,0,0) 70%);
        z-index: 0;
    }

    .title-container {
        position: relative;
        z-index: 1;
    }

    .main-title {
        font-family: 'Tajawal', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    .subtitle {
        font-family: 'Tajawal', sans-serif;
        font-size: 1.2rem;
        color: rgba(255,255,255,0.8);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .features-list {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .feature-item {
        background: rgba(255,255,255,0.05);
        padding: 0.7rem 1.2rem;
        border-radius: 8px;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1rem;
        color: rgba(255,255,255,0.9);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }

    .feature-item:hover {
        transform: translateY(-2px);
        background: rgba(255,255,255,0.1);
    }

    /* تنسيق العناوين الفرعية */
    .section-header {
        background: linear-gradient(to left, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
        border-radius: 10px;
        padding: 1rem 1.5rem;
        margin: 2rem 0 1rem 0;
        font-family: 'Tajawal', sans-serif;
        font-size: 1.5rem;
        color: #ffffff;
        position: relative;
        overflow: hidden;
    }

    .section-header::after {
        content: '';
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        width: 4px;
        background: #64ffda;
        border-radius: 2px;
    }

    @media (max-width: 768px) {
        .main-title {
            font-size: 1.8rem;
        }

        .subtitle {
            font-size: 1rem;
        }

        .feature-item {
            font-size: 0.9rem;
        }

        .section-header {
            font-size: 1.3rem;
            padding: 0.8rem 1.2rem;
        }
    }

    /* تنسيق قسم الإدخال */
    .input-section {
        background: rgba(255,255,255,0.03);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
    }

    /* تنسيق عناوين الأقسام */
    .section-title {
        font-family: 'Tajawal', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1.5rem;
        padding-right: 1rem;
        position: relative;
        display: flex;
        align-items: center;
    }

    .section-title::before {
        content: '';
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 100%;
        background: linear-gradient(to bottom, #64ffda, #48bb8d);
        border-radius: 2px;
    }

    /* تنسيق القوائم */
    .options-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }

    .option-item {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }

    .option-item:hover {
        background: rgba(255,255,255,0.08);
        transform: translateY(-2px);
    }

    /* تنسيق حقول الإدخال */
    .stNumberInput > div > div {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        padding: 0.5rem !important;
    }

    .stNumberInput > div > div:focus-within {
        border-color: #64ffda !important;
        box-shadow: 0 0 0 1px #64ffda !important;
    }

    /* تنسيق مربعات الاختيار */
    .stCheckbox > label {
        background: rgba(255,255,255,0.05);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }

    .stCheckbox > label:hover {
        background: rgba(255,255,255,0.08);
        transform: translateY(-2px);
    }

    /* تنسيق النتائج */
    .result-section {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }

    .result-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .result-item:last-child {
        border-bottom: none;
    }

    .result-label {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.9);
    }

    .result-value {
        font-size: 1.2rem;
        font-weight: 600;
        color: #64ffda;
    }

    /* تنسيق الأزرار */
    .stButton > button {
        background: linear-gradient(45deg, #64ffda, #48bb8d) !important;
        color: #1a1a2e !important;
        font-weight: 600 !important;
        padding: 0.8rem 2rem !important;
        border: none !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(100,255,218,0.2) !important;
    }

    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .options-grid {
            grid-template-columns: 1fr;
        }

        .section-title {
            font-size: 1.2rem;
        }

        .result-item {
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
    # تجميع الإضافات المطلوبة
    extras = []
    if cover: extras.append("تصميم غلاف")
    if carton: extras.append("كرتون فاخر")
    if nylon: extras.append("تغليف نايلون")
    if ruler: extras.append("مسطرة خاصة")

    # إنشاء HTML للنتائج مع تنسيق محسن
    result_html = f"""
        <div class="result-container">
            <div class="result-section">
                <div class="result-header">
                    <span class="header-icon">📋</span>
                    <span class="header-text">تفاصيل الطلب</span>
                </div>
                <div class="result-content">
                    <div class="detail-row">• عدد الصفحات الملونة: {colored_pages} صفحة</div>
                    <div class="detail-row">• عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة</div>
                </div>
            </div>
    """
    
    # إضافة الإضافات إذا وجدت
    if extras:
        result_html += f"""
            <div class="result-section">
                <div class="result-header">
                    <span class="header-icon">✨</span>
                    <span class="header-text">الإضافات المطلوبة</span>
                </div>
                <div class="result-content">
                    {"".join(f'<div class="detail-row">• {extra}</div>' for extra in extras)}
                </div>
            </div>
        """
    
    # إضافة التفاصيل المالية
    result_html += f"""
            <div class="result-section">
                <div class="result-header">
                    <span class="header-icon">💰</span>
                    <span class="header-text">التفاصيل المالية</span>
                </div>
                <div class="result-content">
                    <div class="cost-row">
                        <div class="cost-label">التكلفة قبل التقريب:</div>
                        <div class="cost-value">{total_cost:,} دينار</div>
                    </div>
                    <div class="cost-row final">
                        <div class="cost-label">التكلفة النهائية:</div>
                        <div class="cost-value">{rounded_cost:,} دينار</div>
                    </div>
                </div>
            </div>
        </div>
    """

    # إضافة الأنماط المحسنة
    st.markdown("""
        <style>
        .result-container {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }
        
        .result-section {
            margin-bottom: 2rem;
        }
        
        .result-section:last-child {
            margin-bottom: 0;
        }
        
        .result-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.2rem;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 1rem;
            padding-right: 1rem;
            border-right: 4px solid #64ffda;
        }
        
        .header-icon {
            font-size: 1.4rem;
        }
        
        .header-text {
            margin-right: 0.5rem;
        }
        
        .result-content {
            padding: 0.5rem 1rem;
        }
        
        .detail-row {
            padding: 0.5rem 0;
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
        }
        
        .cost-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            color: rgba(255,255,255,0.9);
        }
        
        .cost-row:last-child {
            border-bottom: none;
        }
        
        .cost-label {
            font-size: 1.1rem;
        }
        
        .cost-value {
            font-weight: bold;
            color: #64ffda;
            font-size: 1.2rem;
        }
        
        .cost-row.final .cost-value {
            color: #4CAF50;
            font-size: 1.3rem;
        }
        
        @media (max-width: 768px) {
            .result-container {
                padding: 1rem;
            }
            
            .cost-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # عرض النتائج
    st.markdown(result_html, unsafe_allow_html=True)
    return None

def main():
    # إضافة العنوان الرئيسي
    st.markdown("""
        <div class="main-header">
            <div class="title-container">
                <h1 class="main-title">حاسبة تكلفة الطباعة الذكية 🖨️</h1>
                <p class="subtitle">حاسبة متطورة لتقدير تكاليف الطباعة بدقة عالية مع دعم كامل للإضافات والخيارات المتنوعة</p>
                <div class="features-list">
                    <div class="feature-item">✨ دقة في الحساب</div>
                    <div class="feature-item">🚀 سرعة في الأداء</div>
                    <div class="feature-item">💡 خيارات متعددة</div>
                    <div class="feature-item">📊 تقارير مفصلة</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # قسم إدخال البيانات
    st.markdown('<div class="section-title">📝 تفاصيل الطباعة</div>', unsafe_allow_html=True)
    
    # إضافة قسم الإدخال مع التصميم المحسن
    st.markdown("""
        <div class="input-section">
            <div class="section-title">📄 عدد الصفحات</div>
        </div>
    """, unsafe_allow_html=True)
    
    # حقول الإدخال
    colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    # قسم الخيارات الإضافية
    st.markdown('<div class="section-title">✨ الخيارات الإضافية</div>', unsafe_allow_html=True)
    
    # تنظيم الخيارات في شكل شبكة
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("تصميم غلاف")
        carton = st.checkbox("كرتون فاخر")
    with col2:
        nylon = st.checkbox("تغليف نايلون")
        ruler = st.checkbox("مسطرة خاصة")
    
    # دالة حساب التكلفة
    def calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler):
        colored_cost = colored_pages * 50
        bw_cost = bw_pages * 25
        
        extras_cost = 0
        if cover: extras_cost += 1000
        if carton: extras_cost += 500
        if nylon: extras_cost += 250
        if ruler: extras_cost += 150
        
        return colored_cost + bw_cost + extras_cost
    
    # زر الحساب مع تصميم محسن
    st.markdown('<div style="margin: 2rem 0;"></div>', unsafe_allow_html=True)
    if st.button("حساب التكلفة", key="calculate_button"):
        total_cost = calculate_total_cost(colored_pages, bw_pages, cover, carton, nylon, ruler)
        rounded_cost = round(total_cost / 100) * 100
        
        # عرض النتائج
        generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)

if __name__ == "__main__":
    main()
