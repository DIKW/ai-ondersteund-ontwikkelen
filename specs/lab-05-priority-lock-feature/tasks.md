# Tasks: Prioriteit vastzetten na indienen

| Taak | Eigenaar/Rol | Bewijs | Stopvoorwaarde |
|---|---|---|---|
| Controleer de huidige `update_priority`-logica en bepaal exact waar statusafhankelijk gedrag moet worden afgeschermd | Implementer | Kort overzicht van `src/change_request_tracker/service.py` | De code is traceerbaar gekoppeld aan de businessregel uit de spec |
| Voeg statuscheck toe in `update_priority` zodat `DRAFT` nog mag wijzigen, maar `SUBMITTED` en later niet meer | Implementer | Gewijzigde `service.py`-logica met duidelijke `ValueError` | De prioriteitswijziging is geblokkeerd op de juiste statussen |
| Voeg een positieve test toe voor `DRAFT`-wijziging | Implementer | Nieuwe of aangepaste test in `tests/test_service.py` | De feature werkt in de toegestane case |
| Voeg een negatieve test toe voor `SUBMITTED`-wijziging | Implementer | Nieuwe of aangepaste test in `tests/test_service.py` | De verboden wijziging is testgedekt en faalt met duidelijke melding |
| Verifieer statusbehoud bij mislukte wijziging | Implementer | Testassertie die status onveranderd laat | De status blijft intact bij een mislukte prioriteitswijziging |
| Voer `bash scripts/check.sh` uit en bevestig groen | Implementer | Uitvoer van `scripts/check.sh` zonder fouten | Alle relevante checks zijn groen en de feature is binnen scope |
