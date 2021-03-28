# Create the pdf file and delete unnecessary files.
lualatex presentation.tex
pdflatex presentation.tex
rm *.aux
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
