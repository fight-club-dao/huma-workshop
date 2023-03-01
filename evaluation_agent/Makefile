clean:
	rm -rf build evaluation_agent.zip

build-lambda: clean
	mkdir -p build
	cp -r *.py build
	pip install -r requirements.txt -t build
	cd build && zip -r ../evaluation_agent.zip .
