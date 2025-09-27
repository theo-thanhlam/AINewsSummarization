from google import genai
from google.genai import types
from .prompts import SYSTEM_PROMPT
from .baseSchemas import BaseResponseSchema

import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GOOGLE_FLASH_MODEL = "gemini-2.5-flash-lite"


class BaseAgent:
    def __init__(self, temperature=0.75, system_prompt=SYSTEM_PROMPT, response_schema=BaseResponseSchema, model=GOOGLE_FLASH_MODEL):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = model
        self.config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=temperature,
            response_mime_type="application/json",
            response_schema=response_schema,
            system_instruction=system_prompt
        )