from datetime import timedelta
from src.seir import DiseaseState
from src.simulation.simulation import Simulation
from src.world import world
from src.world.environments import InitialGroup

class ImmuneByAgeExtension(Simulation):
    def __init__(self,parent: Simulation):
        self.ImmunePortion = 0.5
        self.MinAgeToImmune = -1
        self.MaxAgeToImmune = 9
        self.parent = parent

    def start_of_day_processing(self):
        pass
    
    def end_of_day_processing(self):
        """
        if portion of population that is immune > self.ImmunePortion Do nothing
        else immune by age group
        """
        tmp = [1 for p in self.parent._world.all_people() if(( p.get_disease_state() == DiseaseState.IMMUNE) and ( p.get_disease_state() != DiseaseState.DECEASED))]
        cnt  = sum(tmp)
        num_people  = sum([1 for p in self.parent._world.all_people() if p.get_disease_state() != DiseaseState.DECEASED])
        potionUntilNow = cnt / num_people
        peopleToImmune=[]
        if self.ImmunePortion > potionUntilNow:
            peopleToImmune = [p for p in self.parent._world.all_people() if  (self.MinAgeToImmune < p.get_age_category()) and (p.get_age_category() < self.MaxAgeToImmune)]
        for person in peopleToImmune:
            ok, events = person.immune_and_get_events(start_date = self.parent._date ,delta_time =  timedelta(1))
            self.parent.register_events(events)
        self.MinAgeToImmune = self.MinAgeToImmune + 10
        self.MaxAgeToImmune = self.MaxAgeToImmune + 10
        print("")
