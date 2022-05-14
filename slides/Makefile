# Compiles the marp deck into pdf and html

# This command only works if you have marp-cli: npm install -g @marp-team/marp-cli
# Optional: chrome/chromium in your system for the PDF
MARP=marp
# This command needs marp-cli from docker: docker pull marpteam/marp-cli
#MARP=docker run --rm --init -v "$(PWD)":/home/marp/app/ marpteam/marp-cli

# You can overwrite these from the command line
# For example: make -e THEME=marp-viu
THEME=marp-viu
THEME_SET=themes
THEME_OPTS=--theme $(THEME) --theme-set "$(THEME_SET)"

# Convert all .md files in this directory
SRCS=$(shell find . -name '*.md')
OBJS=$(patsubst %.md,%.html,$(SRCS))
OBJS_PDFS=$(patsubst %.md,%.pdf,$(SRCS))

all: $(OBJS)

allpdfs: $(OBJS_PDFS)

%.pdf: %.md
	PUPPETEER_TIMEOUT=0 $(MARP) "$<" -o "$@" --no-config $(THEME_OPTS) --pdf --allow-local-files --html --pdf-notes

%.html: %.md
	$(MARP) "$<" -o "$@" --no-config $(THEME_OPTS) --bespoke.progress true --html
	#--bespoke.transition

clean:
	/bin/rm -rf *.html *.pdf

.PHONY: all clean
