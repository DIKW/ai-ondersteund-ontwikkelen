# Labs-audit v0.2.1 — Middagprogramma AI-ondersteunde Softwareontwikkeling 

**Auditeur:** DIKW Academy (research-agent)
**Datum:** 23 augustus 2026
**Object:** GitHub-repo [DIKW/ai-ondersteund-ontwikkelen](https://github.com/DIKW/ai-ondersteund-ontwikkelen/tree/main) — 9 labs in `docs/labs/`, `knowledge-lab/`, `.github/agents/`, `specs/template/`, `.devcontainer/`, scripts, trainer-guide, learner-start.
**GitHub-snapshot:** laatste commit `d75957d` ("update labs", 23 aug 2026, 10:19 UTC) — alle 9 labs inhoudelijk gelezen na deze update.
**Doelgroep:** 12 ervaren softwareontwikkelaars, in teams van 2-3 (twee mensen + één AI-agent als junior developer).
**Scope:** didactische waarde van het middagprogramma (hands-on), afzonderlijk van de ochtendslides (zie `slides-audit-v0.2.1.md`).

> **Kort oordeel:** de labs zijn de **grootste winst van v0.2.1**. Waar in v0.1 de hands-on niet reviewbaar was en grotendeels was uitbesteed aan Microsoft Learn-huiswerk, is er nu een **geloofwaardige, reproduceerbare trainingsomgeving** met 9 labs, een devcontainer, agent-rolbestanden, governance-grenzen en sterke didactische patronen (baseline-vs-verbeterd met metrics, provenance, confidence-markering). Het resterende probleem: de labs zijn **skeletten** — geen uitgewerkte voorbeelden, geen model-oplossingen, geen scoringsrubrieken, geen herstelpaden. Ze zijn nu goed genoeg voor een ervaren trainer die ze live invult, maar nog niet zelfstandig genoeg voor multi-trainer- of zelfstandige cursusuitvoering.

---

## 1. Repo-inventaris

De GitHub-repo bevat (bevestigd via API):

```
.devcontainer/        Dockerfile, devcontainer.json, verify-environment.sh
.github/agents/      implementer.agent.md, planner.agent.md, reviewer.agent.md
.github/             copilot-instructions.md, pull_request_template.md
docs/labs/           lab-01 t/m lab-09 (zie §2)
docs/                domain.md, learner-start.md, trainer-guide.md, decisions/training-repository-scope.md (ADR)
knowledge-lab/       README, SCHEMA, WORKFLOW, index, log, raw/, concepts/, entities/, queries/
specs/template/      constitution.md, plan.md, spec.md, tasks.md
src/change_request_tracker/  cli.py, models.py, service.py, __init__.py
tests/               test_cli.py, test_service.py
scripts/             check.sh, run-demo.sh
AGENTS.md, README.md, LICENSE, pyproject.toml
```

Dit is een **echte, professionele trainingsrepo** — geen speelgoed. De aanwezigheid van een ADR (`training-repository-scope.md`), een PR-template, een `verify-environment.sh`, en gescheiden `learner-start`/`trainer-guide` toont volwassen repo-hygiëne.

---

## 2. De 9 labs

| Lab | Bestand | Doel | Tijd | Koppeling ochtend |
|---|---|---|---|---|
| 01 | `lab-01-analysis-to-spec.md` | businessbehoefte → beperkte spec + 3-5 acceptatiecriteria | 60-75 min | Dag 1 — SDD (1.3) |
| 02 | `lab-02-spec-to-change.md` | spec → kleine implementatie met bewijs + review | 60-75 min | Dag 1 — features & review (1.6) |
| 03 | `lab-03-evidence-driven-review.md` | review op bewijs (spec → code → test → review) | — | Dag 1/2 — review-gate |
| 04 | `lab-04-design-the-loop.md` | ontwerp planner-implementer-reviewer-lus (rolmatrix, handoffs, stopvoorwaarden) | 45-60 min | Dag 2 — loop engineering (2.2) |
| 05 | `lab-05-run-the-loop.md` | draai de lus met echte rollen + gecontroleerde handoffs | 60-75 min | Dag 2 — teamwork (2.3) |
| 06 | `lab-06-loop-tuning-with-metrics.md` | baseline vs. verbeterde cyclus met metrics | 45-60 min | Dag 2 — context/evals (2.3a) |
| 07 | `lab-07-llmwiki-start.md` | veilige start llm-wiki (grenzen, scope, bronselectie) | 45-60 min | Dag 3 — llm-wiki (3.2) |
| 08 | `lab-08-llmwiki-content-intake.md` | gecontroleerd content toevoegen met provenance + confidence | 60-75 min | Dag 3 — kennisgraaf (3.3/3.4) |
| 09 | `lab-09-skill-standardize-handoffs-optional.md` | (optioneel) handoffs standaardiseren als skill | — | Dag 2 — skills/loops |

Elk lab volgt een **consistente sjabloon**: Doel · Tijd · Startpunt · Stappen · Verwachte artefacten · Kwaliteitscheck · Stop/escalatie · Reflectie. Dat is didactisch goed steigerwerk.

---

## 3. Sterke punten (didactisch)

1. **Cognitieve progressie.** De labs bouwen logisch op: analyseren (01) → implementeren-met-bewijs (02) → reviewen (03) → ontwerpen (04) → draaien (05) → meten/verbeteren (06) → kennis vastleggen (07/08) → standaardiseren (09). Van observeren naar geleide oefening naar zelfstandige toepassing — precies de volgorde die didactisch hoort.
2. **Koppeling aan ochtendtheorie.** Lab 01/02 = SDD, 04/05/06 = loop engineering, 07/08 = llm-wiki/kennisgraaf. De mapping is schoon en sluit aan op de ochtendmodules.
3. **Sterk meetpatroon (lab 06).** "Draai een baseline, kies één verbetering, draai opnieuw, vergelijk met metrics, behoud/verwerp." Dit is dé kern van volwassen loop-engineering: verbeteren op basis van bewijs, niet op gevoel. Didactisch het sterkste lab.
4. **Provenance + confidence (lab 08).** Bronverwijzingen, tags uit vaste taxonomie, expliciete confidence-markering, en het zichtbaar maken (niet stilzwijgend oplossen) van onzekerheden en tegenstrijdigheden. Dit is precies hoe een echte llm-wiki hoort te werken en neemt de v0.1-kritiek "dag 3 is speculatief" weg.
5. **Governance ingebouwd in de labs.** Lab 07 controleert expliciet "geen productie- of klantdata", "geen externe ongeverifieerde bronnen", en kent escalatie bij bronkwaliteit-conflicten. Lab 08 vereist menselijke review op traceerbaarheid en governance. Hierdoor is de ochtend-security-module niet losse theorie maar wordt hij in de middag geoefend.
6. **Reproduceerbare omgeving.** Devcontainer met Dockerfile + `verify-environment.sh`, `AGENTS.md`, `copilot-instructions.md`, PR-template, ADR. Dit maakt de setup veel betrouwbaarder dan in v0.1; de daadwerkelijke opstarttijd per deelnemer heb ik niet live getest — adviseer een proefdraai vooraf om te bevestigen dat de build soepel verloopt.
7. **Rolbestanden voor de driehoek.** `.github/agents/implementer/planner/reviewer.agent.md` ondersteunen de planner-implementer-reviewer-oefening (lab 04/05) met echte, in te laden agent-rolbeschrijvingen.
8. **Resilience.** `trainer-guide.md` bevat een fallback "zonder Copilot CLI" (deelnemers schrijven spec/plan/review handmatig in markdown) en een dag-3-bronpakket-instructie. De training valt niet om als een tool ontbreekt.
9. **Append-only log + index.** `knowledge-lab/log.md` (append-only) en `index.md` dwingen traceerbaarheid af — een echt werkpatroon, geen speeltuin.

---

## 4. Zwakke punten (didactisch)

1. **Labs zijn skeletten.** Elk lab is ~20-30 regels: 5-7 algemene stappen, één-regel-kwaliteitscheck, één reflectievraag. Er zijn **geen uitgewerkte voorbeelden, geen startcode-snippets, geen model-oplossing/branch, geen verwachte diff, geen tijdgebakken sub-taken, geen troubleshooting/herstelpad, geen scoringsrubriek**. Voor ervaren devs laat "Schrijf een beperkte spec" zonder voorbeeldantwoord het successubjectief.
2. **Geen model-oplossingen / referentie-implementaties.** Een trainingsrepo voor zelfstandig of multi-trainer-gebruik heeft model-antwoorden nodig (bijv. een `solutions/`-branch of ingevulde `specs/examples/`). Nu zijn er alleen blanco templates (`specs/template/*`). Een deelnemer of trainer kan niet zelf-checken of kalibreren.
3. **Geen programmatische "klaar"-controle.** `scripts/check.sh` en `verify-environment.sh` bestaan, maar de labs verwijzen er niet naar als "zo bevestig je dat je klaar bent". De labs zeggen alleen "draai tests" zonder vast te leggen welke test-output "voldoende" is.
4. **Tijdsrealiteit middag.** Dag 1-middag is 13:15-16:30 (~3u15). Lab 01+02 = 2-2,5u. De outline noemt óók "Microsoft Learn LAB 01-03" in dezelfde middag — dat past niet. De README stelt dat MS Learn "huiswerk" is, maar de outline plaatst LAB 01-03 nog in de dag-1-middag. **Conflict tussen outline en README.**
5. **Lab-nummering vs slides mismatch.** Slides/README noemen huiswerk "LAB_AKA_03/14/15" (Microsoft) en een "5 eigen labs"-tabel; de repo heeft 9 eigen labs (`lab-01`..`lab-09`). Er is **geen mapping** van slide-module (1.5, 1.6, 2.4, 2.5, 3.4) naar repo-labbestand. Een deelnemer die module 1.5 "Hands-on: eerste Copilot-stappen" leest, weet niet dat dit repo-lab 01/02 is.
6. **Dag-3 "queryn" is optimistisch.** Lab 08 stelt "stel elkaars wiki vragen en test of de kennis bruikbaar is" — maar `knowledge-lab/queries/README.md` bevat slechts de placeholder "Plaats hier voorbeeldvragen die met de wiki beantwoord kunnen worden"; er is geen query/agent-tool meegeleverd. Het "queryn" veronderstelt mogelijkheden die niet worden aangeleverd. Met alleen markdown is dit in 2 uur niet haalbaar zonder een (al dan niet AI-gestuurde) query-tool of een expliciete terugval naar "schrijf 3 vragen op".
7. **Geen scoringsrubriek.** "Kwaliteitscheck" is één zin ("Scope is klein en toetsbaar"). Er is geen rubriek waarmee een trainer objectief scoort "is dit een goede spec/loop/wiki". Dit blijft een v0.1-should-fix.
8. **Geen voorbeeld van een falende loop.** Lab 06 meet verbetering, maar er is geen lab waarin deelnemers een **bewust kapotte** loop (thrashing, doom loop, context drift) diagnosticeren — terwijl dat de meest leerzame ervaring is voor herkenning van failure modes uit de ochtend.

---

## 5. Beoordeling per lab langs didactische criteria

| Lab | Setup-betrouwbaarheid | Instructiehelderheid | Progressie | Theorie-koppeling | Verificatie | Tijdsrealisme |
|---|---|---|---|---|---|---|
| 01 | ✅ devcontainer | ⚠️ skelet | ✅ analyse→spec | ✅ SDD | ⚠️ geen rubriek | ✅ |
| 02 | ✅ | ⚠️ skelet | ✅ spec→change | ✅ review | ⚠️ geen modeloplossing | ✅ |
| 03 | ✅ | ⚠️ skelet | ✅ bewijs-review | ✅ review-gate | ⚠️ | ⚠️ tijd onbekend |
| 04 | ✅ | ⚠️ skelet | ✅ ontwerpen | ✅ loop eng. | ⚠️ | ✅ |
| 05 | ✅ + agent-rollen | ⚠️ skelet | ✅ draaien | ✅ teamwork | ⚠️ | ✅ |
| 06 | ✅ | ✅ sterk patroon | ✅ meten/verbeteren | ✅ evals | ✅ metrics | ✅ |
| 07 | ✅ | ✅ governance | ✅ veilige start | ✅ llm-wiki | ⚠️ | ✅ |
| 08 | ✅ | ✅ provenance | ✅ content-intake | ✅ kennisgraaf | ✅ review | ⚠️ queryn optimistisch |
| 09 | ✅ | ⚠️ optioneel | ✅ standaardiseren | ✅ skills | ⚠️ | optioneel |

---

## 6. AI-risico's en governance in de labs

- **Positief:** lab 07 dwingt grenzen af (geen klantdata, geen ongeverifieerde bronnen); lab 08 markeert confidence en vereist menselijke review op traceerbaarheid. De ochtend-security-module wordt in de middag geoefend.
- **Gat:** geen lab behandelt **prompt-injectie als praktijk** — bijv. een README of issue-body met een verborgen instructie die de agent moet herkennen en weigeren. Terwijl dit dé threat is die in de ochtend (module 04) wordt benoemd, blijft het in de labs ongeoefend. Aanbeveling: voeg een "rode-team"-mini-lab toe waarin een indirecte-injectie in `raw/` zit die de agent moet tegenhouden.

---

## 7. Conclusie en prioriteiten

**De labs zijn van "niet reviewbaar" (v0.1) geëvolueerd naar een geloofwaardige, goed gestructureerde, governance-bewuste set van 9 labs met sterke didactische patronen.** Dit is de belangrijkste verbetering van v0.2.1 en verdient erkenning.

**De volgende stap is "vlees op het skelet":** uitgewerkte voorbeelden, model-oplossingen, scoringsrubrieken, herstelpaden, en een mapping-tabel van slide-module naar labbestand. Zonder die stap blijven de labs afhankelijk van een trainer die alles live invult — goed voor één sterke trainer, niet schaalbaar.

### Must fix (labs)
1. **Mapping-tabel** slide-module (1.5, 1.6, 2.4, 2.5, 3.4) → repo-labbestand; synchroniseer README "5 labs" met de 9 labs.
2. **Conflict outline vs README**: haal "Microsoft Learn LAB 01-03" uit de dag-1-middag (het is huiswerk volgens README) — maak outline en README consistent.
3. **Model-oplossingen**: voeg een `solutions/`-branch of ingevulde `specs/examples/` toe zodat deelnemers/trainers kunnen zelf-checken en kalibreren.
4. **Scoringsrubriek** per lab: wat maakt een spec/loop/wiki "voldoende" / "goed" / "voorbeeldig" — meetbaar en objectief.

### Should fix (labs)
5. **Programmatische "klaar"-check**: koppel elk lab aan een `scripts/check.sh`-stap met verwachte output (groene tests + spec-check), zodat "klaar" objectief vaststelbaar is.
6. **Dag-3 "queryn" realistisch maken**: lever een minimale query/agent-tool bij `knowledge-lab/` (of degradeer de stap expliciet naar "schrijf 3 vragen op die je later zou stellen").
7. **Rode-team mini-lab** voor indirecte prompt-injectie (sluit aan bij ochtend-module 04).
8. **Voorbeeld van een falende loop** (thrashing/doom-loop diagnosticeren) — sluit aan bij failure-modes uit ochtend 2.2.
9. **Tijdschattingen** compleet maken (lab 03 ontbreekt) en per lab een time-box per sub-stap.

### Nice to have (labs)
10. Een "trainer-answer-key" naast elke `trainer-guide.md` met verwachte artefacten per lab.
11. Een `CHANGELOG` en lab-versienummers zodat wijzigingen (zoals de recente uitbreiding 4→9 labs) traceerbaar zijn.

---

## 8. Onderzoeksbasis

- [GitHub-repo DIKW/ai-ondersteund-ontwikkelen](https://github.com/DIKW/ai-ondersteund-ontwikkelen/tree/main) — lab-bestanden, devcontainer, agents, knowledge-lab, scripts (direct ingelezen via raw + API).
- [Anthropic — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — didactisch referentiekader voor context/evals (lab 06).
- [OWASP — Secure Coding with AI Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html) — referentie voor het aanbevolen rode-team prompt-injectie-lab.

*Zie ook:* `slides-audit-v0.2.1.md` — analyse van de ochtendslides en de koppeling naar deze labs.
