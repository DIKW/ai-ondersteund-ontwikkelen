# Lab 03 modeluitwerking

## Reviewinput (startstate)
- Startstate: `lab-02-solution` (inclusief codewijziging en tests uit Lab 02).
- Inputspec: `docs/lab-uitwerkingen/lab-02/model-uitwerking.md`.
- Inputbewijs: compacte diff en testuitkomst (`OK`) uit Lab 02.

## Doel van deze review
Toets of de Lab 02-wijziging aantoonbaar spec-conform is, binnen scope blijft en regressierisico voldoende afdekt.

## Bevindingen per ernst

### Blokkerend
- **Bevinding:** De businessregel rond whitespace-only invoer is niet expliciet vastgelegd in de bronregel, terwijl de implementatie dit wel afdwingt.
- **Waarom blokkerend:** Zonder expliciete regel kan een team dezelfde code later als "te streng" terugdraaien, waardoor gedrag gaat divergeren.
- **Benodigd bewijs:** expliciete bevestiging in spec/open vraag of een korte besluitnotitie bij de regel.

### Belangrijk
- **Bevinding:** De wijziging blijft functioneel binnen submit-validatie, maar de review moet expliciet benoemen dat prioriteitsgedrag buiten scope bleef.
- **Waarom belangrijk:** Dit voorkomt scope creep in vervolglabs en maakt besluitvorming reproduceerbaar.
- **Bewijs:** diff raakt alleen `submit_change_request` en submit-gerelateerde tests.

### Suggestie
- **Bevinding:** Foutmelding kan consistentie winnen met vaste volgorde van ontbrekende velden (`title, description, requester`) in alle communicatie.
- **Waarom suggestie:** Geen functionele fout, wel betere uitlegbaarheid voor gebruikers en reviewers.

## Reviewbesluit
- **Besluit:** `REWORK (documentair)`.
- **Onderbouwing:** Code en tests zijn sterk, maar de blocker vraagt om expliciete vastlegging van de whitespace-regel in spec/decision-note.
- **Vervolgstap:** Leg de regel expliciet vast; codewijziging is niet vereist als de regel wordt bevestigd.

## Eventuele kleine herstelactie
- In dit modelvoorbeeld volstaat een documentaire herstelactie (regel expliciteren). Geen extra productcode nodig.
