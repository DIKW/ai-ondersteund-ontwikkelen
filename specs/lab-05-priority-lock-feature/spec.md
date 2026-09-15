# Spec: Prioriteit vastzetten na indienen

## Probleem
Na indienen van een wijzigingsverzoek mag de prioriteit niet meer worden gewijzigd. In de huidige workflow is dit nog niet expliciet afgeschermd. Daardoor kan de prioriteitswaarde op een later moment nog wijzigen terwijl het verzoek al in de processtroom zit.

## Doel
Zorgen dat prioriteit alleen nog mag worden gewijzigd zolang een verzoek in `DRAFT` is. Zodra het verzoek is ingediend (`SUBMITTED` en later), is `priority` read-only.

## Scope
- Validatie van `priority`-wijzigingen afhankelijk van de status.
- In `DRAFT` mag de prioriteit worden aangepast.
- Na `SUBMITTED` mag de prioriteit niet meer wijzigen.
- Bij een verboden wijziging: duidelijke foutmelding en geen statuswijziging of mutatie.

## Niet-doen-lijst
- Geen wijziging van andere statusovergangen.
- Geen database- of UI-wijziging.
- Geen standaardisatie van prioriteitswaarden buiten de bestaande, eenvoudige domeinwaarden.
- Geen extra businessregels die niet in dit domein staan.

## Acceptatiecriteria
- Een wijzigingsverzoek in `DRAFT` kan een `priority` krijgen of wijzigen.
- Een wijzigingsverzoek in `SUBMITTED` kan geen nieuwe `priority` meer accepteren.
- Een wijzigingsverzoek in `IN_REVIEW`, `APPROVED`, `REJECTED` of `CLOSED` kan geen nieuwe `priority` meer accepteren.
- Een verboden prioriteitswijziging geeft een duidelijke foutmelding.
- De status van het verzoek blijft intact bij een mislukte prioriteitswijziging.

## Open vragen
- Moet whitespace-only waarde voor `priority` worden behandeld als ongeldige invoer? Antwoord: Ja
- Is de prioriteitswaarde nog beperkt tot de huidige eenvoudige set, of wordt later een standaardisatie-opdracht uitgewerkt? Voor nu alleen de eenvoudige set.
