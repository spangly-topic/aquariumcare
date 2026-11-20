# === Stage 7: Связи между сущностями ===
# Project: AquariumCare
from datetime import date


class Aquarium:
    def __init__(self, name, volume, tank_type, water_change=None):
        self.name = name
        self.volume = volume
        self.tank_type = tank_type
        self.water_change = water_change


class WaterMeasurement:
    def __init__(self, aquarium, ph, temperature, nitrate, ammonia, nitrite, measured_on):
        self.aquarium = aquarium
        self.ph = ph
        self.temperature = temperature
        self.nitrate = nitrate
        self.ammonia = ammonia
        self.nitrite = nitrite
        self.measured_on = measured_on


def link_is_consistent(aquarium, measurements):
    for measurement in measurements:
        if measurement.aquarium is not aquarium:
            return False
    return True


def get_measurements_for(aquarium, measurements):
    if link_is_consistent(aquarium, measurements):
        return [m for m in measurements if m.aquarium is aquarium]
    return []


if __name__ == "__main__":
    tank = Aquarium("Community", 54, "freshwater", date(2025, 1, 15))
    ok = [
        WaterMeasurement(tank, 7.0, 24.0, 10, 0.0, 0.0, date(2025, 1, 20)),
        WaterMeasurement(tank, 6.8, 23.5, 15, 0.0, 0.1, date(2025, 1, 27)),
    ]
    print(get_measurements_for(tank, ok))
    print(get_measurements_for(tank, [WaterMeasurement(tank, 7.0, 24.0, 10, 0.0, 0.0, date(2025, 1, 20)),
                                      WaterMeasurement(Aquarium("Other", 20, "saltwater"), 8.0, 26.0, 5, 0.0, 0.0, date(2025, 1, 28))]))
