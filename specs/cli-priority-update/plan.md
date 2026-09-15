# Plan: prioriteit wijzigen via de CLI

## Maximaal 5 stappen
1. Voeg in `tests/test_cli.py` eerst parser- en CLI-integratietests toe voor het gewenste commando, succesvolle persistente wijziging in `DRAFT`, zichtbare uitvoer en geweigerde wijziging zonder bestandsmutatie in `SUBMITTED`.
2. Voeg in `tests/test_service.py` gerichte statusbrede testdekking toe die bevestigt dat `update_priority` voor `IN_REVIEW`, `APPROVED`, `REJECTED` en `CLOSED` dezelfde bestaande blokkade en gegevensbehoud biedt; behoud de bestaande positieve `DRAFT`-test.
3. Voeg in `src/change_request_tracker/cli.py` de `priority`-subparser en dispatch toe, roep `update_priority` aan en gebruik de bestaande opslag- en printfuncties na succes. Voeg geen prioriteitsvalidatie of statuslogica aan de CLI toe.
4. Voer eerst de gerichte CLI- en servicetests uit en daarna `bash scripts/check.sh`; vergelijk het bewijs met AC1-AC6 en stop bij regressie of benodigde scopegroei.

## Relevante bestanden
- Te wijzigen door de Implementer: `src/change_request_tracker/cli.py`.
- Te wijzigen door de Implementer: `tests/test_cli.py`.
- Te wijzigen door de Implementer: `tests/test_service.py`.
- Alleen als leidende bron te raadplegen: `docs/domain.md`.
- Alleen als bestaande eigenaar van de businessregel te raadplegen: `src/change_request_tracker/service.py`.
- Planningsartefacten: `specs/cli-priority-update/spec.md`, `specs/cli-priority-update/plan.md` en `specs/cli-priority-update/tasks.md`.

## Risico's
- Dubbele statuslogica in de CLI kan afwijken van `ChangeRequestService.update_priority`; mitigatie is uitsluitend delegeren aan de service.
- Opslaan vóór succesvolle service-uitvoering kan een geweigerde wijziging toch naar schijf schrijven; de negatieve CLI-test vergelijkt daarom de opgeslagen prioriteit en status voor en na de opdracht.
- Nieuwe validatie van prioriteitswaarden zou een niet-gedefinieerde businessregel introduceren; de parser geeft de waarde daarom ongewijzigd door.
- Alleen `SUBMITTED` testen op CLI-niveau kan latere statussen onbewezen laten; compacte service-tests leveren statusbreed bewijs zonder herhaling van dure subprocesscenario's.
- Exacte fouttekst of succesuitvoer is niet als nieuwe businessregel vastgelegd; tests sluiten aan bij de bestaande servicefout en `_print_request`-uitvoer.

## Verificatie
- Parser-test: `priority 1 HIGH` levert command, integer-id en ongewijzigde prioriteit op.
- Positieve CLI-integratietest: een opgeslagen `DRAFT` wordt `HIGH`, blijft `DRAFT`, retourneert exitcode 0 en toont id, status en prioriteit.
- Negatieve CLI-integratietest: een opgeslagen `SUBMITTED` retourneert exitcode 1, toont de bestaande duidelijke servicefout en laat het JSON-bestand inhoudelijk ongewijzigd voor prioriteit en status.
- Service-tests: `DRAFT` blijft toegestaan en iedere niet-`DRAFT`-status weigert de wijziging met behoud van prioriteit en status.
- Gerichte uitvoering: `python -m unittest tests.test_cli tests.test_service -v`.
- Afsluitende uitvoering: `bash scripts/check.sh` moet succesvol eindigen.