# Compiles the marp deck into pdf and html

# You can overwrite these from the command line.
# For example: make -e THEME=marp-viu
THEME=marp-viu
THEME_SET=themes

#all: index.html 01-conceptos-basicos.html 02-historia.html 03-simetrica.html 04-complejidad.html A1-glosario.html A2-rng.html

SRCS=$(shell find . -name '*.md')
OBJS=$(patsubst %.md,%.html,$(SRCS))

all: $(OBJS)

%.pdf: %.md
	marp "$<" -o "$@" --no-config --theme $(THEME) --theme-set $(THEME_SET) --pdf --allow-local-files --pdf-notes

%.html: %.md
	marp "$<" -o "$@" --no-config --theme $(THEME) --theme-set $(THEME_SET) --bespoke.progress true
	#--bespoke.transition

clean:
	/bin/rm -f *.pdf *html

.PHONY: all clean
