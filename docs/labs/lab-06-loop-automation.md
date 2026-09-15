# Lab 06: automatiseer de loop met een orchestrator

- **Doel:** maak een orchestrator-agent die de bestaande Planner, Implementer en Reviewer als subagents aanroept en hun samenwerking bestuurt.
- **Tijd:** 45-60 min
- **Startpunt:** de drie custom agents en de handmatig uitgevoerde workflow uit lab 05.

## Van losse agents naar een workflow

In lab 05 heb je gewerkt met drie gespecialiseerde agents:

- de **Planner** maakt een afgebakend plan;
- de **Implementer** voert een goedgekeurd plan uit en verzamelt testbewijs;
- de **Reviewer** beoordeelt scope, spec-naleving, risico en bewijs.

Deze agents hebben ieder een duidelijke rol en een handoff-contract. Toch werken ze nog niet zelfstandig samen. Een kop als `Handoff naar Implementer` beschrijft alleen welke output de Planner moet opleveren. Die tekst roept de Implementer niet daadwerkelijk aan. Daarom moest je in lab 05 zelf tussen agents wisselen en iedere volgende stap starten.

Wat nog ontbreekt, is een uitvoerende workflow: een agent die de volgorde bewaakt, de juiste subagent aanroept, diens resultaat doorgeeft en bepaalt of de loop doorgaat of stopt.

## Wat je in dit lab bouwt

Je voegt een vierde custom agent toe: de **Loop Orchestrator**. Deze agent implementeert zelf geen feature en voert zelf geen review uit. De orchestrator coordineert de bestaande rollen:

```text
Menselijke opdracht
		  |
		  v
  Loop Orchestrator
		  |
		  v
	  Planner
		  |
		  v
	Implementer <--------+
		  |                |
		  v                |
	  Reviewer            |
		  |                |
		  +-- rework ------+
		  |
		  +-- akkoord/escalatie --> menselijke gatekeeper
```

De orchestrator gebruikt hiervoor de `agent`-tool van GitHub Copilot. Daarmee kan een hoofdagent een custom agent als subagent starten, een gerichte opdracht meegeven en het eindresultaat terugontvangen. De orchestrator verwerkt dat resultaat en roept daarna de volgende subagent aan.

## Gewenst gedrag

De nieuwe orchestrator moet:

1. De Planner als subagent aanroepen voor een klein, uitvoerbaar plan.
2. Controleren of de planner-handoff alle verplichte velden bevat.
3. Stoppen voor menselijke goedkeuring als het plan onduidelijk is of een businessregel ontbreekt.
4. Na een goedgekeurd plan de Implementer als subagent aanroepen.
5. De implementatie, gewijzigde bestanden en het testbewijs doorgeven aan de Reviewer.
6. Het oordeel van de Reviewer verwerken als `akkoord voor menselijke merge-review`, `terug naar implementer` of `escaleren`.
7. Bij rework de Implementer opnieuw aanroepen met alleen de concrete reviewbevindingen.
8. Na maximaal twee rework-rondes stoppen en escaleren.
9. Nooit zelfstandig mergen, releasen of deployen.

## Opdracht

Maak het volgende bestand:

```text
.github/agents/loop-orchestrator.agent.md
```

Neem in de frontmatter minimaal op:

```yaml
---
name: Loop Orchestrator
description: Orchestreert een begrensde planner-implementer-reviewer-loop voor een goedgekeurde feature.
tools: [agent, read, search]
agents: [Planner, Implementer, Reviewer]
---
```

Hiermee krijgt de orchestrator toegang tot de tool voor subagents en wordt expliciet beperkt welke agents hij mag aanroepen. De bestaande agents behouden hun eigen toolrechten: de Planner en Reviewer werken beperkt, terwijl de Implementer code mag wijzigen en checks mag uitvoeren.

Beschrijf daarna in de body van de agent:

- de vaste volgorde van de workflow;
- welke volledige context iedere subagent ontvangt;
- hoe de orchestrator de verplichte handoffvelden controleert;
- wanneer rework is toegestaan;
- het maximale aantal rework-rondes;
- wanneer de loop direct stopt en naar een mens escaleert;
- welke eindrapportage de orchestrator moet opleveren.

## Uitvoeren van de loop

1. Selecteer `Loop Orchestrator` in de agentkiezer van GitHub Copilot Chat.
2. Geef één kleine, concrete feature-opdracht met een verwijzing naar de leidende spec of domeinregel.
3. Laat de orchestrator de Planner als subagent aanroepen.
4. Controleer het plan bij het menselijke goedkeuringsmoment.
5. Geef alleen bij een bruikbaar plan toestemming om de uitvoering te vervolgen.
6. Observeer hoe de orchestrator daarna de Implementer en Reviewer aanroept.
7. Controleer of een reviewer-oordeel tot de juiste vervolgstap leidt.
8. Bewaar de eindrapportage met de handoffs en het testbewijs.

## Menselijke gates

De loop is autonoom binnen een goedgekeurde scope, maar niet onbeperkt autonoom. De menselijke gatekeeper blijft verantwoordelijk voor:

- goedkeuring van het plan en de scope;
- beslissingen bij onduidelijke of ontbrekende businessregels;
- toestemming voor scope-uitbreiding;
- het uiteindelijke mergebesluit;
- release- en deployment-acties.

## Stop- en escalatievoorwaarden

De orchestrator stopt en escaleert wanneer:

- de Planner geen complete of eenduidige handoff kan maken;
- een businessregel niet in de domeindocumentatie, spec of tests staat;
- uitvoering een bestand of wijziging buiten de goedgekeurde scope vereist;
- een dependency, secret, recht of infrastructuurwijziging nodig blijkt;
- tests geen voldoende bewijs leveren;
- de Reviewer `escaleren` als oordeel geeft;
- na twee rework-rondes nog geen akkoord mogelijk is.

## Verwachte artefacten

- `.github/agents/loop-orchestrator.agent.md`;
- een zichtbaar subagentverloop van Planner naar Implementer naar Reviewer;
- de planner-handoff waarop menselijke goedkeuring is gegeven;
- testbewijs van de Implementer;
- het expliciete reviewoordeel;
- een eindrapportage van de orchestrator met het resultaat en eventuele open punten.

## Kwaliteitscheck

- De orchestrator gebruikt de `agent`-tool en beperkt subagents tot de drie bestaande rollen.
- De orchestrator voert de inhoudelijke taken niet zelf uit.
- Iedere subagent krijgt voldoende context om zijn input-contract te volgen.
- De volgorde Planner -> Implementer -> Reviewer is zichtbaar in de uitvoering.
- Rework is begrensd en gebruikt concrete reviewerbevindingen.
- Stopvoorwaarden en menselijke gates zijn expliciet.
- De eindrapportage maakt plan, wijzigingen, bewijs en oordeel traceerbaar.

**Verwachte uitkomst:**

- Het script eindigt succesvol met exitcode `0`.
- De nieuwe orchestrator-agent is aanwezig en wordt door GitHub Copilot herkend.
- Vanuit één initiële feature-opdracht zijn de drie gespecialiseerde agents als subagents aangeroepen.
- De loop eindigt met een expliciet oordeel of een traceerbare escalatie.

## Reflectie

- Welke beslissingen kon de orchestrator veilig zelfstandig nemen?
- Op welk moment bleef menselijke goedkeuring noodzakelijk?
- Welke context moest expliciet worden doorgegeven om contextverlies tussen subagents te voorkomen?
- Wat is nu het verschil tussen een verzameling agents en een werkende agent-loop?
