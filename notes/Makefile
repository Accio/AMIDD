all: render-gitbook

render-gitbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

render-epubbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"

render-pdfbook:
	Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')"
	
render-all:
	Rscript -e "bookdown::render_book('index.Rmd', 'all')"
