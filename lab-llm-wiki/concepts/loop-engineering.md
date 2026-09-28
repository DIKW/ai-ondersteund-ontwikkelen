---
title: Loop Engineering
created: 2026-09-18
updated: 2026-09-28
type: concept
tags: [loop-engineering, verification, review, governance]
sources: [raw/articles/dikw-loop-engineering.md, raw/articles/ibm-loop-engineering.md, "raw/articles/Loop engineering Getting started with loops.md"]
confidence: medium
contested: false
---

## Definitie

Loop Engineering is het ontwerpen van systemen die AI-agents door een gecontroleerde werkcyclus leiden. De cyclus maakt doel, context, acties, kwaliteitsgates, verificatie en stop- of escalatievoorwaarden expliciet. Het gaat daarmee niet alleen om betere prompts, maar om het ontwerpen van het proces waarin een agent werkt.

## Basispatroon

Een softwareontwikkellus kan bestaan uit:

1. **Plan**: verzamel relevante code, documentatie, afhankelijkheden en risico's.
2. **Specificeer**: leg doel, scope, niet-doelen, grenzen en acceptatiecriteria vast.
3. **Implementeer**: voer een afgebakende wijziging uit.
4. **Verifieer**: verzamel objectief bewijs met tests, scans of andere passende controles.
5. **Review**: laat een onafhankelijke reviewer de wijziging en het bewijs beoordelen.
6. **Opleveren, herhalen of escaleren**: lever alleen op na de kwaliteitsgates; stuur terug of escaleer bij fouten, onzekerheid of onvoldoende bewijs.

De cyclus is herhaalbaar: een mislukte verificatie of review brengt het werk terug naar een eerdere stap.

## Agentic loop volgens IBM

IBM beschrijft een vergelijkbare lus met vier fasen: **Goal**, **Action**, **Observation** en **Adjustment**. Het doel bevat toetsbare stopcriteria, de agent voert een actie uit, het systeem observeert het resultaat en de aanpak wordt aangepast voordat de volgende iteratie start. Deze fasering is een compactere operationele beschrijving van de hierboven beschreven plan-, implementatie- en verificatiestappen. ^[raw/articles/ibm-loop-engineering.md]

## Lusvormen volgens Anthropic

Anthropic onderscheidt in een Claude Code-artikel vier vormen naar trigger en stopconditie:

- **Turn-based:** een gebruiker start iedere cyclus; geschikt voor losse, kortere taken.
- **Goal-based:** een expliciet doel en een maximumaantal beurten begrenzen de iteratie.
- **Time-based:** een interval start herhaald werk; het stopt wanneer het wordt uitgezet of de taak klaar is.
- **Proactive:** een event of schema start een terugkerende routine zonder menselijke start per taak; elke taak heeft een eigen stopconditie.

Dit is Anthropic's productgerichte indeling, geen universele standaard. Ze deelt loops in naar start- en stopmechanisme; IBM's **Goal**, **Action**, **Observation** en **Adjustment** beschrijven juist fasen binnen een iteratie. Beide invalshoeken kunnen elkaar aanvullen. De bron adviseert expliciete grenzen, verificatie, kleine pilots en bewaking van model- en tokengebruik. [^1]

## Relatie met Spec-Driven Development

[[concepts/spec-driven-development]] bepaalt wat het juiste resultaat is. Loop Engineering organiseert hoe een AI-agent daar gecontroleerd naartoe werkt. Acceptatiecriteria worden daardoor ook stopvoorwaarden van de loop.

De overgang van vibe coding naar Loop Engineering is volgens de bron een overgang van `prompt and hope` naar `specify and verify`. Vibe coding kan nuttig blijven voor verkenning, maar is op zichzelf geen voldoende kwaliteitsproces voor gedeelde of bedrijfskritische codebases.

De grafische control-flowpatronen voor agentworkflows staan beschreven in [[concepts/agentic-workflow-patterns]].

## Technische bouwstenen

Een loop heeft doorgaans een doel en trigger, specificatie, relevante context, skills of instructies, state of geheugen, gecontroleerde tools, verificatiegates, review en escalatie, en observability. IBM noemt daarnaast automatisering of scheduling, hooks, context engineering, worktrees, subagents en een persistente `spine` die voortgang en context tussen iteraties bewaart. ^[raw/articles/ibm-loop-engineering.md] Een kleine enkelvoudige loop is een verstandig startpunt. Meer autonomie of meerdere agents zijn pas gerechtvaardigd wanneer betrouwbaarheid, herstelbaarheid, parallel werk of onafhankelijke verificatie dat nodig maken.

## Kennislaag

Een blijvende kennislaag voorkomt dat besluiten, domeinregels, verificatiebewijs en reviewcontext telkens opnieuw uit chats moeten worden gereconstrueerd. Een llm-wiki met Markdown, metadata, bronverwijzingen en wikilinks kan die context voor mensen en agents beschikbaar houden.

## Onzekerheid

Deze pagina is gebaseerd op één bron en heeft daarom `confidence: medium`. De bron beschrijft een conceptueel patroon; concrete implementatiekeuzes, meetcriteria en organisatiebrede stopvoorwaarden zijn contextafhankelijk.

## Bron

- [[concepts/spec-driven-development]]
- [DIKW: Loop Engineering voorbij de hype](https://dikw.com/technologie/loop-engineering/)
- [IBM Think: What is loop engineering?](https://www.ibm.com/think/topics/loop-engineering)
- [Anthropic: Getting started with loops](https://claude.com/blog/getting-started-with-loops) [^1]

[^1]: `raw/articles/Loop engineering Getting started with loops.md`. De bronmetadata noemt alleen "Jun 30" als publicatiedatum; het jaar is niet vastgelegd.
