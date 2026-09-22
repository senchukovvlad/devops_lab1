"""Головний модуль програми."""

from devops_lab1.lib import calculate_length, greet


def main():
  """Головна функція для демонстрації імпорту з lib.py."""
  user = "Vlad"
  message = greet(user)
  length = calculate_length(message)

  print(message)
  print(f"Кількість символів у повідомленні: {length}")


if __name__ == "__main__":
  main()