from setuptools import setup

setup(
    name='sheesh-man',
    version='1.0.0',
    py_modules=['app'],
    entry_points={
        'console_scripts': [
            'sheesh-man=app:main'
        ]
    },
    install_requires=[],
    author='Fadhel',
    author_email='fadhelijlalfalah@gmail.com',
    description='SSH key manager tool',
    license='MIT',
    keywords='ssh key manager',
    url='https://github.com/fadhelmurphy/sheesh-man',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
