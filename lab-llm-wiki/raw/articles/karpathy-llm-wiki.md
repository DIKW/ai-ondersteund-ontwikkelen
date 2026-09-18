---
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
ingested: 2026-09-18
sha256: a07aa74dce95d16a0822ce3a468e9fc3461229e52c08bccbf05201eefa7c777d
---

# LLM Wiki

Bron: Andrej Karpathy, `llm-wiki.md`.

## Kernidee

Een LLM-wiki is een persistente, compounding kennisbasis van onderling verbonden Markdown-bestanden. In tegenstelling tot RAG, waarbij een model bij iedere vraag kennis opnieuw uit ruwe documenten reconstrueert, integreert de LLM nieuwe bronnen in een bestaande wiki. De wiki bevat daardoor een steeds rijkere synthese, kruisverwijzingen en gemarkeerde tegenstrijdigheden.

De mens beheert bronselectie, verkenning en vragen. De LLM vat samen, legt verbanden, werkt pagina's bij en doet het boekhoudkundige onderhoud. Obsidian kan als editor en graph view dienen; de wiki blijft een verzameling gewone Markdown-bestanden.

## Architectuur

De architectuur bestaat uit drie lagen:

1. Raw sources: een gecureerde verzameling artikelen, papers, afbeeldingen en databestanden. Deze bronnen zijn immutable en vormen de bron van waarheid.
2. De wiki: LLM-gegenereerde Markdown-bestanden zoals samenvattingen, entiteitspagina's, conceptpagina's, vergelijkingen en syntheses.
3. Het schema: een document dat structuur, conventies en workflows beschrijft voor ingest, query en onderhoud.

## Kernoperaties

Bij ingest leest de LLM een bron, bespreekt de belangrijkste inzichten, schrijft of actualiseert wiki-pagina's, werkt de index bij, past relevante bestaande pagina's aan en voegt een logregel toe. Bij query zoekt de LLM relevante pagina's, leest die en synthetiseert een antwoord met citaties. Waardevolle antwoorden, vergelijkingen en ontdekte verbanden kunnen teruggeschreven worden als nieuwe wiki-pagina's. Bij lint controleert de LLM onder meer tegenstrijdigheden, verouderde claims, weespagina's, ontbrekende kruisverwijzingen en kennishiaten.

## Index en log

`index.md` is een inhoudelijke catalogus met links, korte samenvattingen en optionele metadata. `log.md` is een chronologisch, append-only overzicht van ingests, queries en lint-acties. De index helpt relevante pagina's te vinden; de log maakt de ontwikkeling van de wiki navolgbaar.

## Ontwerpkeuzes

De gist beschrijft een patroon en geen vaste implementatie. Directorystructuur, schema, paginavorm en tooling mogen per domein verschillen. De essentie is de scheiding tussen immutable bronnen en een door de LLM onderhouden, gekoppelde Markdown-kennislaag.
