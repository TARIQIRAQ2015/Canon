import streamlit as st

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
    
    /* تنسيق عام */
    * {
        font-family: 'Tajawal', sans-serif;
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
    
    .premium-header h1 {
        font-size: clamp(2.5rem, 5vw, 4.5rem) !important;
        letter-spacing: 1px;
        font-weight: 800;
        transform: perspective(1000px) translateZ(30px);
        text-shadow: 
            0 1px 0 #ccc,
            0 2px 0 #c9c9c9,
            0 3px 0 #bbb,
            0 4px 0 #b9b9b9,
            0 5px 0 #aaa,
            0 6px 1px rgba(0,0,0,.1),
            0 0 5px rgba(0,0,0,.1),
            0 1px 3px rgba(0,0,0,.3),
            0 3px 5px rgba(0,0,0,.2),
            0 5px 10px rgba(0,0,0,.25),
            0 10px 10px rgba(0,0,0,.2),
            0 20px 20px rgba(0,0,0,.15);
    }
    
    .premium-header .subtitle {
        font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-top: 1rem;
        font-weight: 500;
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
        font-size: 1rem !important;
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
        font-size: 1.2rem !important;
        color: #D4AF37 !important;
        font-weight: 500 !important;
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
    
    .result-label {
        font-size: clamp(1.2rem, 2vw, 1.5rem);
        font-weight: 600;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .result-value {
        font-size: clamp(2rem, 4vw, 3rem) !important;
        font-weight: 800;
        text-shadow: 
            0 2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.2);
        transform: perspective(1000px) translateZ(30px);
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
        font-size: clamp(1.5rem, 3vw, 2rem);
        background: linear-gradient(45deg, #FFD700, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        padding: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* تنسيق الإيموجيات */
    .emoji-icon {
        font-size: 1.5rem;
        margin-left: 0.5rem;
        -webkit-text-fill-color: initial;  /* إزالة التأثير الذهبي من الإيموجيات */
    }

    /* تنسيق محسن لحقول الإدخال */
    .input-container {
        background: linear-gradient(165deg, rgba(30,30,30,0.9), rgba(15,15,15,0.9));
        border: 1px solid rgba(212,175,55,0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.3),
            inset 0 2px 10px rgba(255,255,255,0.1),
            0 0 0 1px rgba(212,175,55,0.1);
        backdrop-filter: blur(10px);
        transform-style: preserve-3d;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }

    .input-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 100%;
        background: linear-gradient(180deg, 
            rgba(212,175,55,0.1) 0%,
            transparent 15%,
            transparent 85%,
            rgba(212,175,55,0.1) 100%);
        pointer-events: none;
    }

    .input-container:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: rgba(212,175,55,0.4);
        box-shadow: 
            0 15px 30px rgba(0,0,0,0.4),
            inset 0 2px 15px rgba(255,255,255,0.1),
            0 0 0 1px rgba(212,175,55,0.2);
    }

    .input-label {
        font-size: clamp(1.1rem, 2vw, 1.3rem);
        font-weight: 600;
        color: #D4AF37;
        margin-bottom: 1rem;
        text-shadow: 
            0 2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.2);
        transform: perspective(1000px) translateZ(20px);
    }

    .input-label::before {
        content: '';
        position: absolute;
        right: 0;
        top: 50%;
        width: 3px;
        height: 100%;
        background: linear-gradient(180deg, #D4AF37, transparent);
        transform: translateY(-50%);
        border-radius: 3px;
    }

    /* تحسين مظهر حقول الأرقام */
    .stNumberInput {
        background: transparent !important;
        position: relative;
    }

    .stNumberInput > div > div > input {
        background: rgba(0,0,0,0.4) !important;
        border: 2px solid rgba(212,175,55,0.3) !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        font-size: 1.2rem !important;
        padding: 1.2rem !important;
        height: 3.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 
            inset 0 2px 10px rgba(0,0,0,0.3),
            0 5px 15px rgba(0,0,0,0.2);
    }

    .stNumberInput > div > div > input:focus {
        border-color: #D4AF37 !important;
        box-shadow: 
            0 0 20px rgba(212,175,55,0.2),
            inset 0 2px 10px rgba(0,0,0,0.3) !important;
        transform: translateY(-2px);
        background: rgba(0,0,0,0.5) !important;
    }

    /* تحسين أزرار الزيادة والنقصان */
    .stNumberInput [data-testid="stDecrement"], 
    .stNumberInput [data-testid="stIncrement"] {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d) !important;
        color: #D4AF37 !important;
        border: 2px solid rgba(212,175,55,0.3) !important;
        border-radius: 12px !important;
        width: 45px !important;
        height: 45px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 
            0 5px 15px rgba(0,0,0,0.2),
            inset 0 2px 5px rgba(255,255,255,0.1);
    }

    .stNumberInput [data-testid="stDecrement"]:hover, 
    .stNumberInput [data-testid="stIncrement"]:hover {
        background: linear-gradient(145deg, #D4AF37, #B8860B) !important;
        color: #000000 !important;
        transform: translateY(-2px) scale(1.1);
        box-shadow: 
            0 8px 20px rgba(212,175,55,0.3),
            inset 0 2px 5px rgba(255,255,255,0.2);
    }

    .stNumberInput [data-testid="stDecrement"]:active, 
    .stNumberInput [data-testid="stIncrement"]:active {
        transform: translateY(1px) scale(0.95);
    }

    /* تأثير الضوء عند التحويم */
    .input-container::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at center, 
            rgba(212,175,55,0.1),
            transparent 70%);
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
        transform: rotate(30deg);
    }

    .input-container:hover::after {
        opacity: 1;
    }

    /* إضافة CSS للشريط المتحرك */
    .progress-container {
        background: rgba(0,0,0,0.3);
        border-radius: 50px;
        padding: 5px;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(212,175,55,0.3);
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #D4AF37, #FFD700);
        height: 10px;
        border-radius: 50px;
        transition: width 0.5s ease;
        position: relative;
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    .info-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .info-card {
        background: rgba(20,20,20,0.95);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transform-style: preserve-3d;
        transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .info-card:hover {
        transform: translateZ(20px) rotateX(10deg);
    }
    
    .info-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 50% 0%, 
            rgba(212,175,55,0.4),
            transparent 70%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .info-card:hover::before {
        opacity: 1;
    }

    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        opacity: 0.6;
    }
    
    .particle {
        position: absolute;
        background: linear-gradient(45deg, #D4AF37, transparent);
        border-radius: 50%;
        pointer-events: none;
        animation: float 20s infinite;
        filter: blur(2px);
    }
    
    @keyframes float {
        0% { 
            transform: translateY(0) rotate(0deg) scale(1);
            opacity: 0;
        }
        50% { 
            transform: translateY(-50vh) rotate(180deg) scale(1.5);
            opacity: 0.5;
        }
        100% { 
            transform: translateY(-100vh) rotate(360deg) scale(1);
            opacity: 0;
        }
    }

    .premium-button-3d {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        color: #D4AF37;
        padding: 1rem 2rem;
        border: none;
        border-radius: 15px;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.2s;
        cursor: pointer;
    }
    
    .premium-button-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: #D4AF37;
        transform: translateZ(-10px);
        border-radius: 15px;
        filter: blur(10px);
        opacity: 0;
        transition: opacity 0.2s;
    }
    
    .premium-button-3d:hover {
        transform: translateY(-5px);
    }
    
    .premium-button-3d:hover::before {
        opacity: 0.5;
    }
    
    .premium-button-3d:active {
        transform: translateY(0);
    }

    .neon-title {
        color: #fff;
        text-shadow:
            0 0 5px #D4AF37,
            0 0 10px #D4AF37,
            0 0 20px #D4AF37,
            0 0 40px #D4AF37;
        animation: neon 1.5s ease-in-out infinite alternate;
    }
    
    @keyframes neon {
        from {
            text-shadow:
                0 0 5px #D4AF37,
                0 0 10px #D4AF37,
                0 0 20px #D4AF37,
                0 0 40px #D4AF37;
        }
        to {
            text-shadow:
                0 0 10px #D4AF37,
                0 0 20px #D4AF37,
                0 0 40px #D4AF37,
                0 0 80px #D4AF37;
        }
    }

    /* تحسين النصوص والعناوين */
    h1, h2, h3, p, .input-label, .result-label {
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    /* تحسين العنوان الرئيسي */
    .premium-header h1 {
        font-size: clamp(2.5rem, 5vw, 4.5rem) !important;
        letter-spacing: 1px;
        font-weight: 800;
        transform: perspective(1000px) translateZ(30px);
        text-shadow: 
            0 1px 0 #ccc,
            0 2px 0 #c9c9c9,
            0 3px 0 #bbb,
            0 4px 0 #b9b9b9,
            0 5px 0 #aaa,
            0 6px 1px rgba(0,0,0,.1),
            0 0 5px rgba(0,0,0,.1),
            0 1px 3px rgba(0,0,0,.3),
            0 3px 5px rgba(0,0,0,.2),
            0 5px 10px rgba(0,0,0,.25),
            0 10px 10px rgba(0,0,0,.2),
            0 20px 20px rgba(0,0,0,.15);
    }

    /* تحسين العنوان الفرعي */
    .subtitle {
        font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-top: 1rem;
        font-weight: 500;
    }

    /* تحسين عناوين الأقسام */
    .section-title {
        font-size: clamp(1.5rem, 3vw, 2rem);
        background: linear-gradient(45deg, #FFD700, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        padding: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* تحسين تسميات الإدخال */
    .input-label {
        font-size: clamp(1.1rem, 2vw, 1.3rem);
        font-weight: 600;
        color: #D4AF37;
        margin-bottom: 1rem;
        text-shadow: 
            0 2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.2);
        transform: perspective(1000px) translateZ(20px);
    }

    /* تحسين بطاقات المعلومات */
    .info-card h3 {
        font-size: clamp(1.3rem, 2.5vw, 1.8rem);
        color: #D4AF37;
        margin-bottom: 1rem;
        font-weight: 700;
        text-shadow: 
            0 2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.2);
        transform: perspective(1000px) translateZ(25px);
    }

    .info-card p {
        font-size: clamp(1rem, 1.8vw, 1.2rem);
        color: #fff;
        line-height: 1.6;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* تحسين الخيارات */
    .premium-checkbox label {
        font-size: clamp(1rem, 1.8vw, 1.2rem);
        font-weight: 500;
        color: #D4AF37;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
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
        font-size: clamp(2.8rem, 5vw, 4.8rem) !important;
        font-weight: 800;
        color: #D4AF37;
        text-shadow: 
            0 2px 2px rgba(0,0,0,0.5),
            0 4px 4px rgba(0,0,0,0.3),
            0 6px 8px rgba(0,0,0,0.2);
        margin-bottom: 1.5rem;
    }

    .premium-header .subtitle {
        font-size: clamp(1.3rem, 2.5vw, 1.8rem) !important;
        color: #FFD700;
        font-weight: 500;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        opacity: 0.9;
        line-height: 1.6;
    }

    /* تحسين عنوان القسم */
    .section-title {
        font-size: clamp(1.6rem, 3vw, 2.2rem);
        font-weight: 700;
        background: linear-gradient(45deg, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 0.5rem 0;
        display: flex;
        align-items: center;
        gap: 1rem;
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
        background: linear-gradient(145deg, rgba(26,26,26,0.95), rgba(45,45,45,0.95));
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
        font-size: 1.8rem;
        color: #D4AF37;
        margin-bottom: 1.5rem;
        text-align: center;
        font-weight: 600;
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
        font-size: 1.1rem;
        color: #FFD700;
    }

    .summary-value {
        font-size: 1.1rem;
        color: #fff;
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
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .input-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-top: 1.5rem;
    }

    .extras-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin-top: 1.5rem;
    }

    .services-section {
        margin-top: 2rem;
        text-align: center;
    }

    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 1.5rem;
    }

    .service-card {
        background: linear-gradient(145deg, rgba(25,25,25,0.95), rgba(35,35,35,0.95));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 2rem;
        transition: all 0.3s ease;
    }

    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(212,175,55,0.2);
    }

    .service-card h3 {
        color: #D4AF37;
        font-size: 1.4rem;
        margin-bottom: 1rem;
    }

    .service-card p {
        color: #fff;
        opacity: 0.9;
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
        padding: 2rem;
        margin-bottom: 2rem;
        border: 2px solid rgba(212,175,55,0.3);
        text-align: center;
    }

    /* تنسيق الأقسام */
    .section-container {
        background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
        border: 2px solid rgba(212,175,55,0.3);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
    }

    .section-title {
        color: #D4AF37;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }

    /* تنسيق حقول الإدخال */
    .input-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-top: 1.5rem;
    }

    .input-container {
        text-align: center;
        padding: 1.5rem;
    }

    /* تنسيق الإضافات */
    .extras-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
    }

    .premium-checkbox {
        text-align: center;
        padding: 1rem;
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
        margin-top: 1.5rem;
    }

    .service-card {
        background: rgba(25,25,25,0.95);
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
    }

    /* تنسيق الخلاصة */
    .summary-section {
        text-align: center;
        margin-top: 2rem;
    }

    .summary-item {
        padding: 1rem;
        border-bottom: 1px solid rgba(212,175,55,0.2);
    }

    /* تحسينات عامة */
    .emoji-icon {
        font-size: 1.5rem;
        margin-left: 0.5rem;
    }

    .input-label, .result-label, .summary-label {
        color: #D4AF37;
        margin-bottom: 0.5rem;
    }

    .stNumberInput {
        margin: 0 auto;
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

def show_summary(color_pages, bw_color_pages, bw_pages, has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder, exact_total):
    st.markdown("""
        <style>
        .summary-section {
            background: linear-gradient(145deg, rgba(20,20,20,0.95), rgba(30,30,30,0.95));
            border: 2px solid rgba(212,175,55,0.3);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .summary-title {
            font-size: 1.8rem;
            color: #D4AF37;
            margin-bottom: 1.5rem;
            text-align: center;
            font-weight: 600;
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
            font-size: 1.1rem;
            color: #FFD700;
        }

        .summary-value {
            font-size: 1.1rem;
            color: #fff;
        }
        </style>

        <div class="summary-section">
            <div class="summary-title">📋 خلاصة الطلب</div>
    """, unsafe_allow_html=True)

    # إضافة تفاصيل الصفحات
    if color_pages > 0:
        st.markdown(f"""
            <div class="summary-item">
                <div class="summary-label">🎨 صفحات ملونة</div>
                <div class="summary-value">{color_pages} صفحة</div>
            </div>
        """, unsafe_allow_html=True)

    if bw_color_pages > 0:
        st.markdown(f"""
            <div class="summary-item">
                <div class="summary-label">🖌️ صفحات مع تأثيرات لونية</div>
                <div class="summary-value">{bw_color_pages} صفحة</div>
            </div>
        """, unsafe_allow_html=True)

    if bw_pages > 0:
        st.markdown(f"""
            <div class="summary-item">
                <div class="summary-label">📄 صفحات أبيض وأسود</div>
                <div class="summary-value">{bw_pages} صفحة</div>
            </div>
        """, unsafe_allow_html=True)

    # إضافة الإضافات المختارة
    extras = []
    if has_cover: extras.append("⭐ تصميم غلاف ملون فاخر")
    if has_empty_last: extras.append("📄 صفحة ختامية مميزة")
    if has_carton: extras.append("📦 كرتون فاخر")
    if has_nylon: extras.append("✨ نايلون شفاف")
    if has_paper_holder: extras.append("📁 حاملة أوراق")

    if extras:
        st.markdown("""
            <div class="summary-item">
                <div class="summary-label">✨ الإضافات المختارة</div>
                <div class="summary-value">
        """, unsafe_allow_html=True)
        for extra in extras:
            st.markdown(f"<div>{extra}</div>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    # إضافة السعر النهائي
    st.markdown(f"""
        <div class="summary-item" style="margin-top: 1rem;">
            <div class="summary-label" style="font-size: 1.3rem;">💰 السعر النهائي</div>
            <div class="summary-value" style="font-size: 1.3rem; color: #D4AF37;">{exact_total:,} دينار</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def main():
    # إضافة زر العودة للأعلى
    st.markdown("""
        <style>
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
            z-index: 9999;
            text-decoration: none;
            backdrop-filter: blur(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }

        .back-to-top::after {
            content: '';
            width: 15px;
            height: 15px;
            border-left: 3px solid #D4AF37;
            border-top: 3px solid #D4AF37;
            transform: rotate(45deg);
            margin-bottom: -5px;
        }

        .back-to-top:hover {
            transform: translateY(-5px);
            border-color: #D4AF37;
            box-shadow: 0 8px 25px rgba(212,175,55,0.3);
        }

        .back-to-top:hover::after {
            border-color: #FFD700;
        }
        </style>

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

    # في بداية الصفحة (أعلى الكود)
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)
    
    # العنوان الرئيسي
    st.markdown("""
        <div class="premium-header">
            <h1><span style="color: initial; background: none; -webkit-text-fill-color: initial;">🖨️</span> مكتب طارق الياسين</h1>
            <div class="subtitle">
                نقدم خدمات طباعة احترافية بجودة عالية وكفاءة مميزة
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # تعديل CSS للتنسيق الأفقي
    st.markdown("""
        <style>
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
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .input-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .extras-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .services-section {
            margin-top: 2rem;
            text-align: center;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 1.5rem;
        }

        .service-card {
            background: linear-gradient(145deg, rgba(25,25,25,0.95), rgba(35,35,35,0.95));
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 15px;
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(212,175,55,0.2);
        }

        .service-card h3 {
            color: #D4AF37;
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }

        .service-card p {
            color: #fff;
            opacity: 0.9;
        }
        </style>
    """, unsafe_allow_html=True)

    # تنظيم المحتوى بشكل أفقي
    st.markdown('<div class="horizontal-layout">', unsafe_allow_html=True)

    # 1. قسم تفاصيل الطباعة
    st.markdown("""
        <div class="section-container">
            <h2>
                <span class="emoji-icon">📋</span>
                <span class="section-title">تفاصيل الطباعة</span>
            </h2>
            <div class="input-grid">
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="input-container premium-input">', unsafe_allow_html=True)
        st.markdown('<div class="input-label"><span class="input-icon">🎨</span>طباعة ملونة عالية الجودة</div>', unsafe_allow_html=True)
        color_pages = st.number_input("", min_value=0, value=0, key="color_pages", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="input-container premium-input">', unsafe_allow_html=True)
        st.markdown('<div class="input-label"><span class="input-icon">🖌️</span>طباعة مع تأثيرات لونية</div>', unsafe_allow_html=True)
        bw_color_pages = st.number_input("", min_value=0, value=0, key="bw_color_pages", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="input-container premium-input">', unsafe_allow_html=True)
        st.markdown('<div class="input-label"><span class="input-icon">📄</span>طباعة أبيض وأسود</div>', unsafe_allow_html=True)
        bw_pages = st.number_input("", min_value=0, value=0, key="bw_pages", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

    # 2. قسم الإضافات
    st.markdown("""
        <div class="section-container">
            <h2>
                <span class="emoji-icon">⭐</span>
                <span class="section-title">الإضافات الاختيارية</span>
            </h2>
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
                    <div class="result-label">المبلغ الأساسي</div>
                    <div class="result-value">{:,} دينار</div>
                </div>
                <div class="result-card">
                    <div class="result-label">المبلغ النهائي</div>
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

    # استدعاء دالة الخلاصة في نهاية main()
    show_summary(color_pages, bw_color_pages, bw_pages, has_cover, has_empty_last, has_carton, has_nylon, has_paper_holder, exact_total)

if __name__ == "__main__":
    main() 
