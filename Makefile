build:
	docker system prune -fa
	docker-compose up --build -d