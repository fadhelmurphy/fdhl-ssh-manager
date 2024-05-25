from setuptools import setup

setup(
    name='fdhl-ssh-manager',
    version='1.0.0',
    py_modules=['switcher'],
    entry_points={
        'console_scripts': [
            'fdhl-ssh-manager=switcher:main'
        ]
    },
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='SSH key manager tool',
    license='MIT',
    keywords='ssh key manager',
    url='https://github.com/yourusername/fdhl-ssh-manager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
