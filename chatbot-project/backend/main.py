from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging
from typing import Optional

app = FastAPI()

# OpenRouter API details
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Configure logging
logging.basicConfig(level=logging.INFO)

class ChatRequest(BaseModel):
    prompt: str
    image_url: Optional[str] = None  # Allow image_url to be None

@app.post("/chat")  # Ensure this is defined as a POST route
async def chat_with_openrouter(request: ChatRequest):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [{"role": "user", "content": [{"type": "text", "text": request.prompt}]}]
    
    if request.image_url:  # Only include image_url if it is not None or empty
        messages[0]["content"].append({
            "type": "image_url",
            "image_url": {"url": request.image_url}
        })

    data = {"model": "qwen/qwen2.5-vl-3b-instruct:free", "messages": messages}
    
    try:
        logging.info(f"Sending request to OpenRouter: {data}")
        response = requests.post(OPENROUTER_API_URL, json=data, headers=headers)
        response.raise_for_status()
        logging.info(f"Received response from OpenRouter: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error communicating with OpenRouter: {e}")
        return {"error": f"Error communicating with OpenRouter: {str(e)}"}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": f"Unexpected error: {str(e)}"}

# Run using: uvicorn filename:app --reload
