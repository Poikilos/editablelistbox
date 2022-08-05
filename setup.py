import setuptools
import sys
# - For nose, see https://github.com/poikilos/mgep/blob/master/setup.py

install_requires = []
if os.path.isfile("requirements.txt"):
    with open("requirements.txt", "r") as ins:
        for rawL in ins:
            line = rawL.strip()
            if len(line) < 1:
                continue
            install_requires.append(line)

description = (
    "Make an editable Listbox in Tkinter."
)
long_description = description
if os.path.isfile("readme.md"):
    with open("readme.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name='editablelistbox',
    version='2.0.0',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        # ('License :: OSI Approved :: ...'),
        # 'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Widget Sets',
    ],
    license='CC BY-SA 4.0',
    keywords='python tkinter editable listbox',
    url="https://github.com/poikilos/editablelistbox",
    author="David Duran, Jake Gustafson",
    author_email=("noreply@example.com,"
                  " 7557867+poikilos@users.noreply.github.com")
    # packages=setuptools.find_packages(),
    # packages=["editablelistbox"],  # only for directories
    py_modules=["editablelistbox"],  # for py files in the root of the package
    include_package_data=True,  # look for MANIFEST.in
    # scripts=['example-minimal.py'] ,
    # See <https://stackoverflow.com/questions/27784271/
    # how-can-i-use-setuptools-to-generate-a-console-scripts-entry-
    # point-which-calls>
    entry_points={
        'console_scripts': [
            # 'editablelistbox_example_minimal=example_minimal:main',
        ],
    },
    install_requires=install_requires,
    # test_suite='nose.collector',
    # tests_require=['nose', 'nose-cover3'],
    zip_safe=True,  # False: can't run zipped due to needing data files.
 )
