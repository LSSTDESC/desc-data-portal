image = dataportal:latest

build:
	docker build . -t $(image)

run:
	docker run --env-file env.list -p 5000:5000 $(image)
