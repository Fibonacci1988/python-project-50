gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
