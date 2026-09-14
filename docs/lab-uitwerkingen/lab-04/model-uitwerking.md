# Lab 04 modeluitwerking

## Doel van deze uitwerking
Deze uitwerking beschrijft eerst de noodzakelijke aanpassingen in de agent-definities om een echte planner-implementer-reviewer loop te kunnen draaien, en daarna de voorbeeldhandoffs die in Lab 05 als werkelijke loop zullen worden uitgevoerd.

## 1) Noodzakelijke aanpassingen per agent

### 1.1 Planner-agent: van rolbeschrijving naar plan-contract

#### Probleem in de oorspronkelijke vorm
De eerste versie van `planner.agent.md` was nog te algemeen: het beschreef een rol, maar niet wat de planner verplicht moest opleveren om een implementer te laten starten. Er ontbrak een expliciet handoff-contract.

#### Aanpassingen die nodig zijn
1. Maak de input expliciet.
   - De planner moet eerst de domeinregels, spec en relevante tests lezen.
   - Hij mag geen aannames doen die niet in `docs/domain.md`, een spec of een test staan.
2. Maak de output verplicht.
   - Maximaal 5 stappen.
   - `doel`, `in scope`, `buiten scope`, `acceptatiecriteria`, `risico's`, `verificatieplan`, `stopvoorwaarden`.
3. Maak de handoff naar implementer formeel.
   - Niet: “een kort plan”, maar een vaste handoff met verplichte velden.
4. Voeg stop- en escalatieregels toe.
   - Als de businessregel onduidelijk is, stop en escaleer.
   - Als de wijziging buiten scope valt, stop.
5. Verwijder onduidelijkheid in bevoegdheden.
   - De planner mag geen code of tests wijzigen; dat is niet onder de planner-functie.

#### Resultaat
De planner levert een plan dat een implementer zonder extra interpretatie kan uitvoeren.

#### Voorbeeld van de vaste planner-output
```text
Doel:
In scope:
Buiten scope:
Acceptatiecriteria:
Risico's:
Verificatiestappen:
Stopvoorwaarden:
Aannames:
Open vragen:
```

### 1.2 Implementer-agent: van "code uitvoeren" naar "scope-bounded executor"

#### Probleem in de oorspronkelijke vorm
De implementer beschreef nog vooral een taak, maar niet dat hij alleen een goedgekeurd plan mag uitvoeren en een review-ready handoff moet opleveren.

#### Aanpassingen die nodig zijn
1. Vereis een goedgekeurd planner-handoff als input.
   - Niet starten zonder plan.
2. Beperk de scope expliciet.
   - Geen extra verbeteringen, geen "kleine extra's".
3. Voeg verplichte output toe voor review.
   - Gewijzigde bestanden
   - Uitgevoerde checks
   - Bewijslast
   - Open punten
4. Voeg escalatiecriteria toe.
   - Als het plan onduidelijk is, als de scope blijkt te veranderen of als het bewijs ontbreekt, stop.
5. Beperk de toolset tot read/search/edit/execute zonder redevoering over ongewenste acties.

#### Resultaat
De implementer is geen vrije uitvoerder meer, maar een scope-bounded executor die een traceerbaar bewijs naar reviewer stuurt.

#### Voorbeeld van de vaste implementer-output
```text
Uitgevoerde wijziging:
Gewijzigde bestanden:
Testbewijs:
Bekende beperkingen/open punten:
Vraag aan reviewer:
```

### 1.3 Reviewer-agent: van vrije beoordeling naar evidence-based gate

#### Probleem in de oorspronkelijke vorm
De reviewer was te kort en te vaag. Hij gaf wel een oordeel, maar niet hoe die conclusie moest worden onderbouwd of hoe de handoff aan de menselijke gate moest lopen.

#### Aanpassingen die nodig zijn
1. Maak de input door de planner en implementer expliciet.
   - spec + plan + diff + testbewijs
2. Maak de output controleerbaar.
   - must have: verdict + rationale + risico + bewijsdekking
3. Voeg `rework` en `escaleren` expliciet toe als verschillende outcomes.
   - Niet alleen “akkoord” versus “terug naar implementer”.
4. Maak de handoff aan de human gate expliciet.
   - Samenvatting
   - Spec-conformiteit
   - Bewijsdekking
   - Risico
   - Besluitadvies
   - Voorwaarden voor vervolg
5. Voeg een stopregel toe bij onvoldoende bewijs.
   - Als er geen duidelijk bewijs is, geen acceptatie.

#### Resultaat
De reviewer is geen losse opinie, maar de bewijsgate die controleert of een wijziging al dan niet veilig door kan gaan.

#### Voorbeeld van de vaste reviewer-output
```text
Besluit: akkoord / terug naar implementer / escaleren
Spec-conformiteit:
Bewijsdekking:
Risico's:
Openstaande vragen:
Voorwaarden voor vervolg:
```

