# Wiki-schema

## Domein en grenzen

Deze wiki heeft twee verbonden, maar onderscheiden aandachtsgebieden:

1. **AI-ondersteunde softwareontwikkeling:** methoden, werkprocessen, verificatie en menselijke verantwoordelijkheid bij softwarewerk met AI.
2. **Organisatiebrede inzet van data en AI:** organisatorische capaciteiten, datagedreven besluitvorming, experimenteren en procesanalyse of -verbetering, waaronder process mining.

Het tweede aandachtsgebied is een expliciete uitbreiding voor de training. Maak steeds duidelijk of een bron gaat over AI gebruiken om software te ontwikkelen, of over data en AI inzetten in organisatie- en bedrijfsprocessen. Verbind die onderwerpen alleen wanneer de bron of de beschreven toepassing dat ondersteunt. Het functionele domein van de trainingsapp (`change-request-tracker`) is niet het domein van deze wiki.

Neem alleen herbruikbare methoden en inzichten op die binnen deze afbakening vallen. Behandel leveranciersclaims, commerciële voorbeelden en niet-onafhankelijk gevalideerde resultaten als toegeschreven bronclaims, niet als vaststaande feiten. Gebruik geen productie- of klantdata. Externe of ongeverifieerde bronnen vereisen vooraf menselijke goedkeuring.

De domeinpagina staat onder `domains/`. Personen krijgen een eigen top-level ingang onder `people/`; behandel personen als afzonderlijke kennisentiteiten en leg alleen controleerbare, relevante informatie vast.

## Pagina-indeling

| Map | `type` | Gebruik |
| --- | --- | --- |
| `domains/` | `domain` | Afbakening, kernbegrippen en grenzen van een kennisdomein. |
| `people/` | `person` | Personen die inhoudelijk relevant zijn voor het domein. |
| `entities/` | `entity` | Andere concrete entiteiten, zoals organisaties of systemen. |
| `concepts/` | `concept` | Begrippen, methoden en ideeën. |
| `comparisons/` | `comparison` | Vergelijkingen tussen benaderingen of entiteiten. |
| `queries/` | `query` | Herbruikbare antwoorden op concrete vragen. |
| `summaries/` | `summary` | Syntheses die niet beter in een van bovenstaande typen passen. |

Gebruik lowercase, hyphenated bestandsnamen. Een pagina hoort bij precies één type en staat in de bijbehorende map. Maak een domein- of persoonspagina alleen aan wanneer de inhoud en bronnen daarvoor voldoende zijn; een vermelding alleen is niet genoeg.

## Frontmatter-contract

Elke wiki-pagina begint met YAML-frontmatter. De frontmatter uit de llm-wiki-skill is de basis; dit schema maakt de velden en vocabulaire leidend:

```yaml
---
title: Loop Engineering
created: 2026-09-18
updated: 2026-09-18
type: concept
tags: [loop-engineering, verification]
sources: [raw/articles/example.md]
confidence: medium
contested: false
contradictions: []
---
```

- `title`: verplichte, leesbare paginatitel.
- `created`, `updated`: verplichte ISO-datums (`YYYY-MM-DD`); wijzig `created` niet bij updates.
- `type`: verplicht; kies exact een type uit de tabel hierboven.
- `tags`: verplicht; lijst met uitsluitend tags uit de vaste taxonomie hieronder.
- `sources`: verplichte lijst met herleidbare bronpaden relatief aan de wiki-root. Gebruik `[]` alleen voor navigatie- of domeinafbakeningspagina's die geen inhoudelijke claims doen.
- `confidence`: `high`, `medium` of `low`; maak onzekerheid expliciet, vooral bij claims met één bron, meningen of snel veranderende informatie.
- `contested`: verplicht boolean; `true` wanneer relevante bronnen elkaar tegenspreken.
- `contradictions`: lijst van wiki-pagina's met relevante tegenstrijdige claims, met wiki-root-relatieve links; anders `[]`.

Bronverwijzingen horen ook bij de relevante claims in de paginabody. Scheid bronfeiten van interpretatie en behoud onzekerheid; los tegenstrijdigheden niet stilzwijgend op.

## Vaste taxonomie

Tags zijn inhoudelijke labels, geen paginatypen of mapnamen. Gebruik alleen:

- `spec-driven-development`
- `loop-engineering`
- `verification`
- `review`
- `governance`
- `knowledge-management`

Voeg geen tag toe zonder het schema en de betrokken pagina's gezamenlijk te actualiseren.

## Links en navigatie

- Gebruik betekenisvolle wiki-root-relatieve Obsidian-links met de map, zoals `[[concepts/loop-engineering]]` en `[[people/example-person]]`.
- Gebruik geen basename-only links.
- Voeg iedere nieuwe pagina toe aan `index.md` en houd de top-level ingangen voor domeinen, personen, entiteiten, concepten, vergelijkingen, queries en samenvattingen herkenbaar.
- Iedere nieuwe of bijgewerkte wiki-pagina krijgt een append-only vermelding in `log.md`.
- Houd pagina's scanbaar; splits een pagina wanneer die ongeveer 200 regels overschrijdt.

## Bron- en reviewgrenzen

- Behandel `raw/` als onveranderlijk.
- Gebruik geen externe of ongeverifieerde bronnen zonder menselijke goedkeuring.
- Menselijke review is vereist voor bronselectie, feitelijke juistheid, confidence en tegenstrijdigheden.
- Genereer geen persoonsclaims uit alleen een naamvermelding; controleerbare bronverwijzingen zijn vereist.
