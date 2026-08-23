# Lab 07: LLMWiki starten

- **Doel:** richt een veilige, navolgbare startsituatie in voor werken met de LLMWiki-structuur.
- **Tijd:** 45-60 min
- **Startpunt:** `knowledge-lab/README.md`, `knowledge-lab/SCHEMA.md`, `knowledge-lab/WORKFLOW.md`

## Stappen
1. Lees `SCHEMA.md`, `index.md` en de meest recente regels in `log.md`.
2. Controleer de grenzen: geen externe ongeverifieerde bronnen, geen productie- of klantdata.
3. Kies 1 trainingsvraag die binnen de taxonomie past.
4. Definieer welke bronbestanden in `knowledge-lab/raw/` als input worden gebruikt.
5. Leg in een kort startnotitie vast: scope, bronnen, verwachte pagina's en reviewmoment.
6. Voeg een nieuwe append-only logregel toe voor de start van de oefening.

## Voorbeeld startnotitie

Gebruik dit als compact format:

- Vraag: Welke controles zijn nodig voor veilige AI-ondersteunde merge-review?
- Scope: maximaal 3 wiki-pagina's (1 concept, 1 proces, 1 checklist).
- Bronnen: `knowledge-lab/raw/...` (expliciete bestandsnamen opnemen).
- Taxonomie-tags: `verification`, `review`, `governance`.
- Reviewmoment: menselijke review na eerste conceptversie.
- Bekende onzekerheid: definities van "voldoende bewijs" verschillen per team.

## Verwachte artefacten
- Startnotitie met scope en bronselectie
- Geactualiseerde `knowledge-lab/log.md` (append-only)
- Bevestiging dat de oefening binnen taxonomie en grenzen valt

## Kwaliteitscheck
- Bronnen zijn expliciet en controleerbaar.
- Scope is klein genoeg voor maximaal drie wiki-pagina's.
- Menselijke reviewmomenten zijn vooraf vastgelegd.

## Stop/escalatie
- Escaleer als bronkwaliteit of herkomst onduidelijk is.
- Stop bij conflict met `SCHEMA.md`-grenzen.

## Klaarcheck
Controleer objectief:
- Startnotitie bevat vraag, scope, bronlijst, tags en reviewmoment.
- `knowledge-lab/log.md` heeft een nieuwe append-only regel.
- Scope blijft binnen maximaal 3 wiki-pagina's.
- Gekozen tags vallen binnen de taxonomie uit `SCHEMA.md`.

## Handoff naar lab 08
Gebruik deze output als ingang voor lab 08:
- Goedgekeurde bronlijst.
- Gekozen taxonomie-tags.
- Gedefinieerde trainingsvraag.
- Open onzekerheden die expliciet gemarkeerd moeten blijven.

## Reflectie
- Welke startkeuze verkleinde het risico op hallucinatie of scope-uitbreiding het meest?
