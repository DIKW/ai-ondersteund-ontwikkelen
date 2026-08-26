# Plan: Validatie bij indienen wijzigingsverzoek

## Maximaal 5 stappen
1. Verwijder de tolerantietest `test_submit_without_required_fields_does_not_raise` en activeer `test_submit_requires_title_description_and_requester` (skip verwijderen) in `tests/test_service.py`.
2. Voeg validatie toe aan `submit_change_request` in `src/change_request_tracker/service.py`: controleer vóór statuswissel of `title`, `description` en `requester` niet leeg zijn (`.strip()`). Gooi `ValueError` bij ontbrekende waarde; status blijft `DRAFT`.
3. Voeg drie gerichte tests toe — één per ontbrekend verplicht veld — zodat elk acceptatiecriterium afzonderlijk gedekt is.
4. Voer `bash scripts/check.sh` uit en bevestig dat alle tests slagen.

## Relevante bestanden
- `src/change_request_tracker/service.py` — validatielogica toevoegen
- `tests/test_service.py` — bestaande skip activeren, tolerantietest verwijderen, nieuwe tests toevoegen
- `docs/domain.md` — leidend domeinmodel
- `docs/lab-uitwerkingen/lab-02-mijn-uitwerking/new-feature-voor-lab-02.md` — featurebeschrijving en acceptatiecriteria

## Aannames
- Whitespace-only invoer (`"   "`) wordt als leeg beschouwd (`.strip() == ""`). Te bevestigen vóór implementatie (zie Open vragen).

## Risico's
- Geen andere code roept `submit_change_request` aan buiten de tests — laag risico op onbedoelde regressie.

## Open vragen
- Moet whitespace-only invoer als leeg worden beschouwd, of geldt strikt `== ""`?
