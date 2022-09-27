import random
from abc import abstractmethod

from pydantic import BaseModel

from data_generation.random_util import get_random_time, get_random_room


class BasePoint(BaseModel):
    is_actionable: bool

    @abstractmethod
    def get_point(self) -> str:
        ...


class BookMeetingPoint(BasePoint):
    is_actionable: bool = True

    def get_point(self) -> str:
        action = random.choice(["Schedule", "Book", "Plan"])
        location = random.choice([f" in {get_random_room()}", ""])
        return random.choice([
            f"{action} a meeting{location} at {get_random_time()}",
        ])
