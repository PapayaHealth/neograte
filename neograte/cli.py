from importlib import import_module
from neograte.config import Configuration, Execution
from py2neo import Graph
import os
import re
import sys


class MigrationManager:
  def __init__(self):
    self.config = Configuration()
    self.graph = Graph(host=self.config.host, user=self.config.user, 
      password=self.config.password)

  def _do_migration(self, module_names):
    sys.path.insert(0, os.getcwd())

    if self.config.execution == Execution.DOWNGRADE:
      raise NotImplemented('Downgrade not supported yet')
    else:
      for module in module_names:
        m = import_module('{}.{}'.format(self.config.migrations_path, module))
        migration = getattr(m, 'Migration')(self.graph)
        migration.upgrade()

  def find_migration_modules(self):
    migration_module_names = list()

    for file in os.listdir(self.config.migrations_path):
      if re.match('^[0-9]{4}\_[0-9_a-z]+\.py$', file):
        migration_module_names.append(file[:-3])

    return sorted(migration_module_names)

  def run(self):
    migration_modules = self.find_migration_modules()
    self._do_migration(migration_modules)


def main():
  migration = MigrationManager()
  migration.run()
