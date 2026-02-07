import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found. Please set it in .env file")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Create FastAPI app
app = FastAPI(title="AI Code Review System")

# Enable CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request body model
class CodeRequest(BaseModel):
    code: str
    language: str


# Home route
@app.get("/")
def home():
    return {
        "message": "AI Code Review Backend Running Successfully 🚀"
    }


# Review API
@app.post("/review")
async def review_code(request: CodeRequest):

    prompt = f"""
You are a professional software engineer.

Review this {request.language} code.

Check:
✔ Bugs
✔ Docstrings
✔ Type hints
✔ Error handling
✔ Input validation
✔ Code quality
✔ Best practices

Give suggestions and improved code.

Code:
{request.code}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI code reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=700
    )

    review = response.choices[0].message.content

    return {
        "review": review
    }
