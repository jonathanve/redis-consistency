
venv:
	virtualenv -p /usr/bin/python3.8 venv

init:
	pip install -r requirements.txt

fire_forget:
	python fire_forget.py

transactions:
	python transactions.py

scripting:
	python scripting.py
