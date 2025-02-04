import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_toggle as tog

# تعيين الإعدادات الأولية
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide"
)

# تطبيق الأنماط المتقدمة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700&display=swap');
    
    /* الأنماط الأساسية */
    .main {
        font-family: 'Cairo', sans-serif !important;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
        padding: 2rem;
    }
    
    /* تنسيق العنوان */
    h1 {
        background: linear-gradient(120deg, #f59e0b 0%, #fbbf24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
        text-shadow: 0px 2px 4px rgba(251, 191, 36, 0.2);
    }
    
    /* تنسيق القوائم المنسدلة */
    .stSelectbox > div > div {
        background: rgba(30, 41, 59, 0.8);
        border: 2px solid rgba(251, 191, 36, 0.3);
        border-radius: 12px;
        color: #e2e8f0;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div:hover {
        border-color: #f59e0b;
        box-shadow: 0 0 15px rgba(251, 191, 36, 0.2);
    }
    
    /* تنسيق الأزرار */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
        color: #0f172a;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(251, 191, 36, 0.3);
    }
    
    /* تنسيق النتيجة */
    .result-card {
        background: rgba(30, 41, 59, 0.9);
        border: 2px solid #f59e0b;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(251, 191, 36, 0.15);
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* تنسيق متجاوب */
    @media screen and (max-width: 768px) {
        .main { padding: 1rem; }
        h1 { font-size: 2rem !important; }
        .result-card { padding: 1rem; }
    }
    </style>
    """, unsafe_allow_html=True)

# اختيار اللغة في البداية
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# تعريف الخيارات حسب اللغة
if language == "العربية":
    st.title("🖨️ حاسبة تكلفة الطباعة")
    
    # القوائم المنسدلة للصفحات
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
    col1, col2 = st.columns(2)
    with col1:
        last_page_empty = st.checkbox("✨ الصفحة الأخيرة فارغة")
        cover = st.checkbox("📔 إضافة غلاف ملون")
    with col2:
        carton = st.checkbox("📦 إضافة كرتون")
        nylon = st.checkbox("🎁 إضافة تغليف")

else:
    st.title("🖨️ Printing Cost Calculator")
    
    # Dropdown menus for pages
    colored_pages = st.selectbox("Number of Colored Pages",
                               list(range(0, 501)),
                               format_func=lambda x: f"{x} pages")
    
    bw_color_pages = st.selectbox("Number of Black & White Pages with Few Colors",
                                 list(range(0, 501)),
                                 format_func=lambda x: f"{x} pages")
    
    bw_pages = st.selectbox("Number of Black & White Pages Only",
                           list(range(0, 501)),
                           format_func=lambda x: f"{x} pages")
    
    # Additional options
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
                <h2 style='color: #f59e0b; text-align: center; margin-bottom: 1rem;'>ملخص التكلفة</h2>
                <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; text-align: center;'>
                    <div>
                        <h3 style='color: #f59e0b;'>التكلفة الإجمالية</h3>
                        <p style='font-size: 2rem; font-weight: bold;'>{total_cost} دينار</p>
                    </div>
                    <div>
                        <h3 style='color: #f59e0b;'>عدد الصفحات</h3>
                        <p style='font-size: 1.5rem;'>{total_pages} صفحة</p>
                    </div>
                    <div>
                        <h3 style='color: #f59e0b;'>الإضافات</h3>
                        <p style='font-size: 1.5rem;'>{extras} عناصر</p>
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
                <h2 style='color: #f59e0b; text-align: center; margin-bottom: 1rem;'>Cost Summary</h2>
                <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; text-align: center;'>
                    <div>
                        <h3 style='color: #f59e0b;'>Total Cost</h3>
                        <p style='font-size: 2rem; font-weight: bold;'>{total_cost} Dinar</p>
                    </div>
                    <div>
                        <h3 style='color: #f59e0b;'>Total Pages</h3>
                        <p style='font-size: 1.5rem;'>{total_pages} pages</p>
                    </div>
                    <div>
                        <h3 style='color: #f59e0b;'>Add-ons</h3>
                        <p style='font-size: 1.5rem;'>{extras} items</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
