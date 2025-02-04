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
    }
    
    /* تنسيق الهيدر */
    .header {
        background: linear-gradient(to right, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.9));
        padding: 2rem;
        margin: -6rem -4rem 2rem -4rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
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
        <div class='title'>حاسبة تكلفة الطباعة</div>
    </div>
""", unsafe_allow_html=True)

# اختيار اللغة
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# تعريف الخيارات حسب اللغة
if language == "العربية":
    # القوائم المنسدلة للصفحات
    st.markdown("### 📄 تفاصيل الطباعة")
    colored_pages = st.selectbox("عدد الصفحات الملونة", 
                               list(range(0, 501)),
                               format_func=lambda x: f"{x} صفحة")
    
    bw_color_pages = st.selectbox("عدد الصفحات الأبيض والأسود مع ألوان قليلة",
                                 list(range(0, 501)),
                                 format_func=lambda x: f"{x} صفحة")
    
    bw_pages = st.selectbox("عدد الصفحات الأبيض والأسود فقط",
                           list(range(0, 501)),
                           format_func=lambda x: f"{x} صفحة")
    
    # الخيارات الإضافية
    st.markdown("### 🎨 الإضافات")
    col1, col2 = st.columns(2)
    with col1:
        last_page_empty = st.checkbox("✨ الصفحة الأخيرة فارغة")
        cover = st.checkbox("📔 إضافة غلاف ملون")
    with col2:
        carton = st.checkbox("📦 إضافة كرتون")
        nylon = st.checkbox("🎁 إضافة تغليف")

else:
    st.markdown("### 📄 Printing Details")
    colored_pages = st.selectbox("Number of Colored Pages",
                               list(range(0, 501)),
                               format_func=lambda x: f"{x} pages")
    
    bw_color_pages = st.selectbox("Number of Black & White Pages with Few Colors",
                                 list(range(0, 501)),
                                 format_func=lambda x: f"{x} pages")
    
    bw_pages = st.selectbox("Number of Black & White Pages Only",
                           list(range(0, 501)),
                           format_func=lambda x: f"{x} pages")
    
    st.markdown("### 🎨 Add-ons")
    col1, col2 = st.columns(2)
    with col1:
        last_page_empty = st.checkbox("✨ Last Page Empty")
        cover = st.checkbox("📔 Add Colored Cover")
    with col2:
        carton = st.checkbox("📦 Add Carton")
        nylon = st.checkbox("🎁 Add Wrapping")

# دالة حساب التكلفة
def calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon):
    total_cost = 0
    total_cost += colored_pages * 50
    total_cost += bw_color_pages * 40
    total_cost += bw_pages * 35
    if last_page_empty: total_cost += 25
    if cover: total_cost += 250
    if carton: total_cost += 250
    if nylon: total_cost += 250
    return total_cost

# عرض النتيجة
if language == "العربية":
    if st.button("💰 حساب التكلفة الإجمالية"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        total_pages = colored_pages + bw_color_pages + bw_pages
        extras = sum([cover, carton, nylon])
        
        st.markdown(f"""
            <div class='result-card'>
                <h2 style='color: #3B82F6; text-align: center; margin-bottom: 1.5rem; font-size: 2rem;'>ملخص التكلفة</h2>
                <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;'>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>التكلفة الإجمالية</h3>
                        <p style='font-size: 2.5rem; font-weight: 800; margin: 0; background: linear-gradient(120deg, #60A5FA, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{total_cost} دينار</p>
                    </div>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>عدد الصفحات</h3>
                        <p style='font-size: 2rem; margin: 0;'>{total_pages} صفحة</p>
                    </div>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>الإضافات</h3>
                        <p style='font-size: 2rem; margin: 0;'>{extras} عناصر</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    if st.button("💰 Calculate Total Cost"):
        total_cost = calculate_total_cost(colored_pages, bw_color_pages, bw_pages, last_page_empty, cover, carton, nylon)
        total_pages = colored_pages + bw_color_pages + bw_pages
        extras = sum([cover, carton, nylon])
        
        st.markdown(f"""
            <div class='result-card'>
                <h2 style='color: #3B82F6; text-align: center; margin-bottom: 1.5rem; font-size: 2rem;'>Cost Summary</h2>
                <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;'>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>Total Cost</h3>
                        <p style='font-size: 2.5rem; font-weight: 800; margin: 0; background: linear-gradient(120deg, #60A5FA, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{total_cost} Dinar</p>
                    </div>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>Total Pages</h3>
                        <p style='font-size: 2rem; margin: 0;'>{total_pages} pages</p>
                    </div>
                    <div class='stat-box' style='text-align: center;'>
                        <h3 style='color: #60A5FA; margin-bottom: 0.5rem;'>Add-ons</h3>
                        <p style='font-size: 2rem; margin: 0;'>{extras} items</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
