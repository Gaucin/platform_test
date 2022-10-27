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
	@docker exec -it buroparlamentario_app sh

.PHONY: proxy_sh
proxy_sh:
	@docker exec -it buroparlamentario_proxy sh

.PHONY: db_psql
db_psql:
	@docker exec -it buroparlamentario_db psql -U buroparlamentario_admin -d buroparlamentario

.PHONY: shell_plus
shell_plus:
	@docker exec -it buroparlamentario_app python manage.py shell_plus

.PHONY: superuser
superuser:
	@docker exec -it buroparlamentario_app python manage.py createsuperuser

.PHONY: black
black:
	black . --exclude postgres_data

.PHONY: makemigrations
makemigrations:
	@docker exec -it buroparlamentario_app python manage.py makemigrations

.PHONY: migrate
migrate:
	@docker exec -it buroparlamentario_app python manage.py migrate

.PHONY: catalogs_data
catalogs_data:
	@docker exec -it buroparlamentario_app python manage.py loaddata state township settlement circumscription district political_party topic social_network

.PHONY: admin_data
admin_data:
	@docker exec -it buroparlamentario_app python manage.py loaddata group admin_user

.PHONY: candidate_data
candidate_data:
	@docker exec -it buroparlamentario_app python manage.py loaddata user candidate_profile administrative_career legislative_career other_experience academic_path proposal candidate_social_network
