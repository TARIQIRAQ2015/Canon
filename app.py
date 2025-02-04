import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Cairo', sans-serif !important;
        background: linear-gradient(145deg, #0B1120 0%, #1E293B 100%);
        color: #E2E8F0;
        padding: 0;
        margin: 0;
    }
    
    /* تنسيق الهيدر */
    .header {
        background: linear-gradient(to right, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
        padding: 3rem 2rem;
        margin: -6rem -4rem 2rem -4rem;
        border-bottom: 2px solid rgba(96, 165, 250, 0.2);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    /* تأثيرات الخلفية المتحركة */
    .header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(56, 189, 248, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 50%);
        animation: pulse 8s ease-in-out infinite alternate;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.5; }
        100% { transform: scale(1.2); opacity: 0.8; }
    }
    
    /* تنسيق العنوان الرئيسي */
    .title-container {
        position: relative;
        z-index: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
    
    .title-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .title {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(120deg, 
            #60A5FA 0%, 
            #3B82F6 25%, 
            #2563EB 50%, 
            #60A5FA 75%, 
            #3B82F6 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 8s linear infinite;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        text-shadow: 
            0 0 10px rgba(96, 165, 250, 0.3),
            0 0 20px rgba(59, 130, 246, 0.2),
            0 0 30px rgba(37, 99, 235, 0.1);
    }
    
    @keyframes shine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    .title-separator {
        width: 150px;
        height: 4px;
        background: linear-gradient(to right, 
            transparent 0%,
            #60A5FA 20%,
            #3B82F6 50%,
            #60A5FA 80%,
            transparent 100%);
        margin: 1rem auto;
        border-radius: 2px;
    }
    
    /* تنسيق العنوان */
    .title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #60A5FA 0%, #3B82F6 50%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    /* تنسيق القوائم المنسدلة */
    .stSelectbox > div > div {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 12px;
        color: #E2E8F0;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #3B82F6;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
    }
    
    /* تنسيق الأزرار */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
    }
    
    /* تنسيق مربعات الاختيار */
    .stCheckbox > label {
        background: rgba(30, 41, 59, 0.6);
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(96, 165, 250, 0.2);
        transition: all 0.3s ease;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    
    .stCheckbox > label:hover {
        border-color: #3B82F6;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
    }
    
    /* تنسيق النتيجة */
    .result-card {
        background: rgba(30, 41, 59, 0.6);
        border: 2px solid #3B82F6;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.15);
        animation: fadeIn 0.5s ease-out;
    }
    
    .stat-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.2);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* تنسيق عام */
    .main {
        direction: rtl;
        text-align: right;
    }
    
    [data-language="English"] .main {
        direction: ltr;
        text-align: left;
    }

    /* تنسيق ملخص التكلفة */
    .cost-summary {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(96, 165, 250, 0.2);
    }

    .cost-item {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(96, 165, 250, 0.1);
    }

    .cost-item:last-child {
        border-bottom: none;
    }

    .total-cost {
        font-size: 1.5rem;
        font-weight: 700;
        color: #60A5FA;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 2px solid rgba(96, 165, 250, 0.2);
    }

    .cost-details {
        background: rgba(15, 23, 42, 0.6);
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-size: 0.9rem;
        color: #94A3B8;
    }

    .copy-button {
        background: #3B82F6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        cursor: pointer;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }

    .copy-button:hover {
        background: #2563EB;
    }
    
    /* تنسيق متجاوب */
    @media screen and (max-width: 768px) {
        .header { margin: -3rem -1rem 1rem -1rem; padding: 1rem; }
        .title { font-size: 2rem; }
        .stat-box { padding: 1rem; }
    }
    </style>
    """, unsafe_allow_html=True)

# عرض العنوان في الهيدر
st.markdown("""
    <div class='header'>
        <div class='title-container'>
            <div class='title'>حاسبة تكلفة الطباعة</div>
            <div class='title-separator'></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# اختيار اللغة
language = st.selectbox("", ["العربية", "English"])

# تعريف الخيارات حسب اللغة
if language == "العربية":
    st.markdown("""<style>.main { direction: rtl; text-align: right; }</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>.main { direction: ltr; text-align: left; }</style>""", unsafe_allow_html=True)

# القسم الرئيسي للتطبيق
def main():
    # تفاصيل الطباعة
    st.subheader("تفاصيل الطباعة")
    
    colored_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
    bw_color_pages = st.number_input("عدد الصفحات السوداء من ملف ملون", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات السوداء", min_value=0, value=0)
    
    # الإضافات
    st.subheader("الإضافات")
    
    last_page_empty = st.checkbox("الصفحة الأخيرة فارغة")
    cover = st.checkbox("تصميم غلاف")
    carton = st.checkbox("كرتون")
    nylon = st.checkbox("نايلون")
    ruler = st.checkbox("مسطرة")
    
    # دالة حساب التكلفة
    def calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon, ruler):
        total_cost = 0
        total_cost += colored_pages * 50
        total_cost += bw_color_pages * 40
        total_cost += bw_pages * 35
        if last_page_empty: total_cost += 25
        if cover: total_cost += 250
        if carton: total_cost += 250
        if nylon: total_cost += 250
        if ruler: total_cost += 100
        return total_cost

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, 
                                    last_page_empty, cover, carton, nylon, ruler)
    
    # عرض النتائج
    st.markdown("""
        <div class='cost-summary'>
            <h3>ملخص التكلفة</h3>
            <div class='cost-item'>
                <span>الصفحات الملونة ({} صفحة)</span>
                <span>{} ريال</span>
            </div>
            <div class='cost-item'>
                <span>الصفحات السوداء من ملف ملون ({} صفحة)</span>
                <span>{} ريال</span>
            </div>
            <div class='cost-item'>
                <span>الصفحات السوداء ({} صفحة)</span>
                <span>{} ريال</span>
            </div>
    """.format(
        colored_pages, colored_pages * 50,
        bw_color_pages, bw_color_pages * 40,
        bw_pages, bw_pages * 35
    ), unsafe_allow_html=True)

    # عرض الإضافات المحددة
    if last_page_empty or cover or carton or nylon or ruler:
        st.markdown("<div class='cost-item'><h4>الإضافات المحددة:</h4></div>", unsafe_allow_html=True)
        if last_page_empty:
            st.markdown("<div class='cost-item'><span>الصفحة الأخيرة فارغة</span><span>25 ريال</span></div>", unsafe_allow_html=True)
        if cover:
            st.markdown("<div class='cost-item'><span>تصميم غلاف</span><span>250 ريال</span></div>", unsafe_allow_html=True)
        if carton:
            st.markdown("<div class='cost-item'><span>كرتون</span><span>250 ريال</span></div>", unsafe_allow_html=True)
        if nylon:
            st.markdown("<div class='cost-item'><span>نايلون</span><span>250 ريال</span></div>", unsafe_allow_html=True)
        if ruler:
            st.markdown("<div class='cost-item'><span>مسطرة</span><span>100 ريال</span></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='total-cost'>
            <span>التكلفة الإجمالية:</span>
            <span>{total_cost} ريال</span>
        </div>
        
        <div class='cost-details'>
            <h4>تفاصيل الطلب:</h4>
            <p>
            - عدد الصفحات الملونة: {colored_pages} صفحة<br>
            - عدد الصفحات السوداء من ملف ملون: {bw_color_pages} صفحة<br>
            - عدد الصفحات السوداء: {bw_pages} صفحة<br>
            {"- الصفحة الأخيرة فارغة<br>" if last_page_empty else ""}
            {"- تصميم غلاف<br>" if cover else ""}
            {"- كرتون<br>" if carton else ""}
            {"- نايلون<br>" if nylon else ""}
            {"- مسطرة<br>" if ruler else ""}
            <br>
            <strong>المجموع الكلي: {total_cost} ريال</strong>
            </p>
        </div>
        
        <button class='copy-button' onclick="navigator.clipboard.writeText(`تفاصيل الطلب:
- عدد الصفحات الملونة: {colored_pages} صفحة
- عدد الصفحات السوداء من ملف ملون: {bw_color_pages} صفحة
- عدد الصفحات السوداء: {bw_pages} صفحة
{"- الصفحة الأخيرة فارغة" if last_page_empty else ""}
{"- تصميم غلاف" if cover else ""}
{"- كرتون" if carton else ""}
{"- نايلون" if nylon else ""}
{"- مسطرة" if ruler else ""}

المجموع الكلي: {total_cost} ريال`)">
            نسخ التفاصيل
        </button>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
