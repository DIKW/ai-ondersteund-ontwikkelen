# Lab 02 traceability

## Bronketen
- Uitgangsspec: `docs/lab-uitwerkingen/lab-01/model-uitwerking.md`
- Planner-input feature: `docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`
- Domeinregel: `docs/domain.md` (dag 1: verzoek moet volledig zijn bij indienen)
- Implementatiepunt: `src/change_request_tracker/service.py` (`submit_change_request`)
- Testbasis: `tests/test_service.py`

## Herleiding
- Lab 01 definieert dat submit alleen mag slagen bij complete velden.
- Lab 02 vertaalt dit naar concrete validatie in de submit-flow.
- Testbewijs toont dat:
  - complete input nog steeds werkt;
  - incomplete input wordt geblokkeerd met validatiefout;
  - status bij falende submit op `DRAFT` blijft staan.
- Review bevestigt dat wijziging beperkt blijft en geen dag-2-prioriteitsgedrag raakt.

## Concreet gewijzigd
- `src/change_request_tracker/service.py`: required-field controle in `submit_change_request` op `title`, `description`, `requester` met expliciete foutmelding.
- `tests/test_service.py`: permissieve submit-test omgezet naar negatieve padtest; eerder overgeslagen validatietest geactiveerd.

## Sub-agent herleidbaarheid
- **Planner-agent**
  - Input: voorbeeldfeature uit Lab 01 + Lab 02 scope + domeinregel + bestaande code/tests.
  - Output: klein uitvoerbaar plan met 5 stappen, risico's en open vraag over whitespace-regel.
- **Implementer-agent**
  - Input: goedgekeurd planner-plan.
  - Output: beperkte diff in service/tests + geslaagde checkrun (`bash scripts/check.sh`).
- **Reviewer-agent**
  - Input: spec, planoutput, implementerdiff en testbewijs.
  - Output: oordeel `akkoord voor menselijke merge-review` met expliciet restpunt voor documentaire verduidelijking.

Deze keten maakt zichtbaar dat de Lab 02-uitwerking niet alleen een eindresultaat is, maar ook een reproduceerbaar planner -> implementer -> reviewer spoor bevat.

## Scopebewaking
Buiten scope gebleven:
- priority update-regels;
- extra statusovergangen;
- opslag/netwerk/integraties.
