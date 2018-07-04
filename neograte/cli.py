import re
import os

class MigrationManager:
  def find_migration_modules(self):
    migration_module_names = list()

    for file in os.listdir('migrations'):
      if re.match('^[0-9]{4}\_[0-9_a-z]+\.py$', file):
        migration_module_names.append(file[:-3])

    return migration_module_names

  def run(self):
    migration_modules = self.find_migration_modules()
    pass


def main():
  migration = MigrationManager()
  migration.run()
