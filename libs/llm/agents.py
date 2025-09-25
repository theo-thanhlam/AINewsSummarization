from google import genai
from google.genai import types
from .schemas import SummerizeResponseSchema
from .prompts import SYSTEM_PROMPT, SUMMERIZE_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GOOGLE_FLASH_MODEL = "gemini-2.5-flash"



class SummarizeAgent:
    def __init__(self, temperature:float = 0.9):
        
        self.response:SummerizeResponseSchema = None
        self.config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=temperature,
            response_mime_type="application/json",
            response_schema=SummerizeResponseSchema,
            system_instruction=SYSTEM_PROMPT
           
        )
        
    def summerize(self, title:str, story:str):
        prompt = SUMMERIZE_PROMPT.format(title=title, story=story)
        self.response = client.models.generate_content(
            model=GOOGLE_FLASH_MODEL,
            config = self.config,
            contents=[prompt]
            
        )
        
    
    def getSummerization(self):
        if not self.response:
            raise Exception("Call summerize func first")
        return self.response.parsed