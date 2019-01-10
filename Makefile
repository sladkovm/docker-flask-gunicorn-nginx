build:
	docker system prune -fa
	docker-compose up --build -d

clean:
	docker-compose down
	docker system prune -fa
