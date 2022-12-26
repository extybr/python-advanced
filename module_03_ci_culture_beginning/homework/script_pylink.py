import subprocess

if __name__ == "__main__":
    for i in range(1, 5):
        subprocess.call(f"pylint --recursive=y --output-format=json:file.json,colorized task_{i}",
                        shell=True)




