all: render-gitbook

render-gitbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

render-epubbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"

render-pdfbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')"
	
render-all:
	Rscript -e "bookdown::render_book('index.Rmd', 'all')"

proposal: book-proposal-zhang-202005.pdf

book-proposal-zhang-202005.pdf: 00-preface.Rmd
	pandoc -f markdown \
            -V linkcolor:blue \
            -V geometry:a4paper \
            -V geometry:margin=2cm \
            -V mainfont="DejaVu Serif" \
            -V monofont="DejaVu Sans Mono" \
            --pdf-engine=xelatex \
            00-preface.Rmd -o book-proposal-zhang-202005.pdf

00-preface.txt: 00-preface.Rmd
	## to copy the context to xclip (using clipboard)
	pandoc -f markdown 00-preface.Rmd -o 00-preface.txt

copy-00-preface.txt: 00-preface.txt
	xclip -i 00-preface.txt -selection clipboard
