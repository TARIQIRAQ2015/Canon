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

# تحديث CSS للحصول على تصميم فاخر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: #ffffff;
        font-family: 'Tajawal', sans-serif;
    }
    
    .stTitle {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        text-align: center;
        padding: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .stSubheader {
        color: #FFD700 !important;
        font-size: 1.5rem !important;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid #FFD700 !important;
        border-radius: 10px !important;
        padding: 0.5rem !important;
    }
    
    .stCheckbox {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        margin: 0.5rem 0;
    }
    
    .stButton button {
        background: linear-gradient(45deg, #FFD700, #FFA500) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
        padding: 0.7rem 2rem !important;
        border-radius: 25px !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 215, 0, 0.4) !important;
    }
    
    .total-cost {
        font-size: 28px !important;
        font-weight: bold;
        text-align: center;
        padding: 1.5rem;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5);
        border: 2px solid #FFD700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
        margin: 1rem 0;
        backdrop-filter: blur(10px);
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
    # إضافة شعار وعنوان مميز
    st.markdown("""
        <h1 class="stTitle">👑 الطباعة الذهبية الفاخرة</h1>
        <div style="text-align: center; color: #FFD700; margin-bottom: 2rem;">
            نقدم لكم أفضل خدمات الطباعة بجودة عالية
        </div>
    """, unsafe_allow_html=True)
    
    # إنشاء عمودين للتخطيط
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h2 class="stSubheader">📄 عدد الصفحات</h2>', unsafe_allow_html=True)
        color_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
        bw_color_pages = st.number_input("عدد الصفحات الأبيض والأسود مع ألوان قليلة", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات الأبيض والأسود فقط", min_value=0, value=0)
    
    with col2:
        st.markdown('<h2 class="stSubheader">✨ الإضافات الفاخرة</h2>', unsafe_allow_html=True)
        has_cover = st.checkbox("تصميم غلاف ملون فاخر")
        has_empty_last = st.checkbox("صفحة أخيرة فاخرة")
        has_carton = st.checkbox("كرتون فاخر")
        has_nylon = st.checkbox("نايلون شفاف عالي الجودة")
        has_paper_holder = st.checkbox("حاملة أوراق مميزة")

    # حساب التكلفة
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض خط فاصل مميز
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # عرض التكلفة
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="total-cost exact-cost">المبلغ الدقيق: {exact_total:,} دينار</div>', 
                    unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="total-cost rounded-cost">المبلغ النهائي: {rounded_total:,} دينار</div>', 
                    unsafe_allow_html=True)
    
    # زر إعادة التعيين
    st.markdown('<div style="text-align: center; margin-top: 2rem;">', unsafe_allow_html=True)
    if st.button("إعادة تعيين الحساب"):
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
