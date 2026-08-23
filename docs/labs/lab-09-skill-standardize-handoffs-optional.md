# Lab 09 (optioneel): skill maken voor gestandaardiseerde handoffs

- **Doel:** ontwerp een kleine skill die planner- en reviewer-output consistent structureert zonder de menselijke beslismomenten te vervangen.
- **Tijd:** 45-60 min
- **Startpunt:** afgeronde labs 04 t/m 08
- **Positionering:** dag 2 verdieping (advanced), niet verplicht

## Entry criteria (wanneer dit lab doen)

Doe dit lab alleen als:
- Het team labs 04 en 05 succesvol heeft afgerond met expliciete handoffs.
- Er in eerdere cycli aantoonbare variatie of ruis zat in planner/reviewer-output.
- Er tijd is voor een extra experiment zonder impact op basisprogramma.

## Stappen
1. Kies 1 concreet pijnpunt uit eerdere loops (bijvoorbeeld inconsistente plan- of review-output).
2. Definieer een minimaal outputformat met verplichte velden.
3. Maak een skill-concept met:
   - scope en grenzen
   - inputverwachting
   - outputtemplate
   - stop/escalatieregels
4. Test de skill in een kleine oefencyclus op een bestaande mini-wijziging.
5. Vergelijk de outputkwaliteit met en zonder skill.
6. Beslis of de skill behouden, aangepast of afgewezen wordt.

## Minimale skill-output

De skill moet minimaal afdwingen:
- Context: doel, scope, buiten scope.
- Bewijs: test/check en open risico.
- Besluit: accept/rework/escalate met korte rationale.

## Verwachte artefacten
- Skillontwerp (Markdown)
- Voorbeeldoutput met en zonder skill
- Korte evaluatie met besluit

## Evaluatiekader (meetbaar)

Vergelijk "zonder skill" vs "met skill" op 3 metrics:
- Volledigheid handoff (% verplichte velden ingevuld).
- Aantal verduidelijkingsvragen in review.
- Tijd tot reviewbesluit.

Succesindicatie: minimaal 2 van de 3 metrics verbeteren zonder scopegroei.

## Kwaliteitscheck
- De skill verkleint variatie in handoffs aantoonbaar.
- Menselijke gates blijven expliciet aanwezig.
- Scope blijft binnen trainingskaders en zonder extra dependencies.

## Stop/escalatie
- Escaleer als de skill scope buiten handoff-standaardisatie groeit.
- Stop als de skill meer procesfrictie toevoegt dan kwaliteitswinst oplevert.
- Stop direct bij voorstellen voor extra infrastructuur, plugins of externe services.

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Entry criteria waren aantoonbaar van toepassing.
- Evaluatiekader is ingevuld met voor/na-vergelijking.
- Er is een expliciet besluit: behouden, aanpassen of afwijzen.

## Reflectie
- Welke verplichte velden in de skill leverden de grootste kwaliteitswinst op?
