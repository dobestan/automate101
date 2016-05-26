clean:
	find . -name "*.pyc" -exec rm -rf {} \;


migrate:
	python automate101/manage.py makemigrations contents users
	python automate101/manage.py migrate