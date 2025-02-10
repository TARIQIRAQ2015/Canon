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

    # تحديث CSS للتنسيق
    st.markdown("""
        <style>
        /* تنسيق العنوان الرئيسي */
        .header-section {
            background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
            border-radius: 20px;
            padding: 2.5rem;
            margin-bottom: 3rem;
            border: 2px solid rgba(212,175,55,0.3);
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .header-section h1 {
            font-size: 2.5rem;
            color: #D4AF37;
            margin-bottom: 1rem;
        }

        .header-section p {
            color: #FFD700;
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* تنسيق الأقسام */
        .section-container {
            background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
            border: 2px solid rgba(212,175,55,0.3);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            position: relative;
        }

        /* تنسيق العناوين الرئيسية للأقسام */
        .section-title {
            position: absolute;
            top: -15px;
            right: 30px;
            background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
            padding: 5px 20px;
            border-radius: 10px;
            color: #D4AF37;
            font-size: 1.2rem;
            border: 1px solid rgba(212,175,55,0.3);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* تنسيق حقول الإدخال */
        .input-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .input-container {
            background: rgba(25,25,25,0.95);
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .input-container:hover {
            transform: translateY(-3px);
            border-color: #D4AF37;
        }

        /* تنسيق الإضافات */
        .extras-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            margin-top: 2rem;
        }

        .premium-checkbox {
            background: rgba(25,25,25,0.95);
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .premium-checkbox:hover {
            transform: translateY(-2px);
            border-color: #D4AF37;
        }

        /* تنسيق النتائج */
        .results-section {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
            margin: 2rem 0;
        }

        .result-card {
            background: rgba(20,20,20,0.95);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
        }

        /* تنسيق الخدمات */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
        }

        .service-card {
            background: rgba(25,25,25,0.95);
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
        }

        /* تنسيق خلاصة الطلب */
        .summary-section {
            text-align: right;
            direction: rtl;
        }

        .summary-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem 0;
            border-bottom: 1px solid rgba(212,175,55,0.2);
        }

        .summary-title {
            font-size: 1.4rem;
            color: #D4AF37;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .summary-label {
            color: #FFD700;
            font-size: 1.1rem;
        }

        .summary-value {
            color: #fff;
            font-size: 1.1rem;
        }

        /* تحسينات عامة */
        .emoji-icon {
            font-size: 1.2rem;
        }

        /* تنسيق حقول الأرقام */
        .stNumberInput > div > div > input {
            background: rgba(30,30,30,0.95) !important;
            border: 1px solid rgba(212,175,55,0.3) !important;
            color: #fff !important;
            text-align: center !important;
            font-size: 1.1rem !important;
        }

        /* تنسيق مربعات الاختيار */
        .stCheckbox {
            background: transparent !important;
        }

        .stCheckbox > label {
            color: #fff !important;
            font-size: 1rem !important;
        }

        /* تأثيرات التحويم */
        .section-container:hover {
            box-shadow: 0 8px 25px rgba(212,175,55,0.1);
        }

        .service-card:hover {
            transform: translateY(-3px);
            border-color: #D4AF37;
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

if __name__ == "__main__":
    main()