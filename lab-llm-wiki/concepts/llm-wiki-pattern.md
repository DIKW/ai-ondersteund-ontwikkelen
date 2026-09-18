---
title: LLM Wiki-patroon
created: 2026-09-18
updated: 2026-09-18
type: concept
tags: [knowledge-management, loop-engineering, verification]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
contested: false
---

# LLM Wiki-patroon

## Kernidee

Het LLM Wiki-patroon beschrijft een persistente, compounding kennisbasis van onderling verbonden Markdown-bestanden. In plaats van bij iedere vraag kennis opnieuw uit ruwe documenten te reconstrueren, integreert een LLM nieuwe bronnen in een bestaande wiki. De opgebouwde synthese, kruisverwijzingen en gemarkeerde tegenstrijdigheden blijven daardoor beschikbaar voor volgende vragen.

De mens beheert bronselectie, verkenning en vragen. De LLM voert het samenvatten, cross-linken, bijwerken en boekhouden uit. De wiki blijft gewone Markdown die bijvoorbeeld met Obsidian kan worden gelezen en verkend.

## Drie lagen

1. **Raw sources**: gecureerde, immutable bronbestanden die de bron van waarheid vormen.
2. **Wiki**: onderhouden Markdown-pagina's zoals samenvattingen, entiteiten, concepten, vergelijkingen en syntheses.
3. **Schema**: regels voor structuur, conventies en workflows voor ingest, query en onderhoud.

Deze repository gebruikt `$WIKI_ROOT/raw/` voor de eerste laag, `$WIKI_ROOT/concepts/`, `$WIKI_ROOT/entities/` en `$WIKI_ROOT/queries/` voor de tweede laag, en `$WIKI_ROOT/SCHEMA.md` voor de derde laag.

## Kernoperaties

- **Ingest**: lees een bron, bespreek de belangrijkste inzichten, maak of actualiseer pagina's, werk index en log bij en verwerk relevante kruisverwijzingen.
- **Query**: zoek relevante pagina's, syntheseer een antwoord met citaties en leg waardevolle nieuwe antwoorden terug in de wiki.
- **Lint**: controleer tegenstrijdigheden, verouderde claims, weespagina's, ontbrekende links en kennishiaten.

`index.md` is de inhoudelijke catalogus; `log.md` is het chronologische, append-only auditspoor.

## Relatie tot Loop Engineering

[[concepts/loop-engineering]] beschrijft hoe een gecontroleerde AI-werkcyclus wordt ontworpen. Het LLM Wiki-patroon levert de blijvende kennislaag waarin bronnen, besluiten en syntheses voor volgende iteraties beschikbaar blijven.

[[concepts/spec-driven-development]] is een voorbeeld van kennis die als expliciete specificatie in zo'n wiki kan worden onderhouden en opnieuw gebruikt.

## Grenzen van het patroon

De gist is een patroon en geen vaste implementatiespecificatie. Directorystructuur, schema, paginavorm en tooling mogen per domein verschillen. De kern is de scheiding tussen immutable bronnen en een door de LLM onderhouden, gekoppelde Markdown-kennislaag.

Deze pagina is gebaseerd op één bron en heeft daarom `confidence: medium`.

## Bron

- [[concepts/loop-engineering]]
- [[concepts/spec-driven-development]]
- [Karpathy: LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
