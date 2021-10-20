#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append(".")

# Importing the relevant libraries
from os import name
from RFEM.enums import *
from RFEM.globalParameter import *
from RFEM.dataTypes import *
from RFEM.initModel import *

def test_global_parameters():
    
    clientModel.service.begin_modification('new')
    #not yet implemented in RFEM6 GM
    GlobalParameter.AddParameter(GlobalParameter, 
                                 no= 1,
                                 name= 'Test_1',
                                 symbol= 'Test_1',
                                 unit_group= GlobalParameterUnitGroup.LENGTH,
                                 definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
                                 definition_parameter= ['1+1'],
                                 comment= 'Comment_1')
    # issue with optimization type
    # GlobalParameter.AddParameter(GlobalParameter, 
    #                              no= 2,
    #                              name= 'Test_2',
    #                              symbol= 'Test_2',
    #                              unit_group= GlobalParameterUnitGroup.LOADS_DENSITY,
    #                              definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION,
    #                              definition_parameter= [50, 0, 100, 4],
    #                              comment= 'Comment_2')
    
    # GlobalParameter.AddParameter(GlobalParameter, 
    #                             no= 3,
    #                             name= 'Test_3',
    #                             symbol= 'Test_3',
    #                             unit_group= GlobalParameterUnitGroup.AREA,
    #                             definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
    #                             definition_parameter= [50, 0, 100, 4],
    #                             comment= 'Comment_3')

    # GlobalParameter.AddParameter(GlobalParameter, 
    #                             no= 4,
    #                             name= 'Test_4',
    #                             symbol= 'Test_4',
    #                             unit_group= GlobalParameterUnitGroup.MATERIAL_QUANTITY_INTEGER,
    #                             definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
    #                             definition_parameter= [50, 0, 100, 4],
    #                             comment= 'Comment_4')

    GlobalParameter.AddParameter(GlobalParameter, 
                                no= 5,
                                name= 'Test_5',
                                symbol= 'Test_5',
                                unit_group= GlobalParameterUnitGroup.DIMENSIONLESS,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
                                definition_parameter= [0.25],
                                comment= 'Comment_5')

    print('Ready!')
    
    clientModel.service.finish_modification()