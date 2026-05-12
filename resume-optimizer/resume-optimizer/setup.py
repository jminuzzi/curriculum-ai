from setuptools import find_packages, setup


setup(
    name='resume-optimizer',
    version='1.0.0',
    description='Ferramenta para upload, análise e otimização de currículos.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi>=0.115.12',
        'uvicorn[standard]>=0.34.0',
        'python-multipart>=0.0.20',
        'pydantic>=2.11.2',
        'pydantic-settings>=2.8.1',
        'PyMuPDF>=1.25.5',
        'streamlit>=1.44.1',
        'requests>=2.32.3',
    ],
)
