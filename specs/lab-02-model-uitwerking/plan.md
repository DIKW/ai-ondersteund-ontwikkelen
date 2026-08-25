# Plan (lab 02 modeluitwerking)

## Maximaal 5 stappen
1. Definieer de vaste structuur voor de Lab 02 modeluitwerking in `docs/lab-uitwerkingen/lab-02/`.
2. Werk een compacte, spec-conforme wijziging uit inclusief scopegrens en motivatie.
3. Leg bewijs vast met testresultaat, reviewuitkomst en een compact git-diff-fragment.
4. Voeg rubric-beoordeling, traceability en trainer-notes toe als aparte artefacten.
5. Link de modeluitwerking vanuit het Lab 02-document en voer checks uit.

## Relevante bestanden
- docs/labs/lab-02-spec-to-change.md
- docs/lab-uitwerkingen/lab-01/model-uitwerking.md
- docs/domain.md
- src/change_request_tracker/service.py
- tests/test_service.py

## Risico's
- De modeluitwerking wordt te groot en verliest het karakter van "kleine wijziging".
- Diff/feedback bevat te veel details, waardoor cursisten de kernstappen niet meer herkennen.
- Bewijs richt zich op alleen positieve paden en mist regressierisico.

## Verificatie
- bash scripts/check.sh
- Handmatige controle op acceptatiecriteria uit `specs/lab-02-model-uitwerking/spec.md`
- Controle dat modeluitwerking een compact git-diff bevat
