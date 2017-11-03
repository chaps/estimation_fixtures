
from nova_api.api import NovaAPI 
from nova_api.nova_exceptions import LoginFailed
import json
import argparse
import sys


class EstimationArgParser(argparse.ArgumentParser):
    
    def __init__(self):
        """ Class extension of argparser with predefined expected arguments.

        """
        super(EstimationArgParser, self).__init__()
        self.add_argument("-c", "--config", help="Read from config file.", 
            #action="store_true"
        )
        self.add_argument("-u", "--user", help="The user for credentials.",
            #action="store_true"
        )
        self.add_argument("-p", "--password", help="The password for credentials.",
            #action="store_true"
        )
        self.add_argument("command", help="The command to raise.")
        pass


class EstimationFixturesCLI(object):
    
    def __init__(self, command, user=None, password=None, config=None, **kwargs):
        """
        """
        
        self.command = command
        self.username = user
        self.password = password 
        self.config_path = config
        if self.config_path:
            self.parse_config(self.config_path) 
        self.api = NovaAPI(self.username, self.password)
        try:
            self.api.login()
            self.api.build_info()
        except LoginFailed as e:
            print(e)
            print("Failed to login with the given credentials".format(str(e)))
            sys.exit(1)
        print("Login Successful issuing command: {}".format(self.command))
        pass

    def parse_config(self, config_path=None):
        """
        """
        if not self.config_path and not config_path:
            raise Exception("No Config to parse")
            pass
        config_path = config_path or self.config_path
        with open(confaig_path, "r+") as cpathf:
            self.config = json.loads(cpathf.read())
            pass
        self.username, self.password = self.config["user"] , self.config["password"]
        pass


    def issue_command(self):
        """
        """
        try:
            print(getattr(self.api, self.command))
        except AttributeError as e:
            print("Command {} does not exists".format(self.command))
            sys.exit(1)
        print(getattr(self.api, "{}_response".format(self.command.replace("get_",""))).json())
        pass

    


