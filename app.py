import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json
import math

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
        background: linear-gradient(135deg, #0F172A, #1E293B) !important;
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
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin: 0 auto;
        max-width: 800px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* تنسيق العنوان */
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(120deg, #60A5FA, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2.5rem;
    }

    /* تنسيق النتيجة */
    .result {
        background: linear-gradient(145deg, rgba(37, 99, 235, 0.1), rgba(99, 102, 241, 0.1));
        backdrop-filter: blur(5px);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: #60A5FA;
        border: 1px solid rgba(96, 165, 250, 0.2);
        transition: all 0.3s ease;
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
        background: rgba(30, 41, 59, 0.6);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 1.5rem;
        text-align: right;
        font-size: 1.2rem;
        line-height: 1.8;
        border: 1px solid rgba(96, 165, 250, 0.2);
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
    
    summary = f"""خلاصة الطلب:
• عدد الصفحات الملونة: {colored_pages} صفحة
• عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة"""

    if extras:
        summary += f"\n• الإضافات المطلوبة: {' + '.join(extras)}"
    
    summary += f"""
• التكلفة قبل التقريب: {total_cost:,} دينار
• التكلفة النهائية بعد التقريب: {rounded_cost:,} دينار"""
    
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
    
    # زر نسخ الملخص
    if st.button("نسخ الملخص", key="copy_button", type="primary"):
        st.markdown(f"""
            <div class="copy-container">
                <textarea id="summary-text" style="position: absolute; left: -9999px;">{summary}</textarea>
                <script>
                    var textArea = document.getElementById('summary-text');
                    textArea.select();
                    try {{
                        navigator.clipboard.writeText(textArea.value).then(function() {{
                            console.log('تم النسخ بنجاح');
                        }});
                    }} catch (err) {{
                        console.error('فشل النسخ:', err);
                    }}
                </script>
            </div>
        """, unsafe_allow_html=True)
        st.success("✨ تم نسخ الملخص بنجاح!")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
