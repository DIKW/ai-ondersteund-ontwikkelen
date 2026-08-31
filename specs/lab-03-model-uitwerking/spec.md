# Spec (lab 03 modeluitwerking)

## Probleem
Cursisten hebben in Lab 03 behoefte aan een concreet voorbeeld van een bewijsgedreven review: welke bevindingen je noteert, hoe je ernst bepaalt en hoe je een onderbouwd reviewbesluit formuleert.

## Doel
Een reviewbare modeluitwerking voor Lab 03 definiëren die laat zien hoe je spec, diff en testbewijs vertaalt naar een gestructureerde review met expliciet besluit.

## Scope
- Gebruik als startstate expliciet `lab-02-solution` (inclusief codewijzigingen en testbewijs uit Lab 02).
- Voeg een map toe voor de Lab 03 modeluitwerking.
- Voeg voor Lab 03 vier artefacten toe:
  - model-uitwerking.md
  - beoordelingscheck.md
  - trainer-notes.md
  - traceability.md
- Voeg in het Lab 03-document een verwijzing naar de modeluitwerking toe.

## Niet-doen-lijst
- Geen nieuwe functionele productwijziging als hoofddoel van Lab 03.
- Geen uitbreiding naar dag-2-prioriteitsregels of andere buiten-scope businessregels.
- Geen wijziging van labdoel of rolverdeling in het werkblad.

## Acceptatiecriteria
- Er bestaat een map docs/lab-uitwerkingen/lab-03 met de vier afgesproken bestanden.
- model-uitwerking.md bevat minimaal:
  - reviewinput (spec, diff, testbewijs) vanuit `lab-02-solution`,
  - bevindingen op drie ernstniveaus (blokkerend, belangrijk, suggestie),
  - reviewbesluit met vervolgstap.
- traceability.md koppelt bevindingen expliciet aan spec, code/diff en testbewijs.
- beoordelingscheck.md beoordeelt de modeluitwerking expliciet met de Lab 03-rubric.
- docs/labs/lab-03-evidence-driven-review.md bevat een duidelijke verwijzing naar de modeluitwerking.

## Open vragen
- Moet de modeluitwerking in Lab 03 altijd één kleine herstelactie bevatten, of volstaat een gemotiveerde acceptatie/rework zonder extra codewijziging? Richtlijn: in dit voorbeeld volstaat een gemotiveerde acceptatie of documentaire rework; een herstelactie is optioneel en alleen zinvol bij aantoonbare trainingsmeerwaarde.
