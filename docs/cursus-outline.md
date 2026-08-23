# Training — AI-ondersteunde softwareontwikkeling

## Gedetailleerde training outline (3 dagen)

**Klant:** 
**Doelgroep:** 12 ervaren softwareontwikkelaars
**Locatie:** In-company bij klant
**Tijd per dag:** 09:30–16:30 (ochtend les + middag oefenen)
**Lunch:** 12:30–13:15
**Voorbereiding per deelnemer:** maximaal 45 minuten (technische checklist + intake)
**Tools:** Visual Studio Code, GitHub Copilot, trainingsrepository met devcontainer

---

## Overkoepelende filosofie

De training combineert uitleg van principes met hands-on oefenblokken. Deelnemers werken in kleine teams aan afgebakende wijzigingen, gebruiken AI bij analyse en implementatie, en ronden iedere oefening af met verificatie en review.

Twee samenhangende concepten:

1. **Spec-Driven Development** — Hoe teams een wijziging eerst scherp beschrijven: doel, scope, acceptatiecriteria en grenzen. De mens definieert *wat*, de AI bepaalt *hoe*.
2. **Loop Engineering** — Hoe AI-ondersteunde ontwikkelstappen worden ingericht als een gecontroleerd proces van plannen, uitvoeren, verifiëren, reviewen en zo nodig bijsturen.

*Geen "vibe coding" — geen ad-hoc gebruik van AI zonder structuur. Wel bewuste, gestuurde samenwerking tussen menselijke domeinkennis en AI-executie.*

---

## Dagoverzicht

| Dag | Thema | Praktische opbrengst |
|-----|-------|---------------------|
| Dag 1 | Specificeren, context geven en gecontroleerd veranderen | Een kleine spec, een beperkte AI-ondersteunde wijziging en aantoonbaar test-/verificatiebewijs |
| Dag 2 | Een ontwikkellus ontwerpen en agents laten samenwerken | Een eenvoudige planner–implementer–reviewer-workflow met heldere rollen en reviewgate |
| Dag 3 | Kennis vastleggen, van wiki naar organisatiebrede semantische laag | Een eerste AI-kennisgraaf op basis van llm-wiki met structuur en semantische laag die 'agent ready' is |

---

### Dag 1 — Historie, specificeren, beveiligen en gecontroleerd veranderen (7 modules)

**Doel:** Deelnemers krijgen de historische context van genAI — hoe we van deep learning naar agents zijn gekomen — en verkennen de nieuwe arbeidsverdeling tussen ontwikkelaar en AI. Zij leren wanneer een korte vraag voldoende is en wanneer een expliciete specificatie nodig is.

### Ochtend (09:30–12:30) — Les

**1. Van Deep Learning tot Agents — Hoe we hier kwamen (09:30–10:15)**
- Fase 1: Deep Learning — de doorbraak van neurale netwerken (AlexNet, 2012)
- Fase 2: Embeddings — taal als vectoren (Word2Vec, GloVe, 2013–2018)
- Fase 3: Transformers — attention is all you need (Google, 2017)
- Fase 4: GPT/BERT — van text completion naar zero-shot redeneren (2018–2023)
- Fase 5: Schaalwet, GPT-4, en de LLM-explosie (2023)
- Fase 6: Instructie-tuning en alignment (RLHF → DPO/GRPO)
- Fase 7: Code-generatie als doorbraak (Copilot 2021, agents 2024–2026)
- Fase 8: Prompt engineering → agents → loop engineering → tool-ecosysteem (skills, MCP, A2A)
- Waar staan we nu? (2026) — wat werkt, wat nog niet, de nieuwe arbeidsverdeling

*(pauze 10:15–10:25)*

**2. Huidige AI-praktijk inventariseren (10:25–10:50)**
- Rondvraag: hoe gebruik je nu AI in je dagelijks werk?
- Wat werkt, wat niet, wat mis je?
- Huidige stack: IDE's, versiebeheer, CI/CD, AI-tools