## 2) Hoe de echte loop werkt met handoffs

De werkelijke loop is niet “agent praat met agent in vrije tekst”, maar een gecontroleerde flow met vaste handoff-structuren.

### 2.1 Flow
1. Planner leest domein en spec.
2. Planner schrijft een scoped plan.
3. Menselijke gatekeeper keurt plan goed of vraagt om bijsturing.
4. Implementer voert alleen dat plan uit.
5. Implementer levert review-ready bewijs aan de reviewer.
6. Reviewer beoordeelt op spec, risico en bewijs.
7. Reviewer levert advies aan de human gatekeeper.
8. Human gatekeeper beslist: accept / rework / escaleren.

### 2.2 Belangrijk onderscheid
Niet alle handoffs zijn gelijk:
- Planner → Implementer = plan + scope + criteria
- Implementer → Reviewer = bewijs + diff + risico
- Reviewer → Human gate = verdict + onderbouwing + voorwaarden

Dit is precies waarom de agent-definities moeten worden gespecificeerd als contracten, niet als losse promptbeschrijvingen.

## 3) Voorbeeld handoff-formaten zoals ze in Lab 05 echt gebruikt zullen worden

### 3.1 Planner → Implementer (voorbeeld)
```text
Doel van wijziging:
Verhogen van validatie bij submit zodat onvolledige wijzigingsverzoeken niet worden ingediend.

In scope:
- Validatie van `title`, `description` en `requester` bij submit.
- Status blijft `DRAFT` bij mislukte submit.
- Bijbehorende tests.

Buiten scope:
- Prioriteitsregels.
- Nieuwe statussen of transitions.
- Database, webinterface of externe systemen.

Acceptatiecriteria:
- Een DRAFT-verzoek met lege `title` kan niet worden ingediend.
- Een DRAFT-verzoek met lege `description` kan niet worden ingediend.
- Een DRAFT-verzoek met lege `requester` kan niet worden ingediend.
- Feitelijke status blijft `DRAFT` bij fout.

Risico's:
- Onduidelijke whitespace-regel kan interpreteerbaar zijn als afwijkende businessregel.
- Te brede validatie kan statusflow verstoren.

Verificatiestappen:
- Run tests voor submit-validatie.
- Controleer negatieve en positieve flow.
- Verifieer statusbehoud bij fout.

Stopvoorwaarden:
- Stop als een businessregel niet is vastgelegd.
- Stop als scope uitbreidt naar prioriteit of statusflow.
```

### 3.2 Implementer → Reviewer (voorbeeld)
```text
Uitgevoerde wijziging:
- Validatie in `submit_change_request` voor verplichte velden `title`, `description` en `requester`.
- Verkeerde submit-poging resulteert in `ValueError` en status blijft `DRAFT`.

Gewijzigde bestanden:
- `src/change_request_tracker/service.py`
- `tests/test_service.py`

Testbewijs:
- `python -m unittest discover -s tests -v`
- Resultaat: alle tests slagen.

Bekende beperkingen/open punten:
- Whitespace-only waarden moeten later expliciet worden vastgelegd als leeg of niet-leeg.
- Prioriteitsgedrag is buiten scope gebleven.

Vraag aan reviewer:
- Is de submit-validatie voldoende spec-conform en is het bewijs sterk genoeg voor acceptatie?
```

### 3.3 Reviewer → Gatekeeper (voorbeeld)
```text
Samenvatting bevindingen (ernst):
- Laag risico; wijziging is klein en traceerbaar.

Spec-conformiteit:
- voldoet aan de domainregel dat bij indienen de velden verplicht zijn.

Bewijsdekking:
- Positief pad en negatieve paden zijn getest.
- Status blijft `DRAFT` bij mislukte submit is expliciet geverifieerd.

Besluitadvies:
- Accept

Voorwaarden voor vervolg:
- Geen extra scope.
- De whitespace-regel wordt expliciet vastgelegd als follow-up, indien nodig.
```

## 4) Waarom deze handoffs essentieel zijn

Zonder deze vaste handoffs is de loop niet controleerbaar:
- de implementer weet niet precies wat moet worden gebouwd
- de reviewer weet niet precies waarop hij moet beoordelen
- de gatekeeper krijgt geen eenduidige onderbouwing
- de loop verlaat het pad van spec-conformiteit en wordt een vrije chat

## 5) Praktische conclusie voor Lab 04
Het echte doel van Lab 04 is niet alleen “een rolmatrix maken”, maar expliciet vastleggen dat:
- de planner verantwoordelijkheid heeft voor scope en criteria
- de implementer verantwoordelijkheid heeft voor bewijs in beperkte scope
- de reviewer verantwoordelijkheid heeft voor onafhankelijke beoordeling
- de menselijke gatekeeper de enige is die definitief doorlaat of stuit

Daarmee wordt de loop pas een gecontroleerde AI-ontwikkelcyclus in plaats van een losse opdrachtuitwerking.
