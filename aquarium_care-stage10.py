# === Stage 10: Сортировка записей ===
# Project: AquariumCare
from datetime import datetime


class Aquarium:
    def __init__(self, name, volume, tank_type, last_change):
        self.name = name
        self.volume = volume
        self.tank_type = tank_type
        self.created = datetime.now()
        self.last_change = last_change


def sort_by_name(items, reverse=False):
    return sorted(items, key=lambda item: item.name, reverse=reverse)


def sort_by_created(items, reverse=False):
    return sorted(items, key=lambda item: item.created, reverse=reverse)
