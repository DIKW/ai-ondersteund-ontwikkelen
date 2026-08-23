# Lab 04: ontwerp de loop

- **Doel:** ontwerp een gecontroleerde planner-implementer-reviewer-lus.
- **Tijd:** 45-60 min
- **Startpunt:** businessbehoefte over prioriteit na indienen

## Module-mapping (cursus-outline)

| Cursusmodule | Focus | Verwachte laboutput |
|---|---|---|
| Dag 2, module 2 (loop engineering) | Plan -> Spec -> Code -> Test -> Review | Rolmatrix + loopstappen met gates |
| Dag 2, module 3 (teamwerk met AI) | Rollen en rechten | Planner/implementer/reviewer verantwoordelijkheden |
| Dag 2, module 3a (context + evals) | Contextkwaliteit en bewijs | Handoff-formaten + stop/escalatieregels |

## Stappen
1. Maak een rolmatrix.
2. Definieer 3 handoff-formaten.
3. Definieer stopvoorwaarden.
4. Definieer escalatieregels.
5. Leg vast welke acties mensen altijd zelf houden.

## Voorbeeld rolmatrix (invulbaar)

| Rol | Verantwoordelijkheid | Mag zelf beslissen | Moet escaleren bij |
|---|---|---|---|
| Planner | Scope en plan opstellen | Voorstel voor stappenvolgorde | Onduidelijke businessregel |
| Implementer | Wijziging uitvoeren binnen scope | Technische detailkeuze binnen plan | Scopegroei of conflicterende eisen |
| Reviewer | Onafhankelijke toets op bewijs en risico | Advies accept/rework | Ontbrekend kritisch bewijs |
| Menselijke gatekeeper | Go/no-go per fase | Akkoord op vervolgfase | Onacceptabel risico of compliance-twijfel |

## Handoff-templates (3 stuks)

### 1) Planner -> Implementer
- Doel van wijziging:
- In scope:
- Buiten scope:
- Acceptatiecriteria:
- Risico's:
- Verificatiestappen:

### 2) Implementer -> Reviewer
- Uitgevoerde wijziging:
- Gewijzigde bestanden:
- Testbewijs:
- Bekende beperkingen/open punten:
- Vraag aan reviewer:

### 3) Reviewer -> Gatekeeper
- Samenvatting bevindingen (ernst):
- Spec-conformiteit:
- Bewijsdekking:
- Besluitadvies (accept/rework/escalate):
- Voorwaarden voor vervolg:

## Verwachte artefacten
- Rolmatrix
- Handoffs
- Stop- en escalatieregels

## Kwaliteitscheck
- Gebruik onderstaande rubric. Richtlijn: minimaal **voldoende** op alle criteria.

| Criterium | Onvoldoende | Voldoende | Goed | Voorbeeldig |
|---|---|---|---|---|
| Rolscherpte | Rollen overlappen onduidelijk | Rollen zijn onderscheidend | Rollen + verantwoordelijkheden expliciet | Rollen + verantwoordelijkheden + beslisgrenzen expliciet |
| Handoff-kwaliteit | Handoffs missen cruciale info | Handoffs bevatten verplichte velden | Handoffs ondersteunen overdraagbaarheid | Handoffs maken risico's en bewijs expliciet controleerbaar |
| Stopvoorwaarden | Geen concrete stopcriteria | Minimaal 2 concrete stopcriteria | Stopcriteria gekoppeld aan risico's | Stopcriteria + escalatiepad per risico expliciet |
| Escalatie-uitvoerbaarheid | Escalatie vaag | Escalatie trigger is benoemd | Escalatie trigger + eigenaar benoemd | Escalatie trigger + eigenaar + beslistermijn benoemd |

## Klaarcheck
Voer uit in de repository-root:

```bash
bash scripts/check.sh
```

**Verwachte uitkomst:**
- Het script eindigt succesvol (exit code `0`).
- Rolmatrix en 3 handoff-templates zijn ingevuld.
- Rubric scoort minimaal voldoende op alle criteria.

## Stop/escalatie
- Escaleer bij conflict tussen snelheid en controle.

## Reflectie
- Welke handoff voorkomt de meeste misverstanden?
