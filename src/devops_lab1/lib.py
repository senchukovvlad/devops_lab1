"""Модуль допоміжних функцій."""


def greet(name: str) -> str:
  """Повертає персоналізоване привітання."""
  return f"Привіт, {name}!"


def calculate_length(text: str) -> int:
  """Обчислює та повертає кількість символів у рядку."""
  return len(text)
def farewell(name: str) -> str:
  """Повертає повідомлення прощання."""
  return f"До побачення, {name}!"