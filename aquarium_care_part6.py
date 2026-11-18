# === Stage 6: Связанная сущность ===
# Project: AquariumCare
from datetime import datetime


class WaterReading:
    def __init__(self, aquarium_id, ph=None, temperature=None,
                 ammonia=None, nitrite=None, nitrate=None,
                 reading_date=None):
        self.aquarium_id = aquarium_id
        self.ph = ph
        self.temperature = temperature
        self.ammonia = ammonia
        self.nitrite = nitrite
        self.nitrate = nitrate
        self.reading_date = reading_date or datetime.now()

    def add(self, aquarium_id, ph=None, temperature=None,
            ammonia=None, nitrite=None, nitrate=None,
            reading_date=None):
        reading = WaterReading(
            aquarium_id=aquarium_id,
            ph=ph,
            temperature=temperature,
            ammonia=ammonia,
            nitrite=nitrite,
            nitrate=nitrate,
            reading_date=reading_date,
        )
        readings[aquarium_id].append(reading)
        return reading

    def __repr__(self):
        return (
            f"WaterReading(aquarium_id={self.aquarium_id}, "
            f"ph={self.ph}, temperature={self.temperature}, "
            f"ammonia={self.ammonia}, nitrite={self.nitrite}, "
            f"nitrate={self.nitrate}, reading_date={self.reading_date})"
        )


readings = {}


def add_water_reading(aquarium_id, ph=None, temperature=None,
                      ammonia=None, nitrite=None, nitrate=None,
                      reading_date=None):
    return WaterReading.add(readings, aquarium_id, ph, temperature,
                            ammonia, nitrite, nitrate, reading_date)
