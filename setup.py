import os

from setuptools import find_packages, setup


setup(
    name="django-manage-admins",
    zip_safe=False,  # eggs are the devil.
    version="0.1.0",
    description="Manage admin users",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    author="Anders Pearson",
    author_email="anders@appsembler.com",
    url="https://github.com/appsembler/django-manage-admins",
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    python_requires=">=3.5",
    install_requires=["Django>=2.0"],
)
