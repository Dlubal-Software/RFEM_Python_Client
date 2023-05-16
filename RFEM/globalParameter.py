from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, SetAddonStatus
from RFEM.enums import GlobalParameterUnitGroup, GlobalParameterDefinitionType, AddOn


class GlobalParameter():

    @staticmethod
    def AddParameter(
            no: int = 1,
            name: str = '',
            symbol: str = '',
            unit_group=GlobalParameterUnitGroup.LENGTH,
            definition_type=GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE,
            definition_parameter: list = None,
            comment: str = '',
            params: dict = None,
            model=Model):
        '''
        Args:
            no (int): Global Parameter Tag
            name (str): Parameter Name
            symbol (str): Symbol
            unit_group (enum): Global Parameter Unit Group Enumeration
            definition_type (enum): Global Parameter Definition Type Enumeration
            definition_parameter (list): Definition Parameter List
                for definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_FORMULA:
                    definition_parameter = [formula]
                for definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION:
                    definition_parameter = [min, max, increment, steps]
                for definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_ASCENDING:
                    definition_parameter = [min, max, increment, steps]
                for definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_OPTIMIZATION_DESCENDING:
                    definition_parameter = [value, min, max, steps]
                for definition_type = GlobalParameterDefinitionType.DEFINITION_TYPE_VALUE:
                    definition_parameter = [value]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Global Parameter
        clientObject = model.clientModel.factory.create('ns0:global_parameter')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

        # Global Parameter No.
        clientObject.no = no

        # Global Parameter Name
        clientObject.name = name

        # Symbol (HTML)
        clientObject.symbol = symbol

        # Unit Group
        clientObject.unit_group = unit_group.name

        # Definition Type
        clientObject.definition_type = definition_type.name

        if definition_type.name == 'DEFINITION_TYPE_FORMULA':
            if len(definition_parameter) != 1:
                raise ValueError(
                    'WARNING: The definition parameter needs to be of length 1. Kindly check list inputs for completeness and correctness.')
            clientObject.formula = definition_parameter[0]

        elif definition_type.name == 'DEFINITION_TYPE_OPTIMIZATION' or definition_type.name == 'DEFINITION_TYPE_OPTIMIZATION_ASCENDING' or definition_type.name == 'DEFINITION_TYPE_OPTIMIZATION_DESCENDING':
            SetAddonStatus(model.clientModel, AddOn.cost_estimation_active)
            if len(definition_parameter) != 4:
                raise ValueError(
                    'WARNING: The definition parameter needs to be of length 4. Kindly check list inputs for completeness and correctness.')
            clientObject.value = definition_parameter[0]
            clientObject.min = definition_parameter[1]
            clientObject.max = definition_parameter[2]
            clientObject.steps = definition_parameter[3]

        elif definition_type.name == 'DEFINITION_TYPE_VALUE':
            if len(definition_parameter) != 1:
                raise ValueError(
                    'WARNING: The definition parameter needs to be of length 1. Kindly check list inputs for completeness and correctness.')
            clientObject.value = definition_parameter[0]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Global Parameter to client model
        model.clientModel.service.set_global_parameter(clientObject)

    @staticmethod
    def SetFormula(ObjectType, no, parent_no, attribute, formula):

        objectLocation = Model.clientModel.factory.create('ns0:object_location')
        objectLocation.type = ObjectType.name
        objectLocation.no = no
        objectLocation.parent_no = parent_no

        allowedParameters = None
        try:
            allowedParameters = Model.clientModel.service.get_list_of_parameters_formula_allowed_for(
                objectLocation)
        except Exception as inst:
            print(inst)

        parameterAllowed = False
        if allowedParameters != None:
            for location in allowedParameters.object_parameter_location:
                if location.attribute == attribute:
                    parameterAllowed = True


        if parameterAllowed:
            objectParameterLocation = Model.clientModel.factory.create(
                'ns0:object_parameter_location')
            objectParameterLocation.attribute = attribute
            try:
                Model.clientModel.service.set_formula(
                    objectLocation, objectParameterLocation, formula)
                return True
            except Exception as ex:
                print(ex)
                return False
        else:
            print("Parameter not allowed")
            return False

    @staticmethod
    def GetFormula(ObjectType, no, parent_no, attribute):

        objectLocation = Model.clientModel.factory.create('ns0:object_location')
        objectLocation.type = ObjectType.name
        objectLocation.no = no
        objectLocation.parent_no = parent_no

        allowedParameters = None
        try:
            allowedParameters = Model.clientModel.service.get_list_of_parameters_formula_allowed_for(
                objectLocation)
        except Exception as inst:
            print(inst)

        parameterAllowed = False
        if allowedParameters != None:
            for location in allowedParameters.object_parameter_location:
                if location.attribute == attribute:
                    parameterAllowed = True

        formula = None
        if parameterAllowed:
            objectParameterLocation = Model.clientModel.factory.create(
                'ns0:object_parameter_location')
            objectParameterLocation.attribute = attribute
            formula = Model.clientModel.service.get_formula(
                objectLocation, objectParameterLocation)

        return formula
