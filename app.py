import streamlit as st

# تعريف الأسعار
PRICES = {
    'color': 500,
    'bw_with_color': 300,
    'bw': 150,
    'cover': 2000,
    'empty_last': 500,
    'carton': 1000,
    'nylon': 750,
    'paper_holder': 1500
}

def calculate_total_cost(color_pages, bw_color_pages, bw_pages, has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder):
    """حساب التكلفة الإجمالية"""
    total = 0
    total += color_pages * PRICES['color']
    total += bw_color_pages * PRICES['bw_with_color']
    total += bw_pages * PRICES['bw']
    
    if has_cover: total += PRICES['cover']
    if has_empty_last: total += PRICES['empty_last']
    if has_carton: total += PRICES['carton']
    if has_nylon: total += PRICES['nylon']
    if has_paper_holder: total += PRICES['paper_holder']
    
    rounded_total = round(total / 250) * 250
    return total, rounded_total

def main():
    # تعريف المتغيرات
    has_cover = False
    has_empty_last = False
    has_carton = False
    has_nylon = False
    has_paper_holder = False

    # إضافة CSS
    st.markdown("""
        <style>
        * { text-align: center; }

        .main-section {
            background: #141414;
            border: 1px solid #D4AF37;
            border-radius: 20px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            position: relative;
        }

        .section-title {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: #1a1a1a;
            padding: 5px 25px;
            border-radius: 10px;
            color: #D4AF37;
            font-size: 1.2rem;
            border: 1px solid #D4AF37;
            z-index: 1;
            white-space: nowrap;
        }

        .print-options {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-top: 1.5rem;
        }

        .print-option-title {
            color: #D4AF37;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }

        .stNumberInput {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .stNumberInput > div {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .stNumberInput > div > div > input {
            background: #1a1a1a !important;
            border: 1px solid #D4AF37 !important;
            color: #D4AF37 !important;
            font-size: 1.2rem !important;
            text-align: center !important;
            width: 120px !important;
            border-radius: 10px !important;
            padding: 0.5rem !important;
        }

        .stNumberInput [data-testid="stDecrement"],
        .stNumberInput [data-testid="stIncrement"] {
            background: #1a1a1a !important;
            border: 1px solid #D4AF37 !important;
            color: #D4AF37 !important;
            border-radius: 8px !important;
            width: 35px !important;
            height: 35px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.3s ease;
        }

        .stNumberInput [data-testid="stDecrement"]:hover,
        .stNumberInput [data-testid="stIncrement"]:hover {
            background: #D4AF37 !important;
            color: #000 !important;
        }

        .separator {
            width: 1px;
            height: 100%;
            background: linear-gradient(to bottom, transparent, #D4AF37, transparent);
            margin: 0 auto;
            opacity: 0.3;
        }
        </style>
    """, unsafe_allow_html=True)

    # قسم تفاصيل الطباعة
    st.markdown("""
        <div class="main-section">
            <div class="section-title">📋 تفاصيل الطباعة</div>
            <div class="print-options">
    """, unsafe_allow_html=True)

    col1, sep1, col2, sep2, col3 = st.columns([1, 0.1, 1, 0.1, 1])

    with col1:
        st.markdown('<div class="print-option-title">طباعة ملونة عالية الجودة</div>', unsafe_allow_html=True)
        color_pages = st.number_input("", min_value=0, value=0, key="color_pages", label_visibility="collapsed")

    with sep1:
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="print-option-title">طباعة مع تأثيرات لونية</div>', unsafe_allow_html=True)
        bw_color_pages = st.number_input("", min_value=0, value=0, key="bw_color_pages", label_visibility="collapsed")

    with sep2:
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="print-option-title">طباعة أبيض وأسود</div>', unsafe_allow_html=True)
        bw_pages = st.number_input("", min_value=0, value=0, key="bw_pages", label_visibility="collapsed")

    st.markdown('</div></div>', unsafe_allow_html=True)

    # حساب التكلفة وعرض النتائج
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )

    # إضافة قسم الإضافات
    st.markdown("""
        <div class="main-section">
            <div class="section-title">⭐ الإضافات الاختيارية</div>
            <div class="extras-grid">
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_cover = st.checkbox("⭐ تصميم غلاف ملون فاخر")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_empty_last = st.checkbox("📄 صفحة ختامية مميزة")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_carton = st.checkbox("📦 كرتون فاخر")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_nylon = st.checkbox("✨ نايلون شفاف")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_paper_holder = st.checkbox("📁 حاملة أوراق")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    # عرض النتائج
    st.markdown("""
        <div class="main-section">
            <div class="section-title">💰 تفاصيل التكلفة</div>
            <div class="results-grid">
                <div class="result-card">
                    <div class="result-title">المبلغ الأساسي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
                <div class="result-card">
                    <div class="result-title">المبلغ النهائي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
            </div>
        </div>
    """.format(exact_total, rounded_total), unsafe_allow_html=True)

    # إضافة CSS للأقسام الجديدة
    st.markdown("""
        <style>
        /* تنسيق قسم الإضافات */
        .extras-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .premium-checkbox {
            background: rgba(20,20,20,0.95);
            border: 1px solid #D4AF37;
            border-radius: 15px;
            padding: 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .premium-checkbox:hover {
            transform: translateY(-3px);
            border-color: #FFD700;
            box-shadow: 0 5px 15px rgba(212,175,55,0.1);
        }

        /* تنسيق قسم النتائج */
        .results-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
            margin-top: 1.5rem;
        }

        .result-card {
            background: rgba(20,20,20,0.95);
            border: 1px solid #D4AF37;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .result-card:hover {
            transform: translateY(-3px);
            border-color: #FFD700;
            box-shadow: 0 5px 15px rgba(212,175,55,0.1);
        }

        .result-title {
            color: #D4AF37;
            font-size: 1.2rem;
            margin-bottom: 0.8rem;
        }

        .result-value {
            color: #FFD700;
            font-size: 1.5rem;
            font-weight: 500;
        }

        /* تنسيق مربعات الاختيار */
        .stCheckbox {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .stCheckbox > label {
            color: #D4AF37 !important;
            font-size: 1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()