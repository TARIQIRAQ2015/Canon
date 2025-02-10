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

# تحديث الأنماط CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    /* إخفاء العناصر غير المرغوب فيها */
    #MainMenu, header, footer {
        visibility: hidden;
    }

    .stDeployButton {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    /* الأنماط الأساسية */
    .main {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .stApp {
        background: linear-gradient(135deg, #0A0F1E, #1A1F3F) !important;
        margin: 0 !important;
        padding: 1rem !important;
        direction: rtl !important;
    }

    /* تنسيق العنوان الرئيسي */
    .main-title {
        font-size: clamp(2rem, 4vw, 3rem) !important;
        font-weight: bold !important;
        text-align: center !important;
        margin-bottom: 0.5em !important;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(255,255,255,0.3);
        background: linear-gradient(120deg, #60A5FA, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px;
    }

    .subtitle {
        font-size: clamp(1rem, 2vw, 1.5rem);
        text-align: center;
        margin-top: 0.5em;
        color: #e2e2e2;
        opacity: 0.9;
        font-weight: normal;
    }

    /* تنسيق عناصر الإدخال */
    .stSelectbox, .stTextInput, .stNumberInput {
        direction: rtl !important;
    }

    .stSelectbox > div, .stTextInput > div, .stNumberInput > div {
        direction: rtl !important;
    }

    .stSelectbox select, .stTextInput input, .stNumberInput input {
        background: rgba(30, 41, 59, 0.8) !important;
        border: 2px solid rgba(96, 165, 250, 0.2) !important;
        border-radius: 10px !important;
        color: #E2E8F0 !important;
        font-size: clamp(1rem, 1.5vw, 1.2rem) !important;
        padding: 0.8rem !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* تنسيق الأزرار */
    .stButton {
        direction: rtl !important;
        text-align: right !important;
    }

    .stButton button {
        font-size: clamp(1rem, 1.5vw, 1.2rem) !important;
        padding: 10px 24px !important;
        border-radius: 12px !important;
        width: 100% !important;
        background: linear-gradient(135deg, #4F46E5, #6366F1) !important;
        color: white !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }

    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4) !important;
    }

    /* تنسيق الجداول */
    .stTable th, .stTable td {
        text-align: right !important;
        direction: rtl !important;
        font-size: clamp(0.9rem, 1.5vw, 1.1rem) !important;
    }

    thead tr th:first-child,
    tbody tr td:first-child {
        text-align: right !important;
    }

    /* تنسيق حاويات العناصر */
    [data-testid="stMarkdownContainer"] {
        direction: rtl !important;
        text-align: right !important;
    }

    .element-container {
        direction: rtl !important;
    }

    /* تحسينات للأجهزة المحمولة */
    @media (max-width: 768px) {
        .main-title {
            font-size: 1.8rem !important;
            padding: 10px;
        }

        .subtitle {
            font-size: 1rem;
        }

        .stButton button {
            padding: 8px 16px !important;
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
    date_time_str = current_time.strftime("%Y-%m-%d %I:%M %p")
    
    extras = []
    if cover: extras.append("تصميم غلاف")
    if carton: extras.append("كرتون فاخر")
    if nylon: extras.append("تغليف نايلون")
    if ruler: extras.append("مسطرة خاصة")
    
    summary = f"""╔══════════════════════════════════════════════════════════════════╗
║                         ملخص النتائج ✨                         ║
╠══════════════════════════════════════════════════════════════════╣
║ وقت الحساب ⏰: {date_time_str}
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

    # إنشاء وعرض الملخص
    summary = generate_summary(colored_pages, bw_pages, cover, carton, nylon, ruler, total_cost, rounded_cost)
    st.markdown(f"<div class='summary'>{summary}</div>", unsafe_allow_html=True)
    
    # زر النسخ الجديد
    st.markdown(f"""
        <div class="copy-button-container">
            <button class="modern-copy-button" onclick="copyToClipboard()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                </svg>
                نسخ النتائج
            </button>
            <textarea id="summary-text" style="position: absolute; left: -9999px;">{summary}</textarea>
            <script>
                function copyToClipboard() {{
                    var textArea = document.getElementById('summary-text');
                    textArea.select();
                    try {{
                        navigator.clipboard.writeText(textArea.value).then(function() {{
                            const streamlitDoc = window.parent.document;
                            const div = streamlitDoc.createElement('div');
                            div.innerHTML = `
                                <div class="stAlert success" style="
                                    padding: 16px;
                                    border-radius: 8px;
                                    margin-top: 16px;
                                    background: rgba(45, 212, 191, 0.1);
                                    border: 1px solid rgba(45, 212, 191, 0.2);
                                    color: #2DD4BF;">
                                    ✨ تم نسخ النتائج بنجاح!
                                </div>`;
                            streamlitDoc.body.appendChild(div);
                            setTimeout(() => div.remove(), 3000);
                        }});
                    }} catch (err) {{
                        console.error('فشل النسخ:', err);
                    }}
                }}
            </script>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
