# Plan (lab 03 modeluitwerking)

## Maximaal 5 stappen
1. Valideer de startstate `lab-02-solution` en bepaal de reviewinput uit Lab 02: spec, compacte diff en testbewijs.
2. Schrijf voorbeeldbevindingen op drie ernstniveaus (blokkerend, belangrijk, suggestie).
3. Koppel elke bevinding aan concreet bewijs uit spec, code/diff en tests.
4. Formuleer een expliciet reviewbesluit (accept, rework of escalate) met vervolgstap.
5. Leg de modeluitwerking vast in vaste artefacten en link deze vanuit Lab 03.

## Relevante bestanden
- docs/labs/lab-03-evidence-driven-review.md
- docs/lab-uitwerkingen/lab-02/model-uitwerking.md
- docs/lab-uitwerkingen/lab-03/model-uitwerking.md
- docs/lab-uitwerkingen/lab-03/traceability.md
- docs/lab-uitwerkingen/lab-03/beoordelingscheck.md
- docs/lab-uitwerkingen/lab-03/trainer-notes.md

## Risico's
- Reviewbevindingen blijven te algemeen en niet controleerbaar.
- Te veel focus op schrijfstijl in plaats van risico en bewijs.
- Modeluitwerking stuurt te veel op één exact antwoord en beperkt eigen denkkracht van cursisten.

## Verificatie
- Handmatige controle op acceptatiecriteria uit `specs/lab-03-model-uitwerking/spec.md`.
- Reviewbesluit is herleidbaar naar minimaal één bevinding met bewijs.
- `bash scripts/check.sh` blijft groen als er een kleine herstelwijziging is gedaan; bij docs-only wijziging volstaat expliciete documentatie van deze keuze.
