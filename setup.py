import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get-music-lizhanqi",
    version="0.0.58",
    author="Example Author",
    author_email="3101978435@qq.com",
    description="可以下载音乐的包哦",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "tests"},
    packages=setuptools.find_packages(where="tests"),
    python_requires=">=3.0",
    install_requires=["requests"],
    entry_points={
        'console_scripts': ["get-music=get_music.get_music:main"
            ],
    },
)
