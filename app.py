import streamlit as st
import pyperclip

# تعيين تكوين الصفحة
st.set_page_config(
    page_title="Print Calculator Pro",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تعريف الأسعار الثابتة
PRICES = {
    'color': 50,
    'bw_with_color': 40,
    'bw': 35,
    'cover': 250,
    'empty_last': 25,
    'carton': 250,
    'nylon': 250,
    'paper_holder': 250,
}

# تحسين CSS العام
st.markdown("""
    <style>
        /* تحسين المظهر العام */
        .stApp {
            background: linear-gradient(
                135deg, 
                #0a192f 0%,
                #0c1b2b 50%,
                #0a192f 100%
            );
            background-attachment: fixed;
        }
        
        /* تحسين العناوين */
        h1, h2, h3 {
            background: linear-gradient(120deg, #64ffda, #00bfa5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            letter-spacing: 1px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* تحسين حقول الإدخال */
        .stNumberInput > div > div,
        .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(100, 255, 218, 0.2) !important;
            border-radius: 10px !important;
            color: #e6f1ff !important;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .stNumberInput > div > div:hover,
        .stSelectbox > div > div:hover {
            border-color: #64ffda !important;
            box-shadow: 0 0 15px rgba(100, 255, 218, 0.2);
            transform: translateY(-2px);
        }
        
        /* تحسين الأزرار */
        .stButton > button {
            background: linear-gradient(
                45deg,
                rgba(100, 255, 218, 0.1),
                rgba(0, 191, 165, 0.1)
            ) !important;
            border: 1px solid #64ffda !important;
            color: #64ffda !important;
            border-radius: 10px !important;
            padding: 1rem 2rem !important;
            font-weight: 600 !important;
            letter-spacing: 1px;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }
        
        .stButton > button:hover {
            background: linear-gradient(
                45deg,
                rgba(100, 255, 218, 0.2),
                rgba(0, 191, 165, 0.2)
            ) !important;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(100, 255, 218, 0.2);
        }
        
        /* تحسين شريط التقدم */
        .progress-container {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 3px;
            margin: 1rem 0;
            border: 1px solid rgba(100, 255, 218, 0.2);
            overflow: hidden;
        }
        
        .progress-bar {
            background: linear-gradient(90deg, #64ffda, #00bfa5);
            height: 10px;
            border-radius: 15px;
            transition: width 0.5s ease;
        }
        
        /* تحسين الخانات */
        .element-container {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(100, 255, 218, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .element-container:hover {
            border-color: rgba(100, 255, 218, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        /* تحسين النصوص */
        .stMarkdown {
            color: #8892b0 !important;
            line-height: 1.6;
        }
        
        /* تحسين الروابط */
        a {
            color: #64ffda !important;
            text-decoration: none !important;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #00bfa5 !important;
            text-decoration: none !important;
        }
        
        /* تحسين الصناديق */
        .info-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(100, 255, 218, 0.2);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }
        
        .info-box:hover {
            border-color: #64ffda;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        /* تحسين الشبكة */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        /* تأثيرات إضافية */
        @keyframes glow {
            0% { box-shadow: 0 0 5px rgba(100, 255, 218, 0.2); }
            50% { box-shadow: 0 0 20px rgba(100, 255, 218, 0.4); }
            100% { box-shadow: 0 0 5px rgba(100, 255, 218, 0.2); }
        }
        
        .glow-effect {
            animation: glow 2s infinite;
        }
        
        /* تحسين التفاعلية */
        .interactive-element {
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .interactive-element:hover {
            transform: scale(1.05);
        }
        
        /* تحسين الخط */
        * {
            font-family: 'Tajawal', sans-serif;
        }
    </style>
    
    <!-- إضافة خط Tajawal -->
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

def round_to_250(amount):
    """تقريب المبلغ إلى أقرب 250 دينار (أصغر فئة متداولة)"""
    return round(amount / 250) * 250

def calculate_total_cost(color_pages, bw_color_pages, bw_pages, has_cover, 
                        has_empty_last, has_carton, has_nylon, has_paper_holder):
    """حساب التكلفة الإجمالية"""
    total = 0
    total += color_pages * PRICES['color']
    total += bw_color_pages * PRICES['bw_with_color']
    total += bw_pages * PRICES['bw']
    
    if has_cover:
        total += PRICES['cover']
    if has_empty_last:
        total += PRICES['empty_last']
    if has_carton:
        total += PRICES['carton']
    if has_nylon:
        total += PRICES['nylon']
    if has_paper_holder:
        total += PRICES['paper_holder']
    
    # تقريب المجموع النهائي إلى أقرب 250 دينار
    rounded_total = round_to_250(total)
    return total, rounded_total

def main():
    # تعديل العنوان الرئيسي بدون إيموجي
    st.markdown("""
        <div class="premium-header">
            <h1>مكتب طارق الياسين</h1>
            <div class="subtitle">
                نقدم خدمات طباعة احترافية بجودة عالية وكفاءة مميزة
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # تحديث CSS للتنسيق الجديد
    st.markdown("""
        <style>
        /* تحسين تنسيق حقول الإدخال */
        .input-container {
            background: linear-gradient(165deg, rgba(30,30,30,0.9), rgba(15,15,15,0.9));
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }

        .input-container:hover {
            transform: translateY(-5px);
            border-color: rgba(212,175,55,0.4);
        }

        /* تحسين عنوان حقل الإدخال */
        .input-label {
            color: #FFD700;
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 1rem;
            text-align: center;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        /* تحسين حقل الإدخال نفسه */
        .stNumberInput > div > div > input {
            background: rgba(0,0,0,0.4) !important;
            border: 2px solid rgba(212,175,55,0.3) !important;
            border-radius: 15px !important;
            color: #FFD700 !important;
            font-size: 1.3rem !important;
            padding: 1rem !important;
            text-align: center !important;
            width: 100% !important;
        }

        /* تحسين أزرار الزيادة والنقصان */
        .stNumberInput [data-testid="stDecrement"], 
        .stNumberInput [data-testid="stIncrement"] {
            background: linear-gradient(145deg, #1a1a1a, #2d2d2d) !important;
            color: #D4AF37 !important;
            border: 2px solid rgba(212,175,55,0.3) !important;
            border-radius: 12px !important;
        }

        /* تحسين الخيارات الثلاث */
        .printing-options {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(25,25,25,0.95);
            border-radius: 15px;
            border: 1px solid rgba(212,175,55,0.3);
        }

        .option-item {
            text-align: center;
            padding: 1.5rem 2rem;
            border-radius: 10px;
            transition: all 0.3s ease;
            background: rgba(30,30,30,0.95);
            border: 1px solid rgba(212,175,55,0.2);
            flex: 1;
        }

        .option-item:hover {
            transform: translateY(-3px);
            border-color: #D4AF37;
            box-shadow: 0 5px 15px rgba(212,175,55,0.1);
        }

        .option-title {
            color: #D4AF37;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .option-description {
            color: #fff;
            font-size: 0.9rem;
            opacity: 0.9;
        }
        </style>
    """, unsafe_allow_html=True)

    # تحديث قسم تفاصيل الطباعة
    st.markdown('<div class="title-container"><div class="section-title">تفاصيل الطباعة</div></div>', unsafe_allow_html=True)
    
    # تقسيم الصفحة إلى 3 أعمدة متساوية
    col1, col2, col3 = st.columns(3)

    # العمود الأول (يمين) - طباعة ملونة
    with col3:
        st.markdown("""
            <div class="print-section">
                <div class="print-title">طباعة ملونة</div>
            </div>
        """, unsafe_allow_html=True)
        color_pages = st.number_input(
            "",
            min_value=0,
            max_value=500,
            value=0,
            key="color_pages"
        )

    # العمود الثاني (وسط) - طباعة أبيض وأسود
    with col2:
        st.markdown("""
            <div class="print-section">
                <div class="print-title">طباعة أبيض وأسود</div>
            </div>
        """, unsafe_allow_html=True)
        bw_pages = st.number_input(
            "",
            min_value=0,
            max_value=500,
            value=0,
            key="bw_pages"
        )

    # العمود الثالث (يسار)
    with col1:
        st.markdown("""
            <div class="print-section">
                <div class="print-title">طباعة أبيض وأسود وألوان قليلة</div>
            </div>
        """, unsafe_allow_html=True)
        bw_color_pages = st.number_input(
            "",
            min_value=0,
            max_value=500,
            value=0,
            key="bw_color_pages"
        )
    
    st.markdown('</div></div>', unsafe_allow_html=True)

    # إضافة قسم الإضافات الاختيارية
    st.markdown('<div class="title-container"><div class="section-title">الإضافات الاختيارية</div></div>', unsafe_allow_html=True)
    
    # بداية قالب الإضافات
    st.markdown('<div class="additions-container">', unsafe_allow_html=True)

    # عرض الإضافات في صف واحد
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        has_cover = st.checkbox("تصميم غلاف", key="cover")
    with col2:
        has_empty_last = st.checkbox("الصفحة الأخيرة فارغة", key="empty_last")
    with col3:
        has_carton = st.checkbox("كرتون", key="carton")
    with col4:
        has_nylon = st.checkbox("نايلون شفاف", key="nylon")
    with col5:
        has_paper_holder = st.checkbox("حاملة أوراق", key="paper_holder")
    
    # نهاية قالب الإضافات
    st.markdown('</div>', unsafe_allow_html=True)

    # حساب التكلفة
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض النتائج
    st.markdown(f"""
        <div class="premium-results">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div class="result-card" style="
                    background: rgba(0, 0, 0, 0.7);
                    border: 1px solid #FFD700;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 10px;">السعر الكلي</div>
                    <div style="color: #FFD700; font-size: 1.5rem; font-weight: bold;">دينار {exact_total:,}</div>
                </div>
                <div class="result-card" style="
                    background: rgba(0, 0, 0, 0.7);
                    border: 1px solid #FFD700;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 10px;">السعر النهائي</div>
                    <div style="color: #FFD700; font-size: 1.5rem; font-weight: bold;">دينار {rounded_total:,}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # إضافة الشريط في الواجهة
    total_pages = color_pages + bw_color_pages + bw_pages
    if total_pages > 0:
        progress = min(total_pages / 100, 1)
        st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress * 100}%"></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