**3. De nieuwe verdeling van werk (10:50–11:25)**
- Data: 80% van de code komt steeds vaker van AI (Anthropic, ~400K sessies)
- De echte skill is niet meer *coderen* maar *specificeren*
- Domeinkennis als voornaamste predictor van succes (niet codekunsten)
- **Spec-Driven Development als discipline**: de mens blijft baas over het "wat"
- Wanneer is een korte vraag voldoende vs. een expliciete spec?

*(pauze 11:25–11:35)*

**4. Spec-Driven Development in de praktijk (11:35–12:15)**
- Drie niveaus van SDD: Spec-First → Spec-Anchored → Spec-as-Source
- De vier fasen: Research → Specify → Clarify → Build
- Constitution: het persistente regelsdocument boven elke spec — met voorbeeld
- Echte voorbeelden: spec, constitution en verify-output

**5. Kaders: veiligheid en governance (12:15–12:30)**
- AI-Native SDLC security (Jason Clinton, Anthropic CISO)
- Governance gap: wat betekent het voor jouw organisatie?
- Werkafspraken: wat mag, wat moet, wat niet

### Lunch (12:30–13:15)

### Middag (13:15–16:30) — Oefenen (in teams)

**6. Lab 01: analyse naar spec (13:15–14:15)**
- Teams analyseren domein, code en tests en schrijven een beperkte spec.

**7. Lab 02: spec naar beperkte wijziging (14:15–15:15)**
- Teams vertalen spec naar een kleine wijziging met bewijs.

*(pauze 15:15–15:30)*

**8. Lab 03: bewijsgedreven review (15:30–16:00)**
- Teams reviewen op spec-conformiteit, risico en bewijs.

**9. Peer review en afsluiting (16:00–16:30)**
- Teams beoordelen niet alleen de code, maar ook de spec, gemaakte aannames en het bewijs dat de wijziging doet wat nodig is
- Bespreek: wat ging makkelijk, wat was lastig, hoe communiceer je beter met de agent?

---

## Dag 2 — Van losse sessie naar herhaalbare ontwikkellus

**Doel:** Deelnemers ontwerpen een kleine ontwikkellus waarin de agent niet zomaar "doorgaat", maar stopt op basis van bewijs of escaleert naar een mens.

### Ochtend (09:30–12:30) — Les

**1. Terugblik dag 1 (09:30–10:00)**
- Delen van ervaringen
- Gemene noemers: wat liep bij meerdere vast?

**2. Van losse iteraties naar systematische loops (10:00–11:00)**
- **Loop Engineering**: niet één keer AI gebruiken, maar systemen bouwen die AI-iteraties managen
- De 6-stappen core loop: Plan → Spec → Code → Test → Review → Ship
- Loop patterns en failure modes
- Wanneer stopt de agent? Wanneer escaleert naar de mens?

*(pauze 11:00–11:15)*

**3. Teamwerk met AI (11:15–12:00)**
- Team dynamics: hoe combineer je AI-assistants in teamomgevingen?
- Code review in het AI-tijdperk
- Werkafspraken voor AI-gebruik in duo's en teams
- Rollen en rechten per fasen van de loop

*(pauze 12:00–12:10)*

**3a. Context engineering en evals (12:10–12:30)**
- **Context engineering:** wat het model ziet is belangrijker dan wat jij typt — Anthropic-gidslijnen
- **Evals & CI-guardrails:** eval-driven development, vier lagen guardrails in de CI

### Lunch (12:30–13:15)

### Middag (13:15–16:30) — Oefenen (in teams)

**4. Lab 04: ontwerp de loop (13:15–14:15)**
- Teams ontwerpen rolmatrix, handoffs, stopvoorwaarden en escalatieregels.

**5. Lab 05: voer de loop uit (14:15–15:00)**
- Teams draaien planner-implementer-reviewer met evidence-based gates.

**6. Lab 06: loop tuning met metrics (15:00–15:45)**
- Teams vergelijken baseline en verbeterde cyclus op meetbare criteria.

