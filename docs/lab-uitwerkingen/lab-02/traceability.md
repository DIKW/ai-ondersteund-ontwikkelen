# Lab 02 traceability

## Bronketen
- Uitgangsspec: `docs/lab-uitwerkingen/lab-01/model-uitwerking.md`
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

## Scopebewaking
Buiten scope gebleven:
- priority update-regels;
- extra statusovergangen;
- opslag/netwerk/integraties.
