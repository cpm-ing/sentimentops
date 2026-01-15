from pathlib import Path
import mlflow

def main() -> None:
    mlflow.set_experiment("hello-mlflow")

    artifact_dir = Path("artifacts/hello")
    artifact_dir.mkdir(parents=True, exist_ok=True)

    artifact_file = artifact_dir / "hello.txt"
    artifact_file.write_text("hello mlflow\n", encoding="utf-8")

    with mlflow.start_run(run_name="hello-run") as run:
        mlflow.log_param("w1", "mlflow_hello")
        mlflow.log_metric("hello_metric", 1.0)
        mlflow.log_artifact(str(artifact_file))
        print("run_id:", run.info.run_id)

if __name__ == "__main__":
    main()
