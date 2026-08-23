# Lab 06: loop tuning met meetbare verbetering

- **Doel:** verbeter de planner-implementer-reviewer-lus op basis van concrete meetpunten.
- **Tijd:** 45-60 min
- **Startpunt:** uitkomst van lab 04 en lab 05

## Falend baseline-scenario (oefencasus)

Gebruik eerst bewust dit falende patroon als baseline:
- Planner-handoff bevat geen expliciete niet-doen-lijst.
- Implementer levert alleen positieve testuitkomst (geen negatieve padcheck).
- Reviewer geeft alleen stijlfeedback en geen risicobeoordeling.

Doel: herken thrashing/context drift vroeg en toon dat 1 gerichte interventie dit verbetert.

## Minimale metricsset (houd het licht)

| Metric | Baseline meten | Doelwaarde na interventie |
|---|---|---|
| Aantal review-rondes tot besluit | # rondes | <= baseline - 1 of gelijk met hogere bewijskwaliteit |
| Open onduidelijkheden na review | # open punten | <= 1 |
| Traceerbaarheid van bewijs | % criteria met expliciet bewijs | 100% |

## Stappen
1. Draai een baseline-cyclus op een kleine wijziging en leg metrics vast.
2. Kies precies 1 loopverbetering (handoff-format, gate, testcheck of escalatieregel).
3. Draai dezelfde wijziging opnieuw met de verbeterde lus.
4. Vergelijk baseline versus verbeterde cyclus.
5. Leg vast of de verbetering behouden, aangepast of verworpen wordt.

## Verwachte artefacten
- Baseline-cycluslog
- Verbeterde cycluslog
- Vergelijking met metrics en conclusie

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Interventiekeuze | Geen duidelijke interventie | 1 concrete interventie gekozen | Interventie direct gekoppeld aan faalpatroon | Interventie + rationale + verwachte impact expliciet |
| Metricdiscipline | Geen baseline of target | Baseline en target aanwezig | Baseline, target en vergelijking aanwezig | Vergelijking bevat ook korte oorzaakanalyse |
| Scopebeheersing | Meerdere wijzigingen tegelijk | Exact 1 wijziging in de loop | 1 wijziging + expliciete afwijzing extra ideeën | 1 wijziging + onderbouwde keuze voor vervolgexperiment |
| Besluitkwaliteit | Onheldere conclusie | Behouden/aanpassen/verwerpen gekozen | Keuze onderbouwd met metrics | Keuze onderbouwd met metrics en risico-afweging |

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Baseline en verbeterde meting zijn beide ingevuld.
- Er is een expliciet besluit over de interventie.

## Stop/escalatie
- Escaleer als verbetering leidt tot scopegroei of onduidelijkheid over verantwoordelijkheden.

## Reflectie
- Welke interventie had de hoogste impact op doorlooptijd of foutreductie?
