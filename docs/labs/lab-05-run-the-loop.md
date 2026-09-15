# Lab 05: voer de loop uit op de echte businessregel

- **Doel:** voer de gecontroleerde planner-implementer-reviewer-lus uit voor één concrete feature: prioriteit mag in `DRAFT` wijzigen, maar niet meer nadat het verzoek is ingediend.
- **Tijd:** 60-75 min
- **Startpunt:** ontwerp uit lab 04 en de domeinregel in `docs/domain.md`

## Feature die in deze loop wordt ontwikkeld

De feature is de volgende businessregel uit het domein:

> **Dag 2 (nog niet geïmplementeerde veranderwens):** na indienen mag prioriteit niet meer wijzigen; in `DRAFT` wel.

Dit betekent in praktijk:
- een wijzigingsverzoek in `DRAFT` kan nog een `priority` krijgen of aanpassen
- zodra `status` `SUBMITTED` is, is `priority` read-only
- een poging om de prioriteit te wijzigen na indienen moet worden geblokkeerd
- het gedrag moet duidelijk worden bewezen via tests

## Scope van deze loop

### In scope
- `priority`-behandeling in de service-laag
- validatie van toegestane wijzigingen per status
- tests voor het positieve en negatieve pad
- traceerbare review van het bewijs

### Buiten scope
- database- of opslaglogica
- netwerk of webinterface
- andere statusregels dan de domeinregel hierboven
- extra refactoring of verbeteringen buiten deze feature

## Stappen in de loop

1. **Planner** leest de domeinregel, relevant gedrag en bestaande tests.
2. **Planner** schrijft een klein, expliciet plan met scope, acceptatiecriteria, risico's en verificatie.
3. **Menselijke gatekeeper** keurt het plan goed of vraagt om bijsturing.
4. **Implementer** voert alleen het goedgekeurde plan uit.
5. **Implementer** verzamelt bewijs in testresultaat en diff.
6. **Reviewer** beoordeelt spec-conformiteit, scope en bewijs.
7. **Reviewer** geeft een expliciet besluit: accept / rework / escalate.
8. **Gatekeeper** beslist of de cyclus klaar is of dat er rework nodig is.

## Spec voor deze loop

Gebruik deze als startpunt voor de planner-output en het proefontwerp voor de implementatie:

### Doel
Voorkomen dat een verzoek na indienen nog zijn prioriteit kan wijzigen, terwijl prioriteit in `DRAFT` nog wel mag worden aangepast.

### In scope
- `priority`-logica in `ChangeRequestService`
- validatie van statusafhankelijk gedrag
- bijhorende tests

### Buiten scope
- andere statusflow-implementaties
- extra businessregels of standaardisatie van prioriteitswaarden
- data-opslag of UI

### Acceptatiecriteria
- Een request in `DRAFT` kan een `priority` krijgen of wijzigen.
- Een request in `SUBMITTED` mag niet meer een nieuwe `priority` accepteren.
- De wijziging levert een duidelijke foutmelding op bij verboden transactie.
- Het gedrag is getest met positief en negatief pad.

### Risico's
- Onduidelijkheid over wat precies een "wijziging" van prioriteit is.
- Scope creep door extra validatie of extra statuslogica.
- Onvoldoende bewijs als alleen een codewijziging zonder test is gemaakt.

### Verificatiestappen
- Controleer de bestaande service en tests.
- Voeg testcases toe voor `DRAFT` en `SUBMITTED`.
- Draai de relevante test-suite.
- Verzamel bewijs dat status en prioriteit correct worden afgeschermd.

## Vereiste handoffs

### 1) Planner -> Implementer
Gebruik het handoff-template uit lab 04, maar nu ingevuld voor deze feature:

- Doel van wijziging:
- In scope:
- Buiten scope:
- Acceptatiecriteria:
- Risico's:
- Verificatiestappen:
- Stopvoorwaarden:

### 2) Implementer -> Reviewer
- Uitgevoerde wijziging:
- Gewijzigde bestanden:
- Testbewijs:
- Bekende beperkingen/open punten:
- Vraag aan reviewer:

### 3) Reviewer -> Gatekeeper
- Samenvatting bevindingen (ernst):
- Spec-conformiteit:
- Bewijsdekking:
- Besluitadvies (accept/rework/escalate):
- Voorwaarden voor vervolg:

## Verwachte artefacten

- goedgekeurd plan van de planner
- scope- en acceptatiecriteria per feature
- diff of codewijziging
- testbewijs
- reviewbesluit met expliciet outcome
- verbeteractie voor de volgende cyclus

## Done-definition

Een cyclus is "klaar" als minimaal dit aanwezig is:
- goedgekeurd plan met menselijke gate
- beperkte wijziging binnen de afgesproken scope
- testbewijs dat het gedrag ondersteunt
- reviewoordeel met expliciet besluit (`accept`, `rework`, `escalate`)
- vastgelegde verbeteractie voor de volgende cyclus

## Rework-pad (bij onvolledig bewijs)
1. Reviewer markeert ontbrekend of zwak bewijs als blokkering.
2. Implementer vult alleen het ontbrekende bewijs aan zonder scope-uitbreiding.
3. Planner bevestigt dat rework nog binnen de oorspronkelijke feature valt.
4. Reviewer herbeoordeelt uitsluitend het aangepaste onderdeel.
5. Gatekeeper beslist opnieuw.

**Let op:** rework buiten de geplande tijd mag als optionele verlenging worden gepland.

## Mini-voorbeeld: mislukte handoff en correctie

- **Mislukte handoff:** "Voorkeuren zijn aangepast, tests groen."
  - geen verwijzing naar status
  - geen scopeverwijzing
  - geen expliciete check dat `DRAFT` wel mag en `SUBMITTED` niet meer mag

- **Correctie:**
	- Gewijzigde bestanden: ...
	- Uitgevoerde checks: ...
	- Spec-criterium afgedekt: ...
	- Open risico: ...
	- Reviewvraag: ...

## Kwaliteitscheck

- De loop is zichtbaar en traceerbaar.
- De feature is expliciet gekoppeld aan de domeinregel.
- Er is een menselijk besluitmoment zichtbaar.
- Het reviewbesluit is gebaseerd op bewijs en niet op vermoeden.

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- De loop is uitgevoerd op de feature "prioriteit na indienen vastzetten".
- Er is een expliciet reviewbesluit en een vastgelegde verbeteractie.

## Stop/escalatie
- Escaleer als onzekerheid niet oplosbaar is binnen de feature-scope.
- Escaleer als de wijziging buiten de domeinregel valt of als de review geen sluitend bewijs heeft.

## Reflectie
- Welke handoff of gate was het meest kritieke punt in deze loop?
- Wat gaf de grootste onzekerheid: scope, bewijs of de businessregel zelf?
