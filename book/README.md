Here are the lecture notes that are under development.

I used R markdown and the **bookdown** package (https://github.com/rstudio/bookdown) to write the notes. Please see the page "[Get Started](https://bookdown.org/yihui/bookdown/get-started.html)" at https://bookdown.org/yihui/bookdown/ for how to compile this example into HTML. You may generate a copy of the book in `bookdown::pdf_book` format by calling `bookdown::render_book('index.Rmd', 'bookdown::pdf_book')`. More detailed instructions are available here https://bookdown.org/yihui/bookdown/build-the-book.html.

# Output format

For writing purposes, I use `bookdown::gitbook`.

Note that output formats can be specified either in the YAML metadata of the first Rmd file of the book, or a separate YAML file named `_output.yml` under the root directory of the book ([bookdown manual](https://bookdown.org/yihui/bookdown/output-formats.html)). I use the YAML header in `index.Rmd`.


# Licence

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png"/></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
