poetry run autoflake hk1980 --remove-all-unused-imports --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables -i -r
poetry run black hk1980 -t py39
poetry run isort hk1980 --profile=black
