
venv:
	virtualenv -p /usr/bin/python3.8 venv

init:
	pip install -r requirements.txt

redis:
	docker run -d \
	--name redis \
	-p 6379:6379 \
	redis

fire_forget:
	python fire_forget.py

transactions:
	python transactions.py

scripting:
	python scripting.py
