import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog

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
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Cairo', sans-serif !important;
        background: linear-gradient(145deg, #0B1120 0%, #1E293B 100%);
        color: #E2E8F0;
        padding: 0;
        margin: 0;
        max-width: 100% !important;
        position: relative;
        overflow: hidden;
    }
    
    /* خلفية متحركة */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 0% 0%, rgba(96, 165, 250, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 100% 0%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 100% 100%, rgba(37, 99, 235, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 0% 100%, rgba(96, 165, 250, 0.1) 0%, transparent 50%);
        animation: gradient 15s ease infinite;
        background-size: 200% 200%;
        z-index: -1;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 0%; }
        25% { background-position: 100% 0%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 0%; }
    }
    
    .stApp {
        max-width: 100%;
        padding: 1rem;
    }

    /* إخفاء أزرار تغيير الوضع */
    [data-testid="StyledFullScreenButton"], 
    [data-testid="baseButton-header"] {
        display: none !important;
    }
    
    /* تنسيق القوائم المنسدلة */
    .stSelectbox, .stNumberInput {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(96, 165, 250, 0.2);
        transition: all 0.3s ease;
    }
    
    .stSelectbox:hover, .stNumberInput:hover {
        border-color: rgba(96, 165, 250, 0.5);
        box-shadow: 0 0 15px rgba(96, 165, 250, 0.2);
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
    
    .cost-summary {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid rgba(96, 165, 250, 0.3);
        box-shadow: 
            0 10px 25px rgba(0, 0, 0, 0.2),
            0 0 50px rgba(96, 165, 250, 0.1);
        backdrop-filter: blur(10px);
        transform: perspective(1000px) rotateX(0deg);
        transition: all 0.5s ease;
    }
    
    .cost-summary:hover {
        transform: perspective(1000px) rotateX(2deg);
        box-shadow: 
            0 15px 35px rgba(0, 0, 0, 0.3),
            0 0 70px rgba(96, 165, 250, 0.2);
    }

    .cost-details {
        background: rgba(15, 23, 42, 0.6);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border: 1px solid rgba(96, 165, 250, 0.2);
    }

    .cost-details h4 {
        color: #60A5FA;
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }

    .cost-details p {
        line-height: 1.8;
        margin-bottom: 0.5rem;
    }

    .total-cost {
        background: linear-gradient(120deg, #1E293B, #0F172A);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        border: 2px solid rgba(96, 165, 250, 0.4);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .total-cost::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(96, 165, 250, 0.1),
            transparent
        );
        transform: rotate(45deg);
        animation: shine 3s infinite;
    }
    
    .total-cost span {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #60A5FA, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.3);
    }

    .copy-button {
        background: linear-gradient(120deg, #3B82F6, #2563EB);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }

    .copy-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(37, 99, 235, 0.3);
        background: linear-gradient(120deg, #2563EB, #1D4ED8);
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
    
    colored_pages = st.selectbox("عدد الصفحات الملونة", 
                               list(range(0, 501)),
                               format_func=lambda x: f"{x} صفحة")
    
    bw_color_pages = st.selectbox("عدد الصفحات السوداء من ملف ملون",
                                 list(range(0, 501)),
                                 format_func=lambda x: f"{x} صفحة")
    
    bw_pages = st.selectbox("عدد الصفحات السوداء",
                           list(range(0, 501)),
                           format_func=lambda x: f"{x} صفحة")
    
    # الإضافات
    st.subheader("الإضافات")
    
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("تصميم غلاف")
        carton = st.checkbox("كرتون")
    with col2:
        nylon = st.checkbox("نايلون")
        ruler = st.checkbox("مسطرة")
    
    # دالة حساب التكلفة
    def calculate_total_cost(colored_pages, bw_color_pages, bw_pages, cover, carton, nylon, ruler):
        total_cost = 0
        total_cost += colored_pages * 50
        total_cost += bw_color_pages * 40
        total_cost += bw_pages * 35
        if cover: total_cost += 250
        if carton: total_cost += 250
        if nylon: total_cost += 250
        if ruler: total_cost += 250  # تم تعديل سعر المسطرة إلى 250 دينار
        return total_cost

    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, 
                                    cover, carton, nylon, ruler)
    
    # عرض النتائج
    st.markdown("""
        <div class='cost-summary'>
            <h3 style='text-align: center; font-size: 2rem; margin-bottom: 2rem; 
                      background: linear-gradient(120deg, #60A5FA, #3B82F6); 
                      -webkit-background-clip: text; 
                      -webkit-text-fill-color: transparent;'>
                ملخص التكلفة
            </h3>
            <div class='cost-item'>
                <span>عدد الصفحات الملونة: {} صفحة</span>
                <span>{} دينار</span>
            </div>
            <div class='cost-item'>
                <span>عدد الصفحات السوداء من ملف ملون: {} صفحة</span>
                <span>{} دينار</span>
            </div>
            <div class='cost-item'>
                <span>عدد الصفحات السوداء: {} صفحة</span>
                <span>{} دينار</span>
            </div>
    """.format(
        colored_pages, colored_pages * 50,
        bw_color_pages, bw_color_pages * 40,
        bw_pages, bw_pages * 35
    ), unsafe_allow_html=True)

    # عرض الإضافات المحددة
    if cover or carton or nylon or ruler:
        st.markdown("<div class='cost-item'><h4>الإضافات المحددة:</h4></div>", unsafe_allow_html=True)
        if cover:
            st.markdown("<div class='cost-item'><span>تصميم غلاف</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if carton:
            st.markdown("<div class='cost-item'><span>كرتون</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if nylon:
            st.markdown("<div class='cost-item'><span>نايلون</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if ruler:
            st.markdown("<div class='cost-item'><span>مسطرة</span><span>250 دينار</span></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='total-cost'>
            <h2 style='margin-bottom: 1rem; color: #94A3B8;'>التكلفة الإجمالية</h2>
            <span>{total_cost} دينار</span>
        </div>
        
        <div class='cost-details'>
            <h4>تفاصيل الطلب:</h4>
            <p dir="rtl">
            - عدد الصفحات الملونة: {colored_pages} صفحة<br>
            - عدد الصفحات السوداء من ملف ملون: {bw_color_pages} صفحة<br>
            - عدد الصفحات السوداء: {bw_pages} صفحة<br>
            {"- تصميم غلاف<br>" if cover else ""}
            {"- كرتون<br>" if carton else ""}
            {"- نايلون<br>" if nylon else ""}
            {"- مسطرة<br>" if ruler else ""}
            <br>
            <strong>المجموع الكلي: {total_cost} دينار</strong>
            </p>
        </div>
        
        <button class='copy-button' onclick="navigator.clipboard.writeText(`تفاصيل الطلب:
عدد الصفحات الملونة: {colored_pages} صفحة
عدد الصفحات السوداء من ملف ملون: {bw_color_pages} صفحة
عدد الصفحات السوداء: {bw_pages} صفحة
{"تصميم غلاف" if cover else ""}
{"كرتون" if carton else ""}
{"نايلون" if nylon else ""}
{"مسطرة" if ruler else ""}

المجموع الكلي: {total_cost} دينار`)">
            نسخ التفاصيل
        </button>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
