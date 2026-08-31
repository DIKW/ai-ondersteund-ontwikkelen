# Spec: Validatie bij indienen wijzigingsverzoek

## Probleem
Een DRAFT-verzoek kan momenteel worden ingediend zonder verplichte velden (`title`, `description`, `requester`). Reviewers verliezen tijd aan onvolledige aanvragen.

## Doel
Alleen volledige wijzigingsverzoeken kunnen worden ingediend (DRAFT → SUBMITTED).

## Scope
- Validatie van `title`, `description` en `requester` bij `submit_change_request`.
- Bij ontbrekende waarde: `ValueError` met duidelijke melding; status blijft `DRAFT`.

## Niet-doen-lijst
- Geen wijziging aan prioriteitsregels.
- Geen wijziging aan andere statusovergangen.
- Geen infrastructuur- of dependencywijzigingen.

## Acceptatiecriteria
- Een DRAFT-verzoek met ingevulde `title`, `description` en `requester` kan worden ingediend.
- Een DRAFT-verzoek met lege `title` kan niet worden ingediend; status blijft `DRAFT`.
- Een DRAFT-verzoek met lege `description` kan niet worden ingediend; status blijft `DRAFT`.
- Een DRAFT-verzoek met lege `requester` kan niet worden ingediend; status blijft `DRAFT`.

## Open vragen
- Wordt whitespace-only invoer (bijv. `"   "`) als leeg beschouwd?
