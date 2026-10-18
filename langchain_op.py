from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

class Review(TypedDict):
    summary: str
    sentiment: str

s_model = model.with_structured_output(Review)

result = s_model.invoke("Hardware is great, but software is bloated. Too many pre installed apps, hope next updates fixes this")

print(result)