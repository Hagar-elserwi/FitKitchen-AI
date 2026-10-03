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
    /* light mode */
    .stApp { 
        background-color: #FDF6F5 !important; /* Pastel color */
    }
    div[data-testid="stSidebar"] {
        background-color: #F9EBEA !important;
    }
    h1, h2, h3, p, label, .stMarkdown, li {
        color: #2C1E16 !important;
    }
    div[data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border-top: 6px solid #F6C90E !important;
    }
    
    /* dark mode */
    @media (prefers-color-scheme: dark) {
        .stApp, div[data-testid="stSidebar"], div[data-testid="stForm"] {
            background-color: #000000 !important;
        }
        h1, h2, h3, p, label, .stMarkdown, li, div[data-baseweb="select"] > div, div[data-baseweb="textarea"] > textarea {
            color: #FF0000 !important;
            background-color: #000000 !important;
        }
        div[data-testid="stForm"] {
            border-top: 6px solid #FF0000 !important;
            border-bottom: 1px solid #FF0000 !important;
            border-left: 1px solid #FF0000 !important;
            border-right: 1px solid #FF0000 !important;
        }
        .stButton>button {
            background-color: #FF0000 !important;
            color: #000000 !important;
            border: 2px solid #FF0000 !important;
        }
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t['pantry_header']}")
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
