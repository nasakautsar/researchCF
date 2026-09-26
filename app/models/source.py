from pydantic import BaseModel, Field

class ResearchSource(BaseModel):
  title: str
  url: str
  snippet: str
  source: str
  score: int = Field(default=0, ge=0)