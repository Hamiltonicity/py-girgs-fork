import subprocess

def build():
    print("Running build.py ...")
    subprocess.check_call(["make", "build"])


if __name__ == "__main__":
    build()
