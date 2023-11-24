#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import GlobalParameterUnitGroup, GlobalParameterDefinitionType, ObjectTypes
from RFEM.globalParameter import GlobalParameter
from RFEM.initModel import Model, getPathToRunningRFEM

if Model.clientModel is None:
    Model()

def test_global_parameters():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    GlobalParameter.AddParameter(
                                 no= 1,
                                 name= 'Test_1',
                                 symbol= 'Test_1',
                                 unit_group= GlobalParameterUnitGroup.LENGTH,
                                 definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
                                 definition_parameter= ['1+1'],
                                 comment= 'Comment_1')
    GlobalParameter.AddParameter(
                                 no= 2,
                                 name= 'Test_2',
                                 symbol= 'Test_2',
                                 unit_group= GlobalParameterUnitGroup.LOADS_DENSITY,
                                 definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION,
                                 definition_parameter= [50, 0, 100, 4],
                                 comment= 'Comment_2')

    GlobalParameter.AddParameter(
                                no= 3,
                                name= 'Test_3',
                                symbol= 'Test_3',
                                unit_group= GlobalParameterUnitGroup.AREA,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
                                definition_parameter= [50, 0, 100, 4],
                                comment= 'Comment_3')

    GlobalParameter.AddParameter(
                                no= 4,
                                name= 'Test_4',
                                symbol= 'Test_4',
                                unit_group= GlobalParameterUnitGroup.MATERIAL_QUANTITY_INTEGER,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING,
                                definition_parameter= [50, 0, 100, 4],
                                comment= 'Comment_4')

    GlobalParameter.AddParameter(
                                no= 5,
                                name= 'Test_5',
                                symbol= 'Test_5',
                                unit_group= GlobalParameterUnitGroup.DIMENSIONLESS,
                                definition_type= GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
                                definition_parameter= [0.25],
                                comment= 'Comment_5')

    Model.clientModel.service.finish_modification()

    gp_1 = Model.clientModel.service.get_global_parameter(1)
    assert gp_1.unit_group == 'LENGTH'
    assert gp_1.definition_type == 'DEFINITION_TYPE_FORMULA'
    assert gp_1.formula == '1+1'

    gp_2 = Model.clientModel.service.get_global_parameter(2)
    assert gp_2.min == 0
    assert gp_2.max == 100
    assert gp_2.steps == 4
    assert gp_2.unit_group == 'LOADS_DENSITY'

def test_set_and_get_formula():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.reset()
    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-004 Bus Station-Concrete Design.js'))

    GlobalParameter.AddParameter(
        no=1,
        name='Test_1',
        symbol='Test_1',
        unit_group=GlobalParameterUnitGroup.LENGTH,
        definition_type=GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA,
        definition_parameter=['1+1'],
        comment='Comment_1')

    GlobalParameter.AddParameter(
        no=2,
        name='Test_2',
        symbol='Test_2',
        unit_group=GlobalParameterUnitGroup.LOADS_FORCE_PER_UNIT_LENGTH,
        definition_type=GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
        definition_parameter=[2000],
        comment='Comment_2')

    result = GlobalParameter.IsFormulaAllowed(ObjectTypes.E_OBJECT_TYPE_LINE_LOAD,1,2,"magnitude")
    assert result == True

    result = GlobalParameter.IsFormulaAllowed(ObjectTypes.E_OBJECT_TYPE_NODAL_LOAD,1,2,"magnitude")
    assert result == False

    result = GlobalParameter.SetFormula(ObjectTypes.E_OBJECT_TYPE_LINE_LOAD,1,2,"magnitude","4 + Test_2")
    assert result == True

    result = GlobalParameter.SetFormula(ObjectTypes.E_OBJECT_TYPE_NODAL_LOAD,1,2,"magnitude","4 + Test_2")
    assert result == False

    formula = GlobalParameter.GetFormula(ObjectTypes.E_OBJECT_TYPE_LINE_LOAD,1,2,"magnitude")
    assert formula != None
    assert formula.calculated_value == 2004.0
    assert formula.formula == '4 + Test_2'
    assert formula.is_valid == True