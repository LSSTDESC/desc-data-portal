image = registry.nersc.gov/mp107/dataportal:latest

build:
	docker build . -t $(image)

run:
	docker run --env-file env.list -p 5000:5000 $(image)

push:
	docker push $(image)