**Optioneel (advanced): Lab 09 (verdieping)**
- Skill voor gestandaardiseerde handoffs bij teams die voorlopen.

*(pauze 15:45–16:00)*

**7. Afsluiting (16:00–16:30)**
- Groepsreflectie: wat werkt al, wat moet nog beter?

---

## Dag 3 — Van persoonlijke wiki naar enterprise semantische laag

**Doel:** Kennis dusdanig vastleggen dat een organisatiebrede kennisgraaf ontstaat die voor mens én agent werkt. Van llm-wiki als eerste stap naar het vergezicht op een enterprise semantische laag.

### Ochtend (09:30–12:30) — Les

**1. Terugblik dag 2 (09:30–10:00)**
- Delen van ervaringen uit de planner–implementer–reviewer-oefening
- Wat werkte goed in de driehoek?
- Waar ging kennis verloren tussen sessies?

**2. llm-wiki: gestructureerde kennis voor mens en agent (10:00–11:00)**
- **Het probleem:** kennis die in tickets, chats en PR's verdwijnt — niet vindbaar, niet herbruikbaar
- **Karpathy's llm-wiki patroon:** een compounding knowledge base als gelinkte markdown — kennis wordt één keer samengevat en blijft actueel
- Drie lagen: raw sources (immutable), wiki-paginas (concepten, entiteiten, vergelijkingen), schema (conventies)
- Wikilinks (`[[ ]]`), frontmatter, provenance markers — waarom die structuur agents én mensen helpt
- Cross-referencing als kernprincipe: elke pagina linkt minimaal naar twee andere pagina's
- **Live-demo:** een werkende llm-wiki (Hermes-agent eigen wiki) — ingesten van een bron, paginas aanmaken, cross-linken, queryn
- Verschil met RAG: RAG herontdekt kennis per query; een wiki compileert kennis één keer en houdt het bij

*(pauze 11:00–11:15)*

**3. Van wiki naar kennisgraaf: gbrain en het ecosystem (11:15–12:30)**
- **Waarna komt een llm-wiki?** — wanneer handmatig linken niet meer schaalbaar is
- **gbrain** (Garry Tan): self-wiring knowledge graph — auto-linking zonder LLM (pattern matching), hybride retrieval (vector + BM25), gesynthetiseerde antwoorden met bronvermelding
- Vergelijking van kennisgraaf-systemen:
  - Property graph / vector memory: Cognee, Mem0, LlamaIndex LPG, gbrain
  - RDF/SPARQL triple stores: Oxigraph, Jena Fuseki, GraphDB
  - Praktische conclusie: geen enkel opensource systeem dekt de hele cyclus — realistische architectuur combineert RDF-laag + aparte vectorstore + MCP-laag
- **"Dream cycle"** — achtergrond-processen die kennis verrijken, duplicaten samenvoegen, contradicties herkennen
- **Enterprise vergezicht (horizon — niet vandaag):** van team-wiki naar organisatiebrede semantische laag
  - Hoe schaal je van een projectwiki naar een enterprise knowledge graph?
  - Per-project wikis die cross-linken naar een centrale laag
  - Agents die kennis automatisch capteren uit code reviews, specs, en documentatie
  - De semantische laag als 'agent-ready' infrastructure: agents kunnen kennis zoeken, gebruiken en aanvullen zonder de mens

### Lunch (12:30–13:15)

### Middag (13:15–16:30) — Oefenen (in teams)

**4. Lab 07: LLMWiki starten (13:15–14:15)**
- Veilige start: scope, bronnen, taxonomie, governance en startnotitie.

**5. Lab 08: LLMWiki content toevoegen (14:15–15:15)**
- Content-intake met provenance, confidence en menselijke review.

*(pauze 15:15–15:30)*

