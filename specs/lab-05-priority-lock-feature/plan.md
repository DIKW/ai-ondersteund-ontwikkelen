# Plan: Prioriteit vastzetten na indienen

## Maximaal 5 stappen
1. Controleer de bestaande service- en statuslogica in `src/change_request_tracker/service.py` en bevestig welke statusafhankelijke validatie al aanwezig is.
2. Voeg een kleine statuscheck toe voor `priority`-wijzigingen: in `DRAFT` toegestaan, in `SUBMITTED` en latere statussen verboden.
3. Werk de relevante tests in `tests/test_service.py` bij zodat zowel het positieve pad (`DRAFT`) als het negatieve pad (`SUBMITTED`) expliciet worden afgedekt.
4. Verifieer dat een mislukte prioriteitswijziging een duidelijke foutmelding geeft en dat de status van het verzoek intact blijft.
5. Draai `bash scripts/check.sh` en controleer of de feature voldoet aan de acceptatiecriteria uit de spec zonder extra scope.

## Relevante bestanden
- `src/change_request_tracker/service.py`
- `tests/test_service.py`
- `docs/domain.md`
- `specs/lab-05-priority-lock-feature/spec.md`

## Risico's
- Scope vergroting door extra validatie buiten `priority`.
- Onduidelijkheid over wat een "wijziging" van prioriteit precies inhoudt.
- Onvoldoende testbewijs als alleen code zonder statusafhankelijke testcase wordt toegevoegd.

## Verificatie
- Unittests voor `DRAFT`-wijziging zijn groen.
- Unittests voor `SUBMITTED`-blokkeerregel zijn groen.
- Uitvoer van `bash scripts/check.sh` eindigt succesvol.
- Review kan aantonen dat de feature spec-conform is en binnen de domeinregels blijft.
