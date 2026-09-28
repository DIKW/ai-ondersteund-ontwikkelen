---
title: Organisatiebrede inzet van data, AI en process mining
created: 2026-09-28
updated: 2026-09-28
type: summary
tags: [governance, verification, knowledge-management]
sources: [raw/papers/DIKW-Whitepaper.-Hoe-creeer-je-waarde-met-data-science_.pdf, raw/papers/DIKW_Whitepaper_Intelligence_Fabriek.pdf, raw/papers/DIKW_Whitepaper_Process_Mining-1.pdf, raw/papers/DIKW-Whitepaper.-Wat-is-de-waarde-van-een-datagedreven-organisatie_.pdf]
confidence: low
contested: false
contradictions: []
---

Deze synthese hoort bij de expliciete domeinuitbreiding in [[domains/ai-ondersteunde-softwareontwikkeling]]. De whitepapers richten zich op data- en AI-gebruik in organisaties en bedrijfsprocessen, niet op AI-ondersteunde softwareontwikkeling.

## Organisatiecapaciteit

De whitepaper over datagedreven organisaties beschrijft een volwassenheidsmodel met vijf pijlers: mensen, organisatie, data, tooling en analytische producten. Het model wordt gebruikt om een huidige situatie met een gewenst ambitieniveau te vergelijken en daar een roadmap van af te leiden. De whitepaper over de Intelligence Factory beschrijft een vergelijkbare organisatorische insteek en koppelt analyse aan een productie- en experimenteerritme.

Dit zijn modellen zoals beschreven door de uitgever; de bronnen leveren geen onafhankelijke validatie dat één volwassenheidsmodel voor iedere organisatie geschikt is.

## Experimenteren met data en AI

De whitepapers over data science en de Intelligence Factory benadrukken een terugkerend patroon: begin bij een concreet organisatieprobleem, beoordeel de mogelijke waarde en haalbaarheid, test een oplossing kleinschalig, meet het resultaat en schaal alleen op wanneer de uitkomst dat rechtvaardigt. De bronnen noemen multidisciplinaire samenwerking en ruimte om van mislukte experimenten te leren als organisatorische voorwaarden.

De beschreven telecom- en andere praktijkresultaten zijn claims uit commerciële whitepapers. Ze zijn hier niet onafhankelijk gecontroleerd en gelden niet als algemeen bewijs voor verwachte opbrengsten.

## Process mining

De process-miningbron beschrijft analyse op basis van event logs met ten minste een case-identificatie, een gebeurtenis en een tijdstip. De bron onderscheidt het ontdekken van het feitelijke procesverloop, het vergelijken van dat verloop met het bedoelde proces en het analyseren van prestaties of knelpunten. Interpretatie met domeindeskundigen en het later controleren van de effecten van een proceswijziging maken deel uit van de beschreven verbetercyclus.

Deze werkwijze levert inzichten over bedrijfsprocessen; ze schrijft op zichzelf geen proceswijziging voor. De bron bespreekt ook dat event logs uit bronsystemen moeten worden samengesteld en datakwaliteit de analyse kan beperken.

## Relatie met de bestaande wiki

Deze organisatiegerichte methoden kunnen context bieden voor de keuze of evaluatie van software- en AI-toepassingen. Ze zijn niet hetzelfde als [[concepts/loop-engineering]]: die pagina gaat over het beheerst laten werken van een AI-agent. Evenmin specificeren deze whitepapers hoe [[concepts/spec-driven-development]] softwaregedrag of acceptatiecriteria vastlegt.

## Bronnen en onzekerheid

Alle vier de bronnen zijn DIKW-whitepapers en hebben een commercieel karakter. De PDF-tekst is met MarkItDown geëxtraheerd; tabellen en delen van de data-science-whitepaper bevatten zichtbare OCR- en lay-outfouten. Daarom is de confidence laag. Controleer de oorspronkelijke PDF voor precieze cijfers, tabellen of claims voordat die in trainingsmateriaal als feit worden gebruikt.

- [DIKW: Hoe creëer je waarde met data science?](../raw/papers/DIKW-Whitepaper.-Hoe-creeer-je-waarde-met-data-science_.pdf)
- [DIKW: De AI-fabriek](../raw/papers/DIKW_Whitepaper_Intelligence_Fabriek.pdf)
- [DIKW: Process Mining](../raw/papers/DIKW_Whitepaper_Process_Mining-1.pdf)
- [DIKW: Wat is de waarde van een datagedreven organisatie?](../raw/papers/DIKW-Whitepaper.-Wat-is-de-waarde-van-een-datagedreven-organisatie_.pdf)

**Menselijke review:** Zijn de bronclaims over het volwassenheidsmodel en de beschreven experimenten geschikt voor deze training, gegeven het commerciële karakter en de OCR-onzekerheid?
