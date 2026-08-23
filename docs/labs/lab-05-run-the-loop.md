# Lab 05: voer de loop uit

- **Doel:** voer de volledige beperkte lus uit op dezelfde feature.
- **Tijd:** 60-75 min
- **Startpunt:** ontwerp uit lab 04

## Stappen
1. Plan laten maken en menselijk goedkeuren.
2. Implementatie laten uitvoeren.
3. Bewijs verzamelen (tests/review).
4. Terugsturen of escaleren bij onzekerheid.
5. Voeg 1 verbetering toe aan instructie, test, gate of stopvoorwaarde.

## Done-definition

Een cyclus is "klaar" als minimaal dit aanwezig is:
- Goedgekeurd plan (menselijke gate zichtbaar).
- Beperkte wijziging binnen afgesproken scope.
- Testbewijs of checkresultaat dat de wijziging ondersteunt.
- Reviewoordeel met expliciet besluit (accept/rework/escalate).
- Vastgelegde verbeteractie voor volgende cyclus.

## Rework-pad (bij onvolledig bewijs)
1. Reviewer markeert ontbrekend of zwak bewijs als blokkering.
2. Implementer vult alleen het ontbrekende bewijs aan (geen scope-uitbreiding).
3. Planner bevestigt dat rework nog binnen oorspronkelijke scope valt.
4. Reviewer herbeoordeelt uitsluitend het aangepaste onderdeel.
5. Gatekeeper beslist opnieuw.

**Let op:** rework buiten de geplande tijd mag als optionele verlenging worden gepland.

## Mini-voorbeeld: mislukte handoff en correctie

- **Mislukte handoff:** "Wijziging klaar, tests groen." (geen lijst met tests, geen scopeverwijzing, geen open risico)
- **Correctie:**
	- Gewijzigde bestanden: ...
	- Uitgevoerde checks: ...
	- Spec-criterium afgedekt: ...
	- Open risico: ...
	- Reviewvraag: ...

## Verwachte artefacten
- Plan, diff, reviewoordeel
- Verbeteractie

## Kwaliteitscheck
- Contextbehoud en menselijke goedkeuring zijn zichtbaar.

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Alle onderdelen uit de done-definition zijn aantoonbaar aanwezig.
- Rework (indien nodig) is traceerbaar en binnen scope gebleven.

## Stop/escalatie
- Escaleer als onzekerheid niet oplosbaar is binnen scope.

## Reflectie
- Welke loop-stap was het meest foutgevoelig?
