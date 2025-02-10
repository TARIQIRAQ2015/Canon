import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
import requests
import json
import math

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة الذكية",
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
        background: linear-gradient(145deg, #000428 0%, #004e92 100%);
        color: #E2E8F0;
        padding: 0;
        margin: 0;
        max-width: 100% !important;
        position: relative;
        overflow-x: hidden;
        overflow-y: auto;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 30%, rgba(0, 78, 146, 0.4) 0%, transparent 70%),
            radial-gradient(circle at 80% 70%, rgba(0, 4, 40, 0.4) 0%, transparent 70%);
        animation: backgroundFlow 20s ease infinite alternate;
        z-index: -1;
    }
    
    .stApp {
        max-width: 100%;
        padding: 1rem;
        background: transparent;
    }

    /* إخفاء العناصر غير المرغوب فيها */
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

    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* تنسيق عناصر الإدخال */
    .stSelectbox, .stNumberInput {
        background: rgba(0, 4, 40, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(0, 78, 146, 0.4);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(12px);
        margin-bottom: 1.2rem;
        box-shadow: 
            0 8px 20px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(0, 78, 146, 0.2);
    }
    
    .stSelectbox:hover, .stNumberInput:hover {
        border-color: rgba(0, 168, 255, 0.8);
        box-shadow: 
            0 12px 25px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(0, 78, 146, 0.4);
        transform: translateY(-3px);
    }

    /* تنسيق العناوين */
    .stMarkdown h3 {
        color: #00a8ff;
        font-size: 2rem;
        margin: 2.5rem 0 1.8rem 0;
        font-weight: 800;
        text-shadow: 
            0 0 20px rgba(0, 168, 255, 0.5),
            0 0 40px rgba(0, 168, 255, 0.3);
        letter-spacing: -0.5px;
    }

    /* تنسيق مربعات الاختيار */
    .stCheckbox {
        background: rgba(0, 4, 40, 0.8);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(0, 78, 146, 0.4);
        margin: 1rem 0;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(12px);
        box-shadow: 
            0 8px 20px rgba(0, 0, 0, 0.25),
            0 0 15px rgba(0, 78, 146, 0.2);
    }

    .stCheckbox:hover {
        border-color: rgba(0, 168, 255, 0.7);
        box-shadow: 
            0 12px 25px rgba(0, 0, 0, 0.35),
            0 0 30px rgba(0, 78, 146, 0.4);
        transform: translateX(-8px);
    }
    
    /* تنسيق الهيدر */
    .header {
        background: linear-gradient(135deg, rgba(0, 4, 40, 0.97), rgba(0, 78, 146, 0.97));
        padding: 6rem 2rem;
        margin: -1rem -1rem 4rem -1rem;
        border-bottom: 4px solid rgba(0, 168, 255, 0.4);
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.4),
            0 0 60px rgba(0, 78, 146, 0.3);
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
            radial-gradient(circle at 20% 50%, rgba(0, 168, 255, 0.3) 0%, transparent 70%),
            radial-gradient(circle at 80% 50%, rgba(0, 78, 146, 0.3) 0%, transparent 70%);
        animation: pulse 12s ease-in-out infinite alternate;
    }

    .title {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(120deg, 
            #00a8ff 0%, 
            #0097e6 25%, 
            #00a8ff 50%, 
            #0097e6 75%, 
            #00a8ff 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 12s linear infinite;
        margin: 0.5rem 0;
        letter-spacing: -1px;
        text-shadow: 
            0 0 20px rgba(0, 168, 255, 0.5),
            0 0 40px rgba(0, 151, 230, 0.4),
            0 0 60px rgba(0, 168, 255, 0.3);
    }

    .cost-summary {
        background: linear-gradient(145deg, rgba(0, 4, 40, 0.95), rgba(0, 78, 146, 0.95));
        border-radius: 30px;
        padding: 3rem;
        margin: 4rem 0;
        border: 3px solid rgba(0, 168, 255, 0.5);
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.4),
            0 0 80px rgba(0, 168, 255, 0.2);
        backdrop-filter: blur(20px);
        transform: perspective(1500px) rotateX(0deg);
        transition: all 0.7s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .cost-summary:hover {
        transform: perspective(1500px) rotateX(2deg);
        box-shadow: 
            0 25px 60px rgba(0, 0, 0, 0.5),
            0 0 100px rgba(0, 168, 255, 0.3);
    }

    .cost-summary h3 {
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        text-align: center;
        margin-bottom: 2.5rem;
        color: #fff !important;
        text-shadow: 
            0 0 25px rgba(0, 168, 255, 0.7),
            0 0 50px rgba(0, 168, 255, 0.4);
    }
    
    .cost-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.8rem;
        margin: 1.2rem 0;
        background: rgba(0, 4, 40, 0.7);
        border-radius: 18px;
        border: 2px solid rgba(0, 168, 255, 0.4);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(12px);
        font-size: 1.3rem;
        font-weight: 600;
        box-shadow: 
            0 8px 20px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(0, 78, 146, 0.2);
    }

    .cost-item:hover {
        background: rgba(0, 4, 40, 0.9);
        border-color: rgba(0, 168, 255, 0.6);
        transform: translateX(-10px);
        box-shadow: 
            0 12px 25px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(0, 78, 146, 0.3);
    }

    .total-cost {
        background: linear-gradient(120deg, #000428, #004e92);
        border-radius: 25px;
        padding: 3.5rem;
        margin-top: 3.5rem;
        border: 4px solid rgba(0, 168, 255, 0.6);
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 15px 40px rgba(0, 0, 0, 0.4),
            0 0 60px rgba(0, 168, 255, 0.2);
    }
    
    .total-cost span {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(120deg, #00a8ff, #0097e6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 
            0 0 30px rgba(0, 168, 255, 0.5),
            0 0 60px rgba(0, 168, 255, 0.3);
    }

    .currency-breakdown {
        background: rgba(0, 4, 40, 0.8);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        border: 2px solid rgba(0, 168, 255, 0.4);
    }

    .currency-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        margin: 0.8rem 0;
        background: rgba(0, 78, 146, 0.3);
        border-radius: 12px;
        font-size: 1.2rem;
    }

    /* زر العودة للأعلى */
    .scroll-to-top {
        position: fixed;
        bottom: 30px;
        left: 30px;
        background: linear-gradient(135deg, #00a8ff, #0097e6);
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 
            0 6px 20px rgba(0, 168, 255, 0.5),
            0 0 30px rgba(0, 168, 255, 0.3);
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
        font-size: 1.5rem;
    }

    .scroll-to-top.visible {
        opacity: 1;
        visibility: visible;
    }

    .scroll-to-top:hover {
        transform: translateY(-8px);
        box-shadow: 
            0 8px 25px rgba(0, 168, 255, 0.7),
            0 0 40px rgba(0, 168, 255, 0.4);
    }

    /* تحسينات الأداء */
    * {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    @keyframes backgroundFlow {
        0% { transform: scale(1); }
        100% { transform: scale(1.15); }
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    @keyframes shine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.7; }
        100% { transform: scale(1.4); opacity: 1; }
    }
    </style>

    <script>
    // زر العودة للأعلى
    window.onscroll = function() {
        var scrollButton = document.querySelector('.scroll-to-top');
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollButton.classList.add('visible');
        } else {
            scrollButton.classList.remove('visible');
        }
    };

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
    </script>

    <div class="scroll-to-top" onclick="scrollToTop()">↑</div>
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
    currencies = [250, 500, 1000]
    differences = [abs(amount - (math.floor(amount/c) * c)) for c in currencies]
    min_diff_index = differences.index(min(differences))
    return math.floor(amount/currencies[min_diff_index]) * currencies[min_diff_index]

def main():
    # تعيين اتجاه الصفحة للعربية
    st.markdown("""<style>.main { direction: rtl; text-align: right; }</style>""", unsafe_allow_html=True)

    # عرض العنوان في الهيدر
    st.markdown("""
        <div class='header'>
            <div class='title-container'>
                <div class='title-icon'>🖨️</div>
                <div class='title'>حاسبة تكلفة الطباعة الذكية</div>
                <div class='title-separator'></div>
                <div class='subtitle'>احسب تكلفة طباعتك بدقة عالية وسهولة تامة</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # تفاصيل الطباعة
    st.markdown("<h3>🎨 تفاصيل الطباعة</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        colored_pages = st.number_input("عدد الصفحات الملونة", 
                                      min_value=0, max_value=500,
                                      value=0,
                                      help="أدخل عدد الصفحات الملونة المراد طباعتها")
    
    with col2:
        bw_pages = st.number_input("عدد الصفحات السوداء",
                                  min_value=0, max_value=500,
                                  value=0,
                                  help="أدخل عدد الصفحات السوداء العادية")
    
    # الإضافات
    st.markdown("<h3>✨ الإضافات المتاحة</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        cover = st.checkbox("تصميم غلاف احترافي", help="إضافة غلاف مصمم بشكل احترافي")
        carton = st.checkbox("كرتون فاخر", help="إضافة كرتون عالي الجودة")
    with col2:
        nylon = st.checkbox("تغليف نايلون", help="تغليف العمل بالنايلون للحماية")
        ruler = st.checkbox("مسطرة خاصة", help="إضافة مسطرة خاصة للعمل")
    
    # حساب التكلفة
    total_cost = calculate_total_cost(colored_pages, bw_pages, 
                                    cover, carton, nylon, ruler)
    rounded_cost = round_to_nearest_currency(total_cost)
    
    # عرض النتائج
    st.markdown("""
        <div class='cost-summary'>
            <h3>💫 تفاصيل التكلفة</h3>
            <div class='cost-item'>
                <span>🎨 الصفحات الملونة ({} صفحة)</span>
                <span>{} دينار</span>
            </div>
            <div class='cost-item'>
                <span>📝 الصفحات السوداء ({} صفحة)</span>
                <span>{} دينار</span>
            </div>
    """.format(
        colored_pages, colored_pages * 50,
        bw_pages, bw_pages * 35
    ), unsafe_allow_html=True)

    # عرض الإضافات المحددة
    if cover or carton or nylon or ruler:
        st.markdown("<div class='cost-item'><h4>🎁 الإضافات المختارة:</h4></div>", unsafe_allow_html=True)
        if cover:
            st.markdown("<div class='cost-item'><span>🎨 تصميم غلاف احترافي</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if carton:
            st.markdown("<div class='cost-item'><span>📦 كرتون فاخر</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if nylon:
            st.markdown("<div class='cost-item'><span>✨ تغليف نايلون</span><span>250 دينار</span></div>", unsafe_allow_html=True)
        if ruler:
            st.markdown("<div class='cost-item'><span>📏 مسطرة خاصة</span><span>250 دينار</span></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='total-cost'>
            <h2 style='margin-bottom: 1.5rem; color: #fff;'>💎 التكلفة الإجمالية</h2>
            <span>{total_cost} دينار</span>
            <div class='currency-breakdown'>
                <h4 style='color: #00a8ff; margin-bottom: 1rem;'>التقريب لأقرب عملة متوفرة</h4>
                <div class='currency-item'>
                    <span>المبلغ المقرب</span>
                    <span>{rounded_cost} دينار</span>
                </div>
            </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
