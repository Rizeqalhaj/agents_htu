from django.conf import settings
from crewai import LLM

basic_llm = LLM(
    model=settings.GROQ_MODEL,
    temperature=0,
    api_key=settings.GROQ_API_KEY
)
