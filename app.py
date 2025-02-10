import streamlit as st
from datetime import datetime
import pytz

# تكوين الصفحة
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
    
    .main-title {
        color: white;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 10px;
        margin-bottom: 30px;
    }
    
    .extras-section {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .extras-title {
        color: #64ffda;
        font-size: 1.1rem;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .summary-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 25px;
        margin-top: 30px;
    }
    
    .summary-header {
        color: #64ffda;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #64ffda;
    }
    
    .summary-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        color: white;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .summary-value {
        color: #64ffda;
        font-weight: bold;
    }
    
    .final-cost {
        color: #4CAF50;
        font-weight: bold;
    }
    
    .timestamp {
        color: #64ffda;
        font-size: 0.9rem;
        text-align: left;
        margin-bottom: 15px;
    }
    
    .copy-button {
        position: fixed;
        top: 70px;
        left: 20px;
        padding: 8px 16px;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 5px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.9rem;
    }
    
    .copy-button:hover {
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* تحسين شكل المدخلات */
    .stNumberInput {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 8px !important;
    }
    
    .stCheckbox {
        color: white !important;
    }
    
    /* تحسين شكل العناوين */
    .stMarkdown {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

def round_to_nearest_250(amount):
    """تقريب المبلغ لأقرب 250 دينار"""
    return round(amount / 250) * 250

def get_iraq_time():
    """الحصول على الوقت في العراق"""
    iraq_tz = pytz.timezone('Asia/Baghdad')
    return datetime.now(iraq_tz).strftime("%Y-%m-%d %I:%M %p")

def main():
    # العنوان الرئيسي
    st.markdown('<div class="main-title">🖨️ حاسبة تكلفة الطباعة</div>', unsafe_allow_html=True)
    
    # المدخلات
    colored_pages = st.number_input("عدد الصفحات الملونة:", min_value=0, value=0)
    bw_pages = st.number_input("عدد الصفحات بالأبيض والأسود:", min_value=0, value=0)
    
    # قسم الإضافات
    st.markdown('<div class="extras-title">🎁 الإضافات</div>', unsafe_allow_html=True)
    carton = st.checkbox("📦 كرتون ملون (250 دينار)")
    holder = st.checkbox("📚 حاملة كتب (250 دينار)")
    nylon = st.checkbox("🔲 نايلون شفاف (250 دينار)")
    
    if colored_pages > 0 or bw_pages > 0:
        # حساب التكاليف
        colored_cost = colored_pages * 50
        bw_cost = bw_pages * 35
        extras_cost = sum(250 for x in [carton, holder, nylon] if x)
        total_cost = colored_cost + bw_cost + extras_cost
        rounded_cost = round_to_nearest_250(total_cost)
        current_time = get_iraq_time()

        # نص النسخ
        copy_text = f"""
ملخص الطباعة:
=============
⏰ وقت الحساب: {current_time}

تفاصيل الطلب:
- عدد الصفحات الملونة: {colored_pages} صفحة ({colored_cost:,} دينار)
- عدد الصفحات بالأبيض والأسود: {bw_pages} صفحة ({bw_cost:,} دينار)

الإضافات المختارة:
{' - كرتون ملون (250 دينار)' if carton else ''}
{' - حاملة كتب (250 دينار)' if holder else ''}
{' - نايلون شفاف (250 دينار)' if nylon else ''}
تكلفة الإضافات: {extras_cost:,} دينار

التكاليف:
- المبلغ الإجمالي: {total_cost:,} دينار
- المبلغ النهائي (مقرب): {rounded_cost:,} دينار"""

        # زر النسخ
        st.markdown(
            f'<button class="copy-button" onclick="navigator.clipboard.writeText(`{copy_text}`)">📋 نسخ النتائج</button>',
            unsafe_allow_html=True
        )

        # عرض النتائج
        st.markdown(f"""
            <div class="summary-card">
                <div class="summary-header">📝 ملخص الطباعة</div>
                <div class="timestamp">⏰ وقت الحساب: {current_time}</div>
                
                <div class="summary-row">
                    <span>عدد الصفحات الملونة</span>
                    <span class="summary-value">{colored_pages} صفحة</span>
                </div>
                <div class="summary-row">
                    <span>تكلفة الصفحات الملونة</span>
                    <span class="summary-value">{colored_cost:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span>عدد الصفحات بالأبيض والأسود</span>
                    <span class="summary-value">{bw_pages} صفحة</span>
                </div>
                <div class="summary-row">
                    <span>تكلفة الصفحات بالأبيض والأسود</span>
                    <span class="summary-value">{bw_cost:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span>تكلفة الإضافات</span>
                    <span class="summary-value">{extras_cost:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span>المبلغ الإجمالي</span>
                    <span class="summary-value">{total_cost:,} دينار</span>
                </div>
                <div class="summary-row">
                    <span>المبلغ النهائي (مقرب لأقرب 250 دينار)</span>
                    <span class="final-cost">{rounded_cost:,} دينار</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
