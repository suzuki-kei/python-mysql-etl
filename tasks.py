from invoke import task

@task
def run(context):
    """アプリケーションを実行する."""
    context.run("python src/main/python/application.py --config-dir=./config")

@task(name="test:unit")
def test(context):
    """単体テストを実行する."""
    context.run("python -m unittest discover -s src/test/python -t .")

