import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog
from streamlit_lottie import st_lottie
import requests
import json

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة الذكية",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تحميل الرسوم المتحركة
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_printer = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_szviypry.json')

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
            radial-gradient(circle at 20% 30%, rgba(0, 78, 146, 0.3) 0%, transparent 70%),
            radial-gradient(circle at 80% 70%, rgba(0, 4, 40, 0.3) 0%, transparent 70%);
        animation: backgroundFlow 15s ease infinite alternate;
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
        padding: 1.2rem;
        border: 1px solid rgba(0, 78, 146, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        margin-bottom: 1rem;
    }
    
    .stSelectbox:hover, .stNumberInput:hover {
        border-color: rgba(0, 78, 146, 0.8);
        box-shadow: 0 0 20px rgba(0, 78, 146, 0.4);
        transform: translateY(-2px);
    }

    /* تنسيق العناوين */
    .stMarkdown h3 {
        color: #00a8ff;
        font-size: 1.8rem;
        margin: 2rem 0 1.5rem 0;
        font-weight: 800;
        text-shadow: 0 0 15px rgba(0, 168, 255, 0.4);
    }

    /* تنسيق مربعات الاختيار */
    .stCheckbox {
        background: rgba(0, 4, 40, 0.7);
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid rgba(0, 78, 146, 0.3);
        margin: 0.7rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(8px);
    }

    .stCheckbox:hover {
        border-color: rgba(0, 78, 146, 0.6);
        box-shadow: 0 0 15px rgba(0, 78, 146, 0.3);
        transform: translateX(-5px);
    }
    
    /* تنسيق الهيدر */
    .header {
        background: linear-gradient(135deg, rgba(0, 4, 40, 0.97), rgba(0, 78, 146, 0.97));
        padding: 5rem 2rem;
        margin: -1rem -1rem 4rem -1rem;
        border-bottom: 3px solid rgba(0, 168, 255, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
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
            radial-gradient(circle at 20% 50%, rgba(0, 168, 255, 0.2) 0%, transparent 60%),
            radial-gradient(circle at 80% 50%, rgba(0, 78, 146, 0.2) 0%, transparent 60%);
        animation: pulse 10s ease-in-out infinite alternate;
    }

    .title {
        font-size: 4rem;
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
        animation: shine 10s linear infinite;
        margin: 0.5rem 0;
        letter-spacing: -1px;
        text-shadow: 
            0 0 15px rgba(0, 168, 255, 0.4),
            0 0 30px rgba(0, 151, 230, 0.3),
            0 0 45px rgba(0, 168, 255, 0.2);
    }

    .cost-summary {
        background: linear-gradient(145deg, rgba(0, 4, 40, 0.95), rgba(0, 78, 146, 0.95));
        border-radius: 25px;
        padding: 2.5rem;
        margin: 3rem 0;
        border: 2px solid rgba(0, 168, 255, 0.4);
        box-shadow: 
            0 15px 35px rgba(0, 0, 0, 0.3),
            0 0 70px rgba(0, 168, 255, 0.15);
        backdrop-filter: blur(15px);
        transform: perspective(1500px) rotateX(0deg);
        transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .cost-summary h3 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 2rem;
        color: #fff !important;
        text-shadow: 0 0 20px rgba(0, 168, 255, 0.6);
    }
    
    .cost-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem;
        margin: 1rem 0;
        background: rgba(0, 4, 40, 0.6);
        border-radius: 15px;
        border: 1px solid rgba(0, 168, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(8px);
        font-size: 1.2rem;
        font-weight: 600;
    }

    .cost-item:hover {
        background: rgba(0, 4, 40, 0.8);
        border-color: rgba(0, 168, 255, 0.5);
        transform: translateX(-8px);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .total-cost {
        background: linear-gradient(120deg, #000428, #004e92);
        border-radius: 20px;
        padding: 3rem;
        margin-top: 3rem;
        border: 3px solid rgba(0, 168, 255, 0.5);
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .total-cost span {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(120deg, #00a8ff, #0097e6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(0, 168, 255, 0.4);
    }

    /* زر العودة للأعلى */
    .scroll-to-top {
        position: fixed;
        bottom: 20px;
        left: 20px;
        background: linear-gradient(135deg, #00a8ff, #0097e6);
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 168, 255, 0.4);
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
    }

    .scroll-to-top.visible {
        opacity: 1;
        visibility: visible;
    }

    .scroll-to-top:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0, 168, 255, 0.6);
    }

    /* تحسينات الأداء */
    * {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    @keyframes backgroundFlow {
        0% { transform: scale(1); }
        100% { transform: scale(1.1); }
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    @keyframes shine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.6; }
        100% { transform: scale(1.3); opacity: 0.9; }
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

def main():
    # تعيين اتجاه الصفحة للعربية
    st.markdown("""<style>.main { direction: rtl; text-align: right; }</style>""", unsafe_allow_html=True)

    # عرض العنوان في الهيدر مع الرسوم المتحركة
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

    # عرض الرسوم المتحركة
    with st.container():
        st_lottie(lottie_printer, height=200, key="printer")

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
        </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
