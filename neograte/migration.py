from abc import ABCMeta, abstractmethod


class BaseMigration(metaclass=ABCMeta):
  def __init__(self, graph):
    self.graph = graph

  @abstractmethod
  def upgrade(self): pass

  @abstractmethod
  def downgrade(self): pass
