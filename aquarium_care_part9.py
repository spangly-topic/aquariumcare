# === Stage 9: Фильтрация записей ===
# Project: AquariumCare
from datetime import date


class Aquarium:
    def __init__(self, name, volume, ahtype, last_change):
        self.name = name
        self.volume = volume
        self.ah_type = ahtype
        self.last_change = last_change

    def __repr__(self):
        return f"{''.join([f'{self.name}', f'{self.volume}', f'{self.ah_type}', f'{self.last_change}'])}"


def filter_by_volume(aquariums, volume):
    return [a for a in aquariums if a.volume == volume]


def filter_by_date_range(aquariums, start, end):
    return [a for a in aquariums if start <= a.last_change <= end]


def filter_by_volume_and_date_range(aquariums, volume, start, end):
    return [
        a for a in aquariums
        if a.volume == volume and start <= a.last_change <= end
    ]


def filter_by_volume_min_max(aquariums, min_volume, max_volume):
    return [
        a for a in aquariums
        if min_volume <= a.volume <= max_volume
    ]


def filter_by_date_range_min_max(aquariums, start, end):
    return [
        a for a in aquariums
        if start <= a.last_change <= end
    ]
