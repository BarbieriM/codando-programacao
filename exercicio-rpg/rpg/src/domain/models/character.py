from dataclasses import dataclass

@dataclass
class Character:
    name: str
    character_class: str
    power: int
    hit_points: int
    action: str | None
    level: int