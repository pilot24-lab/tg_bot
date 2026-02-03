from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    tg_id: Optional[int]
    name: str
    created_at: Optional[datetime] = None