# Gogglew Shocker

BMEG 257 sleep-tracking device controller. Reads voltage from a biosensor, classifies sleep stages, and triggers a wake alarm when the subject enters light sleep (N1) during a configured time window.

---

## Project Structure

```
goggle-shocker/
├── main.py                  # Entry point — runs the monitoring loop
├── requirements.txt         # Python dependencies
├── core/
│   ├── models.py            # SleepReading dataclass and Person class
│   ├── data_processor.py    # Timing window check and signal cleaning
│   └── classifier.py        # Sleep stage classification logic
├── data/
│   └── stages.json          # Auto-generated log of readings (NDJSON format)
└── tests/
    ├── test_timing.py        # Tests for DataProcessor
    └── test_algorithm.py     # Tests for StageClassifier
```

### What each file does

| File | What you edit here |
|------|--------------------|
| `core/models.py` | Data structures — `SleepReading`, `Person` |
| `core/data_processor.py` | Wake-window timing logic, signal cleaning/DSP |
| `core/classifier.py` | Sleep stage classification algorithm |
| `main.py` | Wiring it all together, hardware loop |
| `tests/test_timing.py` | Tests for timing/window logic |
| `tests/test_algorithm.py` | Tests for classifier logic |

---

## Onboarding — Getting Started

### 1. Clone the repo

```bash
git clone <repo-url>
cd sleep-shocker
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate     # Mac/Linux
# .venv\Scripts\activate      # Windows
```

You only need to do this once. Every time you open a new terminal, run `source .venv/bin/activate` before working.


### 3. Run the main loop

```bash
python main.py
```

With the current stub values, it will detect an N1 stage immediately and print a wake message. `data/stages.json` will have one line written to it per loop iteration.

---

## Git Workflow — Keep It Simple

We're working directly on `main`. No branches. Here's how to stay out of trouble:

### Before you start working

Always pull first so you have the latest code:

```bash
git pull origin main
```

If you skip this and someone else pushed changes, you'll get a merge conflict. Just pull first.

### Before you push

```bash
git pull origin main        # pull again in case someone pushed while you worked
git add <your files>        # stage only what you changed (see table below)
git commit -m "short description of what you did"
git push origin main
```

### Who owns what

To avoid stepping on each other, try to stick to your area:

| Area | Files |
|------|-------|
| Data structures / Person logic | `core/models.py` |
| Timing and signal processing | `core/data_processor.py` |
| Classification algorithm | `core/classifier.py` |
| Main loop / hardware wiring | `main.py` |
| Tests | `tests/test_timing.py`, `tests/test_algorithm.py` |

If two people edit the same file at the same time, you'll get a merge conflict. Communicate with your group before touching a file someone else is actively working on.