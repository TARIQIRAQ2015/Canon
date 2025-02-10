import streamlit as st
import streamlit_toggle as tog

# تحديث تكوين الصفحة
st.set_page_config(
    page_title="الطباعة الذهبية | حاسبة الأرباح",
    page_icon="👑",
    layout="wide"
)

# تعريف الأسعار الثابتة
PRICES = {
    'color': 50,  # الصفحة الملونة
    'bw_with_color': 40,  # الأبيض والأسود مع ألوان قليلة
    'bw': 35,  # الأبيض والأسود فقط
    'cover': 250,  # تصميم الغلاف الملون
    'empty_last': 25,  # الصفحة الأخيرة فارغة
    'carton': 250,  # كرتون
    'nylon': 250,  # نايلون شفاف
    'paper_holder': 250,  # حاملة اوراق
}

# تحديث CSS للحصول على تصميم أكثر احترافية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: #ffffff;
        font-family: 'Tajawal', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(120deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.9) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,215,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    .main-header h1 {
        font-size: 3.5rem !important;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FFD700, #FFA500, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header .subtitle {
        font-size: 1.2rem;
        color: #FFD700;
        text-align: center;
        font-weight: 400;
        opacity: 0.9;
    }
    
    .input-section {
        background: rgba(0,0,0,0.4);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255,215,0,0.2);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        backdrop-filter: blur(5px);
    }
    
    .input-section h2 {
        font-size: 1.8rem !important;
        margin-bottom: 1.5rem;
        color: #FFD700;
        text-align: right;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .input-section h2 i {
        font-size: 1.5rem;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stNumberInput {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255,215,0,0.1);
    }
    
    .stNumberInput > div > div > input {
        font-size: 1.1rem !important;
        height: 45px !important;
    }
    
    .stCheckbox {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        border: 1px solid rgba(255,215,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stCheckbox:hover {
        background: rgba(255,215,0,0.1);
        border-color: rgba(255,215,0,0.3);
    }
    
    .results-container {
        background: rgba(0,0,0,0.6);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        border: 2px solid rgba(255,215,0,0.3);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    .total-cost {
        font-size: 2rem !important;
        letter-spacing: 1px;
    }
    
    .exact-cost {
        color: #FFD700 !important;
    }
    
    .rounded-cost {
        color: #00ff88 !important;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #FFD700, transparent);
        margin: 2rem 0;
    }
    
    /* تأثير الخلفية المتحركة */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at center, rgba(255,215,0,0.1) 0%, transparent 70%);
        pointer-events: none;
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
    # تحديث العنوان الرئيسي
    st.markdown("""
        <div class="main-header">
            <h1>👑 الطباعة الذهبية الفاخرة</h1>
            <div class="subtitle">
                نقدم لكم أرقى خدمات الطباعة بجودة استثنائية وتصميم عصري
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # إنشاء عمودين للتخطيط
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="input-section">
                <h2><i class="fas fa-file-alt"></i> تفاصيل الطباعة</h2>
            </div>
        """, unsafe_allow_html=True)
        color_pages = st.number_input("عدد الصفحات الملونة الفاخرة", min_value=0, value=0)
        bw_color_pages = st.number_input("عدد الصفحات المميزة مع لمسات لونية", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات الكلاسيكية", min_value=0, value=0)
    
    with col2:
        st.markdown("""
            <div class="input-section">
                <h2><i class="fas fa-star"></i> الإضافات الحصرية</h2>
            </div>
        """, unsafe_allow_html=True)
        has_cover = st.checkbox("⭐ تصميم غلاف ملون فاخر")
        has_empty_last = st.checkbox("📄 صفحة ختامية مميزة")
        has_carton = st.checkbox("📦 كرتون فاخر")
        has_nylon = st.checkbox("✨ نايلون شفاف عالي الجودة")
        has_paper_holder = st.checkbox("📁 حاملة أوراق مميزة")

    # حساب التكلفة
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض النتائج في قسم مميز
    st.markdown("""
        <div class="results-container">
            <div class="divider"></div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="total-cost exact-cost">
                <div style="font-size: 1rem; opacity: 0.8;">المبلغ الأساسي</div>
                {exact_total:,} دينار
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="total-cost rounded-cost">
                <div style="font-size: 1rem; opacity: 0.8;">المبلغ النهائي</div>
                {rounded_total:,} دينار
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # زر إعادة التعيين
    st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <button class="reset-button">إعادة تعيين الحساب</button>
        </div>
    """, unsafe_allow_html=True)
    if st.button("إعادة تعيين الحساب"):
        st.rerun()

if __name__ == "__main__":
    main() 
