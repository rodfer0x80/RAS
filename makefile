.PHONY: update
update:
	./scripts/update.py

.PHONY: run 
run: 
	./scripts/run.py

.PHONY: build 
build: 
	./scripts/build.sh

.PHONY: serve
serve: 
	./scripts/serve.py


