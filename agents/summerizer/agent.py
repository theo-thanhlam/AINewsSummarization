from .prompt import  SUMMERIZE_PROMPT
from ..baseAgents import BaseAgent
from .schema import SummerizeResponseSchema


class SummarizeAgent(BaseAgent):
    def __init__(self):
        super().__init__(response_schema=SummerizeResponseSchema)
    
    def summerize(self, title:str, story:str):
        prompt = SUMMERIZE_PROMPT.format(title=title, story=story)
        self.response = self.client.models.generate_content(
            model=self.model,
            config = self.config,
            contents=[prompt]
            
        )

        
    
    def getSummerization(self):
        if not self.response:
            raise Exception("Call summerize func first")
        return self.response.parsed