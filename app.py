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
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Tajawal', sans-serif !important;
        background: linear-gradient(135deg, #0A0F1E, #1A1F3F) !important;
        color: #E2E8F0;
        direction: rtl;
        text-align: right;
        padding: 2rem;
    }

    /* إخفاء العناصر غير المرغوب فيها */
    header[data-testid="stHeader"], footer, #MainMenu {
        display: none !important;
    }

    /* تنسيق مربع الحاسبة */
    .calculator-box {
        background: rgba(20, 30, 60, 0.7);
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
                    inset 0 0 80px rgba(96, 165, 250, 0.1);
        margin: 0 auto;
        max-width: 850px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        position: relative;
        overflow: hidden;
    }

    .calculator-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(96, 165, 250, 0.1) 0%, transparent 50%);
        animation: glowAnimation 10s infinite linear;
    }

    @keyframes glowAnimation {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* تنسيق العنوان */
    .title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(120deg, #60A5FA, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 3rem;
        text-shadow: 0 0 30px rgba(96, 165, 250, 0.5);
    }

    /* تنسيق النتيجة */
    .result {
        background: linear-gradient(145deg, rgba(37, 99, 235, 0.1), rgba(99, 102, 241, 0.1));
        backdrop-filter: blur(10px);
        padding: 2.5rem;
        border-radius: 20px;
        margin-top: 2rem;
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #60A5FA;
        border: 2px solid rgba(96, 165, 250, 0.3);
        transition: all 0.4s ease;
        box-shadow: 0 0 30px rgba(96, 165, 250, 0.2);
    }

    .result:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }

    /* تنسيق عناصر الإدخال */
    .stNumberInput input {
        background: rgba(30, 41, 59, 0.8) !important;
        border: 2px solid rgba(96, 165, 250, 0.2) !important;
        border-radius: 10px !important;
        color: #E2E8F0 !important;
        font-size: 1.1rem !important;
        padding: 0.8rem !important;
        transition: all 0.3s ease !important;
    }

    .stNumberInput input:focus {
        border-color: #60A5FA !important;
        box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.2) !important;
    }

    /* تنسيق الأقسام */
    .section {
        background: rgba(30, 41, 59, 0.5);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }

    .section:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }

    /* تنسيق ملخص الطلب */
    .summary {
        background: rgba(20, 30, 60, 0.8);
        padding: 2.5rem;
        border-radius: 20px;
        margin-top: 2rem;
        text-align: right;
        font-family: monospace;
        font-size: 1.1rem;
        line-height: 1.8;
        border: 2px solid rgba(96, 165, 250, 0.3);
        white-space: pre;
        overflow-x: auto;
        color: #A5B4FC;
        box-shadow: 0 0 30px rgba(96, 165, 250, 0.1);
    }

    /* تنسيق زر النسخ */
    .stButton button {
        background: linear-gradient(135deg, #4F46E5, #6366F1) !important;
        color: white !important;
        padding: 0.8rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }

    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
        background: linear-gradient(135deg, #6366F1, #4F46E5) !important;
    }

    /* تنسيق أيقونة النسخ */
    .copy-icon {
        position: relative;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 10px 20px;
        background: linear-gradient(135deg, #4F46E5, #6366F1);
        border-radius: 12px;
        border: none;
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        gap: 8px;
        font-family: 'Tajawal', sans-serif;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }

    .copy-icon:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, #6366F1, #4F46E5);
    }

    .copy-icon svg {
        width: 20px;
        height: 20px;
        fill: currentColor;
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
    
    summary = f"""╔══════════════════ ملخص الطلب ══════════════════╗

║  📅 التاريخ: {date_str}
║  🕒 الوقت: {time_str}
║
║  📄 تفاصيل الصفحات:
║  • عدد الصفحات الملونة: {colored_pages} صفحة
║  • عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة
║
"""

    if extras:
        summary += f"""║  ✨ الإضافات المطلوبة:
║  • {' + '.join(extras)}
║
"""
    
    summary += f"""║  💰 التفاصيل المالية:
║  • التكلفة قبل التقريب: {total_cost:,} دينار
║  • التكلفة النهائية: {rounded_cost:,} دينار
║
╚══════════════════════════════════════════════════╝"""
    
    return summary

def main():
    st.markdown("<div class='calculator-box'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>حاسبة تكلفة الطباعة 🖨️</h1>", unsafe_allow_html=True)

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
    st.markdown(f"<div class='summary'>{summary.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
    
    # تحديث زر النسخ ليكون أيقونة
    st.markdown(f"""
        <div class="copy-container">
            <button class="copy-icon" onclick="copyToClipboard()">
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
                            // إظهار رسالة النجاح
                            const element = window.parent.document.querySelector('.stAlert');
                            if (!element) {{
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
                            }}
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
