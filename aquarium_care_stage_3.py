# === Stage 3: Хранилище в памяти ===
# Project: AquariumCare
aquarium_store.py

from uuid import uuid4


class AquariumNotFoundError(KeyError):
    """Исключение, когда аквариум с указанным id не найден."""


class AquariumStore:
    """Хранилище аквариумов в памяти.

    Поддерживает добавление, получение по идентификатору и список.
    """

    def __init__(self):
        self._items = {}

    def add(self, name, volume, aquarium_type):
        aquarium = Aquarium(name=name, volume=volume, aquarium_type=aquarium_type)
        self._items[aquarium.id] = aquarium
        return aquarium

    def get(self, aquarium_id):
        try:
            return self._items[aquarium_id]
        except KeyError as exc:
            raise AquariumNotFoundError(aquarium_id) from exc

    def list(self):
        return list(self._items.values())


class Aquarium:
    """Сущность аквариум."""

    def __init__(self, name, volume, aquarium_type):
        self.id = uuid4().hex
        self.name = name
        self.volume = volume
        self.aquarium_type = aquarium_type
        self.last_change_date = None

    def __repr__(self):
        return (f"Aquarium(id={self.id!r}, name={self.name!r}, "
                f"volume={self.volume}, type={self.aquarium_type!r})")


if __name__ == "__main__":
    store = AquariumStore()
    store.add("Золотые рыбки", 50, "сладководный")
    store.add("Тропикум", 120, "тропический")

    print("Список аквариумов:")
    for aquarium in store.list():
        print(" ", aquarium)

    print("\nПоиск по id:", store.get(store.list()[0].id))

    try:
        store.get("does-not-exist")
    except AquariumNotFoundError as error:
        print("Не найден аквариум:", error)
