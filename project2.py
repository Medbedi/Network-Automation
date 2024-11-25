import paramiko
import time
from datetime import datetime


class SSHClientHelper:
    def __init__(self, hostname, username, password):
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__client = None
        self.__shell = None

        # Establish SSH connection
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client.connect(hostname=self.__hostname, username=self.__username, password=self.__password)

    def __del__(self):
        if self.__client:
            self.__client.close()

    def open_shell(self):
        self.__shell = self.__client.invoke_shell()

    def send_shell_command(self, command):
        if self.__shell:
            self.__shell.send(command + '\n')
            output = ""
            while not self.__shell.recv_ready():
                time.sleep(0.1)
            while self.__shell.recv_ready():
                output += self.__shell.recv(1024).decode("utf-8")
            self.save_output(command, output)
            return output
        else:
            raise Exception("Shell not opened. Call open_shell() first.")

    def exec_command(self, command):
        stdin, stdout, stderr = self.__client.exec_command(command)
        output = stdout.read().decode("utf-8")
        self.save_output(command, output)
        return output

    @staticmethod
    def save_output(command, output):
        with open("config_backup.txt", "w") as file:
            file.write(output)

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        file_name = f"{command}_{day}_{month}_{year}_{hour}_{minute}.txt"
        with open(file_name, "w") as file:
            file.write(output)
