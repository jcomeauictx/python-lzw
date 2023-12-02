all: lzw/__init__.doctest test all_tests
%.doctest: %.py
	-python3 -m doctest $< 2>&1 | tee /tmp/$(@F).log
	less /tmp/$(@F).log
test: test.py
	./$< 2>/tmp/test.log | xxd | xxd -R - /tmp/test.xxd
