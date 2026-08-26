# Tasks: Validatie bij indienen wijzigingsverzoek

| Taak | Eigenaar/Rol | Bewijs | Stopvoorwaarde |
|---|---|---|---|
| Activeer `test_submit_requires_title_description_and_requester`, verwijder tolerantietest | Developer | Gewijzigde `tests/test_service.py` | Test draait zonder skip |
| Voeg validatie toe aan `submit_change_request` | Developer | Gewijzigde `service.py` met `ValueError`-logica per ontbrekend veld | Alle bestaande tests slagen |
| Voeg drie gerichte tests toe (één per ontbrekend veld) | Developer | Nieuwe testmethoden in `test_service.py` | Elk acceptatiecriterium afzonderlijk gedekt |
| Voer `scripts/check.sh` uit en bevestig groen | Developer | Uitvoer check.sh zonder fouten | Alle checks groen |
