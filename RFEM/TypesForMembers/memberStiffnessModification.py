from pytest import param
from RFEM.enums import MemberStiffnessModificationType
from RFEM.initModel import ConvertToDlString, Model, clearAtributes

class MemberStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 assigned_structure_modification: str = "",
                 modification_type = MemberStiffnessModificationType.TYPE_TOTAL_STIFFNESSES_FACTORS,
                 parameters = [1.0],
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Modification Tag
            assigned_structure_modification (str): Assigned Structure Modification
            modification_type (enum): Member Stiffness Modification Type Enumeration Item
            parameters (list):
                if modification_type == "TYPE_TOTAL_STIFFNESSES_FACTORS":
                    parameters = [total_stiffness_factor]
                elif modification_type == "TYPE_PARTIAL_STIFFNESSES_FACTORS":
                    parameters = [factor_of_axial_stiffness, factor_of_bending_y_stiffness, factor_of_bending_z_stiffness,
                                  partial_stiffness_factor_of_shear_y_stiffness, partial_stiffness_factor_of_shear_z_stiffness,
                                  partial_stiffness_factor_of_torsion_stiffness, partial_stiffness_factor_of_weight]
                elif modification_type == "TYPE_CONCRETE_STRUCTURES_ACI":
                    parameters = [concrete_structure_component_type, factor_of_axial_stiffness,
                                  factor_of_bending_y_stiffness, factor_of_bending_z_stiffness]
                elif modification_type == "TYPE_CONCRETE_STRUCTURES_CSA":
                    parameters = [concrete_structure_component_type, factor_of_axial_stiffness,
                                  factor_of_bending_y_stiffness, factor_of_bending_z_stiffness]
                elif modification_type = "TYPE_STEEL_STRUCTURES":
                    parameters = [steel_structure_determine_tau_b, steel_structure_design_method]
                elif modification_type = "TYPE_STEEL_STRUCTURES_CSA":
                    parameters = [steel_structure_csa_determine_tau_b, factor_of_axial_stiffness, factor_of_bending_z_stiffness,
                                  steel_structure_csa_stiffness_factor_of_shear_y_stiffness, steel_structure_csa_stiffness_factor_of_shear_z_stiffness,
                                  steel_structure_csa_stiffness_factor_of_torsion_stiffness]
            comment (str, optional): Comments
            params (dict, optional): Parameters
        """

        # Client model | Member Stiffness Modification
        clientObject = model.clientModel.factory.create('ns0:member_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Stiffness Modification No.
        clientObject.no = no

        # Structure Modification Assignment
        clientObject.assigned_to_structure_modification = ConvertToDlString(assigned_structure_modification)

        # Stiffness Modification Type
        clientObject.type = modification_type.name

        if modification_type.name == "TYPE_TOTAL_STIFFNESSES_FACTORS":
            clientObject.factor_of_axial_stiffness = parameters[0]
            clientObject.factor_of_bending_y_stiffness = parameters[0]
            clientObject.factor_of_bending_z_stiffness = parameters[0]
            clientObject.total_stiffness_factor_of_total_stiffness = parameters[0]

        elif modification_type.name == "TYPE_PARTIAL_STIFFNESSES_FACTORS":
            clientObject.factor_of_axial_stiffness = parameters [0]
            clientObject.factor_of_bending_y_stiffness = parameters [2]
            clientObject.factor_of_bending_z_stiffness = parameters [3]
            clientObject.partial_stiffness_factor_of_shear_y_stiffness = parameters [4]
            clientObject.partial_stiffness_factor_of_shear_z_stiffness = parameters [5]
            clientObject.partial_stiffness_factor_of_torsion_stiffness = parameters [6]
            clientObject.partial_stiffness_factor_of_weight = parameters [7]

        elif modification_type.name == "TYPE_CONCRETE_STRUCTURES_ACI":
            clientObject.concrete_structure_component_type = parameters[0].name
            clientObject.factor_of_axial_stiffness = parameters[1]
            clientObject.factor_of_bending_y_stiffness = parameters[2]
            clientObject.factor_of_bending_z_stiffness = parameters[3]

        elif modification_type.name == "TYPE_CONCRETE_STRUCTURES_CSA":
            clientObject.concrete_structure_component_type = parameters[0].name
            clientObject.factor_of_axial_stiffness = parameters[1]
            clientObject.factor_of_bending_y_stiffness = parameters[2]
            clientObject.factor_of_bending_z_stiffness = parameters[3]

        elif modification_type.name == "TYPE_STEEL_STRUCTURES":
            clientObject.steel_structure_determine_tau_b = parameters[0]

            if parameters[0] == "ITERATIVE":
                clientObject.steel_structure_design_method = parameters[1]

        elif modification_type.name == "TYPE_STEEL_STRUCTURES_CSA":
            clientObject.steel_structure_csa_determine_tau_b = parameters[0].name
            clientObject.factor_of_axial_stiffness = parameters[1]
            clientObject.factor_of_bending_y_stiffness = parameters[2]
            clientObject.factor_of_bending_z_stiffness = parameters[3]
            clientObject.steel_structure_csa_stiffness_factor_of_shear_y_stiffness = parameters[4]
            clientObject.steel_structure_csa_stiffness_factor_of_shear_z_stiffness = parameters[5]
            clientObject.steel_structure_csa_stiffness_factor_of_torsion_stiffness = parameters[6]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Stiffness Modification to client model
        model.clientModel.service.set_member_stiffness_modification(clientObject)
