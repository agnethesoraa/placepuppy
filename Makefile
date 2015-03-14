all:
	@echo 'nothing to do'

production:
	venv/bin/pip install -Ur requirements.txt
	sudo supervisorctl restart placepuppy