**6. Hands-on: Organisatie AI-kennisgraaf bouwen (15:30–16:00)**
- Teams bouwen een eerste llm-wiki voor de organisatie — van schone lei
- Uitgangspunt: een set organisatie-bronnen (docs, architecturen, procesbeschrijvingen) — vooraf aangeleverd
- **Stap 1:** Raw sources ingesten — bronnen vastleggen met metadata en checksums
- **Stap 2:** Concepten en entiteiten uit de bronnen destilleren — AI helpt bij het scherpstellen
- **Stap 3:** Wikilinks leggen — de semantische connecties maken zichtbaar
- **Stap 4:** Schema definiëren — tag-taxonomie en conventies voor organisatie-specifieke context
- **Stap 5:** Queries — primair via beschikbare tooling, fallback via handmatige 3-vragen-oefening
- Focus: de mens curateert en beslist; AI samenvat, kruisverwijst en stelt voor

**7. Van wiki naar enterprise: het pilotexperiment (16:00–16:30)**
- Hoe zou deze pilot wiki opschalen naar de hele organisatie?
- Per team een wiki, cross-geklonken naar een centrale semantische laag — wat zijn de volgende stappen?
- Werkafspraken: welke conventies, tag-taxonomie en review-processen hanteer je organisatiebreed?
- **Voorstel voor één afgebakend pilotexperiment** — gecontroleerde ervaring met een live project voordat werkafspraken breder worden gestandaardiseerd

---

## Voorbereiding en randvoorwaarden

Om de trainingsdagen volledig aan leren en oefenen te besteden, regelen we vooraf:

- Een veilige, gesanitiseerde trainingsrepository en één afgebakende klant-oefencase
- GitHub- en GitHub Copilot-toegang voor alle deelnemers
- Een actuele installatie van Visual Studio (Code) en Git
- Akkoord voor gebruik van de trainingsrepository met devcontainer en Copilot CLI
- Een inhoudelijke contactpersoon voor domeinvragen en opvolging

Deelnemers ontvangen vooraf een korte technische checklist en intake. De totale voorbereiding per deelnemer bedraagt maximaal 45 minuten.

De lab-omgeving zal in de vorm van een dev-container-definitie beschikbaar worden gesteld door DIKW Academy.

Aanvullende Microsoft Learn-oefeningen kunnen optioneel als huiswerk worden ingezet.

---

## Concrete eindresultaten

Na de training beschikt de klant over:

1. **Twee reviewbare voorbeelden** van AI-ondersteunde wijzigingen, inclusief spec en verificatiebewijs
2. **Een eenvoudige workflow** voor planner, implementer en reviewer
3. **Een eerste concept voor een organisatie kennisgraaf**, AI-gedreven llm-wiki
4. **Een lijst** met kansrijke vervolgexperimenten, harde grenzen en open organisatievragen
5. **Een voorstel voor één afgebakend pilotexperiment**

---

## Tijdsinvestering totaal per deelnemer

| Onderdeel | Duur |
|-----------|------|
| Dag 1 (training) | 5 uur 45 min |
| Huiswerk / oefeningen | 2 uur |
| Dag 2 (training) | 5 uur 45 min |
| Huiswerk / oefeningen | 2 uur |
| Dag 3 (training) | 5 uur 45 min |
| Huiswerk / oefeningen | 2 uur |
| Voorbereiding (voor de training) | 45 min |
| **Totaal** | **~18 uur** |

---

## Bronnen & Referenties

**Microsoft Learn GitHub Copilot Exercises** (optioneel als huiswerk)
- https://microsoftlearning.github.io/mslearn-github-copilot-dev/
- LAB 01–03: aanvullende basisoefeningen
- LAB 15: aanvullende oefening custom agents/handoffs

**Kennisgrafen & Wiki**
- Karpathy: LLM Wiki patroon (compounding knowledge base)
- Garry Tan: gbrain — self-wiring knowledge graph (25.4k stars)
- Wiki-skill: llm-wiki (drie-lagen architectuur, cross-referencing, provenance)

**Wiki-concepten**
- Anthropic: *Agentic coding and persistent returns to expertise* (400K sessies analyse)
- Addy Osmani: Loop Engineering, Software Factories
- Panaversity: Spec-Driven Development Crash Course

