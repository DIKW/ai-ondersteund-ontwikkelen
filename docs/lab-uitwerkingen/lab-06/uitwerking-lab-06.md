# Uitwerking lab 06: de orchestrator-loop voorbereiden

In deze uitwerking bereid je eerst de oefening en de feature-opdracht voor. Start de `Loop Orchestrator` pas wanneer je bij **Startprompt voor de Loop Orchestrator** bent aangekomen. Tot dat moment wijzig je geen productiecode of tests.

## Aanleiding

In lab 05 heb je de Planner, Implementer en Reviewer handmatig na elkaar gebruikt. De rollen en handoffs waren aanwezig, maar de agents riepen elkaar niet zelf aan. In lab 06 gebruik je de nieuwe `Loop Orchestrator` om deze workflow uit te voeren:

```text
Feature-opdracht
			 |
			 v
		Planner
			 |
			 v
Menselijke goedkeuring van spec, plan en tasks
			 |
			 v
	Implementer
			 |
			 v
		Reviewer
			 |
			 +-- rework --> Implementer --> Reviewer
			 |
			 +-- akkoord/escalatie --> menselijke gatekeeper
```

## Gekozen extra feature

Je ontwikkelt een CLI-commando waarmee de prioriteit van een bestaand wijzigingsverzoek kan worden aangepast.

Gewenst gebruik:

```bash
PYTHONPATH=src python -m change_request_tracker.cli \
	--db .issues.json priority 1 HIGH
```

De leidende businessregel staat al in `docs/domain.md`:

> Na indienen mag prioriteit niet meer wijzigen; in `DRAFT` wel.

Je introduceert dus geen nieuwe businessregel. De service implementeert deze regel al via `ChangeRequestService.update_priority()`. De ontbrekende functionaliteit is dat deze servicebewerking nog niet als regulier CLI-commando beschikbaar is.

## Verwachte wijziging

Laat de Planner de exacte wijziging onderzoeken en vastleggen. Op basis van de huidige code is de voorlopige verwachting:

- in `src/change_request_tracker/cli.py` een subcommando `priority` met een issue-id en nieuwe prioriteit;
- in `src/change_request_tracker/cli.py` aanroep van `update_priority()` en opslag van het bijgewerkte verzoek;
- in `tests/test_cli.py` tests voor het toegestane en verboden pad;
- in een nieuwe map onder `specs/` de bestanden `spec.md`, `plan.md` en `tasks.md`.

Een wijziging van `src/change_request_tracker/service.py` wordt niet verwacht, omdat de benodigde businesslogica daar al aanwezig is. De Planner moet dit controleren en mag deze aanname corrigeren op basis van de repository.

## Verwacht testbewijs

De Planner bepaalt de definitieve testtaken. Controleer dat er minimaal bewijs wordt gepland voor de volgende situaties:

- de prioriteit van een opgeslagen `DRAFT`-verzoek via de CLI kan worden gewijzigd;
- het commando bij succes exitcode `0` en een duidelijke bevestiging geeft;
- de gewijzigde prioriteit na herladen uit het JSON-bestand behouden blijft;
- een prioriteitswijziging na `SUBMITTED` exitcode `1` geeft;
- het verboden pad een duidelijke foutmelding toont;
- de opgeslagen prioriteit na een verboden wijziging ongewijzigd blijft;
- `bash scripts/check.sh` succesvol eindigt.

De Planner beschrijft deze tests en koppelt ze aan de acceptatiecriteria. De Implementer schrijft en draait de tests. De Reviewer beoordeelt of het bewijs de acceptatiecriteria daadwerkelijk afdekt.

## Buiten scope

- Nieuwe prioriteitswaarden of validatieregels bedenken.
- Statusovergangen wijzigen.
- Database-, netwerk- of webfunctionaliteit toevoegen.
- Dependencies toevoegen.
- Bestaande servicecode refactoren zonder noodzaak voor deze feature.
- Mergen, releasen of deployen.

## Startprompt voor de Loop Orchestrator

Selecteer in GitHub Copilot Chat de agent `Loop Orchestrator` en gebruik daarna deze prompt:

