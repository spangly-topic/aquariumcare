# === Stage 4: Редактирование записей ===
# Project: AquariumCare
aquarium_edit.py

"""AquariumCare — модуль редактирования сущности аквариум."""


class AquariumField:
    """Описание допустимого поля аквариума."""

    __slots__ = ("name", "value")

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "AquariumField(%r, %r)" % (self.name, self.value)


ALLOWED_FIELDS = ("name", "volume", "aquarium_type", "last_change_date")


def validate_field_name(name):
    if name not in ALLOWED_FIELDS:
        raise ValueError("Поле %r не допустимо для редактирования аквариума" % name)
    return True


def validate_volume(value):
    try:        # noqa: SIM105
        value = float(value)
    except (TypeError, ValueError):
        raise ValueError("Объём должен быть числом")
    if value <= 0:
        raise ValueError("Объём должен быть положительным")
    return value


def validate_name(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Название должно быть непустой строкой")
    return value.strip()


def validate_aquarium_type(value):
    allowed = {"freshwater", "saltwater", "aquarium"}
    if value not in allowed:
        raise ValueError("Тип %r не допустим" % value)
    return value


def validate_last_change_date(value):
    try:
        return value  # предполагаем корректный объект даты
    except TypeError:
        raise ValueError("Дата подмены должна быть объектом даты")


VALIDATORS = {
    "name": validate_name,
    "volume": validate_volume,
    "aquarium_type": validate_aquarium_type,
    "last_change_date": validate_last_change_date,
}


def apply_update(aquarium, update):
    """Применить частичное обновление к аквариуму.

    update — словарь или список AquariumField.
    Меняются только допустимые поля с валидированными значениями.
    """
    if isinstance(update, list):
        changes = {}
        for field in update:
            validate_field_name(field.name)
            changes[field.name] = field.value
    elif isinstance(update, dict):
        changes = update
    else:
        raise TypeError("update должен быть dict или списком AquariumField")

    for name, value in changes.items():
        validator = VALIDATORS.get(name)
        if validator is None:
            raise ValueError("Поле %r не допустимо для редактирования" % name)
        setattr(aquarium, name, validator(value))

    return changes
