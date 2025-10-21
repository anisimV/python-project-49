# Makefile для проекта hexlet-code

# Установка зависимостей и синхронизация пакета
install:
	uv sync

# Быстрый запуск точки входа brain-games
brain-games:
	uv run brain-games

# Сборка пакета (создание wheel)
build:
	uv build

# Установка собранного пакета из dist/*.whl
package-install:
	uv tool install dist/*.whl


# Проверка линтером Ruff
lint:
	uv run ruff check brain_games
