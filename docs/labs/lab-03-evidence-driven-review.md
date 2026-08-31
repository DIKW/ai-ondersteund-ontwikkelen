# Lab 03: bewijsgedreven review

- **Doel:** beoordeel een wijziging primair op bewijs, regressierisico en spec-conformiteit.
- **Tijd:** 45-60 min
- **Startpunt:** state `lab-02-solution` (uitkomst van lab 02 inclusief codewijziging en testresultaten)

## Stappen
1. **(8-10 min)** Lees spec, plan en diff zonder direct op stijl te focussen.
2. **(8-10 min)** Classificeer bevindingen op ernst: blokkerend, belangrijk, suggestie.
3. **(8-10 min)** Controleer of acceptatiecriteria aantoonbaar afgedekt zijn.
4. **(8-10 min)** Controleer op scope-afwijking ten opzichte van de spec.
5. **(8-10 min)** Formuleer reviewbesluit: accepteren, terugsturen of escaleren.
6. **(5-10 min)** Verwerk 1 terugkoppeling in de wijziging of motiveer waarom niet.

## Voorbeeldbevindingen per ernstniveau
- **Blokkerend:** "Acceptatiecriterium voor ongeldige invoer is niet afgedekt; er ontbreekt een negatieve test voor submit met leeg requester."
- **Belangrijk:** "Wijziging raakt ook prioriteitsgedrag terwijl de spec alleen submit-validatie beschrijft; scope-afwijking motiveren of terugdraaien."
- **Suggestie:** "Foutmelding kan specifieker, zodat reviewer sneller ziet welk veld ontbreekt."

## Verwachte artefacten
- Reviewoordeel met bevindingen per ernst
- Besluit met onderbouwing
- Eventuele kleine herstelwijziging + testbewijs

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Ernstclassificatie | Bevindingen zonder prioriteit | Bevindingen ingedeeld op ernst | Ernst is onderbouwd met impact | Ernst is onderbouwd met impact en herstelrichting |
| Bewijs-koppeling | Geen bewijsverwijzingen | Bevindingen verwijzen naar spec of test | Bevindingen verwijzen naar spec en test | Elke bevinding is volledig herleidbaar naar spec, code en testbewijs |
| Scopecontrole | Scope-afwijking niet benoemd | Scope-afwijking benoemd indien aanwezig | Scope-afwijking + risico benoemd | Scope-afwijking + risico + besluitoptie expliciet |
| Besluitkwaliteit | Onhelder reviewbesluit | Duidelijk besluit (accept/rework/escalate) | Besluit met onderbouwing | Besluit met onderbouwing en expliciete vervolgstap |

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Review bevat minimaal 1 bevinding per relevant risico en een expliciet besluit.

## Stop/escalatie
- Escaleer bij onduidelijke businessregel of als bewijs ontbreekt voor een kritisch criterium.

## Reflectie
- Welke reviewbevinding gaf het meeste risicoreductie tegen minimale extra inspanning?

## Modeluitwerking
- Referentie-uitwerking voor nabespreking: `docs/lab-uitwerkingen/lab-03/`
