# clean the directory from unneeded files

all: doc

doc :
	./generate_html.py

read:
	open generated_html/index.html

.PHONY : clean
clean :
	-rm -rf *~ *.pyc html

