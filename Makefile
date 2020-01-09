iAMIDD-proposal.pdf:README.md
	pandoc --number-sections --shift-heading-level-by=-1 README.md -V geometry:"top=3cm, bottom=3cm, left=2cm, right=2cm" -o iAMIDD-proposal.pdf
