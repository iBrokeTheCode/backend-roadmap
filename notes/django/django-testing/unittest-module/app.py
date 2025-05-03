class SuperHero:
    def __init__(self, name: str, strength: int) -> None:
        self.name = name
        self.strength = strength

    def __str__(self) -> str:
        return self.name

    def is_stronger_than(self, other_hero: "SuperHero") -> bool:
        return self.strength > other_hero.strength
