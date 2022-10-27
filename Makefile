.PHONY: run
run:
	@docker-compose up

.PHONY: down
down:
	@docker-compose down

.PHONY: build
build:
	@docker-compose build

.PHONY: rebuild
rebuild:
	@docker-compose build --no-cache

.PHONY: app_sh
app_sh:
	@docker exec -it platformio_app sh

.PHONY: proxy_sh
proxy_sh:
	@docker exec -it platformio_proxy sh

.PHONY: db_psql
db_psql:
	@docker exec -it platformio_db psql -U platformuser -d platformio

.PHONY: shell_plus
shell_plus:
	@docker exec -it platformio_app python manage.py shell_plus

.PHONY: superuser
superuser:
	@docker exec -it platformio_app python manage.py createsuperuser

.PHONY: black
black:
	black . --exclude postgres_data

.PHONY: makemigrations
makemigrations:
	@docker exec -it platformio_app python manage.py makemigrations

.PHONY: migrate
migrate:
	@docker exec -it platformio_app python manage.py migrate
