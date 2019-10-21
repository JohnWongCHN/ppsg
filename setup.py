from setuptools import setup, find_packages

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='ppsg',
    version='0.0.2',
    description='A Python Project Structure Generator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='John Wong',
    author_email='john-wong@outlook.com',
    url='',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=['ez_setup', 'tests*']), # 不包括哪些Package
    package_data={'ppsg': ['templates/*']}, # 包括相关文件
    include_package_data=True,
    install_requires=[
        'Click',
        'Jinja2'
    ],
    # 添加命令行入口
    entry_points="""
        [console_scripts]
        ppsg = ppsg.ppsg:main
    """,
)