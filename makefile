install:
	pip install -r requirements.txt

run:
	python src/main.py --token ${token}

debug:
	python src/main.py --token ${token} --debug
