---
name: llm-wiki
description: 'Build and maintain an interlinked Markdown knowledge base in a configurable wiki root using the Karpathy LLM Wiki pattern. Use when starting a wiki, ingesting sources, querying wiki content, updating pages, or linting wiki health.'
argument-hint: '[start, ingest, query, lint, or a wiki task]'
user-invocable: true
disable-model-invocation: false
---

# LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked Markdown files. Compile knowledge once into maintained pages instead of rediscovering it for every query.

## Configuration

Set the wiki root in this single variable before using the skill:

```text
WIKI_ROOT = lab-llm-wiki/
```

To reuse this skill for another wiki, change only `WIKI_ROOT`. Resolve every `$WIKI_ROOT/...` path below relative to the repository root unless the configured value is absolute.

## Wiki location

Use `$WIKI_ROOT` as the wiki root. Do not create or use `~/wiki`, external storage, production data, or customer data for this repository task.

## Activate for

- Starting or initializing a wiki
- Ingesting, adding, or processing an approved source
- Asking a question that should be answered from the wiki
- Creating or updating entities, concepts, comparisons, or filed queries
- Linting, auditing, or health-checking the wiki

## Mandatory orientation

Before every wiki operation:

1. Read `$WIKI_ROOT/SCHEMA.md`.
2. Read `$WIKI_ROOT/index.md`.
3. Read the last 20-30 lines of `$WIKI_ROOT/log.md`.
4. Search for existing pages before creating a new page.
5. Confirm the source is approved and contains no production or customer data.

This prevents duplicate pages, missed cross-references, schema violations, and repeated work.

## Three-layer architecture

1. **Raw sources:** `$WIKI_ROOT/raw/` is immutable. Read it, never edit, rename, or delete it.
2. **Wiki pages:** `$WIKI_ROOT/entities/`, `$WIKI_ROOT/concepts/`, `$WIKI_ROOT/queries/`, and other approved Markdown pages are maintained summaries and syntheses.
3. **Schema and navigation:** `$WIKI_ROOT/SCHEMA.md` defines conventions and tags; `$WIKI_ROOT/index.md` catalogs pages; `$WIKI_ROOT/log.md` is the append-only activity record.

## Repository constraints

- Treat `$WIKI_ROOT/SCHEMA.md` as authoritative. Use `$WIKI_ROOT/WORKFLOW.md` when the configured wiki provides one.
- Use only tags already present in the schema taxonomy: `spec-driven-development`, `loop-engineering`, `verification`, `review`, `governance`, and `knowledge-management`.
- Add at most three new or updated wiki pages per exercise unless the user explicitly approves a larger scope.
- Human review is required for source selection, factual correctness, confidence, and contradictions.
- Never silently resolve uncertainty or conflicting sources.
- Do not infer business rules that are absent from the domain docs, specs, or tests.

## Starting a new wiki

When the wiki is not initialized:

1. Confirm the domain and the first training question with the user.
2. Confirm the approved source files under `$WIKI_ROOT/raw/`.
3. Keep the initial scope small and testable.
4. Ensure `SCHEMA.md`, `index.md`, and `log.md` exist and reflect the domain.
5. Record the start action in `log.md`.
6. Require human review before treating generated pages as accepted knowledge.

For lab 07, the start note must state the question, scope, explicit source list, taxonomy tags, review moment, and known uncertainty.

## Page conventions

Use lowercase, hyphenated filenames. Every page should contain YAML frontmatter:

```yaml
---
title: Page title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [verification, review]
sources: [raw/source.md]
confidence: high | medium | low
contested: true | false
contradictions: [other-page]
---
```

Use `confidence`, `contested`, and `contradictions` when claims are single-source, opinion-heavy, fast-changing, uncertain, or conflicting. Every tag must exist in `SCHEMA.md`.

Every new or updated page must:

- include traceable source references
- include meaningful `[[wikilinks]]` to related pages
- be added or updated in `index.md`
- be recorded in `log.md`

Keep pages scannable. Split a page when it grows beyond roughly 200 lines. Create a page when a concept or entity is central to one source or appears in multiple sources; do not create pages for passing mentions.

## Operations

### Ingest

1. Read and verify the approved source in `$WIKI_ROOT/raw/`.
2. Search `$WIKI_ROOT/index.md` and existing pages for covered concepts and entities.
3. Create or update only pages justified by the page threshold.
4. Preserve provenance, use valid tags, update the `updated` date, and mark confidence.
5. Add meaningful cross-links and note contradictions explicitly.
6. Update `$WIKI_ROOT/index.md` once, then append one dated action to `$WIKI_ROOT/log.md` listing every changed file.
7. Report changed files, sources, confidence, uncertainties, and the human review question.

Raw source frontmatter may include:

```yaml
---
source_url: https://example.com/source
ingested: YYYY-MM-DD
sha256: <sha256 of body after frontmatter>
---
```

On re-ingest, compare the body hash. Identical content can be skipped; changed content is source drift and requires review.

### Query

1. Read `index.md` and identify relevant pages.
2. Read those pages and synthesize only from their documented content.
3. Cite the pages used with `[[page-name]]` references.
4. State confidence and remaining uncertainty or contradictions.
5. File substantial, reusable answers under `$WIKI_ROOT/queries/` and log whether the answer was filed.

### Lint

Check and report, grouped by severity:

1. Broken `[[wikilinks]]`.
2. Orphan pages with no inbound links.
3. Pages missing from `index.md`.
4. Missing or invalid frontmatter fields.
5. Tags absent from the schema taxonomy.
6. Low-confidence or single-source pages without an explicit confidence signal.
7. Contested pages and unresolved contradictions.
8. Raw-source hash drift.
9. Pages over roughly 200 lines.
10. Log rotation needs when the log exceeds 500 entries.

Append a dated lint entry to `log.md` with the issue count and report concrete file paths and suggested actions.

## Update, archive, and bulk rules

When information conflicts, compare source dates, preserve both positions when necessary, mark the page as contested, record the contradiction, and request human review. Do not overwrite silently.

For bulk ingest, read all sources first, perform one duplicate search, update pages in one pass, update the index once, and append one batch log entry. Ask before changes would affect more than three existing pages.

When archiving superseded content, move it to an archive location, remove it from `index.md`, repair references, and log the action.

## Completion check

A wiki operation is complete only when:

- orientation was performed
- source provenance is present
- tags are valid
- uncertainty and contradictions are explicit
- `index.md` is current
- `log.md` has an append-only entry
- the change stays within the approved page limit
- the output names changed files and the required human review decision
