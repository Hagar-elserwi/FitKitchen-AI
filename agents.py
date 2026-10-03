import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# ==========================================
# SECTION 1: Environment & Setup
# ==========================================

load_dotenv()
groq_token = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-20b", 
    api_key=groq_token,
    temperature=0.7
)

# ==========================================
# SECTION 2: Prompts Definition
# ==========================================

chef_prompt = ChatPromptTemplate.from_template(
    """You are an elite fitness chef. 
    The user's fitness goal is: {goal}. 
    They have these ingredients: {ingredients}. 
    Create a short, healthy, and delicious recipe using ONLY these ingredients. 
    
    IMPORTANT: You MUST write the entire response in {language}.
    
    Output Format:
    - 🍲 Recipe Name:
    - ⏱️ Prep Time:
    - 📋 Instructions:"""
)

nutritionist_prompt = ChatPromptTemplate.from_template(
    """You are a certified sports nutritionist. 
    The user's fitness goal is: {goal}. 
    Analyze this recipe created by the chef: {recipe}. 
    
    IMPORTANT: You MUST write the entire response in {language}.
    
    Output Format:
    - 🔥 Estimated Calories:
    - 🥩 Protein: | 🍚 Carbs: | 🥑 Fats:
    - 💡 Nutritionist Note: (1 sentence on why this fits their goal)"""
)

# ==========================================
# SECTION 3: Chains & Execution Logic
# ==========================================

chef_chain = chef_prompt | llm
nutritionist_chain = nutritionist_prompt | llm

def run_fitkitchen_agents(goal, ingredients, language):
    """
    Executes the Multi-Agent flow: Chef -> Nutritionist.
    Takes user goal, ingredients, and language as input, returns recipe and analysis.
    """
    # Step 1: The Chef creates the recipe in the specified language
    recipe_response = chef_chain.invoke({
        "goal": goal, 
        "ingredients": ingredients, 
        "language": language
    })
    recipe_text = recipe_response.content
    
    # Step 2: The Nutritionist analyzes the recipe in the specified language
    analysis_response = nutritionist_chain.invoke({
        "goal": goal, 
        "recipe": recipe_text, 
        "language": language
    })
    analysis_text = analysis_response.content
    
    return recipe_text, analysis_text