import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get-music-lizhanqi",
    version="1.0.6",
    author="Li Zhan Qi",
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
    python_requires=">=3.7",
    install_requires=["requests",'rich','lxml'],
    entry_points={
        'console_scripts': ["get-music=get_music.get_music:main",
                            "get-music-lizhanqi=get_music.get_music:main"
            ],
    },
)
