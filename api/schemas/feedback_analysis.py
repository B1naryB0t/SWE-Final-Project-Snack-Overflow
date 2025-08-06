from typing import Dict

from pydantic import BaseModel


class FeedbackAnalysis(BaseModel):
	average_rating: float
	total_reviews: int
	ratings_breakdown: Dict[int, int]  # e.g., {5: 10, 4: 3, 3: 1}
