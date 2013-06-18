.PHONY: docs test clean

bin/python:
	virtualenv . --python python2
	bin/python setup.py develop

bin/sphinx:
	bin/pip install sphinx

test: bin/python
	bin/pip install tox
	bin/tox

docs: bin/sphinx
	SPHINXBUILD=../bin/sphinx-build $(MAKE) -C docs html $^

clean:
	rm -rf bin .tox include/ lib/ man/ runcommands.egg-info/ build/
