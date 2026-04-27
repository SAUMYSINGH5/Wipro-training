from abc import ABC, abstractclassmethod, abstractmethod


class FM(ABC):
    #@abstractmethod
    def calculate_area(self):
        print('Area from FM')

    #@abstractmethod
    def calculate_perimeter(self):
        print('Perimeter from FM')