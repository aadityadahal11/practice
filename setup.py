from setuptools import setup, find_packages

setup(
    name="pimaker",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "opencv-python",          # Do NOT lock versions unless needed
        "mediapipe",
        "pygame",
        "pyautogui",
        "numpy",                  # remove version pin
        "pillow",
        "keras-facenet",
        "tensorflow",             # or "tensorflow-cpu" if you want lighter
        "scikit-learn",
        "pickle-mixin",
        "comtypes",
        "pycaw",
        "fer",
        "pyzbar"
    ],
    author="Aaditya Dahal",
    description="A collection of AI-powered computer vision tools",
    python_requires=">=3.10"
)