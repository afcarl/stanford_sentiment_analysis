import setuptools

setuptools.setup(author="Kazi Nazmul Haue",
                 author_email="shezan.huq@gmail.com",
                 name="stanford_sentiment",
                 description="stanford sentiment analysis",
                 version="1",
                 packages=setuptools.find_packages(),
                 package_data={'': ['*.txt', '*.md']},
                 install_requires=[],
                 license="DataRobin",
                 platforms=['Linux']
                 )
