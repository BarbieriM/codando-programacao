from src.domain.models import Monster


class MonsterFactory:
    def call(self) -> Monster:
        raise NotImplementedError() 