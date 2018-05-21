from setuptools import setup, find_packages

setup(
    name='yangsutil',
    version='0.0.1',
    description='Utilities',
    long_description='Utilities',
    keywords=['util', 'datetime', 'request', 'crypt'],
    license='MIT',
    python_requires='>=3.5',
    author='seiren87',
    author_email='seiren87dev@gmail.com',
    url='https://github.com/seiren87/yangsutil',
    install_requires=[
        'dateutils==0.6.6',
        'pycrypto==2.6.1',
        'requests==2.18.4',
        'bs4==0.0.1'
    ],
    packages=find_packages(
        exclude=['testcases']
    ),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
