from setuptools import find_packages, setup

test_deps = ["pytest==6.2.5"]

dev_deps = ["flake8==4.0.", "flake8-bugbear==21.9.2", "black==21.10b0", "mypy==0.910"]

doc_deps = ["pdoc==8.0.1"]

setup(
    name="spectrumdevice",
    package_data={"spectrumdevice": ["py.typed"]},
    packages=find_packages(exclude=['tests']),
    version=0.1,
    include_package_data=True,
    install_requires=[
        "numpy==1.21.4",
        "matplotlib==3.5.0"
    ],
    extras_require={
        "dev": dev_deps,
        "test": test_deps,
        "doc": doc_deps
    }
)
