# Compiles the marp deck into pdf and html

# This command only works if you have marp-cli: npm install -g @marp-team/marp-cli
# Optional: chrome/chromium in your system for the PDF
MARP=marp
# Alternatively, this command needs marp-cli from docker: docker pull marpteam/marp-cli
#MARP=docker run --rm --init -v "$(PWD)":/home/marp/app/ marpteam/marp-cli

IN_DIR=slides
OUT_DIR=build

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

build:
	mkdir -p $(OUT_DIR)
	cp -r $(IN_DIR)/images $(OUT_DIR)/.

pdfs: build
	PUPPETEER_TIMEOUT=0 $(MARP) -I $(IN_DIR) -o $(OUT_DIR) --no-config $(THEME_OPTS) --pdf --allow-local-files --html --pdf-notes

serve:
	$(MARP) -I $(IN_DIR) -w -s

release: pdfs
	rm -rf $(OUT_DIR)/themes
	rm -rf $(OUT_DIR)/images
	cd $(OUT_DIR) && zip $(VERSION)-slides.zip *pdf && rm *.pdf

htmls: build
	$(MARP) -I $(IN_DIR) -o $(OUT_DIR) --no-config $(THEME_OPTS) --bespoke.progress true --html --bespoke.transition

clean:
	/bin/rm -rf $(OUT_DIR)

.PHONY: all clean
