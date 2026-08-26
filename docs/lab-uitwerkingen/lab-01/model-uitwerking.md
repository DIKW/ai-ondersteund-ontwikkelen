# Lab 01 modeluitwerking

## Probleem
In de huidige startsituatie kan een wijzigingsverzoek worden ingediend zonder verplichte inhoud. Daardoor komen onvolledige verzoeken in de workflow terecht, wat review en besluitvorming vertraagt.

## Doel
Alleen volledige verzoeken mogen van DRAFT naar SUBMITTED.

## Scope
- Focus op indienen (`submit`) van een verzoek.
- Verplichte velden: `title`, `description`, `requester`.
- Vastleggen van toetsbare acceptatiecriteria voor deze regel.

## Niet-doen-lijst
- Geen wijziging aan prioriteitsregels.
- Geen wijziging aan statusovergangen buiten `DRAFT -> SUBMITTED`.
- Geen wijziging aan opslag, netwerk of externe systemen.

## Acceptatiecriteria
- Een DRAFT-verzoek met ingevulde `title`, `description` en `requester` kan succesvol worden ingediend.
- Een DRAFT-verzoek met lege `title` kan niet worden ingediend en geeft een duidelijke validatiefout.
- Een DRAFT-verzoek met lege `description` kan niet worden ingediend en geeft een duidelijke validatiefout.
- Een DRAFT-verzoek met lege `requester` kan niet worden ingediend en geeft een duidelijke validatiefout.
- Na een mislukte submit-poging blijft de status van het verzoek `DRAFT`.

## Open vraag
Worden waarden met alleen whitespace (bijvoorbeeld `"   "`) als leeg beschouwd? Dit moet expliciet worden besloten voordat implementatie start.
