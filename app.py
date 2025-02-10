import streamlit as st
import pyperclip

# تعيين تكوين الصفحة
st.set_page_config(
    page_title="مكتب طارق الياسين",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تعريف الأسعار الثابتة
PRICES = {
    'color': 50,
    'bw_with_color': 40,
    'bw': 35,
    'cover': 250,
    'empty_last': 25,
    'carton': 250,
    'nylon': 250,
    'paper_holder': 250,
}

# تصميم CSS جديد وفاخر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    
    /* تحسين الخطوط العامة */
    * {
        font-family: 'Tajawal', sans-serif !important;
        letter-spacing: 0.3px;
    }
    
    .main {
        background: linear-gradient(135deg, #000000, #1a1a1a);
        color: #ffffff;
        position: relative;
        overflow: hidden;
    }
    
    .main::before {
        content: '';
        position: fixed;
        width: 200%;
        height: 200%;
        top: -50%;
        left: -50%;
        z-index: -1;
        background: 
            radial-gradient(circle at 30% 30%, rgba(212,175,55,0.05) 0%, transparent 30%),
            radial-gradient(circle at 70% 70%, rgba(212,175,55,0.05) 0%, transparent 30%),
            radial-gradient(circle at 50% 50%, rgba(212,175,55,0.05) 0%, transparent 50%),
            linear-gradient(45deg, transparent 48%, rgba(212,175,55,0.02) 50%, transparent 52%);
        animation: gradientBG 15s ease infinite;
    }
    
    /* تأثير متحرك للخلفية */
    @keyframes gradientBG {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* تنسيق الهيدر */
    .premium-header {
        background: linear-gradient(to right, rgba(0,0,0,0.9), rgba(20,20,20,0.9));
        padding: 3rem 2rem;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 3rem;
        border-bottom: 2px solid #B8860B;
    }
    
    .premium-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(184,134,11,0.2), transparent 70%);
        pointer-events: none;
    }
    
    /* تحسين العنوان الرئيسي */
    .premium-header h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #D4AF37 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }
    
    .premium-header .subtitle {
        font-size: 1.5rem !important;
        color: #FFD700 !important;
        font-weight: 500 !important;
        text-align: center !important;
    }
    
    /* تنسيق الأقسام */
    .premium-section {
        background: rgba(20,20,20,0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(184,134,11,0.3);
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .premium-section::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(212,175,55,0.1), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }
    
    .premium-section h2 {
        color: #D4AF37;
        font-size: 2rem !important;
        font-weight: 700;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(184,134,11,0.3);
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    /* تنسيق حقول الإدخال */
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid #D4AF37 !important;
        color: #ffffff !important;
        font-size: 1.3rem !important;
        height: 2.5rem !important;
    }
    
    .stNumberInput > div > div > input:focus {
        box-shadow: 0 0 10px rgba(212,175,55,0.3) !important;
        border-color: #FFD700 !important;
    }
    
    /* تنسيق مربعات الاختيار */
    .premium-checkbox {
        background: linear-gradient(145deg, rgba(25,25,25,0.95), rgba(35,35,35,0.95));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 1.5rem 2rem;
        margin: 1.2rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .premium-checkbox:hover {
        transform: translateY(-3px);
        border-color: rgba(212,175,55,0.5);
        box-shadow: 0 8px 20px rgba(212,175,55,0.2);
    }
    
    .premium-checkbox label {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        color: #D4AF37 !important;
        text-align: center !important;
    }
    
    .stCheckbox {
        scale: 1.2;
    }
    
    /* تنسيق النتائج */
    .premium-results {
        background: linear-gradient(135deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
        border-radius: 25px;
        padding: 2.5rem;
        margin-top: 3rem;
        border: 2px solid rgba(184,134,11,0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        text-align: center;
    }
    
    .result-card {
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(184,134,11,0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        animation: cardPulse 2s ease-in-out infinite;
    }
    
    @keyframes cardPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    /* تحسين نص النتائج */
    .result-label {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #D4AF37 !important;
        text-align: center !important;
    }
    
    .result-value {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #FFD700 !important;
        text-align: center !important;
    }
    
    /* تنسيق الزر */
    .premium-button {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d);
        color: #D4AF37;
        font-family: 'Tajawal', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.8rem 2.5rem;
        border: 2px solid #D4AF37;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .premium-button:hover {
        background: linear-gradient(45deg, #D4AF37, #B8860B);
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212,175,55,0.3);
    }
    
    .reset-button-container {
        margin-top: 2rem;
        text-align: center;
    }
    
    .premium-reset-button {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d);
        color: #D4AF37;
        font-family: 'Tajawal', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.8rem 2.5rem;
        border: 2px solid #D4AF37;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .premium-reset-button:hover {
        background: linear-gradient(45deg, #D4AF37, #B8860B);
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212,175,55,0.3);
    }
    
    .premium-reset-button i {
        margin-left: 8px;
    }
    
    div[data-testid="stButton"] {
        text-align: center;
        margin-top: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d) !important;
        color: #D4AF37 !important;
        font-family: 'Tajawal', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        padding: 0.8rem 2.5rem !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 50px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #D4AF37, #B8860B) !important;
        color: #000000 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212,175,55,0.3) !important;
    }
    
    html {
        scroll-behavior: smooth;
        scroll-padding-top: 2rem;
    }
    
    /* تحسين أزرار التقليل والزيادة */
    .stNumberInput [data-testid="stDecrement"], 
    .stNumberInput [data-testid="stIncrement"] {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d) !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 5px !important;
        transition: all 0.3s ease;
    }
    
    .stNumberInput [data-testid="stDecrement"]:hover, 
    .stNumberInput [data-testid="stIncrement"]:hover {
        background: linear-gradient(45deg, #D4AF37, #B8860B) !important;
        color: #000000 !important;
    }
    
    /* تحسين أيقونات العناوين */
    .section-icon {
        color: #D4AF37;
        font-size: 1.5rem;
        margin-left: 0.5rem;
        background: linear-gradient(45deg, #FFD700, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* تنسيق أيقونات الخيارات */
    .premium-checkbox .stCheckbox label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .premium-checkbox .stCheckbox label::before {
        color: #D4AF37;
    }
    
    /* تحديث CSS لفصل تنسيق الإيموجيات عن العناوين */
    .section-title {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: #D4AF37 !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }
    
    /* تنسيق الإيموجيات */
    .emoji-icon {
        font-size: 1.5rem;
        margin-left: 0.5rem;
        -webkit-text-fill-color: initial;  /* إزالة التأثير الذهبي من الإيموجيات */
    }

    /* تنسيق محسن لحقول الإدخال */
    .input-container {
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        position: relative;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* تنسيق عنوان حقل الإدخال */
    .input-label {
        color: #FFD700;
        font-weight: bold;
        text-align: center;
        margin-bottom: 15px;
        font-size: 1.1rem;
    }

    /* تنسيق حقل الإدخال نفسه */
    .stNumberInput {
        width: 80% !important;
        margin: 0 auto;
    }

    /* تنسيق الأرقام في حقل الإدخال */
    .stNumberInput input {
        background: rgba(0, 0, 0, 0.5) !important;
        border: 1px solid #FFD700 !important;
        color: #FFD700 !important;
        text-align: center !important;
        font-size: 1.2rem !important;
        padding: 10px !important;
        border-radius: 10px !important;
        width: 100% !important;
        transition: all 0.3s ease;
    }

    .stNumberInput input:focus {
        border-color: #FFD700 !important;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.3) !important;
        background: rgba(0, 0, 0, 0.7) !important;
    }

    /* تنسيق أزرار + و - */
    .stNumberInput button {
        background: rgba(255, 215, 0, 0.1) !important;
        border: 1px solid #FFD700 !important;
        color: #FFD700 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }

    .stNumberInput button:hover {
        background: rgba(255, 215, 0, 0.2) !important;
        transform: translateY(-2px);
    }

    /* تحسين العنوان الرئيسي */
    .premium-header h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #D4AF37 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }

    .premium-header .subtitle {
        font-size: 1.5rem !important;
        color: #FFD700 !important;
        font-weight: 500 !important;
        text-align: center !important;
    }

    /* تحسين عناوين الأقسام */
    .section-title {
        background: rgba(0, 0, 0, 0.9);
        border: 2px solid #FFD700;
        border-radius: 15px;
        color: #FFD700;
        padding: 8px 25px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 10px auto;
        position: relative;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center !important;
    }

    /* تحسين بطاقات المعلومات */
    .info-card h3 {
        font-size: 1.3rem !important;
        color: #D4AF37 !important;
        margin-bottom: 1rem !important;
        font-weight: 700 !important;
        text-shadow: 
            0 2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.2);
        transform: perspective(1000px) translateZ(25px);
    }

    .info-card p {
        font-size: 1.2rem !important;
        color: #fff !important;
        line-height: 1.6 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* تحسين الخيارات */
    .premium-checkbox label {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        color: #D4AF37 !important;
        text-align: center !important;
    }

    /* تحسين التجاوب مع الأجهزة */
    @media (max-width: 768px) {
        .premium-header {
            padding: 2rem 1rem;
        }

        .premium-section {
            padding: 1.5rem;
        }

        .info-cards {
            grid-template-columns: 1fr;
        }

        .result-card {
            padding: 1.5rem;
        }
    }

    /* تأثيرات 3D إضافية */
    .premium-section, .info-card, .result-card {
        transform-style: preserve-3d;
        perspective: 1000px;
    }

    .premium-section:hover, .info-card:hover, .result-card:hover {
        transform: translateZ(20px) scale(1.02);
    }

    /* تحسين القراءة */
    * {
        letter-spacing: 0.3px;
        word-spacing: 1px;
    }

    /* تحسين مظهر حقول الإدخال */
    .premium-input {
        background: linear-gradient(165deg, rgba(25,25,25,0.95), rgba(15,15,15,0.95));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 1.8rem;
        margin: 1.2rem 0;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            inset 0 2px 10px rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }

    .premium-input:hover {
        transform: translateY(-3px);
        border-color: rgba(212,175,55,0.5);
        box-shadow: 
            0 15px 30px rgba(0,0,0,0.3),
            inset 0 2px 15px rgba(255,255,255,0.1);
    }

    .input-icon {
        font-size: 1.4rem;
        margin-left: 1rem;
        vertical-align: middle;
    }

    .input-label {
        display: flex;
        align-items: center;
        font-size: 1.2rem;
        font-weight: 600;
        color: #D4AF37;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* تحسين العنوان الرئيسي */
    .premium-header h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #D4AF37 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }

    .premium-header .subtitle {
        font-size: 1.5rem !important;
        color: #FFD700 !important;
        font-weight: 500 !important;
        text-align: center !important;
    }

    /* تحسين عنوان القسم */
    .section-title {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: #D4AF37 !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }

    .emoji-icon {
        font-size: 1.8rem;
        margin-left: 0.5rem;
    }

    /* تحديث CSS للزر */
    .back-to-top {
        position: fixed;
        bottom: 30px;
        left: 30px;
        width: 55px;
        height: 55px;
        background: linear-gradient(145deg, rgba(26,26,26,0.9), rgba(45,45,45,0.9));
        border: 2px solid rgba(212,175,55,0.5);
        border-radius: 50%;
        display: none;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        z-index: 9999;
        box-shadow: 
            0 5px 15px rgba(0,0,0,0.3),
            inset 0 2px 10px rgba(255,255,255,0.1);
        backdrop-filter: blur(5px);
    }

    .back-to-top::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: -1;
    }

    .back-to-top::after {
        content: '';
        width: 15px;
        height: 15px;
        border-left: 3px solid #D4AF37;
        border-top: 3px solid #D4AF37;
        transform: rotate(45deg);
        margin-bottom: -5px;
        transition: all 0.3s ease;
    }

    .back-to-top:hover {
        transform: translateY(-5px) scale(1.05);
        border-color: #D4AF37;
        box-shadow: 
            0 8px 25px rgba(212,175,55,0.3),
            inset 0 2px 15px rgba(255,255,255,0.2);
    }

    .back-to-top:hover::before {
        opacity: 0.1;
    }

    .back-to-top:hover::after {
        border-color: #FFD700;
        transform: rotate(45deg) scale(1.2);
    }

    .summary-section {
        background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
        border: 2px solid rgba(212,175,55,0.3);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .summary-title {
        font-size: 1.6rem !important;
        font-weight: 600 !important;
        color: #D4AF37 !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }

    .summary-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(212,175,55,0.2);
    }

    .summary-item:last-child {
        border-bottom: none;
    }

    .summary-label {
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        color: #FFD700 !important;
    }

    .summary-value {
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        color: #FFFFFF !important;
    }

    /* تعديل CSS للتنسيق الأفقي */
    .horizontal-layout {
        display: flex;
        flex-direction: column;
        gap: 2rem;
        padding: 2rem 0;
    }

    .section-container {
        background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
        border: 2px solid rgba(212,175,55,0.3);
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        position: relative;
    }

    .input-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-top: 1.5rem;
    }

    .extras-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .services-section {
        margin-top: 4rem;
        padding: 2rem;
        background: linear-gradient(165deg, rgba(30,30,30,0.9), rgba(15,15,15,0.9));
        border-radius: 20px;
        border: 1px solid rgba(212,175,55,0.2);
    }

    .services-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        max-width: 800px;
        margin: 0 auto;
    }

    .service-card {
        background: linear-gradient(145deg, rgba(25,25,25,0.95), rgba(35,35,35,0.95));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.4s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .service-card:hover {
        transform: translateY(-5px);
        border-color: #D4AF37;
        box-shadow: 0 8px 25px rgba(212,175,55,0.2);
    }

    .service-card h3 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #D4AF37 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }

    .service-card p {
        font-size: 1.2rem !important;
        font-weight: 400 !important;
        color: #FFFFFF !important;
        text-align: center !important;
        line-height: 1.6 !important;
    }

    /* تنسيق عام للنصوص */
    * {
        text-align: center;
    }

    /* تنسيق القسم الرئيسي */
    .main-container {
        display: flex;
        flex-direction: column;
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

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
        padding: 8px 25px;
        border-radius: 12px;
        color: #D4AF37;
        font-size: 1.2rem;
        font-weight: 600;
        border: 1px solid rgba(212,175,55,0.3);
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        transform: none !important;
        text-align: center !important;
    }

    /* تنسيق حقول الإدخال */
    .input-container {
        background: rgba(25,25,25,0.95);
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        margin-top: 1.5rem;
    }

    .input-label {
        color: #FFD700;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    /* تنسيق حقول الأرقام */
    .stNumberInput > div > div > input {
        background: rgba(0,0,0,0.4) !important;
        border: 2px solid rgba(212,175,55,0.3) !important;
        border-radius: 15px !important;
        color: #FFD700 !important;
        font-size: 1.3rem !important;
        padding: 1.2rem !important;
        text-align: center !important;
        width: 100% !important;
    }

    .stNumberInput > div > div > input:focus {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 20px rgba(212,175,55,0.2) !important;
        transform: translateY(-2px);
    }

    /* تنسيق الخيارات الثلاث */
    .printing-options {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 2rem;
        padding: 1.5rem;
        background: rgba(25,25,25,0.95);
        border-radius: 15px;
        border: 1px solid rgba(212,175,55,0.3);
    }

    .option-item {
        text-align: center;
        padding: 1.5rem 2rem;
        border-radius: 10px;
        transition: all 0.3s ease;
        background: rgba(30,30,30,0.95);
        border: 1px solid rgba(212,175,55,0.2);
        flex: 1;
    }

    .option-item:hover {
        transform: translateY(-3px);
        border-color: #D4AF37;
        box-shadow: 0 5px 15px rgba(212,175,55,0.1);
    }

    .option-title {
        color: #D4AF37;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .option-description {
        color: #fff;
        font-size: 0.9rem;
        opacity: 0.9;
    }

    /* تنسيق قسم الإضافات الاختيارية */
    .extras-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .premium-checkbox {
        background: linear-gradient(145deg, rgba(25,25,25,0.95), rgba(35,35,35,0.95));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    .premium-checkbox:hover {
        transform: translateY(-3px);
        border-color: #D4AF37;
        box-shadow: 0 5px 15px rgba(212,175,55,0.1);
    }

    .premium-checkbox label {
        color: #D4AF37 !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        text-align: center !important;
    }

    /* تحسين مظهر مربعات الاختيار */
    .stCheckbox {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .stCheckbox > div {
        display: flex;
        justify-content: center;
    }

    .stCheckbox label {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
    }

    /* تحديث CSS لتصحيح انحراف النصوص */
    .section-container {
        position: relative;
        padding-top: 3rem;
    }

    .section-title {
        position: absolute;
        top: -15px;
        right: 30px;
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        padding: 8px 25px;
        border-radius: 12px;
        color: #D4AF37;
        font-size: 1.2rem;
        font-weight: 600;
        border: 1px solid rgba(212,175,55,0.3);
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        transform: none !important;
        text-align: center !important;
    }

    /* تحسين عناوين حقول الإدخال */
    .input-label {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        padding: 10px 20px;
        border-radius: 10px;
        color: #D4AF37;
        font-size: 1.2rem;
        font-weight: 500;
        border: 1px solid rgba(212,175,55,0.3);
        margin-bottom: 1.5rem;
        transform: none !important;
        text-align: center !important;
        width: auto !important;
    }

    /* تحسين عناوين الخيارات */
    .option-title {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        padding: 8px 20px;
        border-radius: 8px;
        color: #D4AF37;
        font-size: 1.1rem;
        font-weight: 500;
        border: 1px solid rgba(212,175,55,0.3);
        margin-bottom: 1rem;
        transform: none !important;
        text-align: center !important;
    }

    /* تأكيد على عدم وجود انحراف في جميع النصوص */
    * {
        transform: none !important;
        text-align: center !important;
    }

    /* تنسيق عنوان تفاصيل الطباعة */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        text-align: center !important;
        color: #FFD700 !important;
        padding: 1rem 0 !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
    }
    
    /* لضمان توسيط جميع العناوين */
    [data-testid="stMarkdownContainer"] {
        text-align: center !important;
    }

    /* الحاوية الرئيسية للعنوان */
    .title-container {
        text-align: center !important;
        width: 100% !important;
        direction: rtl !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto !important;
    }

    /* إخفاء أزرار المشاركة والتحرير */
    .stDeployButton, [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* إخفاء القائمة العلوية بالكامل */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* إخفاء زر القائمة الجانبية */
    button[kind="header"] {
        display: none !important;
    }
    
    /* إخفاء أي عناصر إضافية في الهيدر */
    .stApp header {
        display: none !important;
    }

    /* تنسيق شامل للمحاذاة */
    .stApp {
        direction: rtl !important;
    }

    /* تنسيق حاوية العنوان */
    .title-container {
        text-align: center !important;
        width: 100% !important;
        direction: rtl !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto !important;
    }

    /* تنسيق العنوان نفسه */
    .section-title {
        background: rgba(0, 0, 0, 0.9);
        border: 2px solid #FFD700;
        border-radius: 15px;
        color: #FFD700;
        padding: 8px 25px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 10px auto;
        position: relative;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center !important;
    }

    /* تنسيق الأعمدة */
    .stColumn {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* تنسيق حاويات الإدخال */
    .input-container {
        text-align: center !important;
        margin: 0 auto !important;
    }

    /* تنسيق عناصر streamlit */
    [data-testid="stMarkdownContainer"] {
        text-align: center !important;
    }

    /* تنسيق حاوية الأزرار */
    .number-controls {
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 8px;
        margin-bottom: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
        width: fit-content;
    }

    /* تنسيق الأزرار نفسها */
    .number-controls button {
        background: rgba(255, 215, 0, 0.1) !important;
        border: 1px solid #FFD700 !important;
        color: #FFD700 !important;
        width: 35px !important;
        height: 35px !important;
        border-radius: 8px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        font-size: 1.2rem !important;
        padding: 0 !important;
    }

    .number-controls button:hover {
        background: rgba(255, 215, 0, 0.2) !important;
        transform: translateY(-2px);
    }

    /* تنسيق النقطة بين الأزرار */
    .number-controls .dot {
        color: #FFD700;
        font-size: 1.2rem;
        margin: 0 5px;
    }

    /* تنسيق أيقونة المعلومات */
    .number-controls .info-icon {
        color: #FFD700;
        font-size: 1.2rem;
        margin-left: 5px;
        cursor: help;
    }
    </style>

    <!-- زر العودة للأعلى -->
    <a href="#top" class="back-to-top" id="backToTop"></a>

    <script>
    window.onscroll = function() {
        var btn = document.getElementById("backToTop");
        if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
            btn.style.display = "flex";
        } else {
            btn.style.display = "none";
        }
    }
    </script>
""", unsafe_allow_html=True)

def round_to_250(amount):
    """تقريب المبلغ إلى أقرب 250 دينار (أصغر فئة متداولة)"""
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
    rounded_total = round_to_250(total)
    return total, rounded_total

def show_summary(color_pages, bw_color_pages, bw_pages, has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder, exact_total):
    # التحقق من عدد الصفحات
    if color_pages > 500 or bw_color_pages > 500 or bw_pages > 500:
        st.error("⚠️ عذراً، لا يمكن طباعة أكثر من 500 صفحة في النوع الواحد")
        return

    # تجهيز نص الملخص
    summary_text = f"""═══════════════════════════════════════
           ملخص الطلب ✨           
═══════════════════════════════════════"""

    # إضافة تفاصيل الصفحات مع الأسعار
    if color_pages > 0:
        price = color_pages * PRICES['color']
        summary_text += f"""
🎨 طباعة ملونة:
   • عدد الصفحات: {color_pages} صفحة
   • سعر الصفحة: {PRICES['color']} دينار
   • المجموع: {price:,} دينار
───────────────────────────────────────"""

    if bw_color_pages > 0:
        price = bw_color_pages * PRICES['bw_with_color']
        summary_text += f"""
🖌️ طباعة أبيض وأسود وقليل ألوان:
   • عدد الصفحات: {bw_color_pages} صفحة
   • سعر الصفحة: {PRICES['bw_with_color']} دينار
   • المجموع: {price:,} دينار
───────────────────────────────────────"""

    if bw_pages > 0:
        price = bw_pages * PRICES['bw']
        summary_text += f"""
طباعة أبيض وأسود:
   • عدد الصفحات: {bw_pages} صفحة
   • سعر الصفحة: {PRICES['bw']} دينار
   • المجموع: {price:,} دينار
───────────────────────────────────────"""

    # إضافة الإضافات المختارة مع الأسعار
    extras = []
    extras_total = 0
    if has_cover: 
        extras.append(("تصميم غلاف ملون", PRICES['cover']))
        extras_total += PRICES['cover']
    if has_empty_last: 
        extras.append(("الصفحة الاخيرة فارغة", PRICES['empty_last']))
        extras_total += PRICES['empty_last']
    if has_carton: 
        extras.append(("كرتون", PRICES['carton']))
        extras_total += PRICES['carton']
    if has_nylon: 
        extras.append(("نايلون شفاف", PRICES['nylon']))
        extras_total += PRICES['nylon']
    if has_paper_holder: 
        extras.append(("حاملة أوراق", PRICES['paper_holder']))
        extras_total += PRICES['paper_holder']

    if extras:
        summary_text += """
الإضافات المختارة:"""
        for extra, price in extras:
            summary_text += f"""
   • {extra}: {price} دينار"""
        summary_text += f"""
   • مجموع الإضافات: {extras_total} دينار
───────────────────────────────────────"""

    # إضافة الأسعار النهائية
    rounded_total = round_to_250(exact_total)
    summary_text += f"""
💵 السعر الكلي: {exact_total} دينار
💰 السعر بعد التقريب للفئة المناسبة: {rounded_total} دينار
═══════════════════════════════════════"""

    # عرض الملخص باستخدام st.code
    st.code(summary_text, language=None)

def main():
    # تعديل العنوان الرئيسي بدون إيموجي
    st.markdown("""
        <div class="premium-header">
            <h1>مكتب طارق الياسين</h1>
            <div class="subtitle">
                نقدم خدمات طباعة احترافية بجودة عالية وكفاءة مميزة
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # تحديث CSS للتنسيق الجديد
    st.markdown("""
        <style>
        /* تحسين تنسيق حقول الإدخال */
        .input-container {
            background: linear-gradient(165deg, rgba(30,30,30,0.9), rgba(15,15,15,0.9));
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }

        .input-container:hover {
            transform: translateY(-5px);
            border-color: rgba(212,175,55,0.4);
        }

        /* تحسين عنوان حقل الإدخال */
        .input-label {
            color: #FFD700;
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 1rem;
            text-align: center;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        /* تحسين حقل الإدخال نفسه */
        .stNumberInput {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* تحسين الأرقام في حقل الإدخال */
        .stNumberInput input {
            text-align: center !important;
            width: 100% !important;
        }

        /* تحسين الخيارات الثلاث */
        .printing-options {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(25,25,25,0.95);
            border-radius: 15px;
            border: 1px solid rgba(212,175,55,0.3);
        }

        .option-item {
            text-align: center;
            padding: 1.5rem 2rem;
            border-radius: 10px;
            transition: all 0.3s ease;
            background: rgba(30,30,30,0.95);
            border: 1px solid rgba(212,175,55,0.2);
            flex: 1;
        }

        .option-item:hover {
            transform: translateY(-3px);
            border-color: #D4AF37;
            box-shadow: 0 5px 15px rgba(212,175,55,0.1);
        }

        .option-title {
            color: #D4AF37;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .option-description {
            color: #fff;
            font-size: 0.9rem;
            opacity: 0.9;
        }
        </style>
    """, unsafe_allow_html=True)

    # تحديث قسم تفاصيل الطباعة
    st.markdown('<div class="title-container"><div class="section-title">تفاصيل الطباعة</div></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    # طباعة أبيض وأسود مع تأثيرات لونية (أول عمود على اليمين)
    with col1:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown('<div class="input-label">طباعة أبيض وأسود وقليل ألوان </div>', unsafe_allow_html=True)
        bw_color_pages = st.number_input(
            "طباعة أبيض وأسود وقليل ألوان",
            min_value=0,
            max_value=500,
            value=0,
            help="الحد الأقصى 500 صفحة"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # طباعة أبيض وأسود (العمود الثاني)
    with col2:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown('<div class="input-label">طباعة أبيض وأسود</div>', unsafe_allow_html=True)
        bw_pages = st.number_input(
            "طباعة أبيض وأسود",
            min_value=0,
            max_value=500,
            value=0,
            help="الحد الأقصى 500 صفحة"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # طباعة ملونة (العمود الثالث)
    with col3:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown('<div class="input-label">طباعة ملونة </div>', unsafe_allow_html=True)
        color_pages = st.number_input(
            "طباعة ملونة",
            min_value=0,
            max_value=500,
            value=0,
            help="الحد الأقصى 500 صفحة"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

    # إضافة قسم الإضافات الاختيارية
    st.markdown('<div class="title-container"><div class="section-title">الإضافات الاختيارية</div></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_cover = st.checkbox("تصميم غلاف ملون")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_empty_last = st.checkbox("صفحة ختامية فارغة")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_carton = st.checkbox("كرتون")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_nylon = st.checkbox("نايلون شفاف")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        st.markdown('<div class="premium-checkbox">', unsafe_allow_html=True)
        has_paper_holder = st.checkbox("حاملة أوراق")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

    # حساب التكلفة
    exact_total, rounded_total = calculate_total_cost(
        color_pages, bw_color_pages, bw_pages,
        has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder
    )
    
    # عرض النتائج
    st.markdown("""
        <div class="premium-results">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div class="result-card">
                    <div class="result-label">السعر الكلي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
                <div class="result-card">
                    <div class="result-label">السعر النهائي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
            </div>
        </div>
    """.format(exact_total, rounded_total), unsafe_allow_html=True)
    
    # إضافة الشريط في الواجهة
    total_pages = color_pages + bw_color_pages + bw_pages
    if total_pages > 0:
        progress = min(total_pages / 100, 1)
        st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress * 100}%"></div>
            </div>
        """, unsafe_allow_html=True)

    # استدعاء دالة الخلاصة
    show_summary(color_pages, bw_color_pages, bw_pages, has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder, exact_total)

    # إضافة قسم الخدمات في النهاية مع تحسين التصميم
    st.markdown("""
        <div class="services-section">
            <div class="services-grid">
                <div class="service-card">
                    <h3>⚡ خدمة سريعة</h3>
                    <p>إنجاز في وقت قياسي</p>
                </div>
                <div class="service-card">
                    <h3>💰 أسعار تنافسية</h3>
                    <p>قيمة مقابل الجودة</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
