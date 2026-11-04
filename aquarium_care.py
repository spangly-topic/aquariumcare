# === Stage 1: Каркас модуля ===
# Project: AquariumCare
aquarium.py

from datetime import date


class Aquarium:
    def __init__(self, name: str, volume: float, type_: str, last_change: date):
        self.name = name
        self.volume = volume
        self.type = type_
        self.last_change = last_change

    def __str__(self):
        return (
            f"Аквариум: {self.name}, "
            f"объём: {self.volume} л, "
            f"тип: {self.type}, "
            f"последняя подмена: {self.last_change}"
        )


def create_demo_aquariums() -> list:
    return [
        Aquarium("Рыбный", 120.0, "свежий", date(2025, 1, 15)),
        Aquarium("Коралловый", 40.0, "морской", date(2025, 2, 3)),
        Aquarium("Золотые рыбки", 60.0, "свежий", date(2025, 3, 20)),
    ]


def main() -> None:
    print("=== AquariumCare — уход за аквариумами ===")
    for aquarium in create_demo_aquariums():
        print(aquarium)


if __name__ == "__main__":
    main()
