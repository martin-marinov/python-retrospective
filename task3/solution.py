from itertools import chain


class Person:

    GENDERS = ('M', 'F')

    def __init__(self, name, birth_year, gender,
                 father=None, mother=None, *arg, **kwargs):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.__parents = [parent for parent in (father, mother) if parent]
        self.__children = []

        # Update parents' children
        for parent in self.__parents:
            parent.__children.append(self)

    def get_brothers(self):
        return list(self.__get_siblings(gender='M'))

    def get_sisters(self):
        return list(self.__get_siblings(gender='F'))

    def children(self, gender=None):
        if not gender in self.GENDERS:
            return self.__children
        else:
            return [child for child in self.__children
                    if child.gender == gender]

    def is_direct_successor(self, other_person):
        return other_person in self.__children

    def __get_siblings(self, gender):
        return set(sibling for sibling in
                   chain(*[parent.children() for parent in self.__parents])
                   if not sibling is self and sibling.gender == gender)
