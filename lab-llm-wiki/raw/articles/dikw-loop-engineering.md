---
source_url: https://dikw.com/technologie/loop-engineering/
ingested: 2026-09-18
sha256: 3799776b3a2c72012b58df7c93102d0b85f026d75e27821b0bc7a890568daf8a
---

# Loop Engineering voorbij de hype

Bron: DIKW Intelligence.

## Wat is Loop Engineering?

Loop Engineering is het ontwerpen van systemen die AI-agents zelfstandig door een gecontroleerde werkcyclus leiden. De cyclus maakt stappen, context, kwaliteitsgates en stopvoorwaarden expliciet. Voor softwareontwikkeling betekent dit dat een wijziging wordt gepland, gespecificeerd, geïmplementeerd, getest, gereviewd en pas daarna opgeleverd.

## Van vibe coding naar engineering

Vibe coding is bruikbaar voor prototypes en kleine hulpmiddelen, maar prompten, accepteren en opnieuw proberen is geen voldoende proces voor gedeelde codebases of bedrijfskritische systemen. Loop Engineering verschuift de nadruk van prompt and hope naar specify and verify.

## Spec-Driven Development

Volgens de bron begint een goede loop met het expliciet maken van wat goed betekent. Spec-Driven Development behandelt de specificatie als bron van waarheid. De specificatie bevat onder meer doel, scope, randvoorwaarden, architectuurregels, security- en privacy-eisen, acceptatiecriteria en benodigd verificatiebewijs.

SDD bepaalt wat het juiste resultaat is; Loop Engineering organiseert hoe een AI-agent daar gecontroleerd naartoe werkt. Acceptatiecriteria functioneren daarbij als stopvoorwaarden.

## Basisloop

De voorgestelde ontwikkellus bestaat uit:

1. Plan: verzamel change request, code, architectuur, documentatie, afhankelijkheden en risico's.
2. Specificeer: leg doel, scope, niet-doelen, acceptatiecriteria en grenzen vast.
3. Implementeer: voer een afgebakende wijziging uit en leg tussenresultaten vast.
4. Verifieer: verzamel objectief bewijs, zoals tests, linting, scans of gebruikersacceptatie.
5. Review: laat een onafhankelijke reviewer spec, code en bewijs beoordelen.
6. Opleveren, herhalen of escaleren: lever alleen op na de gates; stuur terug of escaleer bij fouten, onzekerheid of onvoldoende bewijs.

Een loop is dus een herhaalbaar proces met doel, context, actie, verificatie en een besluit over de volgende stap.

## Technische bouwstenen

De bron noemt doel en trigger, specificatie, context, skills of instructies, state of geheugen, tools, verificatiegates, review en escalatie, en observability. Een kleine enkelvoudige loop is meestal het beste startpunt; meer autonomie is pas passend wanneer uitkomsten betrouwbaar en herstelbaar zijn.

## Kennis als geheugen

Een blijvende kennislaag voorkomt dat architectuurkeuzes, domeinregels, incidenten en reviewbesluiten telkens opnieuw uit chats moeten worden gereconstrueerd. Een llm-wiki kan dit ondersteunen met gestructureerde Markdown, bronverwijzingen, metadata en links tussen gerelateerde onderwerpen.

## Naar Graph Engineering

Graph Engineering is volgens de bron een mogelijke vervolgstap wanneer werk meerdere gespecialiseerde agents, parallelle taken, verschillende tools of onafhankelijke verificatie nodig heeft. Een kennisgraaf organiseert wat het systeem weet; een uitvoerbare graaf organiseert wie of wat het werk doet. Begin met één heldere loop en voeg complexiteit alleen toe wanneer daar een concrete reden voor is.
