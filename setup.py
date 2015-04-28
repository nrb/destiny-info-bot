from setuptools import setup, find_packages

setup(
    name='destiny_bot',
    version='0.0.17',
    description='Set of commands that scrape destinytracker.com for info.',
    author='Nolan Brubaker',
    author_email='palendae@gmail.com',
    packages=find_packages(),
    py_modules=[
        'caching',
        'check',
        'destiny_bot',
        'scraper',
        'functions'
    ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'beautifulsoup4==4.3.2',
        'requests==2.2.1',
        'helga',
        'pytz',
    ],
    entry_points = dict(
        helga_plugins=[
            'nightfall = destiny_bot:nightfall',
            'heroic = destiny_bot:heroic',
            'daily = destiny_bot:daily',
            'crucible = destiny_bot:crucible',
            'xur = destiny_bot:xur',
            'bounties = destiny_bot:bounties',
        ]
    )
)
