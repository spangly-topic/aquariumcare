# === Stage 5: Удаление и восстановление ===
# Project: AquariumCare
def remove_aquarium(aquariums, name, restore=False):
    """Удаляет аквариум. При restore — помечает как мягко удалённый."""
    for aquarium in aquariums:
        if aquarium["name"] == name:
            if restore:
                aquarium["_deleted"] = True
                return True
            aquariums.remove(aquarium)
            return True
    return False


def get_deleted_aquariums(aquariums):
    """Возвращает список мягко удалённых аквариумов."""
    return [a for a in aquariums if a.get("_deleted", False)]


def restore_aquarium(aquarium):
    """Восстанавливает мягко удалённый аквариум."""
    aquarium.pop("_deleted", None)
    return True


def get_active_aquariums(aquariums):
    """Возвращает только активные (не удалённые) аквариумы."""
    return [a for a in aquariums if not a.get("_deleted", False)]


def remove_aquarium_by_id(aquariums, aquarium_id, restore=False):
    """Удаляет аквариум по идентификатору."""
    for aquarium in aquariums:
        if aquarium.get("id") == aquarium_id:
            if restore:
                aquarium["_deleted"] = True
                return True
            aquariums.remove(aquarium)
            return True
    return False


def soft_delete_aquarium(aquariums, name, deleted_at=None):
    """Помечает аквариум как мягко удалённый с меткой времени."""
    for aquarium in aquariums:
        if aquarium["name"] == name:
            aquarium["_deleted"] = True
            aquarium["_deleted_at"] = deleted_at
            return True
    return False
