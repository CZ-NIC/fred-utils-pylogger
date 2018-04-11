APP = pylogger

.PHONY: default isort test

default: test

isort:
	isort --recursive ${APP}

test:
	tox

