from invoke import task


@task
def update_deps(c):
    """Pin all dependencies and upgrade environment."""
    c.run("pip-compile --upgrade")
    c.run(
        "pip-compile --upgrade --output-file dev-requirements.txt dev-requirements.in"
    )
    c.run("pip install --upgrade -r requirements.txt -r dev-requirements.txt")


@task
def run_server(c):
    """Start Uvicorn server with hot reloading on port 8000."""
    cmd = "uvicorn src.app:app --reload"
    c.run(cmd)


@task
def run_reorder_imports(c):
    """Run imports reordering."""
    c.run("reorder-python-imports --application-directories=.:src:tests")


@task
def run_black(c):
    """Run Black formatter."""
    c.run("black src/")
    c.run("black tests/")


@task
def run_flake8(c):
    """Run flake8."""
    c.run("flake8")


@task(run_reorder_imports, run_black, run_flake8)
def run_lint_format(c):
    """Run chained import reorder, black and flake8."""
    print("Done")
