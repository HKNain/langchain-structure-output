
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define the Pydantic model for validation
class Student(BaseModel):
    name: str
    age: int
    skills: list[str]

# Load JSON Schema from a separate file
schema_path = Path(__file__).parent / "student_schema.json"

with open(schema_path, "r", encoding="utf-8") as file:
    student_schema = json.load(file)

# Call Gemini using the loaded schema
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=(
        "Extract student details: "
        "John Doe is 21 years old and knows Python and Go."
    ),
    config={
        "response_mime_type": "application/json",
        "response_json_schema": student_schema,
    },
)

# Validate Gemini's response
student = Student.model_validate_json(response.text)

print(student)
print(student.model_dump_json(indent=2))
