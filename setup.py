from setuptools import setup, find_packages

setup(
    name='destiny_bot',
    version='0.0.2',
    description='Set of commands that scrape destinytracker.com for info.',
    author='Nolan Brubaker',
    author_email='palendae@gmail.com',
    packages=find_packages(),
    py_modules=['destiny_bot', 'scraper'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'beautifulsoup4==4.3.2',
        'requests==2.2.1',
        'helga==1.6.3',
    ],
    entry_points = dict(
        helga_plugins=[
            'nightfall = destiny_bot:nightfall',
            'heroic = destiny_bot:heroic',
        ]
    )
)
