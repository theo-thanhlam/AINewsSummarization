from pydantic import BaseModel
from typing import List

class SummerizeResponseSchema(BaseModel):
    summary: str
    key_takeaways: List[str]