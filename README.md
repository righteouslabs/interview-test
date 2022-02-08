# 🧠 Righteous AI Interview Test

This is a company standard interview test that checks problem solving and research skills.

The program implements many technologies at once. It checks how quickly and efficiently you can diagnose problems and keep moving forward.

It is unrealistic to know everything nor is this expected here. Prioritize learning what is required to solve the problem. The key is to perform time management well.

A successful candidate should, without getting help from an expert, be able to quickly assess the high level program behavior, extract business requirements, and make the necessary code changes without having to know every detail.

To start the interview, follow below instructions:

# 👉 Start

1. 🐋 Download and install [`Docker`](https://docs.docker.com/engine/install/) on your local machine
    - On *Windows* systems, you may have to setup [*Windows Subsystem Linux (WSL)*](https://docs.microsoft.com/en-us/windows/wsl/install) before installing Docker
    - Check additional help text for *Windows* on Microsoft documentation [here](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)
1. 🐧 Switch to using Docker Linux Engine
    - If you are not sure what this is then don't worry 😅
    - This is set by default for new Docker installations
    - This can also be explicitly done using PowerShell command on *Windows* when Docker is installed in default path:
        ```powershell
        & "$Env:ProgramFiles\Docker\Docker\DockerCli.exe" -SwitchLinuxEngine
        ```
1. ⬇️ Get the interview test code on to your local computer
    - This avoids having to install [Git](https://git-scm.com/) as well
    - [`Git clone`](https://git-scm.com/docs/git-clone) command will be run locally from inside the `alpine/git` Docker container
    - On *Windows* run the command in PowerShell
        ```powershell
        docker run -ti --rm -v "$($ENV:USERPROFILE):/root" -v "$($PWD):/git" alpine/git clone https://github.com/righteouslabs/interview-test
        ```
    - On *Linux / UNIX / Mac OS* run the command in bash
        ```bash
        docker run -ti --rm -v ${HOME}:/root -v $(pwd):/git alpine/git clone https://github.com/righteouslabs/interview-test
        ```
    - If you are familiar with Git then you can skip this step and clone the interview source code directly
1. ➡️ Change the current working directory to the interview test code
    - On *Windows / Linux / UNIX / Mac OS* run the command in the same folder where you ran the `git clone` command from previous step
        ```powershell
        cd interview-test
        ```
1. ▶️ Run the interview test program
    - The test program is written in [`Python`](https://www.python.org/) and running inside a [Docker container](https://www.docker.com/resources/what-container)
    - On *Windows / Linux / UNIX / Mac OS* run the command in source code folder
        ```bash
        docker-compose build
        docker-compose run --rm interview-test
        ```
1. 🤔 Make the necessary changes in the Python source code so you get the correct secret value
    - Only the correct secret value will be accepted for the interview
1. ✨ There is a **bonus** question that goes beyond Python code
    - To get this bonus question, you will have to make a new HTTP REST API call
    - Make an additional HTTP REST API call to the `/bonus` endpoint with the same algorithm but half the sequence length (i.e. `a_n where n = L/2`)

# 💁 Hints

1. Read the command output to find out what's missing

    The instructions are meant to be a high-level guide. Not a detailed set of instructions covering all issues.

    You will encounter problems, and this is expected, but do your best to troubleshoot on your own with the information you have. Research online as much as you can before asking an expert for help.

1. Remember to rebuild the container after making code changes

    This test involves Docker containers. This means any code changes made locally don't automatically get pushed inside the container. The container needs to be re-built (or code to be mapped via volumes, but this is advanced for this test)
