---
title: Patronen voor agentische workflows
created: 2026-09-28
updated: 2026-09-28
type: concept
tags: [loop-engineering, verification, governance, review]
sources: ["raw/articles/Agentic workflow patterns, drawn as graphs 1.md"]
confidence: low
contested: false
contradictions: []
---

## Doel

Een workflowgraaf maakt de volgorde, vertakkingen en samenkomst van stappen zichtbaar. De bron behandelt een toolgebruikende agent als een mogelijke stap en beschrijft vijf terugkerende vormen. Het zijn ontwerpvormen, geen voorgeschreven framework-API's.

## Vijf vormen

- **Chaining:** opeenvolgende stappen geven hun uitvoer door aan de volgende. Dit maakt tussenresultaten zichtbaar, maar extra modelaanroepen kunnen latency en kosten verhogen.
- **Routing:** een beslissing stuurt een invoer naar een van meerdere paden. Een expliciet foutpad kan herstel of escalatie mogelijk maken.
- **Parallelization:** onafhankelijke deelopdrachten lopen naast elkaar en komen samen bij een join. De join moet wachten op de resultaten die de vervolgstap nodig heeft.
- **Reflection:** een stap genereert een resultaat, een andere beoordeelt het en de workflow herhaalt zo nodig. Stel een stopconditie en limiet in; een open einde kan onbeperkt blijven itereren.
- **Human-in-the-loop:** een goedkeuringsstap vertakt bijvoorbeeld naar accepteren of afwijzen. Pauzeren, time-outs en hervatten vragen ondersteuning van de runtime; een getekende gate alleen voert dit niet uit.

Patronen kunnen worden gecombineerd, bijvoorbeeld routeren, parallelle beoordelingen samenvoegen en daarna menselijke goedkeuring vragen.

## Control flow is niet de runtime

De bron maakt onderscheid tussen de editor die een graaf modelleert en de runtime die hem uitvoert. Controleer voor een gekozen runtime expliciet ondersteuning voor cycli, parallelle joins, retries, menselijke pauzes en hervatten. Een DAG-runtime voert een getekende teruglus niet vanzelf uit; vaste herhalingen of een begrensde loop binnen een stap zijn mogelijke alternatieven.

Deze uitspraken over editor- en runtimegedrag komen uit een Workflow Builder-artikel en zijn afhankelijk van de gebruikte uitvoeringstechnologie. Verifieer ze voor het eigen framework. De patronen vullen [[concepts/loop-engineering]] aan: die beschrijft hoe doelen, verificatie en stopvoorwaarden een agentloop beheersen. [[concepts/spec-driven-development]] kan de gewenste uitkomst en acceptatiecriteria vastleggen.

## Bron en onzekerheid

De bron is gepubliceerd door een leverancier van workflow-editors en promoot diens product. De vijf vormen zijn hier weergegeven als de indeling van die bron, niet als een volledige of algemeen gestandaardiseerde taxonomie. Confidence is daarom laag.

- [Workflow Builder: Agentic workflow patterns, drawn as graphs](../raw/articles/Agentic%20workflow%20patterns,%20drawn%20as%20graphs%201.md) ([oorspronkelijk artikel](https://www.workflowbuilder.io/blog/agentic-workflow-patterns))