```text
Ontwikkel een CLI-feature waarmee de prioriteit van een bestaand
wijzigingsverzoek kan worden aangepast.

Leidende businessregel:
- docs/domain.md
- Prioriteit mag alleen in DRAFT worden gewijzigd.
- Na indienen mag de prioriteit niet meer wijzigen.

Gewenst CLI-gebruik:

PYTHONPATH=src python -m change_request_tracker.cli \
	--db .issues.json priority 1 HIGH

Laat de Planner eerst spec.md, plan.md en tasks.md maken.
Stop daarna voor mijn expliciete goedkeuring.
Na goedkeuring mag de loop automatisch doorgaan via Implementer en Reviewer,
met maximaal twee rework-rondes.

Buiten scope:
- nieuwe prioriteitswaarden of validatieregels bedenken;
- wijzigingen aan statusovergangen;
- database-, netwerk- of UI-functionaliteit;
- dependencies toevoegen;
- merge, release of deployment.
```

## Verwachte uitvoering

### 1. Planner

De orchestrator roept de Planner als subagent aan. De Planner maakt in vaste volgorde:

1. `spec.md` met probleem, doel, scope, niet-doen-lijst en toetsbare acceptatiecriteria;
2. `plan.md` met maximaal vijf technische stappen, relevante bestanden, risico's en verificatie;
3. `tasks.md` met geordende implementatie- en testtaken, eigenaar, bewijs en stopvoorwaarden.

De Planner moet ieder acceptatiecriterium koppelen aan minimaal een test- of verificatietaak.

### 2. Menselijke plangoedkeuring

De orchestrator toont de drie artefacten en stopt. Controleer:

- of de businessregel correct is overgenomen;
- of scope en niet-doen-lijst duidelijk zijn;
- of alleen noodzakelijke bestanden worden genoemd;
- of positieve en negatieve CLI-tests zijn gepland;
- of ieder acceptatiecriterium traceerbaar bewijs heeft;
- of er geen blokkerende open vragen zijn.

Antwoord alleen wanneer dit klopt exact:

```text
goedgekeurd voor uitvoering
```

Antwoord bij onvolledige of onjuiste artefacten met `aanpassen` en concrete feedback. De Implementer mag dan nog niet starten.

### 3. Automatische implementatie en review

Na goedkeuring mag de orchestrator zonder extra menselijke handoff:

1. de Implementer aanroepen met de goedgekeurde spec, het plan en de tasks;
2. de implementatie en tests laten uitvoeren;
3. `bash scripts/check.sh` laten draaien;
4. de Reviewer aanroepen met alle artefacten, wijzigingen en het testbewijs;
5. concrete rework maximaal twee keer terugsturen naar de Implementer;
6. opnieuw laten reviewen na iedere rework-ronde.

Deze automatische flow mag alleen doorgaan zolang spec, scope, tasks en toegestane bestanden ongewijzigd blijven.

### 4. Menselijke eindgate

De loop stopt bij:

- `akkoord voor menselijke merge-review`;
- `escaleren`;
- een benodigde wijziging van spec, scope, tasks of toegestane bestanden;
- onvoldoende bewijs na maximaal twee rework-rondes.

De orchestrator mergeert niet. De menselijke gatekeeper beoordeelt de eindrapportage en beslist over het vervolg.

## Observatieverslag

Vul dit gedeelte in nadat de loop daadwerkelijk is uitgevoerd.

### Planner-handoff

- Spec-pad:
- Plan-pad:
- Tasks-pad:
- Open vragen:
- Menselijk besluit:

### Implementer-handoff

- Gewijzigde bestanden:
- Uitgevoerde tasks:
- Uitgevoerde checks/tests:
- Bewijs per acceptatiecriterium:
- Bekende beperkingen:

### Reviewer-oordeel

- Oordeel:
- Spec-conformiteit:
- Bewijsdekking:
- Risico's:
- Reden:

### Loopresultaat

- Aantal subagentaanroepen:
- Aantal rework-rondes:
- Reden van stoppen:
- Vereiste menselijke vervolgstap:

## Reflectie na uitvoering

- Stopte de orchestrator daadwerkelijk na de planning voor menselijke goedkeuring?
- Liep Implementer naar Reviewer daarna automatisch door?
- Werd bij rework alleen werk binnen de goedgekeurde scope uitgevoerd?
- Was de context bij iedere subagent voldoende en traceerbaar?
- Welke instructie in de orchestrator moet na deze proef worden aangescherpt?
