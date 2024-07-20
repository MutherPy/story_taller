
makemigration:
	read -p "Provide alembic migration message: " message; \
	export $(xargs < .env) && cd src && alembic revision --autogenerate -m $$message

migrate:
	export $(xargs < .env) && cd src && alembic upgrade head
