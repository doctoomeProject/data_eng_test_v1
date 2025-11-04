# Makefile for local interview DB setup

.PHONY: up load down rebuild

# Start MySQL container
up:
	docker compose up -d
	@echo "✅ MySQL container started."

# Load data into MySQL
load:
	@echo "⏳ Waiting 10 seconds for MySQL to initialize..."
	sleep 10
	python load_mysql.py
	@echo "✅ Data successfully loaded into MySQL."

# Stop container
down:
	docker compose down
	@echo "🛑 MySQL container stopped."

# Full rebuild (fresh DB + load)
build:
	docker compose down
	docker volume prune -f
	docker compose up -d
	@echo "⏳ Waiting 10 seconds for MySQL to initialize..."
	sleep 10
	python load_mysql.py
	@echo "✅ Database rebuilt and loaded."
