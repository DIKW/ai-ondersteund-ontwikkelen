# Lab 08: LLMWiki content toevoegen

- **Doel:** voeg gecontroleerd content toe aan de wiki met bronverwijzingen, tags en expliciete confidence.
- **Tijd:** 60-75 min
- **Startpunt:** uitkomst van lab 07 en `knowledge-lab/WORKFLOW.md`

## Querypad (realistisch)

### Primair pad (met beschikbare AI-tooling)
1. Stel een vraag over de aangemaakte wiki-inhoud.
2. Laat antwoord formuleren op basis van de wiki-pagina's.
3. Controleer of het antwoord expliciet bronverwijzingen en confidence bevat.

### Fallback-pad (zonder querytool)
1. Schrijf 3 vragen op die de wiki moet kunnen beantwoorden.
2. Beantwoord die vragen handmatig op basis van de wiki-pagina's.
3. Noteer per antwoord gebruikte bronnen en confidence-inschatting.

Beide paden zijn geldig binnen dit lab.

## Stappen
1. Selecteer maximaal drie onderwerpen uit de goedgekeurde bronnen in `raw/`.
2. Controleer per onderwerp of er al een pagina bestaat om doublures te voorkomen.
3. Maak of actualiseer pagina's met:
   - bronverwijzingen
   - tags uit de vaste taxonomie
   - betekenisvolle wikilinks naar gerelateerde pagina's
4. Markeer per pagina onzekerheden, lage confidence en eventuele tegenstrijdigheden.
5. Werk `knowledge-lab/index.md` bij met links naar nieuwe of gewijzigde pagina's.
6. Voeg in `knowledge-lab/log.md` een append-only wijzigingsregel toe met datum en korte samenvatting.
7. Laat een menselijke reviewer controleren op juistheid, traceerbaarheid en governance.

## Voorbeeldqueryset en verwachte antwoordkwaliteit

Voorbeeldvragen:
1. Welke reviewcontroles zijn verplicht voor een AI-ondersteunde wijziging?
2. Welke onzekerheden moeten expliciet gemarkeerd blijven in de wiki?
3. Hoe borg je dat nieuwe kennis binnen scope en taxonomie blijft?

Verwachte antwoordkwaliteit:
- Antwoord verwijst naar concrete wiki-secties of pagina's.
- Antwoord maakt onzekerheden zichtbaar in plaats van te verbergen.
- Antwoord bevat een confidence-inschatting en eventuele open punten.

## Verwachte artefacten
- Maximaal drie nieuwe of geactualiseerde wiki-pagina's
- Bijgewerkte `knowledge-lab/index.md`
- Nieuwe append-only logregel in `knowledge-lab/log.md`
- Reviewuitkomst met akkoord of terugkoppeling

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Brontraceerbaarheid | Bronnen ontbreken of zijn vaag | Bronnen per pagina aanwezig | Bronnen per claim of sectie aanwezig | Bronnen per claim + consistent door index/log te volgen |
| Taxonomie-consistentie | Tags buiten schema of inconsistent | Tags binnen schema | Tags binnen schema en semantisch passend | Tags binnen schema, passend en consistent over pagina's |
| Confidence-discipline | Geen confidence/ onzekerheden | Confidence of onzekerheden benoemd | Confidence en onzekerheden expliciet per pagina | Confidence en onzekerheden expliciet + impact op gebruik benoemd |
| Querybaarheid | Vragen niet te beantwoorden | Minimaal 3 vragen beantwoord | 3 vragen beantwoord met bronverwijzing | 3 vragen beantwoord met bronverwijzing, confidence en open punten |

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Primair pad of fallback-pad is volledig uitgevoerd.
- Rubric scoort minimaal voldoende op alle criteria.

## Stop/escalatie
- Escaleer als meer dan drie bestaande pagina's geraakt moeten worden.
- Escaleer bij inhoudelijke tegenstrijdigheid die niet met bestaande bronnen te beslechten is.

## Reflectie
- Welke contentkeuze leverde de hoogste informatiewaarde op met de laagste onderhoudslast?
