# Backend FastAPI

## Development

#### Install in conda environment

```
conda create -n fastapi-vue-crud python=3.7
conda activate fastapi-vue-crud
pip install -r requirements.txt -r dev-requirements.txt
```

#### Invoke tasks

```
invoke -l
Available tasks:

  run-black             Run Black formatter.
  run-flake8            Run flake8.
  run-lint-format       Run chained import reorder, black and flake8.
  run-reorder-imports   Run imports reordering.
  run-server            Start Uvicorn server with hot reloading on port 8000.
  update-deps           Pin all dependencies and upgrade environment.
```

#### Run tests

PyCharm : Right-click the `server/tests` folder and hit `Run 'pytest' in tests`.

## Run

```
invoke run_server
```
