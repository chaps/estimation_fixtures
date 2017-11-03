from distutils.core import setup

setup(
    name="estimation_fixtures",
    version="0.1.0",
    author="Chaps",
    author_email="drumchaps@gmail.com",
    maintainer="Chaps",
    maintainer_email="drumchaps@gmail.com",
    url="https://github.org/drumchaps/estimation_fixtures",
    packages=[
        "estimation_fixtures",
    ],
    package_dir={'': 'src'},
    install_requires=["requests", "pytest", "nova-api"],
    dependency_links=[
        "git+https://github.com/chaps/nova_api.git/#egg=nova-api-0.1.0"
    ],
    entry_points = {
        "console_scripts": [
            "estimation_fixtures=estimation_fixtures.main:main"
        ]
    }
)
