2) EE Coding Kata V1 Setting<br>

Topics:<br>
    * Setting up Locally and Testing<br><br>

Project Setup:<br>
    * IDE: VSCode<br>
    * System code stored in src directory as arithmetic.py<br>
    * Basic Unit tests stored in test directory as test_arithmetic.py<br>
    * .travis.yml specifies instructions for the CI process<br><br>

Local Testing:<br>
    Testing Libraries used : pytest , pytest-cov, flake8.<br>
    Methodology:<br>
        ******ALL TESTING CARRIED OUT IN MAC TERMINAL LOCALLY**************<br>
        1) Unit testing carried out by using pytest --cov command.<br>
        This performs the unit tests on all scripts within the root directory and returns PASS or FAIL. --cov flagchecks for code coverage.<br>
            command: pytest --cov<br>
        2) Flake8 is used to check if the written code within the root directory conforms with the python PEP8 standard after the formatting package black has been run to format the code to PEP8 standards.<br>
            command: flake8 .




