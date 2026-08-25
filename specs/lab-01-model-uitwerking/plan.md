# Plan (lab 01 modeluitwerking)

## Maximaal 5 stappen
1. Definieer de vaste structuur voor modeluitwerkingen in docs/lab-uitwerkingen/.
2. Schrijf een complete modeluitwerking voor Lab 01 conform het spec-template.
3. Voeg een expliciete rubric-beoordeling toe op de modeluitwerking.
4. Voeg traceability en trainer-notes toe voor didactische kalibratie.
5. Link de modeluitwerking vanuit het Lab 01-document en voer checks uit.

## Trainingsstate in GitHub
- Gebruik per lab een vaste feature branch voor uitwerking (bijvoorbeeld `training/lab-01`).
- Gebruik tags voor reproduceerbare trainingsstates:
	- `lab-01-start`
	- `lab-01-solution`
- Herhaal dit patroon voor volgende labs (`lab-02-start`, `lab-02-solution`, etc.).
- Gebruik de start-tag voor oefenstart en de solution-tag als referentie-uitwerking tijdens review.

## Relevante bestanden
- docs/labs/lab-01-analysis-to-spec.md
- docs/domain.md
- tests/test_service.py
- specs/template/spec.md

## Risico's
- Modeluitwerking wordt te dwingend en ontmoedigt eigen denkwerk.
- Te veel detail maakt het document moeilijk inzetbaar tijdens de training.

## Verificatie
- bash scripts/check.sh
- Handmatige controle op acceptatiecriteria uit spec.md
