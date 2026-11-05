# === Stage 2: Проверка полей ===
# Project: AquariumCare
"""Модуль AquariumCare: валидация сущности «аквариум» и нормализация ввода.

Содержит вспомогательные определения для самостоятельной проверки полей
сущности «аквариум» (название, объём, тип, дата подмены) и функции
нормализации пользовательского ввода. Используется только стандартная
библиотека Python.
"""

import datetime
import re


class AquariumError(Exception):
    """Основа для всех ошибок валидации сущности аквариум."""


class AquariumValidationError(AquariumError):
    """Исключение, содержащее понятное сообщение об ошибке валидации."""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Поле {field}: {message}")


def normalize_text(value):
    """Нормализует текстовое значение: убирает лишние пробелы и приводит
    к нижнему регистру. Возвращает строку или None, если вход None."""
    if value is None:
        return None
    return value.strip().lower()


def normalize_int(value):
    """Приводит целочисленное значение к типу int, пропуская пустоту и
    None. Поддерживает десятичную и римскую запись для объёма."""
    if value is None:
        return None
    if isinstance(value, bool):
        raise AquariumValidationError("объём", "значение должно быть числом")
    if isinstance(value, int):
        return value
    text = str(value).strip()
    if text == "" or text.lower() == "null":
        return None
    if re.fullmatch(r"[+-]?\d+", text):
        return int(text)
    roman_map = {
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
        "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
    }
    if text.lower() in roman_map:
        return roman_map[text.lower()]
    raise AquariumValidationError("объём", "нужно целое число (например, 25 или xx)")


def normalize_date(value):
    """Нормализует дату подмены в объект datetime.date. Принимает строки
    в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД, а также объекты date."""
    if isinstance(value, datetime.date):
        return value
    if value is None or str(value).strip() == "":
        return None
    text = str(value).strip()
    patterns = ["%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y", "%m.%d.%Y"]
    for fmt in patterns:
        try:
            return datetime.date.fromformat(text, fmt)
        except ValueError:
            continue
    raise AquariumValidationError(
        "дата подмены", "нужна дата в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД"
    )


def normalize_choice(value, valid, field="тип"):
    """Проверяет, что значение относится к допустимому набору valid и
    возвращает нормализованное (строчное) значение."""
    if value is None:
        return None
    normalized = normalize_text(value)
    if normalized is None:
        return None
    if normalized not in valid:
        raise AquariumValidationError(
            field,
            f"недопустимое значение: {value}. Допустимые: {', '.join(valid)}",
        )
    return normalized


def validate_aquarium(name, volume, aq_type, change_date):
    """Валидирует все поля сущности «аквариум» и возвращает нормализованный
    словарь с проверенными данными. При ошибке поднимает AquariumValidationError."""
    errors = []

    normalized_name = normalize_text(name)
    if not normalized_name:
        errors.append("название не может быть пустым")
    elif len(normalized_name) > 64:
        errors.append("название не должно превышать 64 символа")

    volume_value = normalize_int(volume)
    if volume_value is None:
        errors.append("объём не указан")
    elif volume_value <= 0:
        errors.append("объём должен быть положительным числом")

    normalized_type = normalize_choice(aq_type, {"freshwater", "saltwater", "brackish"})
    if normalized_type is None:
        errors.append("тип аквариума не указан")

    change_date_value = normalize_date(change_date)
    if change_date_value is None:
        errors.append("дата подмены не указана")
    elif change_date_value.year < 1900 or change_date_value.year > datetime.date.today().year:
        errors.append("дата подмены вне разумных пределов")

    if errors:
        raise AquariumValidationError(
            "аквариум", "; ".join(errors)
        )

    return {
        "name": normalized_name,
        "volume": volume_value,
        "type": normalized_type,
        "change_date": change_date_value,
    }


def build_aquarium(name, volume, aq_type, change_date):
    """Удобная обёртка, создающая нормализованную сущность аквариум в виде
    словаря с проверкой полей. Использует validate_aquarium."""
    return validate_aquarium(name, volume, aq_type, change_date)
