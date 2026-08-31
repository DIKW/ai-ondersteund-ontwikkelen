# Nieuwe feature voor Lab 02 (planner-input)

## Context
Deze feature is de startinput voor Lab 02 en komt voort uit de Lab 01-modeluitwerking.

## Featurevraag
Als product owner wil ik dat alleen volledige wijzigingsverzoeken kunnen worden ingediend, zodat reviewers geen tijd verliezen aan onvolledige aanvragen.

## Scope
- Gedrag: alleen submit van `DRAFT` naar `SUBMITTED`.
- Verplichte velden: `title`, `description`, `requester`.
- Bij ontbrekende waarde: duidelijke validatiefout.
- Bij mislukte submit: status blijft `DRAFT`.

## Buiten scope
- Geen wijziging aan prioriteitsregels.
- Geen wijziging aan andere statusovergangen.
- Geen infrastructuur- of dependencywijzigingen.

## Acceptatiecriteria (overgenomen uit Lab 01)
- Een DRAFT-verzoek met ingevulde `title`, `description` en `requester` kan worden ingediend.
- Een DRAFT-verzoek met lege `title` kan niet worden ingediend.
- Een DRAFT-verzoek met lege `description` kan niet worden ingediend.
- Een DRAFT-verzoek met lege `requester` kan niet worden ingediend.
- Na mislukte submit blijft status `DRAFT`.

## Open vraag voor planner/reviewer
- Wordt whitespace-only invoer (bijvoorbeeld "   ") als leeg beschouwd?
