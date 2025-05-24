from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Mateo Espinal",
    author_email="mateo.espinal@est.iudigital.edu.co",
    description="ETL para análisis de datos de una libreria",
    py_modules=["actividad1", "actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"
    ]
)
