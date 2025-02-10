import streamlit as st
from datetime import datetime, timedelta
import pytz

def round_to_nearest_currency(amount):
    """تقريب المبلغ لأقرب فئة عملة متداولة"""
    currency_denominations = [250, 500, 1000]
    min_diff = float('inf')
    rounded_amount = amount
    
    for denom in currency_denominations:
        quotient = round(amount / denom)
        rounded = quotient * denom
        diff = abs(amount - rounded)
        if diff < min_diff:
            min_diff = diff
            rounded_amount = rounded
    
    return rounded_amount

def get_iraq_time():
    """الحصول على الوقت في العراق"""
    iraq_tz = pytz.timezone('Asia/Baghdad')
    return datetime.now(iraq_tz).strftime("%Y-%m-%d %I:%M %p")

def calculate_cost(colored_pages, bw_pages):
    """حساب التكلفة الإجمالية"""
    colored_cost = colored_pages * 50
    bw_cost = bw_pages * 35
    total = colored_cost + bw_cost
    return total

st.set_page_config(page_title="حاسبة تكلفة الطباعة", page_icon="🖨️", layout="wide")

# إضافة CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    * {
        font-family: 'Tajawal', sans-serif !important;
    }

    .stApp {
        background-color: #1a1a2e;
    }

    .main-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .card-header {
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #64ffda;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .info-label {
        color: rgba(255,255,255,0.9);
    }

    .info-value {
        color: #64ffda;
        font-weight: bold;
    }

    .final-value {
        color: #4CAF50 !important;
        font-size: 1.2rem;
    }

    .timestamp {
        color: #64ffda;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("🖨️ حاسبة تكلفة الطباعة")
    
    colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    if colored_pages > 0 or bw_pages > 0:
        total_cost = calculate_cost(colored_pages, bw_pages)
        rounded_cost = round_to_nearest_currency(total_cost)
        current_time = get_iraq_time()

        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
                <div class="main-card">
                    <div class="timestamp">⏰ {current_time}</div>
                    <div class="card-header">📊 ملخص الطلب والتكلفة</div>
                    
                    <div class="info-row">
                        <span class="info-label">عدد الصفحات الملونة</span>
                        <span class="info-value">{colored_pages} صفحة</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">تكلفة الصفحات الملونة</span>
                        <span class="info-value">{colored_pages * 50:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">عدد الصفحات بالأبيض والأسود</span>
                        <span class="info-value">{bw_pages} صفحة</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">تكلفة الصفحات بالأبيض والأسود</span>
                        <span class="info-value">{bw_pages * 35:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">التكلفة قبل التقريب</span>
                        <span class="info-value">{total_cost:,} دينار</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">التكلفة النهائية</span>
                        <span class="final-value">{rounded_cost:,} دينار</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # نص النسخ
        copy_text = f"""
تفاصيل الطلب:
=============
⏰ {current_time}
عدد الصفحات الملونة: {colored_pages} صفحة
عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة
التكلفة قبل التقريب: {total_cost:,} دينار
التكلفة النهائية: {rounded_cost:,} دينار"""

        if st.button("نسخ النتائج 📋"):
            st.code(copy_text)
            st.success("تم نسخ النتائج بنجاح! يمكنك لصقها في أي مكان.")

if __name__ == "__main__":
    main()
