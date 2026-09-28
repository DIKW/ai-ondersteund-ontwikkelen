---
title: Agentic Operating Model
created: 2026-09-28
updated: 2026-09-28
type: concept
tags: [governance, verification, review, loop-engineering]
sources: ["raw/papers/The Agentic Operating Model.pdf"]
confidence: low
contested: false
contradictions: []
---

## Kernidee

The Agentic Operating Model (AOM) is een door LangChain voorgesteld organisatiepatroon om mensen, processen en technologie op elkaar af te stemmen bij het ontwikkelen en beheren van AI-agents. Het model is gericht op productiegebruik op organisatieniveau; het is geen technische workflow- of frameworkstandaard.

## Drie samenhangende onderdelen

- **People:** de paper onderscheidt platform engineers, agent engineers en niet-technische domeinbouwers. Een platformteam levert gedeelde infrastructuur en patronen; domeinteams bouwen toepassingen; vakdeskundigen leveren domeinkennis, feedback en evaluatievoorbeelden. In een vroege fase kunnen platform- en agent engineering door één team worden gedaan.
- **Process:** de Agent Development Lifecycle (ADLC) beschrijft **Build**, **Test**, **Deploy** en **Monitor**, met **Iterate** en **Govern** als doorlopende activiteiten. De paper legt nadruk op evalueren vóór promotie, productiegedrag observeren en op basis van fouten verbeteren.
- **Technology:** ondersteunende mogelijkheden omvatten agent-frameworks en runtimes, evaluatie- en observability-instrumenten, versiebeheer van gedragsartefacten en gecontroleerde uitvoering. De paper werkt dit vooral uit met producten van LangChain; de functies zijn algemener dan die specifieke stack.

Governance, security, compliance, kostenbeheer (FinOps) en interoperabiliteit lopen volgens het model door alle drie de onderdelen heen. Een praktisch gevolg is dat voor iedere agent eigenaarschap, toegangsgrenzen, evaluatiecriteria en passende menselijke controle expliciet moeten zijn.

## Evaluatie en continue verbetering

De paper beschrijft evaluatie als terugkerend werk, niet alleen als een release-gate. Mogelijke evaluatiegegevens zijn samengestelde praktijkvoorbeelden, synthetische randgevallen, verwachte uitvoeringstrajecten, regressiegevallen en adversariële gevallen. Evaluatie kan deterministische controles, vergelijking met bekende antwoorden, menselijke beoordeling of selectief gebruik van een taalmodel als beoordelaar combineren.

De voorgestelde verbeterlus loopt van productie-observatie naar foutpatroon, oorzaakanalyse, gerichte aanpassing en regressie-evaluatie. Traces en feedback kunnen daarvoor input leveren; observability alleen verbetert een agent niet zonder een proces en eigenaar die signalen omzet in gecontroleerde wijzigingen. Dit sluit aan bij [[concepts/loop-engineering]], maar de AOM beschrijft de organisatie rond een portfolio van agents, niet alleen één agentlus.

## Risico en volwassenheid

De paper stelt voor controles op te schalen met de mogelijke impact van een agent: van begrensde, informatieve taken via acties in systemen tot autonome of hoog-risicotaken. Naarmate de impact stijgt, noemt de paper onder meer strengere toegangsbeperking, evaluatie, menselijke goedkeuring, isolatie en expliciet eigenaarschap. Behandel deze indeling als het voorstel van de auteur; de paper vervangt geen toepasselijke wet- of regelgeving of lokale risicoanalyse.

Ook schetst de paper een volwassenheidsreis van verkennen naar bouwen, operationeel beheren en organisatiebreed schalen. De fasen kunnen helpen om ontbrekende capaciteiten te bespreken, maar zijn geen onafhankelijk gevalideerde benchmark. [[concepts/agentic-workflow-patterns]] beschrijft een lager, technisch niveau: patronen voor de control flow van afzonderlijke workflows.

## Bron en onzekerheid

Dit is een LangChain-whitepaper die een operating model presenteert én de producten van de uitgever als implementatie ervan promoot. Productspecifieke voordelen, praktijkresultaten, kostenbesparingen en volwassenheidsindicatoren zijn claims van de uitgever en hier niet onafhankelijk geverifieerd. De PDF-extractie bevat bovendien beschadigde tabellen en OCR-fouten; controleer de originele PDF voordat precieze cijfers of tabeldetails in trainingsmateriaal worden gebruikt.

- [The Agentic Operating Model](../raw/papers/The%20Agentic%20Operating%20Model.pdf)

**Menselijke review (2026-09-28):** Goedgekeurd als denkkader voor trainingsdoeleinden. De LangChain-productinvulling en voorgestelde risicotaxonomie zijn niet als norm onderschreven; de lage confidence blijft gelden voor niet-onafhankelijk geverifieerde claims en OCR-onzekerheid.
