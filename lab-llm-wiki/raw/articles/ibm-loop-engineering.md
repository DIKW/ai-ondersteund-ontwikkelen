---
source_url: https://www.ibm.com/think/topics/loop-engineering
ingested: 2026-09-18
sha256: a1d5a2825503be54867911c116a0785d574f2a02afc4023367c389ed9458b139
---

# What is loop engineering?

Bron: IBM Think. Gepubliceerd op 17 juli 2026. Auteurs: Ivan Belcic en Cole Stryker.

## Definitie

Loop engineering is het ontwerpen van agentic workflows die AI-agents iteratief naar een gebruikersdoel leiden met minimale menselijke interventie. In plaats van bij iedere stap handmatig te prompten, kan een agent dynamisch handelen, observeren, beslissen en itereren. De ontwikkelaar ontwerpt daarmee het systeem dat agents prompt, controleert en stuurt.

## Verschil met prompt engineering

Prompt engineering optimaliseert een afzonderlijke instructie. Loop engineering ontwerpt geautomatiseerde systemen die zichzelf prompten en hun werk evalueren. Prompt chains volgen een rigide structuur; loops zijn dynamischer. Loops passen beter bij langlopende agents voor softwareontwikkeling, onderhoud en meerstapstaken.

## Agentic loop stages

IBM beschrijft vier fasen:

1. Goal: een specifiek, toetsbaar doel met duidelijke stopcriteria wordt bij iedere iteratie geëvalueerd.
2. Action: de agent handelt op basis van doel en voortgang, bijvoorbeeld door code te genereren of tests uit te voeren.
3. Observation: het systeem beoordeelt het resultaat, bijvoorbeeld met CI-tests.
4. Adjustment: feedback wordt gebruikt om de aanpak aan te passen voordat de loop opnieuw start.

## Componenten

Een goed ontworpen loop kan bestaan uit automatisering of scheduling, hooks, context engineering, tooltoegang, worktrees, skills, subagents en een spine. Automatisering bepaalt wanneer een loop start. Hooks kunnen kwaliteits- en beveiligingscontroles voor of na gebeurtenissen uitvoeren. Context engineering beperkt context tot relevante informatie. Tools geven toegang tot code, bestanden, terminals, databases en tests. Worktrees isoleren parallel werk. Skills bevatten kennis voor een terugkerende taak. Subagents kunnen gespecialiseerde taken of onafhankelijke verificatie uitvoeren. De spine bewaart persistente toestand en voorkomt dat fouten of context verloren gaan.

## Menselijke betrokkenheid

IBM benadrukt dat ook robuuste loops menselijke betrokkenheid nodig hebben. Een checker-agent blijft een agent; mensen blijven verantwoordelijk voor code, security, compliance en bedrijfsuitkomsten. Zonder begrip en toezicht kunnen ongeteste code, comprehension debt, intent debt en cognitive surrender ontstaan.
