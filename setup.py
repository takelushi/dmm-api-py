"""Setup for packing."""

import setuptools

version = '0.1.0'
package = 'dmm_api'


def get_requires_from_file(filename):
    return open(filename, 'r', encoding='UTF-8').read().splitlines()


requirements_path = 'requirements.txt'

readme_path = 'README.md'
with open(readme_path, 'r', encoding='UTF-8') as f:
    long_description = f.read()

# Create arguments.
setuptools.setup(
    name='dmm-api',
    version=version,
    description='DMM API client for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/takelushi/dmm-api-py',
    author='Takeru Saito',
    author_email='takelushi@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    keywords='api rest dmm',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=get_requires_from_file(requirements_path),
    tests_require=[],
    extras_require={'test': []},
    # 'cmdclass': {"test": PyTest}
)

exit(0)
