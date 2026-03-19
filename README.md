# AI Platform Starter Kit

AI Platform Starter Kit is a reusable foundation for shipping AI applications with a cleaner delivery baseline: project structure, Streamlit demo surface, FastAPI service scaffold, CI, Docker, documentation, and operating artifacts. It is designed for portfolio projects, internal prototypes, and early production-facing AI systems that need more rigor than a notebook but less ceremony than a full platform build.

## What it includes

- Streamlit app entrypoint for lightweight demos
- FastAPI service scaffold for API delivery
- `src/` package layout for application logic
- `scripts/` for training, evaluation, or setup tasks
- `tests/` for fast validation
- Dockerfile, CI workflow, and lint/test hooks
- Product, architecture, evaluation, risk, launch, and runbook docs

## Why it exists

Most AI demos look fine in isolation but fall apart when asked to show delivery discipline. This starter kit gives a repeatable structure for turning an idea into something portfolio-ready: runnable, testable, documented, and easier to extend.

## Quickstart

```bash
pip install -r requirements.txt
make serve
```

Optional commands:

```bash
make lint
make test
make train
make eval
make api
```

## Recommended use

- Clone the repo as the starting point for a new AI project
- Replace the sample app, model, and scripts with project-specific logic
- Keep the docs set and operating structure, then tailor them to the use case
- Add a live demo and artifact links once the project is complete

## Included docs

- `docs/00_product_brief.md`
- `docs/01_prd_lite.md`
- `docs/02_architecture.md`
- `docs/03_evaluation_report.md`
- `docs/04_model_card.md`
- `docs/05_risk_register.md`
- `docs/06_launch_plan.md`
- `docs/07_runbook.md`
