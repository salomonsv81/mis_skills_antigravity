#!/usr/bin/env python3
import os
import argparse
import sys
from pathlib import Path

# Configuración de Rutas Base según documentación Antigravity
# Workspace Scope: .agent/skills/
# Global Scope: ~/.gemini/antigravity/skills/

def get_base_path(scope):
    if scope == 'global':
        # Expande ~ al directorio home del usuario
        return Path(os.path.expanduser("~/.gemini/antigravity/skills"))
    else:
        # Asume raíz del proyecto actual
        return Path(".agent/skills")

def create_skill_structure(name, description, scope):
    base_path = get_base_path(scope)
    skill_path = base_path / name

    # 1. Validación de existencia
    if skill_path.exists():
        print(f"ERROR: La skill '{name}' ya existe en {skill_path}.")
        sys.exit(1)

    try:
        # 2. Creación de directorios (Scaffolding)
        os.makedirs(skill_path, exist_ok=True)
        os.makedirs(skill_path / "scripts", exist_ok=True)
        os.makedirs(skill_path / "resources", exist_ok=True)
        os.makedirs(skill_path / "examples", exist_ok=True)

        # 3. Creación del SKILL.md Plantilla
        skill_md_content = f"""---
name: {name}
description: {description}
version: 0.1.0
created_by: skill-architect
---

# {name.replace('-', ' ').title()}

## Objetivo
{description}

## Instrucciones
1. 2. ## Restricciones de Seguridad
* No ejecutar sin validación de usuario.
* Respetar los archivos en .gitignore.

## Recursos
"""
        with open(skill_path / "SKILL.md", "w", encoding="utf-8") as f:
            f.write(skill_md_content)

        # 4. Creación de un script placeholder (opcional)
        with open(skill_path / "scripts" / "main.py", "w", encoding="utf-8") as f:
            f.write("#!/usr/bin/env python3\n# Placeholder script for logic\nprint('Hello from Antigravity')")

        print(f"SUCCESS: Skill '{name}' creada exitosamente en {skill_path}")
        print(f"PATH: {skill_path}")

    except Exception as e:
        print(f"ERROR: No se pudo crear la skill: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Antigravity Skill Builder')
    parser.add_argument('--name', required=True, help='Nombre de la skill (kebab-case)')
    parser.add_argument('--description', required=True, help='Descripción semántica para el router')
    parser.add_argument('--scope', choices=['local', 'global'], default='local', help='Scope de instalación')

    args = parser.parse_args()

    create_skill_structure(args.name, args.description, args.scope)