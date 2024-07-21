from pydantic import BaseModel, field_validator
import datetime
<<<<<<< Updated upstream


=======
from typing import Optional


class TodoCreate(BaseModel):
    todowrite: str
    tododate: datetime.datetime
>>>>>>> Stashed changes
