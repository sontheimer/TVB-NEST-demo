# ------------------------------------------------------------------------------
#  Copyright 2020 Forschungszentrum Jülich GmbH
# "Licensed to the Apache Software Foundation (ASF) under one or more contributor
#  license agreements; and to You under the Apache License, Version 2.0. "
#
# Forschungszentrum Jülich
#  Institute: Institute for Advanced Simulation (IAS)
#    Section: Jülich Supercomputing Centre (JSC)
#   Division: High Performance Computing in Neuroscience
# Laboratory: Simulation Laboratory Neuroscience
#       Team: Multi-scale Simulation and Design
#
# ------------------------------------------------------------------------------

class Parameter:
    '''
    Parameter class.
    Hardcoded, without any error and safety handling.
    NOTE: 
    List of hardcoded parameter in the InterscaleHub (to be completed)
    - max_events set in InterscaleHub.py
    - min_delay set in Simulation_mock.py
    - simulation params (ids, size) set in Simulation_mock.py
    - tvb to nest params (size_list, list_id) set in pivot.py

    '''
    def __init__(self):
        '''
        init all param for both directions.
        '''
        path_file = os.path.dirname(__file__)
        self.__parameter = {
                "co_simulation": True,
                "path": path_file + "/../../result_sim/co-simulation/",
                "simulation_time": 1000.0,
                "level_log": 1,
                "resolution": 0.1,
                "nb_neurons": [100],
                # parameter for the synchronization between simulators
                "time_synchronization": 1.2,
                "id_nest_region": [0],
                # parameter for the transformation of data between scale
                "nb_brain_synapses": 1,
                'id_first_neurons': [1],
                "save_spikes": True,
                "save_rate": True
        }
        # path to files containing the MPI port info
        self.__nest_file = '../tests/test_nest_tvb/nest.txt' 
        self.__tvb_file = '../tests/test_nest_tvb/tvb.txt'
        
    def get_nest_path(self):
        return self.__nest_file
    
    def get_tvb_path(self):
        return self.__tvb_file
    
    def get_param(self,direction):
        # direction:
        # 1 --> NEST to TVB
        # 2 --> TVB to NEST
        if direction == 1:
            param = self.__parameter['param_nest_to_tvb']
        elif direction == 2:
            param = self.__parameter['param_tvb_to_nest']
        return param
