2) EE Coding Kata V1 Setting

Topics:
    * Setting up Locally and Testing

Project Setup:
    * IDE: VSCode
    * System code stored in src directory as arithmetic.py
    * Basic Unit tests stored in test directory as test_arithmetic.py
    * .travis.yml specifies instructions for the CI process

Local Testing:
    Testing Libraries used : pytest , pytest-cov, flake8.
    Methodology:
        ******ALL TESTING CARRIED OUT IN MAC TERMINAL LOCALLY**************
        1) Unit testing carried out by using pytest --cov command.
        This performs the unit tests on all scripts within the root directory and returns PASS or FAIL. --cov flagchecks for code coverage.
            command: pytest --cov
        2) Flake8 is used to check if the written code within the root directory conforms with the python PEP8 standard after the formatting package black has been run to format the code to PEP8 standards.
            command: flake8 .




