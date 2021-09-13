from os import close
from RFEM.initModel import *
from RFEM.enums import *

class MemberSetLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Member Sets No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Force(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution= MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = [],
                 force_eccentricity: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = [magnitude]
            LOAD_DISTRIBUTION_UNIFORM_TOTAL: load_parameter = [magnitude]
            LOAD_DISTRIBUTION_CONCENTRATED_1: load_parameter = [relative_distance = False, magnitude, distance_a]
            LOAD_DISTRIBUTION_CONCENTRATED_N: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_2x2: load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
            LOAD_DISTRIBUTION_CONCENTRATED_2: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_TRAPEZOIDAL: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_TAPERED: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_PARABOLIC: load_parameter = [magnitude_1, magnitude_2, magnitude_3]
            LOAD_DISTRIBUTION_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_VARYING_IN_Z: load_parameter = [[distance, delta_distance, magnitude], ...]

        params:
            {'eccentricity_horizontal_alignment': MemberSetLoadEccentricityHorizontalAlignment.ALIGN_NONE,
            'eccentricity_vertical_alignment': MemberSetLoadEccentricityVerticalAlignment.ALIGN_NONE,
            'eccentricity_section_middle': MemberSetLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY,
            'is_eccentricity_at_end_different_from_start': False,
            'eccentricity_y_at_end': 0.0,
            'eccentricity_y_at_start': 0.0,
            'eccentricity_z_at_end': 0.0,
            'eccentricity_z_at_start': 0.0}
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution= load_distribution.name

        #Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM" or load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM_TOTAL":
            clientObject.magnitude = load_parameter
            
        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if load_parameter[0] == False:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]
            
            if load_parameter[2] == False:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING_IN_Z":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Force Eccentiricity
        clientObject.has_force_eccentricity = force_eccentricity

        if force_eccentricity == True:

            params_ecc = {'eccentricity_horizontal_alignment': MemberSetLoadEccentricityHorizontalAlignment.ALIGN_NONE,
                           'eccentricity_vertical_alignment': MemberSetLoadEccentricityVerticalAlignment.ALIGN_NONE,
                           'eccentricity_section_middle': MemberSetLoadEccentricitySectionMiddle.LOAD_ECCENTRICITY_SECTION_MIDDLE_CENTER_OF_GRAVITY,
                           'is_eccentricity_at_end_different_from_start': False,
                           'eccentricity_y_at_end': 0.0,
                           'eccentricity_y_at_start': 0.0,
                           'eccentricity_z_at_end': 0.0,
                           'eccentricity_z_at_start': 0.0}

            params_ecc.update(params)

            if params_ecc['is_eccentricity_at_end_different_from_start'] == False:

                clientObject.eccentricity_horizontal_alignment= params_ecc['eccentricity_horizontal_alignment'].name
                clientObject.eccentricity_vertical_alignment= params_ecc['eccentricity_vertical_alignment'].name
                clientObject.eccentricity_section_middle = params_ecc['eccentricity_section_middle'].name
                clientObject.eccentricity_y_at_end= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_y_at_start= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_z_at_end= params_ecc['eccentricity_z_at_start']
                clientObject.eccentricity_z_at_start= params_ecc['eccentricity_z_at_start']

            elif params_ecc['is_eccentricity_at_end_different_from_start'] == True:

                clientObject.eccentricity_horizontal_alignment= params_ecc['eccentricity_horizontal_alignment']
                clientObject.eccentricity_vertical_alignment= params_ecc['eccentricity_vertical_alignment']
                clientObject.eccentricity_section_middle = params_ecc['eccentricity_section_middle']
                clientObject.eccentricity_y_at_end= params_ecc['eccentricity_y_at_end']
                clientObject.eccentricity_y_at_start= params_ecc['eccentricity_y_at_start']
                clientObject.eccentricity_z_at_end= params_ecc['eccentricity_z_at_end']
                clientObject.eccentricity_z_at_start= params_ecc['eccentricity_z_at_start']
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if 'eccentricity_horizontal_alignment' or 'eccentricity_vertical_alignment' or 'eccentricity_section_middle' or 'is_eccentricity_at_end_different_from_start' or 'eccentricity_y_at_end' or 'eccentricity_y_at_start' or 'eccentricity_z_at_end' or 'eccentricity_z_at_start':
            pass
        else:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Moment(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution= MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction= MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = [],
                 comment: str = '',
                 params: dict = {}):
        '''
        load_parameter:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = magnitude
            LOAD_DISTRIBUTION_CONCENTRATED_1: load_parameter = [relative_distance = False, magnitude, distance_a]
            LOAD_DISTRIBUTION_CONCENTRATED_N: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude, count_n, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_2x2: load_parameter = [relative_distance_a = False, relative_distance_b = False, relative_distance_c = False, magnitude, distance_a, distance_b, distance_c]
            LOAD_DISTRIBUTION_CONCENTRATED_2: load_parameter = [relative_distance_a = False, relative_distance_b = False, magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_CONCENTRATED_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_TRAPEZOIDAL: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_TAPERED: load_parameter = [relative_distance_a = False, relative_distance_b = False,magnitude_1, magnitude_2, distance_a, distance_b]
            LOAD_DISTRIBUTION_PARABOLIC: load_parameter = [magnitude_1, magnitude_2, magnitude_3]
            LOAD_DISTRIBUTION_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_MOMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution= load_distribution.name

        #Load Magnitude and Parameters
        if load_distribution.name == "LOAD_DISTRIBUTION_UNIFORM":
            clientObject.magnitude = load_parameter[0]
            
        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_1":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            if load_parameter[0] == False:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
            else:
                clientObject.magnitude = load_parameter[1]
                clientObject.distance_a_relative = load_parameter[2]

        elif load_distribution.name ==  "LOAD_DISTRIBUTION_CONCENTRATED_N":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude = load_parameter[2]
            clientObject.count_n = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]


        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2x2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.distance_c_is_defined_as_relative = load_parameter[2]
            clientObject.magnitude = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]
            
            if load_parameter[2] == False:
                clientObject.distance_c_absolute = load_parameter[6]
            else:
                clientObject.distance_c_relative = load_parameter[6]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_2":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_CONCENTRATED_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters

            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution.name == "LOAD_DISTRIBUTION_TRAPEZOIDAL":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_TAPERED":
            clientObject.distance_a_is_defined_as_relative = load_parameter[0]
            clientObject.distance_b_is_defined_as_relative = load_parameter[1]
            clientObject.magnitude_1 = load_parameter[2]
            clientObject.magnitude_2 = load_parameter[3]

            if load_parameter[0] == False:
                clientObject.distance_a_absolute = load_parameter[4]
            else:
                clientObject.distance_a_relative = load_parameter[4]

            if load_parameter[1] == False:
                clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.distance_b_relative = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_PARABOLIC":
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Mass(self,
                no: int = 1,
                load_case_no: int = 1,
                member_sets: str = '1',
                individual_mass_components: bool=False,
                mass_components = [],
                comment: str = '',
                params: dict = {}):

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        clientObject.load_type = MemberSetLoadType.E_TYPE_MASS.name

        # Member Load Distribution
        clientObject.load_distribution= MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Individual Mass Components
        clientObject.individual_mass_components = individual_mass_components

        # Mass magnitude
        if individual_mass_components == False:
            clientObject.mass_global = mass_components[0]
        else:
            clientObject.mass_x = mass_components[0]
            clientObject.mass_y = mass_components[1]
            clientObject.mass_z = mass_components[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]
        
        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Temperature(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = [],
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [tt, tb]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            for load_over_total_length: bool= False:
                load_parameter = [tt1, tt2, tb1, tb2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
            for load_over_total_length: bool= True:
                load_parameter = [tt1, tt2, tb1, tb2]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [tt1, tt2, tb1, tb2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            load_parameter = [tb1, tb2, tb3, tt1, tt2, tt3]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_TEMPERATURE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude_t_b = load_parameter[0]
            clientObject.magnitude_t_t = load_parameter[1]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_t_1 = load_parameter[2]
            clientObject.magnitude_t_t_2 = load_parameter[3]

            if load_over_total_length == False:

                if load_parameter[4] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[6]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[6]
        
                if load_parameter[5] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[7]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[7]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_t_1 = load_parameter[2]
            clientObject.magnitude_t_t_2 = load_parameter[3]

            if load_parameter[4] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[6]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[6]
        
            if load_parameter[5] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[7]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[7]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_t_b_1 = load_parameter[0]
            clientObject.magnitude_t_b_2 = load_parameter[1]
            clientObject.magnitude_t_b_3 = load_parameter[2]
            clientObject.magnitude_t_t_1 = load_parameter[3]
            clientObject.magnitude_t_t_2 = load_parameter[4]
            clientObject.magnitude_t_t_3 = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==4
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = load_parameter[i][2]
                mlvlp.magnitude_delta_t = load_parameter[i][3]
                mlvlp.magnitude_t_t = load_parameter[i][2]
                mlvlp.magnitude_t_b = load_parameter[i][3]

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def TemperatureChange(self,
                           no: int = 1,
                           load_case_no: int = 1,
                           member_sets: str = '1',
                           load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                           load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                           load_parameter = [],
                           load_over_total_length: bool= False,
                           comment: str = '',
                           params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [tc, delta_t]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            for load_over_total_length: bool= False:
                load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
            for load_over_total_length: bool= True:
                load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [delta_t_1, delta_t_2, t_c_1, t_c_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            load_parameter = [delta_t_1, delta_t_2, delta_t_3, t_c_1, t_c_2, t_c_3]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_TEMPERATURE_CHANGE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude_delta_t = load_parameter[0]
            clientObject.magnitude_t_c = load_parameter[1]
            

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_t_c_1 = load_parameter[2]
            clientObject.magnitude_t_c_2 = load_parameter[3]

            if load_over_total_length == False:

                if load_parameter[4] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[6]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[6]
        
                if load_parameter[5] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[7]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[7]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_t_c_1 = load_parameter[2]
            clientObject.magnitude_t_c_2 = load_parameter[3]

            if load_parameter[4] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[6]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[6]
        
            if load_parameter[5] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[7]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[7]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_delta_t_1 = load_parameter[0]
            clientObject.magnitude_delta_t_2 = load_parameter[1]
            clientObject.magnitude_delta_t_3 = load_parameter[2]
            clientObject.magnitude_t_c_1 = load_parameter[3]
            clientObject.magnitude_t_c_2 = load_parameter[4]
            clientObject.magnitude_t_c_3 = load_parameter[5]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==4
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = load_parameter[i][2]
                mlvlp.magnitude_delta_t = load_parameter[i][3]
                mlvlp.magnitude_t_t = load_parameter[i][2]
                mlvlp.magnitude_t_b = load_parameter[i][3]

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)
        
    def AxialStrain(self,
                    no: int = 1,
                    load_case_no: int = 1,
                    member_sets: str = '1',
                    load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                    load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X,
                    load_parameter = [],
                    load_over_total_length: bool= False,
                    comment: str = '',
                    params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [epsilon]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            load_parameter = [epsilon1, epsilon2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [epsilon1, epsilon2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [epsilon1, epsilon2, epsilon3]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_AXIAL_STRAIN
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]
            
        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                if load_parameter[2] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[4]
        
                if load_parameter[3] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_parameter[2] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[4]
        
            if load_parameter[3] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load').varying_load_parameters
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def AxialDisplacement(self,
                    no: int = 1,
                    load_case_no: int = 1,
                    member_sets: str = '1',
                    load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X,
                    magnitude : float = 0.0,
                    comment: str = '',
                    params: dict = {}):

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_AXIAL_DISPLACEMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Precamber(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [magnitude]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            load_parameter = [magnitude_1, magnitude_2, magnitude_3]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_PRECAMBER
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                if load_parameter[2] == True:
                    clientObject.distance_a_is_defined_as_relative = True
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_is_defined_as_relative = False
                    clientObject.distance_a_absolute = load_parameter[4]
        
                if load_parameter[3] == True:
                    clientObject.distance_b_is_defined_as_relative = True
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_is_defined_as_relative = False
                    clientObject.distance_b_absolute = load_parameter[5]
            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_parameter[2] == True:
                clientObject.distance_a_is_defined_as_relative = True
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_is_defined_as_relative = False
                clientObject.distance_a_absolute = load_parameter[4]
        
            if load_parameter[3] == True:
                clientObject.distance_b_is_defined_as_relative = True
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_is_defined_as_relative = False
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:

            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution.name == "LOAD_DISTRIBUTION_VARYING":
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load.varying_load_parameters')
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def InitialPrestress(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X,
                 magnitude : float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Initial Prestress Definition
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_INITIAL_PRESTRESS
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Displacement(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [magnitude]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_a]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
        
        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_c_is_defined_as_relative = False, distance_a, distance_b, distance_c]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            load_parameter = [magnitude_1, magnitude_2, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            load_parameter = [magnitude_1, magnitude_2, magnitude_3]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_DISPLACEMENT
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[2]
            else:
                clientObject.distance_a_absolute = load_parameter[2]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[3]
            else:
                clientObject.distance_a_absolute = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[4]
            else:
                clientObject.distance_b_absolute = load_parameter[4]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]
            clientObject.distance_c_is_defined_as_relative = load_parameter[3]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

            if load_parameter[3]:
                clientObject.distance_c_relative = load_parameter[6]
            else:
                clientObject.distance_c_absolute = load_parameter[6]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load.varying_load_parameters')
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                clientObject.distance_a_is_defined_as_relative = load_parameter[2]
                clientObject.distance_b_is_defined_as_relative = load_parameter[3]

                if load_parameter[2]:
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3]:
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_absolute = load_parameter[5]

            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING:
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load.varying_load_parameters')
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def Rotation(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 load_over_total_length: bool= False,
                 comment: str = '',
                 params: dict = {}):
        '''
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            load_parameter = [magnitude]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_a]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]
        
        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            load_parameter = [magnitude, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_c_is_defined_as_relative = False, distance_a, distance_b, distance_c]

        for load_distrubition = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            load_parameter = [magnitude_1, magnitude_2, distance_a_is_defined_as_relative = False, distance_b_is_defined_as_relative = False, distance_a, distance_b]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZIODAL:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            load_parameter = [magnitude_1, magnitude_2, distance_a_relative = False, distance_a_relative = False, a_distance, b_distance]

        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            load_parameter = [magnitude_1, magnitude_2, magnitude_3]
        
        for load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING: 
            load_parameter = [[distance, delta_distance, magnitude], ...]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_ROTATION
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        if load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
            clientObject.magnitude = load_parameter[0]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[2]
            else:
                clientObject.distance_a_absolute = load_parameter[2]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[3]
            else:
                clientObject.distance_a_absolute = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[4]
            else:
                clientObject.distance_b_absolute = load_parameter[4]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
            clientObject.magnitude = load_parameter[0]
            clientObject.distance_a_is_defined_as_relative = load_parameter[1]
            clientObject.distance_b_is_defined_as_relative = load_parameter[2]
            clientObject.distance_c_is_defined_as_relative = load_parameter[3]

            if load_parameter[1]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[2]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

            if load_parameter[3]:
                clientObject.distance_c_relative = load_parameter[6]
            else:
                clientObject.distance_c_absolute = load_parameter[6]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load.varying_load_parameters')
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            if load_over_total_length == False:

                clientObject.distance_a_is_defined_as_relative = load_parameter[2]
                clientObject.distance_b_is_defined_as_relative = load_parameter[3]

                if load_parameter[2]:
                    clientObject.distance_a_relative = load_parameter[4]
                else:
                    clientObject.distance_a_absolute = load_parameter[4]

                if load_parameter[3]:
                    clientObject.distance_b_relative = load_parameter[5]
                else:
                    clientObject.distance_b_absolute = load_parameter[5]

            else:
                clientObject.load_is_over_total_length = True

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]

            clientObject.distance_a_is_defined_as_relative = load_parameter[2]
            clientObject.distance_b_is_defined_as_relative = load_parameter[3]

            if load_parameter[2]:
                clientObject.distance_a_relative = load_parameter[4]
            else:
                clientObject.distance_a_absolute = load_parameter[4]

            if load_parameter[3]:
                clientObject.distance_b_relative = load_parameter[5]
            else:
                clientObject.distance_b_absolute = load_parameter[5]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
            clientObject.magnitude_1 = load_parameter[0]
            clientObject.magnitude_2 = load_parameter[1]
            clientObject.magnitude_3 = load_parameter[2]

        elif load_distribution == MemberSetLoadDistribution.LOAD_DISTRIBUTION_VARYING:
            try:
                len(load_parameter[0])==3
            except:
                print("WARNING: MemberSetLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

            clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_set_load.varying_load_parameters')
            for i in range(len(load_parameter)):
                mlvlp = clientModel.factory.create('ns0:member_set_load_varying_load_parameters')
                mlvlp.no = i+1
                mlvlp.distance = load_parameter[i][0]
                mlvlp.delta_distance = load_parameter[i][1]
                mlvlp.magnitude = load_parameter[i][2]
                mlvlp.note = None
                mlvlp.magnitude_t_c = 0.0
                mlvlp.magnitude_delta_t = 0.0
                mlvlp.magnitude_t_t = 0.0
                mlvlp.magnitude_t_b = 0.0

                clientObject.varying_load_parameters.member_set_load_varying_load_parameters.append(mlvlp)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def PipeContentFull(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_FORWARD,
                 specific_weight : float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_FORWARD for +ZL
        load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_REVERSED for -ZL
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_PIPE_CONTENT_FULL
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        #Member Load Orientation
        clientObject.load_direction_orientation = load_direction_orientation.name

        #Load Magnitude
        clientObject.magnitude = specific_weight

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def PipeContentPartial(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_FORWARD,
                 specific_weight : float = 0.0,
                 filling_height : float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_FORWARD for +ZL
        load_direction_orientation = MemberSetLoadDirectionOrientation.LOAD_DIRECTION_REVERSED for -ZL
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_PIPE_CONTENT_PARTIAL
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberSetLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE.name

        #Member Load Orientation
        clientObject.load_direction_orientation = load_direction_orientation.name

        #Load Magnitude
        clientObject.magnitude = specific_weight

        #Filling Height
        clientObject.filling_height = filling_height
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)

    def PipeInternalPressure(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 pressure : float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Pressure in units bar.
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_PIPE_INTERNAL_PRESSURE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = MemberSetLoadDistribution.LOAD_DISTRIBUTION_UNIFORM.name

        # Member Load Direction
        clientObject.load_direction = MemberSetLoadDirection.LOAD_DIRECTION_LOCAL_X.name

        #Load Magnitude
        clientObject.magnitude = pressure
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)


    def RotaryMotion(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 member_sets: str = '1',
                 angular_acceleration : float = 0.0,
                 angular_velocity : float = 0.0,
                 axis_definition_type = MemberSetLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS,
                 axis_orientation = MemberSetLoadAxisDefinitionAxisOrientation.AXIS_POSITIVE,
                 axis_definition = MemberSetLoadAxisDefinition.AXIS_X,
                 axis_definition_p1 = None,
                 axis_definition_p2 = None,
                 comment: str = '',
                 params: dict = {}):
        '''
        axis_definition_p1 = [x1, y1, z1]
        axis_definition_p2 = [x2, y2, z2]
        '''
        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_set_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Load Type
        load_type = MemberSetLoadType.LOAD_TYPE_ROTARY_MOTION
        clientObject.load_type = load_type.name

        #Angular Acceleration
        clientObject.angular_acceleration = angular_acceleration

        #Angular Velocity
        clientObject.angular_velocity = angular_velocity

        #Axis Definition Type
        clientObject.axis_definition_type = axis_definition_type.name

        #Axis definition
        if axis_definition_type == MemberSetLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS.name:
            clientObject.axis_definition_p1_x = axis_definition_p1[0]
            clientObject.axis_definition_p1_y = axis_definition_p1[1]
            clientObject.axis_definition_p1_z = axis_definition_p1[2]

            clientObject.axis_definition_p2_x = axis_definition_p2[0]
            clientObject.axis_definition_p2_y = axis_definition_p2[1]
            clientObject.axis_definition_p2_z = axis_definition_p2[2]

        elif axis_definition_type == MemberSetLoadAxisDefinitionType.AXIS_DEFINITION_POINT_AND_AXIS.name:
            clientObject.axis_definition_p1_x = axis_definition_p1[0]
            clientObject.axis_definition_p1_y = axis_definition_p1[1]
            clientObject.axis_definition_p1_z = axis_definition_p1[2]

            clientObject.axis_definition_axis = axis_definition.name
            clientObject.axis_definition_axis_orientation = axis_orientation.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_set_load(load_case_no, clientObject)