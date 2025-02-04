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
    }
    
    .stApp {
        max-width: 100%;
        padding: 1rem;
    }

    /* إخفاء أزرار تغيير الوضع والمشاركة */
    [data-testid="StyledFullScreenButton"], 
    .css-ch5dnh,
    .viewerBadge_container__1QSob,
    .styles_terminalButton__JBj5T,
    .styles_viewerBadge__1yB5,
    .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK,
    header button,
    .stDeployButton {
        display: none !important;
    }

    /* إخفاء الهيدر بالكامل */
    header[data-testid="stHeader"] {
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

    /* تنسيق العناوين */
    .stMarkdown h3 {
        color: #60A5FA;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    /* تنسيق مربعات الاختيار */
    .stCheckbox {
        background: rgba(30, 41, 59, 0.6);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid rgba(96, 165, 250, 0.1);
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }

    .stCheckbox:hover {
        border-color: rgba(96, 165, 250, 0.3);
        box-shadow: 0 0 10px rgba(96, 165, 250, 0.1);
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

    .cost-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        margin: 0.5rem 0;
        background: rgba(15, 23, 42, 0.5);
        border-radius: 10px;
        border: 1px solid rgba(96, 165, 250, 0.2);
        transition: all 0.3s ease;
    }

    .cost-item:hover {
        background: rgba(15, 23, 42, 0.7);
        border-color: rgba(96, 165, 250, 0.4);
        transform: translateX(-5px);
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

    @keyframes shine {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    </style>
    """, unsafe_allow_html=True)

def calculate_total_cost(colored_pages, bw_color_pages, bw_pages, cover, carton, nylon, ruler):
    total_cost = 0
    total_cost += colored_pages * 50
    total_cost += bw_color_pages * 40
    total_cost += bw_pages * 35
    if cover: total_cost += 250
    if carton: total_cost += 250
    if nylon: total_cost += 250
    if ruler: total_cost += 250
    return total_cost

def main():
    # تعيين اتجاه الصفحة للعربية
    st.markdown("""<style>.main { direction: rtl; text-align: right; }</style>""", unsafe_allow_html=True)

    # عرض العنوان في الهيدر
    st.markdown("""
        <div class='header'>
            <div class='title-container'>
                <div class='title'>حاسبة تكلفة الطباعة</div>
                <div class='title-separator'></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

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
                <span>الصفحات الملونة ({} صفحة)</span>
                <span>{} دينار</span>
            </div>
            <div class='cost-item'>
                <span>الصفحات السوداء من ملف ملون ({} صفحة)</span>
                <span>{} دينار</span>
            </div>
            <div class='cost-item'>
                <span>الصفحات السوداء ({} صفحة)</span>
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
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
