# Lab 01 traceability

## Bronnen
- Domeinregel dag 1: `docs/domain.md`
- Huidig servicegedrag: `src/change_request_tracker/service.py`
- Huidige testsituatie: `tests/test_service.py`

## Herleiding van modeluitwerking
- Probleemdefinitie komt uit `docs/domain.md` (dag 1: verplicht volledige velden bij indienen) en wordt bevestigd door de huidige baseline-test in `tests/test_service.py` waar submit zonder velden nog slaagt.
- Scope is beperkt tot submit-validatie omdat dat exact de dag-1 lacune is.
- Niet-doen-lijst sluit aan op `docs/domain.md` (dag 2-prioriteitsregel staat los van dag 1).
- Acceptatiecriteria vertalen de domeinregel naar controleerbaar gedrag op service-niveau.
- Open vraag over whitespace is een expliciete interpretatievraag die niet definitief in domeinregels is vastgelegd.
