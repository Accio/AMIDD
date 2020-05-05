all: render-gitbook

render-gitbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

render-epubbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"

render-pdfbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')"
	
render-all:
	Rscript -e "bookdown::render_book('index.Rmd', 'all')"

render-preface: 00-preface.Rmd
	pandoc -f markdown \
            -V linkcolor:blue \
            -V geometry:a4paper \
            -V geometry:margin=2cm \
            -V mainfont="DejaVu Serif" \
            -V monofont="DejaVu Sans Mono" \
            --pdf-engine=xelatex \
            00-preface.Rmd -o 00-preface.pdf


