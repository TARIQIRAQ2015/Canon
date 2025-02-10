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
        background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
    }
    
    .card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.45);
    }
    
    .card-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 20px;
        background: linear-gradient(45deg, #64ffda, #48cae4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .info {
        margin: 15px 0;
        font-size: 1.1rem;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .highlight {
        color: #64ffda;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .final-cost {
        color: #4CAF50;
        font-size: 1.5rem;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
    }
    
    .extras-section {
        background: rgba(255, 255, 255, 0.07);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .extras-title {
        color: #64ffda;
        font-size: 1.3rem;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .copy-button {
        position: fixed;
        top: 70px;
        left: 20px;
        padding: 12px 24px;
        background: linear-gradient(45deg, #64ffda, #48cae4);
        color: #1a1a2e;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(100, 255, 218, 0.2);
    }
    
    .copy-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(100, 255, 218, 0.3);
    }
    
    /* تحسين شكل المدخلات */
    .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    .stCheckbox {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 5px 0;
    }
    
    /* تحسين العناوين */
    .stMarkdown {
        color: white !important;
    }
    
    .timestamp {
        color: #64ffda;
        font-size: 1rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 5px;
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
