# Spec: prioriteit wijzigen via de CLI

## Probleem
De service kan de prioriteit van een wijzigingsverzoek al aanpassen volgens de domeinregel, maar de CLI biedt hiervoor nog geen commando. Daardoor kan een gebruiker de prioriteit van een bestaand wijzigingsverzoek niet via het lokale JSON-opslagbestand wijzigen.

## Doel
Een CLI-commando `priority <id> <priority>` aanbieden waarmee de prioriteit van een bestaand wijzigingsverzoek alleen in `DRAFT` wordt gewijzigd en opgeslagen. Na indienen wordt de wijziging geweigerd en blijven de opgeslagen gegevens intact.

## Scope
- Het CLI-gebruik `PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json priority 1 HIGH`.
- Twee positionele argumenten voor het commando: een numeriek wijzigingsverzoek-id en de nieuwe prioriteitswaarde.
- Hergebruik van `ChangeRequestService.update_priority`; de bestaande service blijft eigenaar van de statusafhankelijke businessregel.
- Opslaan en tonen van het bijgewerkte wijzigingsverzoek na een toegestane wijziging in `DRAFT`.
- Een foutresultaat zonder opslagmutatie wanneer het verzoek `SUBMITTED`, `IN_REVIEW`, `APPROVED`, `REJECTED` of `CLOSED` is.
- CLI- en service-tests als bewijs voor positief gedrag, negatief gedrag en behoud van opgeslagen gegevens.

## Niet-doen-lijst
- Geen nieuwe prioriteitswaarden, normalisatie of validatieregels bedenken.
- Geen wijziging van statusovergangen of van de bestaande service-businessregel.
- Geen apart gedrag ontwerpen voor een niet-bestaand id; de opdracht betreft een bestaand wijzigingsverzoek en bestaand generiek foutgedrag blijft gelden.
- Geen database-, netwerk- of UI-functionaliteit.
- Geen dependencies toevoegen.
- Geen wijzigingen aan demo-, create-, list-, show-, submit-, transition- of close-gedrag.
- Geen merge, release of deployment.

## Acceptatiecriteria
- **AC1:** De CLI-parser accepteert `priority <id> <priority>`, waarbij `<id>` als integer wordt verwerkt en de prioriteitswaarde ongewijzigd aan de bestaande service wordt doorgegeven.
- **AC2:** Voor een bestaand wijzigingsverzoek in `DRAFT` eindigt het priority-commando succesvol, wordt de nieuwe prioriteit opgeslagen in het met `--db` gekozen JSON-bestand en blijft de status `DRAFT`.
- **AC3:** Voor een bestaand wijzigingsverzoek in `SUBMITTED`, `IN_REVIEW`, `APPROVED`, `REJECTED` of `CLOSED` eindigt een prioriteitswijziging met een foutresultaat en een duidelijke foutmelding.
- **AC4:** Na een geweigerde prioriteitswijziging zijn prioriteit en status in het JSON-opslagbestand onveranderd.
- **AC5:** Na een succesvolle wijziging toont de CLI het bijgewerkte wijzigingsverzoek, inclusief id, status en nieuwe prioriteit.
- **AC6:** Alle bestaande controles blijven slagen via `bash scripts/check.sh`.

## Open vragen
- Geen blokkerende open vragen. De exacte set of validatie van prioriteitswaarden blijft volgens de bron en opdracht buiten scope; dit commando hergebruikt het bestaande gedrag.