# Lab 02: spec naar beperkte wijziging

- **Doel:** spec vertalen naar kleine implementatie met bewijs.
- **Tijd:** 60-75 min
- **Startpunt:** voorbeeldfeature uit Lab 01: `docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`

## Definitie: kleine wijziging

Gebruik in dit lab een wijziging die klein en gecontroleerd blijft:

- Raakt bij voorkeur 1 primair gedrag uit de spec.
- Beperkt tot een kleine set bestanden (richtlijn: 1-3 bestanden wijzigen).
- Geen nieuwe dependencies of infrastructuur.
- Inclusief minimaal 1 bewijsstap (test of check) die de wijziging valideert.

Voorbeeld van passende scope: validatie toevoegen op een bestaande service-methode met bijbehorende testaanpassing.

## Stappen
1. Lees eerst de voorbeeldfeature uit Lab 01 en gebruik die als input voor de planner.
2. Vraag de planner om een plan.
3. Beslis als mens of plan klein genoeg is.
4. Laat implementer de wijziging uitvoeren.
5. Laat relevante tests draaien.
6. Laat reviewer of andere deelnemer toetsen tegen de spec.
7. Verwerk 1 bevinding of motiveer afwijzing.

## Verwachte artefacten
- Planner-input: voorbeeldfeature uit Lab 01
- Plan
- Kleine codewijziging
- Testbewijs
- Reviewuitkomst
- Planner input/output (max. 5 stappen, relevante bestanden, aannames, risico's, open vragen)
- Implementer input/output (diff-samenvatting, testuitvoer, onzekerheden)
- Reviewer input/output (oordeel + onderbouwing)

## Modeluitwerking (voor reviewfase)
- Zie `docs/lab-uitwerkingen/lab-02/model-uitwerking.md`.
- Gebruik deze uitwerking pas na de eigen poging van het team, als kalibratie.

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Spec-naleving | Wijziging wijkt af van spec | Wijziging dekt speckern | Wijziging dekt speckern + randvoorwaarde | Wijziging dekt speckern volledig met expliciete traceerbaarheid |
| Scopebeheersing | Scope groeit ongecontroleerd | Wijziging blijft klein | Wijziging blijft klein met expliciete niet-doen-keuzes | Wijziging blijft klein en motiveert actief afgewezen uitbreidingen |
| Testbewijs | Geen of zwak bewijs | Relevante test/check is uitgevoerd | Bewijs toont positief en negatief pad | Bewijs is compleet, reproduceerbaar en herleidbaar naar criteria |
| Reviewkwaliteit | Review is oppervlakkig | Minimaal 1 inhoudelijke bevinding of gemotiveerde afwijzing | Bevindingen zijn geprioriteerd op risico | Review koppelt risico's expliciet aan spec en testbewijs |

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Je hebt een plan, beperkte wijziging, testbewijs en reviewuitkomst.
- De rubric scoort minimaal voldoende op alle criteria.

## Troubleshooting (kort)
- Tests falen: controleer of de wijziging exact de spec raakt en geen extra gedrag introduceert.
- Scope wordt te groot: knip de wijziging op en rond eerst het kleinste specdeel af.
- Review geeft tegenstrijdige signalen: escaleren op onduidelijke businessregel in plaats van gokken.

## Stop/escalatie
- Escaleer als wijziging buiten afgesproken scope groeit.

## Reflectie
- Welk bewijs gaf het meeste vertrouwen?
