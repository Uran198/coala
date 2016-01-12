import os
from subprocess import Popen, PIPE


class GitCommitBear(GlobalBear):
    def run(self):
        """
        Raises issues against style violations on markdown files.
        """
        working_directory = os.getcwd()
        command = "git log -1 --pretty=%B"

    @staticmethod
    def run_command(command):
        process = Popen(command,
                        shell=True,
                        stdout=PIPE,
                        stderr=PIPE,
                        universal_newlines=True)
