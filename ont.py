class Ontology:
  """Container of all concepts."""

  def __init__(self):
    self.concepts = {}

  def create_concept(self, name, parent_name=None):
    """Create a new concept in this ontology."""
    parent = None
    concept = Concept(name, parent_name)
    self.concepts[name] = concept

  def remove_concept(self, name):
    self.concepts.pop(name)

  def rename_concept(self, old_name, new_name):
    c = self.concepts[old_name]
    c.name = new_name
    self.concepts.pop(old_name)
    self.concepts[new_name] = c

  def create_attr(self, concept_name, attr_name, attr_concept):
    self.concepts[concept_name].create_attr(attr_name, attr_concepts)
  
  def remove_attr(self, concept_name, attr_name):
    self.concepts[concept_name].remove_attr(attr_name)

  def status(self):
    num = len(self.concepts.keys())
    print "Number of concepts:", num

  def visualize(self):
    """Visualize the ontology."""


class Concept:
  """Representation of a concept."""

  def __init__(self, name, parent_name=None):
    self.name = name
    self.attrs = []
    self.parent_name = parent_name

  def create_attr(self, name, concept_name):
    """Create a new attribute and add to this concept.
    name: name of attribute
    concept_name: name of concept of attribute"""
    self.attrs.append((name, concept_name))
  
  def remove_attr(self, name):
    self.attrs.pop(name)
