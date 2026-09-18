serve:
	bundle exec jekyll serve

## see https://www.supertechcrew.com/jekyll-check-for-broken-links/ to learn about how to check links in jekyll
## in short, add ``gem 'rake'` and `gem 'html-proofer'` to the Gemfile, run `bundle install`
## and run the following command
htmlproofer:
	bundle exec jekyll build
	bundle exec htmlproofer ./_site

YEAR       ?= 2026
AGENDA_DIR := assets/$(YEAR)
AGENDA_MD  := $(AGENDA_DIR)/$(YEAR)-agenda-A4.md
AGENDA_QR  := $(AGENDA_DIR)/amidd-qr.png
AGENDA_PDF := $(AGENDA_DIR)/AMIDD-$(YEAR)-agenda-A4.pdf

.PHONY: agenda
agenda: $(AGENDA_PDF)

$(AGENDA_QR):
	qrencode -o $@ -s 10 -m 1 -l M "http://www.amidd.ch"

$(AGENDA_PDF): $(AGENDA_MD) $(AGENDA_QR)
	pandoc $< --resource-path=$(AGENDA_DIR) -o $@
	@pages=$$(pdfinfo $@ | awk '/^Pages:/ {print $$2}'); \
	if [ "$$pages" = "1" ]; then \
	        echo "OK: $@ fits on one A4 page."; \
	else \
	        echo "WARNING: $@ is $$pages pages — trim content or tighten spacing in the YAML header."; \
	fi

