clean:
	rm -rf build evaluation_agent.zip

build-lambda: clean
	mkdir -p build
	cp -r *.py build
	cp -r abi build
	pip install -r requirements.txt cython -t build
	cd build && zip -r ../evaluation_agent.zip .
