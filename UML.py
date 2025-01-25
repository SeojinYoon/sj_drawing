
class Class:
    def __init__(self, 
                 name, 
                 is_a = [], 
                 has_a = [], 
                 dependencies = [], 
                 descriptions = []):
            """
            Initialize Class for representing class diagram

            :param is_a(list - string): Generalization 및 Realization 관계 표현: 상속
            :param has_a(list - string): Ownership을 표현
            :param dependencies(list - string): Dependency 표현: 다른 소스코드가 변경될 때 지역적으로 영향을 받는가?
            :param descriptions(list - string): description for class
            """
            self.name = name
            self.is_a = is_a
            self.has_a = has_a
            self.dependencies = dependencies
            self.descriptions = descriptions

class Protocol:
    def __init__(self, 
                 name, 
                 is_a = [],
                 descriptions = []):
      """
      Initialize Class for representing class diagram

      :param is_a(list - string): Generalization 및 Realization 관계 표현: 상속
      :param descriptions(list - string): description for class
      """
      self.name = name
      self.is_a = is_a
      self.descriptions = descriptions


