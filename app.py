import streamlit as st
import streamlit_toggle as tog

# تعيين تكوين الصفحة
st.set_page_config(
    page_title="حاسبة أرباح الطباعة",
    page_icon="🖨️",
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

# تصميم CSS مخصص
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton button {
        background-color: #0066cc;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .total-cost {
        font-size: 24px;
        font-weight: bold;
        color: #0066cc;
        padding: 1rem;
        border-radius: 5px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
    st.title("🖨️ حاسبة أرباح الطباعة")
    
    # إنشاء عمودين للتخطيط
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("عدد الصفحات")
        color_pages = st.number_input("عدد الصفحات الملونة", min_value=0, value=0)
        bw_color_pages = st.number_input("عدد الصفحات الأبيض والأسود مع ألوان قليلة", min_value=0, value=0)
        bw_pages = st.number_input("عدد الصفحات الأبيض والأسود فقط", min_value=0, value=0)
    
    with col2:
        st.subheader("الإضافات الاختيارية")
        has_cover = st.checkbox("تصميم غلاف ملون")
        has_empty_last = st.checkbox("صفحة أخيرة فارغة")
        has_carton = st.checkbox("كرتون")
        has_nylon = st.checkbox("نايلون شفاف")
        has_paper_holder = st.checkbox("حاملة اوراق")

    # حساب التكلفة الإجمالية
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض التكلفة الإجمالية
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<div class="total-cost">المبلغ الدقيق: {exact_total} دينار</div>', 
                    unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="total-cost" style="color: #28a745">المبلغ المقرب: {rounded_total} دينار</div>', 
                    unsafe_allow_html=True)
    
    # زر إعادة التعيين
    if st.button("إعادة تعيين"):
        st.experimental_rerun()

if __name__ == "__main__":
    main() 
