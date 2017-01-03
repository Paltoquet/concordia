from setuptools import setup, find_packages

setup(
	name                 = 'Concordia',
	version              = '1.0',
	description          = 'OCS Concordia project',
	author               = 'Team Concordia',
	url                  = 'http://www.tigli.fr/doku.php?id=cours:oc:gr10_16_17:gr10_16_17',
    install_requires     = ['Flask'],
	packages             = find_packages(),
    include_package_data = True,
    zip_safe             = False
)
