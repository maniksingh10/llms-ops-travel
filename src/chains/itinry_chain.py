from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.config import GROQ_API_KEY

llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interest}. Provide at least 5 bullet points."),
    ("human", "Create an itinerary for my day")
])

def gen_iti(city, interest):
    response = llm.invoke(
        prompt.format_messages(city=city, interest=', '.join(interest))
    )
    
    return response.content
