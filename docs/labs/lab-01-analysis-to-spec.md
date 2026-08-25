# Lab 01: analyse naar spec

- **Doel:** businessbehoefte scherp krijgen voor verplicht ingevulde velden bij indienen.
- **Tijd:** 60-75 min
- **Startpunt:** `docs/domain.md`, `src/change_request_tracker/service.py`, `tests/test_service.py`

## Stappen
1. **(10-15 min)** Lees relevante code, tests en domeindocumentatie.
2. **(10-15 min)** Gebruik Copilot CLI alleen voor analyse (geen codewijzigingen).
3. **(15-20 min)** Schrijf een beperkte spec (probleem, doel, scope, niet-doen-lijst).
4. **(10-15 min)** Formuleer 3-5 acceptatiecriteria die toetsbaar zijn.
5. **(5-10 min)** Noteer minimaal 1 open vraag of aanname.

## Voorbeeld (beperkte spec-fragment)

Gebruik dit als referentie voor omvang en scherpte (kopieer niet blind):

### Probleem
Het systeem accepteert momenteel `submit` voor verzoeken met lege verplichte velden.

### Doel
`submit` mag alleen slagen als `title`, `description` en `requester` gevuld zijn.

### Scope
- Valideer verplichte velden tijdens `submit`.
- Geef een duidelijke foutmelding bij ontbrekende velden.

### Niet doen
- Geen wijziging aan prioriteitsregels.
- Geen wijziging aan statusovergangen buiten `DRAFT -> SUBMITTED`.

### Acceptatiecriteria
- Submit van een volledig verzoek resulteert in status `SUBMITTED`.
- Submit met leeg `title` faalt met expliciete validatiefout.
- Submit met lege `description` faalt met expliciete validatiefout.
- Submit met lege `requester` faalt met expliciete validatiefout.

### Open vraag
Wordt whitespace-only (`"   "`) behandeld als leeg?

## Verwachte artefacten
- Ingevulde spec (Markdown)
- Acceptatiecriteria
- Open vraag/aanname

## Modeluitwerking (voor reviewfase)
- Zie `docs/lab-uitwerkingen/lab-01/model-uitwerking.md`.
- Gebruik deze uitwerking pas na de eigen poging van het team, als kalibratie.

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Scope-afbakening | Scope is breed/vaag | Scope is klein en afgebakend | Scope bevat expliciete niet-doen-lijst | Scope + niet-doen-lijst voorkomen aantoonbaar scope creep |
| Toetsbaarheid criteria | Criteria zijn subjectief | 3-5 criteria, observeerbaar | Criteria zijn observeerbaar en herleidbaar naar gedrag | Criteria bevatten ook expliciete fout-/randgevallen |
| Traceerbaarheid naar bron | Geen koppeling naar domein/code/tests | Minimaal 1 bron genoemd | Relevante domeinregel + code/testlocaties genoemd | Elke kernkeuze is terug te leiden naar een expliciete bron |
| Onzekerheidsmanagement | Geen open vraag/aannames | Minimaal 1 open vraag of aanname benoemd | Open vraag is specifiek en beslisbaar | Open vraag bevat impact en voorgesteld beslismoment |

## Stop/escalatie
- Stop en escaleren bij onduidelijke businessregel.

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Je kunt onderbouwen hoe jouw spec voldoet aan de rubric (minimaal voldoende op alle criteria).

## Reflectie
- Welke aanname had de meeste impact op je spec?
