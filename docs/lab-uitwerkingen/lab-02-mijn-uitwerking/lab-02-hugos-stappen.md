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

# copilot cli

start copilot in de cli

kies de agent die je wilt gebruiken met /agent selecteer de planner

vraag de planner om de feature beschrijving te lezen en een plan te maken. De planner mag geen directories maken dus die moet je met de hand maken. Dat is een security overweging.

Als de directory er is maakt hij volgende de templaes in de spec folder de drie markdown files plan, spec en tasks.

switch naar de algemene agent en commit de specs in deze branche.

switch naar de implamenter agent en vraag : "kun je deze specs voor me implementeren ? @specs/lab-02-validatie-submit/spec.md"

Dan gaat tie de stappen uitvoeren uit tasks:
1) Tests aanpassen in python, review de diff en accepteer met 1 Yes
2) Service.py aanpassen met de feitelijke code change.
3) Nog een test aanpassen
4) Tests uitvoeren >>> alles groen 13? stuks.
5) Commit

De aaname over de whitespaces blijft staan dit wordt in lab03 mogelijk REWORK...

Switch naar de reviewer agent

Vraag : "beoordeel de wijzigingen tegen deze spec : @specs/lab-02-validatie-submit/spec.md "

Beoordeling

Oordeel:  akkoord voor menselijke merge-review ...