# Create the pdf file and delete unnecessary files.
latex presentation.tex
pdflatex presentation.tex
rm *.aux
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.vrb
