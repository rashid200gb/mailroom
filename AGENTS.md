# AGENTS.md — mailroom-live

Read this whole file before doing anything in this repository. It applies to every AI coding
agent (Claude Code, Codex, Cursor, Copilot, etc.).

## 1. What this project is

- **Name:** `mailroom-live`
- **Owner / learner:** Rashid Mahmood Sajid (comfortable in English and Urdu).
- **Purpose:** a *learning* project. We are learning programming fundamentals by building it,
  following **Chapter 13 — Programming Fundamentals in the AI Era** of *The AI Agent Factory*
  (Panaversity): https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/
- **Language:** Python only (the book also shows TypeScript; ignore it here).
- **What the app does:** not decided yet. The learner will describe each feature. Do not invent
  features or "helpful" extras — build only what is asked.

The goal is that **the learner understands every line**, not that the code gets written fast.

## 2. Where the learner is in the course

Covered so far: **up to and including lesson 13.7.**

| Lesson | Topic | Status |
|---|---|---|
| 13.1 | You read, the agent writes | ✅ covered |
| 13.2 | The workbench (uv, Python, Pyright) | ✅ covered |
| 13.3 | Values, types and variables | ✅ covered |
| 13.4 | Decisions and repetition (`if`/`elif`/`else`, `for`) | ✅ covered |
| 13.5 | Two conditions (`and`/`or`/`not`), empty values (`None`, `""`, `[]`), `while` loops | ✅ covered |
| 13.6 | Functions: the signature is the contract (type-labelled params and return) | ✅ covered |
| 13.7 | Lists and dictionaries (`list[...]`, `dict[str, ...]`, records, `.get()`, `len()`, indexing from 0, `KeyError`/`IndexError`, `sorted()` with `key=` and `reverse=True`) | ✅ covered |
| 13.8 | Text from a file | ⏳ not yet |
| 13.9 | Dates | ⏳ not yet |
| 13.10 | When it breaks: reading an error | ⏳ not yet |
| 13.11 | Tests first: the TDG loop (pytest) | ⏳ not yet |
| 13.12 | Judgment | ⏳ not yet |
| 13.13 | How today's tools realize it | ⏳ not yet |
| Lab 13 | Choices that last (adds ruff) | ⏳ not yet |

**Update this table** (and the line above it) whenever the learner says they have finished a
new lesson, and commit that change.

### Allowed concepts (use freely)

- Values and types: `int`, `float`, `str`, `bool`, `None`; variables with type labels
  (`total: float = 0.0`).
- f-strings and `print()`.
- `if` / `elif` / `else`; comparison operators; `and`, `or`, `not`.
- `for` loops over lists / dict items; `range()`; `while` loops.
- Functions with **full type labels** on every parameter and return (`def f(x: int) -> str:`).
- `list[T]`, `dict[K, V]`, a dict used as a record (`inv["status"]`), `.get()`, `len()`,
  indexing, `.append()`, `sorted(..., key=..., reverse=True)`.
- `uv run`, `uv run pyright`.

### Not yet taught — do NOT use without teaching first

File reading/writing, `open()`, CSV/JSON modules, `datetime`, `try`/`except` and raising errors,
pytest and test files, classes, `@dataclass`, `TypedDict`, `Enum`, comprehensions
(list/dict/set), `lambda` (except a tiny `key=` in `sorted()` *after explaining it*), generators,
decorators, `async`, third-party libraries, `import` of anything beyond what is already in the repo.

## 3. The teaching rule (most important)

**If a task needs a concept that is not in the "Allowed" list, STOP and teach it first.**

1. Say plainly: "This needs a new concept: **X** (it's lesson 13.N in the book)" — or say it is
   outside Chapter 13.
2. Teach it with **PRIMM-AI+** (section 4) using a tiny standalone example, *not* the project code.
3. Only after the learner says they understand, use it in the project.
4. Prefer a solution that uses only allowed concepts whenever one exists, even if it is longer.

Never slip a new concept into a large diff where the learner might not notice it.

## 4. How we learn: PRIMM-AI+

Every new piece of code goes through these five steps. The agent is a partner at each one.

| Step | Learner does | Agent does |
|---|---|---|
| **Predict** | Guesses what the code will print / return before it runs. | Shows the code, asks for a prediction, **stays quiet** — does not give the answer. |
| **Run** | Runs it (`uv run ...`) and sees the real output. | Runs it or tells the learner the exact command. |
| **Investigate** | Compares the guess with the real output, asks why. | Explains line by line *on request*; answers "what would break this?" |
| **Modify** | Changes one thing, predicts again, runs again. | Makes exactly the edit the learner describes — nothing more. |
| **Make** | Writes a spec for their own version. | Builds it to that spec; the learner verifies it. |

AI+ rules: the agent is always available as a reading partner, and **nothing is accepted on
faith** — every claim is checked by running the code (and, from 13.11 on, by tests).

## 5. How to work in this repo

- **Small steps.** One small feature per change. Keep functions short.
- **Explain before you write** anything non-trivial: say what you plan and why, then wait for a "go".
- **Plain language.** Avoid jargon; when a term is needed, define it in one line. Urdu
  explanations are welcome if the learner asks.
- **Show the commands** you run so the learner can repeat them.
- After every code change run:
  ```bash
  uv run mailroom-live   # it still runs
  uv run pyright         # strict mode must report 0 errors
  ```
- Name the *choices* (rules) in the code clearly — e.g. what counts as "late" — so they can be
  read and questioned. Rules belong in clearly named variables or functions, not hidden inside
  long expressions.
- Do not add dependencies, config, CI, or tools without asking.
- Commit only when the learner asks. Use short, clear commit messages.

## 6. Workbench

- **Python:** 3.15 (pinned in `.python-version`; `requires-python = ">=3.15"`).
- **Package/project manager:** [uv](https://docs.astral.sh/uv/). Never use `pip` directly.
- **Type checker:** Pyright in **strict** mode (configured in `pyproject.toml` under
  `[tool.pyright]`). Every function needs type labels; a missing label is an error.
- **Linter:** none yet (ruff arrives in Lab 13). **Tests:** none yet (pytest arrives in 13.11).

Common commands:

```bash
uv sync                    # create .venv and install dev tools
uv run mailroom-live       # run the app (calls main() in src/mailroom_live/__init__.py)
uv run python path/to/file.py
uv run pyright             # type-check
uv add <package>           # ONLY with the learner's permission
```

## 7. Project layout

```
mailroom-live/
├── AGENTS.md              # this file
├── README.md
├── pyproject.toml         # project metadata, dev deps, pyright config
├── .python-version        # 3.15
├── uv.lock                # locked dependencies (commit it)
└── src/
    └── mailroom_live/
        └── __init__.py    # main() entry point
```

## 8. Repository

- GitHub: `mailroom-live`, default branch `main`.
- Do not commit `.venv/`, `__pycache__/`, secrets, or `.env` files.
