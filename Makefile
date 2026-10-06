.PHONY: build_infra_ext_iv
build_infra_ext_iv:
	docker compose down -v
	docker compose up -d

.PHONY: start_container
start_container:
	docker start backend_proj_ext_quatro
	docker exec -it backend_proj_ext_quatro sh