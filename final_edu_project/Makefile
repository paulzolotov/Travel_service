FORMAT_FOLDER?='travel_service/'

black:
	python3 -m black ${FORMAT_FOLDER}
isort:
	python3 -m isort ${FORMAT_FOLDER}
flake8:
	python3 -m flake8 ${FORMAT_FOLDER}
interrogate:
	python3 -m interrogate ${FORMAT_FOLDER}

format:
	make black FORMAT_FOLDER=${FORMAT_FOLDER}
	make isort FORMAT_FOLDER=${FORMAT_FOLDER}
	make flake8 FORMAT_FOLDER=${FORMAT_FOLDER}
	make interrogate FORMAT_FOLDER=${FORMAT_FOLDER}