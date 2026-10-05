.PHONY: build_infra_ext_iv
build_infra_ext_iv:
	docker compose down -v
	docker compose up -d