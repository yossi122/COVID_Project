import os
import json
from src.simulation.initial_infection_params import InitialImmuneType, NaiveInitialInfectionParams

from src.simulation.params import Params
from src.world.population_generation import population_loader
from src.world.population_generation import generate_city


def test_CityGeneration():
    file_path = os.path.dirname(__file__) + "/../src/config.json"
    with open(file_path) as json_data_file:
        ConfigData = json.load(json_data_file)
        citiesDataPath = ConfigData['CitiesFilePath']
        paramsDataPath = ConfigData['ParamsFilePath']
    Params.load_from(os.path.join(os.path.dirname(__file__), paramsDataPath), override=True)
    pop = population_loader.PopulationLoader(citiesDataPath)
    tmp_city = pop.get_city_by_name('Haifa')
    city = generate_city(tmp_city,
                         True,
                         internal_workplaces=True,
                         scaling=1.0,
                         verbosity=False,
                         to_world=True)

    humans = city.all_people()
    assert abs(283637 - len(humans)) < 5
    assert len(city.get_all_city_communities()) == 1
    assert city.get_person_from_id(humans[0]._id) is not None

def test_CityEnvGeneration():
    file_path = os.path.dirname(__file__) + "/../src/config.json"
    with open(file_path) as json_data_file:
        ConfigData = json.load(json_data_file)
        citiesDataPath = ConfigData['CitiesFilePath']
        paramsDataPath = ConfigData['ParamsFilePath']
    Params.load_from(os.path.join(os.path.dirname(__file__), paramsDataPath), override=True)
    pop = population_loader.PopulationLoader(citiesDataPath)
    tmp_city = pop.get_city_by_name('Haifa')
    city = generate_city(tmp_city,
                         True,
                         internal_workplaces=True,
                         scaling=1.0,
                         verbosity=False,
                         to_world=True)
    assert len(city.all_environments) > 0

def test_gethouses():
    """
    Checking the method get households
    """
    file_path = os.path.dirname(__file__) + "/../src/config.json"
    with open(file_path) as json_data_file:
        ConfigData = json.load(json_data_file)
        citiesDataPath = ConfigData['CitiesFilePath']
        paramsDataPath = ConfigData['ParamsFilePath']
    Params.load_from(os.path.join(os.path.dirname(__file__), paramsDataPath), override=True)
    pop = population_loader.PopulationLoader(citiesDataPath)
    tmp_city = pop.get_city_by_name('Haifa')
    city = generate_city(tmp_city,
                         True,
                         internal_workplaces=True,
                         scaling=1.0,
                         verbosity=False,
                         to_world=True)
    cnt  = len([p for p in city.all_environments if p.name == 'household'])
    assert len(city.get_all_city_households()) - cnt == 0 

def test_NaiveInitialInfectionParams():
    c = NaiveInitialInfectionParams(10,0.5,'atlit',immune_source=InitialImmuneType.GENERAL_POPULATION)
    assert len(c.__str__()) > 0

def test_chickagoCityEnvGeneration():
    file_path = os.path.dirname(__file__) + "/../src/config.json"
    with open(file_path) as json_data_file:
        ConfigData = json.load(json_data_file)
        citiesDataPath = ConfigData['CitiesFilePath']
        paramsDataPath = ConfigData['ParamsFilePath']
    Params.load_from(os.path.join(os.path.dirname(__file__), paramsDataPath), override=True)
    pop = population_loader.PopulationLoader(citiesDataPath)
    tmp_city = pop.get_city_by_name('Chicago')
    city = generate_city(tmp_city,
                         True,
                         internal_workplaces=True,
                         scaling=1.0,
                         verbosity=False,
                         to_world=True)
    assert len(city.all_environments) > 0