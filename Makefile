.PHONY: build_infra_ext_iv
build_infra_ext_iv:
	docker compose down
	docker compose up -d

.PHONY: start_container
start_container:
	docker start backend_proj_ext_quatro
	docker exec -it backend_proj_ext_quatro sh

.PHONY: fastapi_run
fastapi_run:
	docker start backend_proj_ext_quatro
	docker exec backend_proj_ext_quatro npm run dev 

.PHONY: stop_backend_container
stop_backend_container:
	docker stop backend_proj_ext_quatro

