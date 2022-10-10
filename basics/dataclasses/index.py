""" For DataClass """

from typing import Dict, Tuple
from dataclasses import dataclass, field


@dataclass
class Person:
    
    first_name: str
    last_name: str
    age: int = field(compare=False)
    degree: Tuple[str] = field(default=("Under graduate", "Post graduate"))
    hobbies: Dict[str, str] = field(default_factory=lambda: {
        "in_studies": "designing",
        "in_sports": "cricket",
        "movies": "sci-fi"
    })


class Alien:

    def __init__(self):
        self.person = Person("Karthick Sabari", "Dhilip Sudhakar", 23)

    def get_movie_hobby(self):
        return self.person.hobbies.get('in_sports')


alien = Alien().get_movie_hobby()
print(alien)
