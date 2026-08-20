# Ontwerpbesluit: trainingsrepository-scope

## Beslissingen
- Kleine Python-standaardbibliotheekapplicatie in een devcontainer.
- GitHub Copilot CLI als primaire agentinterface.
- Geen Spec Kit CLI, plugins, externe catalogi of MCP-servers.
- Platformneutrale Markdown-artefacten voor GitHub en Azure DevOps.
- LLMWiki als voorbereid Markdown-concept, niet als live bedrijfsimplementatie.

## Gevolgen en beperkingen
- Focus op leerbaarheid en bewijs, niet op productierealisme.
- Geen externe runtime-dependencies.
- Geen integraties met cloud, databases of externe API's.

## Expliciet niet doen
- Geen secrets/tokens/credentials
- Geen release/deploymentautomatisering
- Geen knowledge graph of RAG-pipeline

## Container image-opmerking
Er is een vaste major/minor Python-image gebruikt. Voor productiegebruik moet deze nog op een immutable digest worden vastgepind.
