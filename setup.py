from setuptools import setup, find_packages

setup(
    name='desinty_bot',
    version='0.0.1',
    description='Set of commands that scrape destinytracker.com for info.',
    author='Nolan Brubaker',
    author_email='palendae@gmail.com',
    packages=find_package(),
    py_modules=['destiny_bot'],
    include_package_data=True,
    zip_safe=True,
    entry_points = dict(
        helga_plugins=[
            'nightfall = destiny_bot:nightfall',
            'heroic = destiny_bot:heroic',
        ]
    )
)
