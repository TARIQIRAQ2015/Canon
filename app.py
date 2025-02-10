import streamlit as st
from datetime import datetime, timedelta

# تعيين إعدادات الصفحة
st.set_page_config(
    page_title="حاسبة تكلفة الطباعة",
    page_icon="🖨️",
    layout="wide"
)

# الأنماط
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    * {
        font-family: 'Tajawal', sans-serif !important;
    }

    .stApp {
        background-color: #1a1a2e;
    }

    .result-card {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }

    .result-title {
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .result-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        color: white;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .result-value {
        color: #64ffda;
        font-weight: bold;
    }

    .final-cost {
        color: #4CAF50 !important;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

def calculate_cost(colored_pages, bw_pages):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50  # 50 دينار للصفحة الملونة
    bw_cost = bw_pages * 35  # 35 دينار للصفحة الأبيض والأسود
    total = colored_cost + bw_cost
    return total

def main():
    st.title("🖨️ حاسبة تكلفة الطباعة")
    
    # إدخال عدد الصفحات
    colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    # حساب التكلفة
    if colored_pages > 0 or bw_pages > 0:
        total_cost = calculate_cost(colored_pages, bw_pages)
        rounded_cost = round(total_cost / 100) * 100  # تقريب إلى أقرب 100
        
        # عرض النتائج
        st.markdown("""
            <div class="result-card">
                <div class="result-title">📋 تفاصيل الطلب</div>
                <div class="result-row">
                    <span>عدد الصفحات الملونة:</span>
                    <span class="result-value">{} صفحة</span>
                </div>
                <div class="result-row">
                    <span>عدد الصفحات بالأبيض والأسود:</span>
                    <span class="result-value">{} صفحة</span>
                </div>
            </div>

            <div class="result-card">
                <div class="result-title">💰 التفاصيل المالية</div>
                <div class="result-row">
                    <span>تكلفة الصفحات الملونة:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>تكلفة الصفحات بالأبيض والأسود:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>التكلفة قبل التقريب:</span>
                    <span class="result-value">{:,} دينار</span>
                </div>
                <div class="result-row">
                    <span>التكلفة النهائية:</span>
                    <span class="result-value final-cost">{:,} دينار</span>
                </div>
            </div>
        """.format(
            colored_pages,
            bw_pages,
            colored_pages * 50,
            bw_pages * 35,
            total_cost,
            rounded_cost
        ), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
