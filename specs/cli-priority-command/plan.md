# Plan: CLI-commando om prioriteit van een wijzigingsverzoek aan te passen

## Maximaal 5 stappen
1. Inventariseer de bestaande implementatie (`src/change_request_tracker/cli.py`, `src/change_request_tracker/service.py`) en bestaande tests (`tests/test_cli.py`, `tests/test_service.py`) regel voor regel tegen AC1, AC2, AC4 en AC5 en documenteer welke bestaande test welk AC al dekt.
2. Voeg in `tests/test_cli.py` één aanvullende test toe die na een succesvolle `priority`-wijziging een tweede, losse CLI-aanroep doet (bijv. `show <id>`) om aan te tonen dat de gewijzigde prioriteit na herladen uit het JSON-bestand zichtbaar blijft (AC3). Wijzig geen productiecode voor deze stap.
3. Voer de gerichte tests uit: `python -m unittest tests.test_cli tests.test_service -v` en vergelijk elk testresultaat met AC1-AC5.
4. Voer `bash scripts/check.sh` uit als eindverificatie (AC6).
5. Als een AC niet aantoonbaar blijkt met bestaande code, escaleer met een concrete beschrijving van het gat in plaats van nieuwe businessregels of ongevraagde productiecode toe te voegen.

## Relevante bestanden
- Alleen lezen/verifiëren: `src/change_request_tracker/cli.py`.
- Alleen lezen/verifiëren: `src/change_request_tracker/service.py`.
- Alleen lezen/verifiëren: `src/change_request_tracker/models.py`.
- Te wijzigen door de Implementer (alleen aanvullen, niet herschrijven): `tests/test_cli.py`.
- Alleen lezen/verifiëren, wijzig alleen bij een aangetoond gat: `tests/test_service.py`.
- Leidende bron, alleen lezen: `docs/domain.md`.
- Ter referentie, alleen lezen: `specs/cli-priority-update/spec.md`, `specs/cli-priority-update/plan.md`, `specs/cli-priority-update/tasks.md`.
- Planningsartefacten: `specs/cli-priority-command/spec.md`, `specs/cli-priority-command/plan.md`, `specs/cli-priority-command/tasks.md`.

## Risico's
- De gevraagde functionaliteit blijkt al volledig te bestaan; risico op onnodige of dubbele productiecodewijziging als de Implementer toch nieuwe logica toevoegt. Mitigatie: taken beperken tot verificatie en één aanvullende test, met een expliciete stopvoorwaarde bij elke poging tot productiecodewijziging zonder aangetoond gat.
- De aanvullende reload-test kan per ongeluk bestaand CLI-gedrag beïnvloeden als de test verkeerd wordt opgezet. Mitigatie: uitsluitend een nieuwe testmethode toevoegen in `tests/test_cli.py`, geen wijziging van bestaande tests of van `cli.py`.
- Verwarring of duplicatie met `specs/cli-priority-update/` kan tot inconsistente planning leiden. Mitigatie: deze plan.md verwijst expliciet naar die eerdere spec en beperkt scope tot het aanvullen van het reload-bewijs.
- Als de bestaande foutmelding of statuscontrole ooit wijzigt, kunnen tests vals-positief worden. Mitigatie: tests blijven exact aansluiten bij de bestaande servicefout (`"Prioriteit kan niet meer worden gewijzigd"`) zonder deze tekst te herdefiniëren.

## Verificatie
- Parser-bewijs: bestaande test `test_parser_accepts_priority_command` toont AC1 aan.
- Positief pad: bestaande test `test_priority_command_updates_draft_and_prints_request` toont AC2 aan (exitcode 0, JSON-prioriteit, weergave).
- Reload-bewijs: nieuwe test in `tests/test_cli.py` toont AC3 aan via een tweede CLI-aanroep na de wijziging.
- Negatief pad: bestaande test `test_priority_command_rejects_submitted_without_persisting_change` toont AC4 en AC5 aan (exitcode 1, ongewijzigde JSON).
- Statusbrede dekking: bestaande service-tests (`test_priority_can_change_while_request_is_draft`, `test_priority_cannot_change_after_submit`, `test_priority_cannot_change_in_later_statuses`) bevestigen AC4/AC5 voor alle niet-`DRAFT`-statussen.
- Gerichte uitvoering: `python -m unittest tests.test_cli tests.test_service -v` moet volledig groen zijn.
- Afsluitende uitvoering: `bash scripts/check.sh` moet exitcode 0 opleveren (AC6).
