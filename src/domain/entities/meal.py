from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Meal:
    id: Optional[int]
    user_id: Optional[int]
    food_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    