# Compiles the marp deck into pdf and html

# This command only works if you have marp-cli: npm install @marp-team/marp-cli
# Optional: to convert the HTMLs to PDFs using the command line, you will need chrome/chromium
MARP=marp
# Alternatively, you can use marp-cli from docker: run "docker pull marpteam/marp-cli" and use:
#MARP=docker run --rm --init -v "$(PWD)":/home/marp/app/ marpteam/marp-cli

IN_DIR=slides
OUT_DIR=build
RELEASE_DIR=release

# You can overwrite these from the command line
# For example: make -e THEME=marp-viu
THEME=marp-viu
THEME_SET=slides-support/slides/themes
THEME_OPTS=--theme $(THEME) --theme-set "$(THEME_SET)"

VERSION=$(shell date '+%Y%m')

all:
	git submodule init
	git submodule update --remote --merge
	make htmls

build: toc
	mkdir -p $(OUT_DIR)
	cp -r $(IN_DIR)/images $(OUT_DIR)/.

pdfs: build
	PUPPETEER_TIMEOUT=0 $(MARP) -I $(IN_DIR) -o $(OUT_DIR) --no-config $(THEME_OPTS) --pdf --allow-local-files --html --pdf-notes

serve:
	$(MARP) -I $(IN_DIR) $(THEME_OPTS) -w -s --bespoke.progress true --html

release: pdfs
	mkdir -p $(RELEASE_DIR)
	cd $(OUT_DIR) && zip ../$(RELEASE_DIR)/$(VERSION)-slides.zip *pdf

htmls: build
	$(MARP) -I $(IN_DIR) -o $(OUT_DIR) --no-config $(THEME_OPTS) --bespoke.progress true --html --bespoke.transition

toc:
	find $(IN_DIR) -name '*.md' -exec python3 slides-support/maketoc.py --input \{} --level 2 \;

clean:
	/bin/rm -rf $(OUT_DIR)

.PHONY: all clean
