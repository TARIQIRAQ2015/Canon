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

    /* إخفاء أزرار تغيير الوضع */
    [data-testid="StyledFullScreenButton"], 
    .css-ch5dnh {
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

    /* تنسيق متجاوب */
    @media screen and (max-width: 768px) {
        .header { margin: -3rem -1rem 1rem -1rem; padding: 1rem; }
        .title { font-size: 2rem; }
        .stat-box { padding: 1rem; }
    }
    
    /* الخلفية المتحركة */
    .main:before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 0% 0%, rgba(96, 165, 250, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 100% 0%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 100% 100%, rgba(37, 99, 235, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 0% 100%, rgba(96, 165, 250, 0.03) 0%, transparent 50%);
        animation: backgroundAnimation 15s ease infinite;
        z-index: -1;
    }

    @keyframes backgroundAnimation {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }

    /* تنسيق تفاصيل التكلفة */
    .cost-details {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border: 1px solid rgba(96, 165, 250, 0.2);
        font-family: 'Cairo', sans-serif;
    }

    .cost-details h4 {
        color: #60A5FA;
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }

    .cost-details p {
        color: #E2E8F0;
        line-height: 1.8;
        margin: 0;
        padding: 0;
    }

    .cost-details strong {
        display: block;
        margin-top: 1rem;
        color: #60A5FA;
        font-size: 1.2rem;
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
    
    cover = st.checkbox("تصميم غلاف")
    carton = st.checkbox("كرتون")
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
        if ruler: total_cost += 250  # تعديل سعر المسطرة إلى 250 دينار
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
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()import streamlit as st
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

    /* إخفاء أزرار تغيير الوضع */
    [data-testid="StyledFullScreenButton"], 
    .css-ch5dnh {
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
    
    /* الخلفية المتحركة */
    .main:before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 0% 0%, rgba(96, 165, 250, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 100% 0%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 100% 100%, rgba(37, 99, 235, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 0% 100%, rgba(96, 165, 250, 0.03) 0%, transparent 50%);
        animation: backgroundAnimation 15s ease infinite;
        z-index: -1;
    }

    @keyframes backgroundAnimation {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }

    /* تنسيق تفاصيل التكلفة */
    .cost-details {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border: 1px solid rgba(96, 165, 250, 0.2);
        font-family: 'Cairo', sans-serif;
    }

    .cost-details h4 {
        color: #60A5FA;
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }

    .cost-details p {
        color: #E2E8F0;
        line-height: 1.8;
        margin: 0;
        padding: 0;
    }

    .cost-details strong {
        display: block;
        margin-top: 1rem;
        color: #60A5FA;
        font-size: 1.2rem;
    }

    .copy-button {
        display: block;
        width: 100%;
        margin-top: 1rem;
        padding: 0.8rem;
        background: linear-gradient(45deg, #3B82F6, #2563EB);
        color: white;
        border: none;
        border-radius: 8px;
        font-family: 'Cairo', sans-serif;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .copy-button:hover {
        background: linear-gradient(45deg, #2563EB, #1D4ED8);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(37, 99, 235, 0.2);
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
    
    cover = st.checkbox("تصميم غلاف")
    carton = st.checkbox("كرتون")
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
        if ruler: total_cost += 250  # تعديل سعر المسطرة إلى 250 دينار
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
- عدد الصفحات الملونة: {colored_pages} صفحة
- عدد الصفحات السوداء من ملف ملون: {bw_color_pages} صفحة
- عدد الصفحات السوداء: {bw_pages} صفحة
{"- تصميم غلاف" if cover else ""}
{"- كرتون" if carton else ""}
{"- نايلون" if nylon else ""}
{"- مسطرة" if ruler else ""}

المجموع الكلي: {total_cost} دينار`)">
            نسخ التفاصيل
        </button>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
