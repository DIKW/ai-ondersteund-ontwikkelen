---
title: Spec-Driven Development
created: 2026-09-18
updated: 2026-09-18
type: concept
tags: [spec-driven-development, verification, review]
sources: [raw/articles/dikw-loop-engineering.md]
confidence: medium
contested: false
---

# Spec-Driven Development

## Definitie

Spec-Driven Development (SDD) behandelt de specificatie als bron van waarheid voordat een AI-agent code schrijft. De specificatie maakt expliciet wat de bedoeling is en onder welke grenzen het resultaat geldig is.

## Inhoud van een bruikbare specificatie

Een specificatie bevat volgens de bron onder meer:

- doel en beoogde gebruikerswaarde
- scope en niet-doelen
- functionele en technische randvoorwaarden
- architectuurregels en relevante afhankelijkheden
- security-, privacy- en compliance-eisen
- acceptatiecriteria
- benodigd verificatiebewijs

## Relatie met Loop Engineering

[[concepts/loop-engineering]] organiseert de gecontroleerde route naar het resultaat; SDD bepaalt wat het juiste resultaat is. De acceptatiecriteria uit de specificatie worden stopvoorwaarden voor de ontwikkellus. Als een criterium niet aantoonbaar is gehaald, gaat het werk terug naar analyse, implementatie of menselijke beoordeling.

## Onzekerheid

Deze pagina is gebaseerd op één bron en heeft daarom `confidence: medium`. De bron geeft geen volledige SDD-standaard; teams moeten zelf bepalen welke specificatievelden en bewijsvormen voor hun domein verplicht zijn.

## Bron

- [[concepts/loop-engineering]]
- [DIKW: Loop Engineering voorbij de hype](https://dikw.com/technologie/loop-engineering/)
