# 🍲 FitKitchen AI: Multi-Agent Recipe & Pantry Auditor

FitKitchen AI is a smart, multi-language web application designed for athletes and fitness enthusiasts. It utilizes a Multi-Agent AI architecture to generate customized, healthy recipes based strictly on the ingredients available in your pantry and your specific fitness goals.

## 🌟 Key Features
- **Multi-Agent System:** Employs a 'Chef Agent' for recipe creation and a 'Nutritionist Agent' for macro analysis and validation.
- **Bilingual Interface:** Full support for both English and Arabic.
- **Smart Ingredient Matching:** Reduces food waste by creating meals ONLY from what you already have.
- **High-Performance AI:** Powered by Groq's lightning-fast API and the `gpt-oss-20b` model via LangChain.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM Orchestration:** LangChain
- **AI Model:** gpt-oss-20b (via Groq API)
- **Environment Management:** python-dotenv

## 🚀 How to Run Locally   

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Hagar-elserwi/FitKitchen-AI.git](https://github.com/Hagar-elserwi/FitKitchen-AI)
   cd FitKitchen-AI
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Set up environment variables:**
   
    Create a .env file in the root directory and add your Groq API key:
   ```bash
   GROQ_API_KEY="your_api_key_here"
3. **Run the application:**
   ```bash
   streamlit run app.py
