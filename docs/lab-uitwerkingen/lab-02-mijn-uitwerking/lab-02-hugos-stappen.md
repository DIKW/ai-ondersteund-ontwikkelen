# uitwerking mmet de hand

Eerst  het goede startpunt uitchecken:

git fetch --tags
git tag | grep -i lab

lab-01-solution
lab-01-start
lab-02-solution
lab-02-start
lab-03-solution
lab-03-start

# maak een nieuwe branche vanaf de start tag van lab 2

Belangrijk: niet alleen de tag uitchecken met git checkout <tag>, want dan werk je meestal detached.

git switch -c lab-02-hugos-oplossing lab-02-start
