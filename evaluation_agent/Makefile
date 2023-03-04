clean:
	rm -rf build evaluation_agent.zip

build-lambda: clean
	mkdir -p build
	cp -r *.py build
	cp -r abi build
	pip install -r requirements.txt cython -t build
	cd build && zip -r ../evaluation_agent.zip .

build-image:
	 docker build -t ea-agent .

push-image: build-image
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 778966706143.dkr.ecr.us-east-2.amazonaws.com
	docker tag ea-agent:latest 778966706143.dkr.ecr.us-east-2.amazonaws.com/ea-agent-2:latest
	docker push 778966706143.dkr.ecr.us-east-2.amazonaws.com/ea-agent-2:latest
