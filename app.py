import os
from dotenv import load_dotenv

# add tokens 
load_dotenv() 
hf_token = os.getenv("GROQ_API_KEY")

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="FitKitchen AI",
    page_icon="🍲",
    layout="centered"
)

# Sidebar settings
lang = st.sidebar.radio("Language / اللغة", ["English", "العربية"])

# CSS Styling inspired by "Bistro Bliss" and modern food UI
custom_css = """
<style>
    /* Import elegant fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Nunito:wght@400;600;700&display=swap');

    /* Warm, clean background */
    .stApp { 
        background-color: #FFFDF8 !important; 
    }
    
    /* Elegant serif typography for headings */
    h1, h2, h3 { 
        font-family: 'Playfair Display', serif !important;
        color: #2C1E16 !important; 
    }
    
    /* Clean sans-serif for body text */
    p, label, .stMarkdown, li {
        font-family: 'Nunito', sans-serif !important;
        color: #4A4A4A !important;
    }
    
    /* Deep Red Pill-shaped Button (like 'Book A Table') */
    .stButton>button {
        background-color: #901A1E !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 50px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        padding: 12px 30px !important;
        box-shadow: 0px 4px 15px rgba(144, 26, 30, 0.3) !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #B22222 !important;
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(178, 34, 34, 0.4) !important;
    }
    
    /* Elegant Form Container with Yellow Accent */
    div[data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: none !important;
        border-top: 6px solid #F6C90E !important; /* Cheerful yellow accent */
        border-radius: 12px !important;
        padding: 30px !important;
        box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.06) !important;
    }
    
    /* Input fields styling */
    div[data-baseweb="select"] > div, div[data-baseweb="textarea"] > textarea {
        border: 1px solid #EAEAEA !important;
        border-radius: 8px !important;
        background-color: #F9F9F9 !important;
        font-family: 'Nunito', sans-serif !important;
    }
    
    /* Focus state for inputs */
    div[data-baseweb="select"] > div:focus-within, div[data-baseweb="textarea"] > textarea:focus {
        border-color: #F6C90E !important;
        box-shadow: 0 0 0 1px #F6C90E !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Dictionary for multi-language support
translations = {
    "English": {
        "title": "🍲 FitKitchen AI",
        "subtitle": "Best food for your fitness goals. Discover smart recipes based on what you have.",
        "goal_header": "What is your taste & goal today?",
        "goals": [
            "High Protein / Clean Bulking",
            "Cutting / Fat Loss",
            "Bulking / Muscle Mass",
            "Keto Diet",
            "Balanced & Healthy"
        ],
        "pantry_header": "What's in your kitchen?",
        "pantry_placeholder": "e.g., chicken strips, butter, heavy cream, garlic, spices...",
        "submit_btn": "Explore Menu & Recipes",
        "warning_msg": "⚠️ Please enter some available ingredients first to craft your recipe!",
        "success_msg": "✨ Chef Agent is preparing your menu...",
        "spinner_msg": "Whisking ingredients and calculating macros... 🍳📊"
    },
    "العربية": {
        "title": "🍲 FitKitchen AI",
        "subtitle": "أفضل الوصفات لأهدافك الرياضية. اكتشف أطباق لذيذة بمكونات مطبخك.",
        "goal_header": "ما هو هدفك وذوقك اليوم؟",
        "goals": [
            "تضخيم صافي / عالي البروتين",
            "تنشيف وحرق دهون",
            "زيادة كتلة عضلية",
            "نظام الكيتو",
            "صحي ومتوازن"
        ],
        "pantry_header": "ماذا يوجد في مطبخك؟",
        "pantry_placeholder": "مثال: فراخ ستربس، زبدة، كريمة طبخ، ثوم، بهارات...",
        "submit_btn": "اكتشف الوصفات والمنيو",
        "warning_msg": "⚠️ من فضلك اكتب بعض المكونات المتاحة لديك أولاً لنبتكر وصفتك!",
        "success_msg": "✨ الشيف الذكي يجهز المنيو الخاص بك...",
        "spinner_msg": "جاري مزج المكونات وحساب السعرات... 🍳📊"
    }
}

t = translations[lang]

# RTL alignment for Arabic
if lang == "العربية":
    st.markdown("""
        <style>
            .stApp { direction: rtl; text-align: right; }
        </style>
    """, unsafe_allow_html=True)

# UI Rendering
st.markdown(f"<h1 style='text-align: center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 1.2rem; margin-bottom: 2rem;'>{t['subtitle']}</p>", unsafe_allow_html=True)

with st.form("recipe_form"):
    st.markdown(f"### {t['goal_header']}")
    fitness_goal = st.selectbox("", t["goals"], label_visibility="collapsed")
    
    st.markdown(f"<br>### {t['pantry_header']}", unsafe_allow_html=True)
    pantry_items = st.text_area("", placeholder=t["pantry_placeholder"], label_visibility="collapsed", height=100)
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label=t["submit_btn"])

# Handle form submission and agent execution
if submit_button:
    if not pantry_items.strip():
        # Warn if no ingredients are provided
        st.warning(t["warning_msg"])
    else:
        st.success(t["success_msg"])
        
        with st.spinner(t["spinner_msg"]):
            # Import the agent function from our agents.py file
            from agents import run_fitkitchen_agents
            
            try:
                # Determine the language to tell the AI based on the sidebar selection
                ai_language = "Arabic" if lang == "العربية" else "English"
                
                # Run the AI agents with user inputs AND language
                recipe, analysis = run_fitkitchen_agents(fitness_goal, pantry_items, ai_language)
                
                # Set dynamic headers based on selected language
                chef_title = "👨‍🍳 وصفة الشيف" if lang == "العربية" else "👨‍🍳 Chef's Recipe"
                nutri_title = "📊 تحليل خبير التغذية" if lang == "العربية" else "📊 Nutritionist Analysis"
                
                # Render the Chef's Recipe
                st.markdown("<br><hr>", unsafe_allow_html=True)
                st.markdown(f"### {chef_title}")
                st.info(recipe)
                
                # Render the Nutritionist's Analysis
                st.markdown(f"### {nutri_title}")
                st.success(analysis)
                
            except Exception as e:
                # Handle API or connection errors safely
                st.error(f"Error connecting to the model. Please check your .env token.\nDetails: {e}")