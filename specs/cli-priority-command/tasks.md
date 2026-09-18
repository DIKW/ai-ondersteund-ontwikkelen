# Tasks: CLI-commando om prioriteit van een wijzigingsverzoek aan te passen

| Taak | Eigenaar/Rol | Bewijs | Stopvoorwaarde |
|---|---|---|---|
| **T1 (AC1, AC2, AC4, AC5) - Inventariseer bestaande dekking:** vergelijk `src/change_request_tracker/cli.py`, `src/change_request_tracker/service.py`, `tests/test_cli.py` en `tests/test_service.py` regel voor regel met AC1, AC2, AC4 en AC5 en noteer per AC welke bestaande test dit al bewijst. | Implementer | Een kort overzicht (in commitmessage of PR-beschrijving) dat elk van AC1, AC2, AC4, AC5 koppelt aan een bestaande, met naam genoemde test. | Stop en escaleer als voor AC1, AC2, AC4 of AC5 geen bestaande test wordt gevonden; bedenk geen nieuwe businessregel om het gat te dichten. |
| **T2 (AC3) - Reload-test eerst toevoegen:** voeg in `tests/test_cli.py` een nieuwe test toe die na `priority 1 HIGH` een aparte CLI-aanroep (bijv. `show 1`) uitvoert in een nieuw subprocess en controleert dat de getoonde prioriteit `HIGH` is. | Implementer | Nieuwe, met naam genoemde testmethode die slaagt en expliciet een tweede CLI-aanroep gebruikt om herladen uit het JSON-bestand aan te tonen. | Stop en escaleer als deze test faalt (zou op een echte regressie in bestaande code wijzen) in plaats van productiecode aan te passen zonder overleg. |
| **T3 (AC1, AC2, AC3, AC4, AC5) - Gerichte testrun:** voer `python -m unittest tests.test_cli tests.test_service -v` uit. | Implementer | Volledige testuitvoer met exitcode 0, inclusief de testnamen die AC1, AC2, AC4, AC5 dekken en de nieuwe test uit T2 voor AC3. | Stop en escaleer bij een falende test; herstel alleen binnen `tests/test_cli.py`, `tests/test_service.py` of, uitsluitend bij een aangetoond gat, `src/change_request_tracker/cli.py`. |
| **T4 (AC6) - Afsluitende repositoryverificatie:** voer `bash scripts/check.sh` uit. | Implementer | Exitcode 0 en volledige testuitvoer zonder fouten. | Stop en escaleer bij een mislukking of bij een diff die buiten de toegestane bestanden valt. |
| **T5 (alle AC's) - Traceerbaarheidsrapport:** documenteer in de PR-/commitbeschrijving dat de functionaliteit al aanwezig was, welke tests dit al bewezen (T1) en welke aanvullende test is toegevoegd (T2), met verwijzing naar `specs/cli-priority-update/` als eerdere planning. | Implementer | Korte samenvatting met AC-naar-bewijs-koppeling en een diff die beperkt blijft tot `tests/test_cli.py` en `specs/cli-priority-command/`. | Stop en escaleer als de diff productiecode bevat zonder dat T1-T3 een concreet gat hebben aangetoond. |

## Traceerbaarheid

| Acceptatiecriterium | Taken | Verwacht bewijs |
|---|---|---|
| AC1 - Parsercontract (integer id, ongewijzigde prioriteitswaarde) | T1, T3 | Bestaande groene test `test_parser_accepts_priority_command`. |
| AC2 - Succesvolle, zichtbare wijziging in `DRAFT` | T1, T3 | Bestaande groene test `test_priority_command_updates_draft_and_prints_request`. |
| AC3 - Behoud na herladen uit JSON, aangetoond via CLI | T2, T3 | Nieuwe groene test met een tweede CLI-aanroep (bijv. `show`) na de wijziging. |
| AC4 - Weigering na indienen (exitcode 1, duidelijke fout) | T1, T3 | Bestaande groene tests `test_priority_command_rejects_submitted_without_persisting_change`, `test_priority_cannot_change_after_submit`, `test_priority_cannot_change_in_later_statuses`. |
| AC5 - Geen gegevensmutatie bij weigering | T1, T3 | Dezelfde bestaande tests als AC4, met JSON-/service-asserties op ongewijzigde prioriteit en status. |
| AC6 - Bestaande controles blijven groen | T4 | `bash scripts/check.sh` eindigt met exitcode 0. |
