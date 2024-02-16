from dataclasses import dataclass

@dataclass
class Monster:
    hit_points:int
    level:int
    action: str | None