import streamlit as st

# تعيين تكوين الصفحة
st.set_page_config(
    page_title="Premium Printing | الطباعة الفاخرة",
    page_icon="👑",
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

# تصميم CSS جديد وفاخر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    
    /* تنسيق عام */
    * {
        font-family: 'Tajawal', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #000000, #1a1a1a);
        color: #ffffff;
    }
    
    /* تنسيق الهيدر */
    .premium-header {
        background: linear-gradient(to right, rgba(0,0,0,0.9), rgba(20,20,20,0.9));
        padding: 3rem 2rem;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 3rem;
        border-bottom: 2px solid #B8860B;
    }
    
    .premium-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(184,134,11,0.2), transparent 70%);
        pointer-events: none;
    }
    
    .premium-header h1 {
        font-size: 4rem !important;
        font-weight: 800;
        background: linear-gradient(45deg, #FFD700, #B8860B, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .premium-header .subtitle {
        color: #D4AF37;
        font-size: 1.3rem;
        font-weight: 500;
        opacity: 0.9;
    }
    
    /* تنسيق الأقسام */
    .premium-section {
        background: rgba(20,20,20,0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(184,134,11,0.3);
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    .premium-section h2 {
        color: #D4AF37;
        font-size: 2rem !important;
        font-weight: 700;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(184,134,11,0.3);
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    /* تنسيق حقول الإدخال */
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(184,134,11,0.3) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        font-size: 1.1rem !important;
        height: 3rem !important;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 10px rgba(212,175,55,0.3) !important;
    }
    
    /* تنسيق مربعات الاختيار */
    .premium-checkbox {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(184,134,11,0.2);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }
    
    .premium-checkbox:hover {
        background: rgba(184,134,11,0.1);
        border-color: rgba(184,134,11,0.4);
        transform: translateY(-2px);
    }
    
    /* تنسيق النتائج */
    .premium-results {
        background: linear-gradient(135deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
        border-radius: 25px;
        padding: 2.5rem;
        margin-top: 3rem;
        border: 2px solid rgba(184,134,11,0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        text-align: center;
    }
    
    .result-card {
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(184,134,11,0.3);
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(184,134,11,0.2);
    }
    
    .result-label {
        color: #D4AF37;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    .result-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* تنسيق الزر */
    .premium-button {
        background: linear-gradient(45deg, #B8860B, #D4AF37) !important;
        color: #000000 !important;
        font-weight: 700 !important;
        padding: 1rem 3rem !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 5px 15px rgba(184,134,11,0.3) !important;
        transition: all 0.3s ease !important;
        margin-top: 2rem !important;
    }
    
    .premium-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(184,134,11,0.4) !important;
    }
    
    .reset-button-container {
        margin-top: 2rem;
        text-align: center;
    }
    
    .premium-reset-button {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d);
        color: #D4AF37;
        font-family: 'Tajawal', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.8rem 2.5rem;
        border: 2px solid #D4AF37;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .premium-reset-button:hover {
        background: linear-gradient(45deg, #D4AF37, #B8860B);
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212,175,55,0.3);
    }
    
    .premium-reset-button i {
        margin-left: 8px;
    }
    </style>
""", unsafe_allow_html=True)

def round_to_nearest_250(amount):
    """تقريب المبلغ إلى أقرب 250 دينار"""
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
    rounded_total = round_to_nearest_250(total)
    return total, rounded_total

def main():
    # العنوان الرئيسي
    st.markdown("""
        <div class="premium-header">
            <h1>👑 الطباعة الذهبية الفاخرة</h1>
            <div class="subtitle">
                نرتقي بمشاريعكم إلى آفاق جديدة من التميز والإبداع
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # الأقسام الرئيسية
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="premium-section">
                <h2>📚 خدمات الطباعة الفاخرة</h2>
            </div>
        """, unsafe_allow_html=True)
        
        color_pages = st.number_input("عدد الصفحات الملونة الفاخرة", min_value=0, value=0)
        bw_color_pages = st.number_input("عدد الصفحات المميزة مع لمسات لونية", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات الكلاسيكية", min_value=0, value=0)
    
    with col2:
        st.markdown("""
            <div class="premium-section">
                <h2>✨ الإضافات الحصرية</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_cover = st.checkbox("⭐ تصميم غلاف ملون فاخر")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_empty_last = st.checkbox("📄 صفحة ختامية مميزة")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_carton = st.checkbox("📦 كرتون فاخر")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_nylon = st.checkbox("✨ نايلون شفاف عالي الجودة")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_paper_holder = st.checkbox("📁 حاملة أوراق مميزة")
        st.markdown('</div>', unsafe_allow_html=True)

    # حساب التكلفة
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض النتائج
    st.markdown("""
        <div class="premium-results">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div class="result-card">
                    <div class="result-label">المبلغ الأساسي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
                <div class="result-card">
                    <div class="result-label">المبلغ النهائي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
            </div>
            
            <div class="reset-button-container">
                <button class="premium-reset-button" id="reset-btn">
                    <i class="fas fa-sync-alt"></i>
                    إعادة تعيين الحساب
                </button>
            </div>
        </div>
    """.format(exact_total, rounded_total), unsafe_allow_html=True)
    
    # إضافة زر إعادة التعيين المخفي لتنفيذ الوظيفة
    if st.button("إعادة تعيين", key="reset_button", type="primary"):
        st.rerun()

if __name__ == "__main__":
    main() 
