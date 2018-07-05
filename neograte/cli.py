from importlib import import_module
from neograte.config import Configuration, Execution
from py2neo import Graph
import re
import os

class MigrationManager:
  def __init__(self):
    self.config = Configuration()
    self.graph = Graph(host=self.config.host, user=self.config.user, 
      password=self.config.password)

  def find_migration_modules(self):
    migration_module_names = list()

    for file in os.listdir('migrations'):
      if re.match('^[0-9]{4}\_[0-9_a-z]+\.py$', file):
        migration_module_names.append(file[:-3])

    return migration_module_names

  def run(self):
    migration_modules = self.find_migration_modules()
    print(self.config.__dict__)
    print(self.graph)


def main():
  migration = MigrationManager()
  migration.run()
