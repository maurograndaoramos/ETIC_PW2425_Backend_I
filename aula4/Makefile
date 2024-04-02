

install:
		poetry install

activate:
	poetry shell


docker.build:
	docker-compose build --force-rm 

docker.shell:
	docker-compose run --rm app bash

run.jorge: activate # Run 'make activate' before 'run.jorge'
	program add jorge

	
