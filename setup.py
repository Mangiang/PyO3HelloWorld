import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    from setuptools_rust import Binding, RustExtension
except ImportError:
    import subprocess
    errno = subprocess.call(
        [sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import Binding, RustExtension


setuptools.setup(
    name="hello_world",
    version="0.0.1",
    author="Arthur Joly",
    author_email="mangiang@orange.fr",
    description="A small Hello World example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mangiang/PyO3HelloWorld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    rust_extensions=[
        RustExtension('hello_world.hello_world',
                      'Cargo.toml', binding=Binding.PyO3)
    ],
    zip_safe=False
)
