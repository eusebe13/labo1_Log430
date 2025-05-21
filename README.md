# labo1_Log430
# Gestionnaire de ventes - Application distribuée en console

## 🔧 Exécution avec Docker

```bash
docker-compose build
docker-compose up
```
---

## 📚 `docs/README.md`

```markdown```
# Documentation technique

## 🔧 Instructions

- `docker-compose up` démarre l’application.
- Les tests unitaires peuvent être exécutés (à implémenter) via `pytest`.

## 📌 Choix technologiques

| Outil        | Justification                           |
|--------------|------------------------------------------|
| SQLAlchemy   | ORM robuste et mature                    |
| PostgreSQL   | SGBD fiable pour la persistance          |
| Docker       | Exécution isolée, indépendante du poste  |

## 📂 Dossiers

- `ADR/` : décisions d’architecture
- `UML/` : diagrammes illustrant la conception

### Analyse statique (Linting)

Ce projet utilise [ruff](https://docs.astral.sh/ruff/) pour faire de l’analyse statique de code Python :

```bash
ruff check .
ruff check . --fix
```

---

### ✅ 4. **(Optionnel) Ajouter un script Makefile**

Créer un fichier `Makefile` avec une commande pratique :

```makefile
lint:
	ruff check .

lint-fix:
	ruff check . --fix
