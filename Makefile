all: lzw/__init__.doctest
%.doctest: %.py
	python3 -m doctest $<
