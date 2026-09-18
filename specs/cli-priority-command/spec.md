# Spec: CLI-commando om prioriteit van een wijzigingsverzoek aan te passen

## Probleem
Er is een CLI-feature gevraagd waarmee de prioriteit van een bestaand wijzigingsverzoek via `PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json priority <id> <priority>` kan worden aangepast, met als leidende businessregel (`docs/domain.md`): prioriteit mag alleen in `DRAFT` wijzigen en niet meer na indienen.

**Belangrijke bevinding bij analyse van de huidige code (te bevestigen door de mens):** deze functionaliteit lijkt al volledig aanwezig te zijn.
- `ChangeRequestService.update_priority` (`src/change_request_tracker/service.py`) implementeert exact deze regel: wijzigen alleen toegestaan wanneer `status is Status.DRAFT`, anders `ValueError("Prioriteit kan niet meer worden gewijzigd")`.
- `src/change_request_tracker/cli.py` bevat al een `priority`-subparser met positionele `id` (int) en `priority` (str), die dispatcht naar `service.update_priority`, alleen bij succes opslaat en het resultaat toont.
- `tests/test_cli.py` bevat al `test_parser_accepts_priority_command`, `test_priority_command_updates_draft_and_prints_request` en `test_priority_command_rejects_submitted_without_persisting_change`.
- `tests/test_service.py` bevat al `test_priority_can_change_while_request_is_draft`, `test_priority_cannot_change_after_submit` en `test_priority_cannot_change_in_later_statuses` (voor `IN_REVIEW`, `APPROVED`, `REJECTED`, `CLOSED`).
- Er bestaat al een eerdere planning hierover in `specs/cli-priority-update/`.

Deze spec behandelt de featureopdracht daarom als een verificatie-opdracht: bevestig dat bestaande code en tests aan alle acceptatiecriteria voldoen, en vul alleen een concreet aantoonbare testdekkingslacune aan (zie AC3) zonder nieuwe businessregels of productiecode te introduceren, tenzij verificatie een echt gebrek blootlegt.

## Doel
Aantoonbaar (via bestaande en, waar nodig, aanvullende tests) vaststellen dat het CLI-commando `priority <id> <priority>` een bestaand wijzigingsverzoek alleen in `DRAFT` van prioriteit laat wisselen, de wijziging persistent opslaat, na indienen wordt geweigerd zonder gegevensmutatie, en dat `bash scripts/check.sh` slaagt.

## Scope
- Het CLI-gebruik `PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json priority 1 HIGH`.
- Verificatie van de bestaande `priority`-subparser, dispatch naar `ChangeRequestService.update_priority`, opslag en weergave.
- Aanvullen van test tests/test_cli.py met een expliciete reload-test via een tweede, losse CLI-aanroep (bijv. `show`), zodat "gewijzigde prioriteit blijft behouden na herladen uit het JSON-bestand" via CLI-gedrag wordt aangetoond, niet alleen via het rechtstreeks inlezen van het JSON-bestand.
- Bevestigen dat een prioriteitswijziging op een niet-`DRAFT`-verzoek (`SUBMITTED`, `IN_REVIEW`, `APPROVED`, `REJECTED`, `CLOSED`) faalt met exitcode 1 en de opgeslagen gegevens ongewijzigd laat.
- Uitvoeren van de gerichte tests en `bash scripts/check.sh` als eindbewijs.

## Niet-doen-lijst
- Geen nieuwe prioriteitswaarden of validatieregels bedenken.
- Geen wijzigingen aan statusovergangen.
- Geen database-, netwerk- of UI-functionaliteit.
- Geen dependencies toevoegen.
- Geen merge, release of deployment.
- Geen productiecodewijziging in `cli.py`, `service.py` of `models.py` tenzij verificatie een concreet, met een test aangetoond gebrek blootlegt ten opzichte van de acceptatiecriteria hieronder.
- Geen dubbele of tegenstrijdige planning naast `specs/cli-priority-update/`; deze spec bouwt voort op die bevindingen en breidt uitsluitend aan waar een concrete lacune bestaat.

## Acceptatiecriteria
- **AC1:** De CLI-parser accepteert `priority <id> <priority>`, waarbij `<id>` als integer wordt verwerkt en de prioriteitswaarde ongewijzigd aan de service wordt doorgegeven.
- **AC2:** Voor een bestaand wijzigingsverzoek in `DRAFT` eindigt het `priority`-commando met exitcode 0 en toont het een duidelijke bevestiging met id, status (`DRAFT`) en de nieuwe prioriteit.
- **AC3:** De gewijzigde prioriteit blijft behouden na herladen uit het JSON-opslagbestand, aantoonbaar via een aparte CLI-aanroep die het bestand na de wijziging opnieuw inleest (bijv. `show`).
- **AC4:** Een prioriteitswijziging op een verzoek in `SUBMITTED`, `IN_REVIEW`, `APPROVED`, `REJECTED` of `CLOSED` eindigt met exitcode 1 en een duidelijke foutmelding.
- **AC5:** Na een geweigerde prioriteitswijziging zijn de opgeslagen prioriteit en status in het JSON-bestand ongewijzigd.
- **AC6:** `bash scripts/check.sh` eindigt succesvol (exitcode 0).

## Open vragen
- Geen blokkerende open vragen. Ter info voor de gatekeeper: de gevraagde functionaliteit lijkt al volledig geïmplementeerd en getest (zie "Belangrijke bevinding" hierboven en `specs/cli-priority-update/`). Deze spec voorkomt dubbel werk door de opdracht te herformuleren als verificatie plus één gerichte aanvullende test (AC3-bewijs via CLI-reload). Bevestig of dit akkoord is, of geef aan of er een andere reden is om de functionaliteit opnieuw te (laten) bouwen.
