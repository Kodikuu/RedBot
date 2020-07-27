install:
	pip3 install -r requirements.txt

run:
	python3 src/main.py --token ${token}

debug:
	python3 src/main.py --token ${token} --debug
