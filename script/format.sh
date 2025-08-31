poetry run autoflake hk1980 --remove-all-unused-imports --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables -i -r
poetry run ruff check --select I --fix .
poetry run ruff format .