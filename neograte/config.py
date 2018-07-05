from argparse import ArgumentParser
from enum import Enum

class Execution(Enum):
  DOWNGRADE = 'downgrade'
  UPGRADE = 'upgrade'

class Configuration:
  host = '127.0.0.1'
  user = 'neo4j'
  password = 'neo4j'
  execution = Execution.UPGRADE

  def __init__(self):
    self._set_up_from_console()

  def _set_up_from_console(self):
    arg_parser = ArgumentParser(description='Neo4j migrations parser')

    arg_parser.add_argument('--host', default=self.host)
    arg_parser.add_argument('--user', default=self.user)
    arg_parser.add_argument('--password', default=self.password)
    arg_parser.add_argument('--downgrade', action='store_true', default=False)
    args = arg_parser.parse_args()

    self.host = args.host
    self.user = args.user
    self.password = args.password

    # Downgrade?

    if args.downgrade:
      self.execution = Execution.DOWNGRADE
