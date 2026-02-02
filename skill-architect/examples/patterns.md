# Ejemplos de Skills Generadas

## 1. Data Utility (Scope: Global)
**Requerimiento:** "Haz una skill para convertir CSVs a JSON rápidamente."
**Resultado:** `~/.gemini/antigravity/skills/csv-to-json/SKILL.md`
* Scripts: `scripts/convert.py`

## 2. DevOps Automation (Scope: Workspace)
**Requerimiento:** "Quiero una skill que verifique si mis contenedores de docker están sanos antes de hacer commit."
**Resultado:** `.agent/skills/health-check-precommit/SKILL.md`
* Acción: Ejecutar `docker ps` y `curl localhost:8080/health`.

## 3. Integration / MCP (Scope: Local)
**Requerimiento:** "Crea una skill que cree tickets en Jira cuando encuentre un comentario TODO en el código."
**Resultado:** `.agent/skills/todo-to-jira/SKILL.md`
* Acción MCP: Usar `jira.create_issue`.