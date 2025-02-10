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

def main():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

        * {
            font-family: 'Tajawal', sans-serif !important;
        }

        .copy-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }

        .result-card {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 25px;
            margin: 20px 0;
        }

        .timestamp {
            color: #64ffda;
            font-size: 0.9rem;
            margin-bottom: 15px;
        }

        .section-title {
            color: white;
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .detail-row {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            color: white;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .final-cost {
            color: #4CAF50 !important;
            font-size: 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🖨️ حاسبة تكلفة الطباعة")
    
    colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    if colored_pages > 0 or bw_pages > 0:
        total_cost = calculate_cost(colored_pages, bw_pages)
        rounded_cost = round_to_nearest_currency(total_cost)
        current_time = get_iraq_time()
        
        result_text = f"""
            <div class="result-card">
                <div class="timestamp">⏰ {current_time}</div>
                <div class="section-title">📊 ملخص الطلب والتكلفة</div>
                
                <div class="detail-row">
                    <span>عدد الصفحات الملونة:</span>
                    <span>{colored_pages} صفحة</span>
                </div>
                <div class="detail-row">
                    <span>تكلفة الصفحات الملونة:</span>
                    <span>{colored_pages * 50:,} دينار</span>
                </div>
                
                <div class="detail-row">
                    <span>عدد الصفحات بالأبيض والأسود:</span>
                    <span>{bw_pages} صفحة</span>
                </div>
                <div class="detail-row">
                    <span>تكلفة الصفحات بالأبيض والأسود:</span>
                    <span>{bw_pages * 35:,} دينار</span>
                </div>
                
                <div class="detail-row">
                    <span>التكلفة قبل التقريب:</span>
                    <span>{total_cost:,} دينار</span>
                </div>
                <div class="detail-row">
                    <span>التكلفة النهائية (مقربة لأقرب فئة):</span>
                    <span class="final-cost">{rounded_cost:,} دينار</span>
                </div>
            </div>
        """
        
        st.markdown(result_text, unsafe_allow_html=True)
        
        # زر نسخ النتائج
        copy_text = f"""
تفاصيل الطلب:
=============
⏰ {current_time}
عدد الصفحات الملونة: {colored_pages} صفحة
عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة
التكلفة قبل التقريب: {total_cost:,} دينار
التكلفة النهائية: {rounded_cost:,} دينار
        """
        
        if st.button("نسخ النتائج 📋"):
            st.code(copy_text)
            st.success("تم نسخ النتائج بنجاح! يمكنك لصقها في أي مكان.")

if __name__ == "__main__":
    main()
