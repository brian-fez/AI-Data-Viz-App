### docker_executor.py
import tempfile
import subprocess
from typing import Optional, List

def code_interpret_docker(code: str, dataset_path: str, error_handler) -> Optional[List[str]]:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as code_file:
        full_code = f"""
dataset_path = '/data/dataset.csv'

{code}
"""
        code_file.write(full_code)
        code_file.flush()

        try:
            result = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-v", f"{dataset_path}:/data/dataset.csv:ro",
                    "-v", f"{code_file.name}:/app/code.py:ro",
                    "python-sandbox",
                    "python", "/app/code.py"
                ],
                capture_output=True,
                text=True,
                timeout=30,
            )
        except Exception as e:
            error_handler(str(e))
            return None

        if result.returncode != 0:
            error_handler(result.stderr)
            return None

        error_handler("")  # Clear last error
        return [result.stdout.strip()]