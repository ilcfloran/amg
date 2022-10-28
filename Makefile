.PHONY: compose-build
compose-build:
	docker-compose \
		--file docker-compose.yaml \
		build --no-cache

.PHONY: compose-up
compose-up: compose-build
	docker-compose \
		--file docker-compose.yaml \
		up \
		-d

.PHONY: compose-down-up
compose-down-up: \
	compose-down \
	compose-up

.PHONY: compose-down
compose-down:
	docker-compose \
		--file docker-compose.yaml \
		down
