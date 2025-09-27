from pydantic import BaseModel
from typing import List
from ..baseSchemas import BaseResponseSchema

class SummerizeResponseSchema(BaseResponseSchema):
    summary: str
    key_takeaways: List[str]