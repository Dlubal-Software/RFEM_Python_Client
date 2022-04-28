from RFEM.initModel import ConvertToDlString, Model, clearAtributes

class MemberResultIntermediatePoint():
    def __init__(self,
                 no: int = 1,
                 members: str = "",
                 point_count: int = 2,
                 uniform_distribution: bool = True,
                 distances = None,
                 comment: str = '',
                 params: dict = None):

        # Client model | Member Result Intermediate Point
        clientObject = Model.clientModel.factory.create('ns0:member_result_intermediate_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Result Intermediate Point No.
        clientObject.no = no

        # Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Point Count
        clientObject.uniform_distribution = uniform_distribution
        if uniform_distribution:
            clientObject.point_count = point_count

        else:
            clientObject.distances = Model.clientModel.factory.create('ns0:member_result_intermediate_point.distances')

            for i,j in enumerate(distances):
                mlvlp = Model.clientModel.factory.create('ns0:member_result_intermediate_point_distances')
                mlvlp.no = i+1
                mlvlp.value = distances[i][0]
                mlvlp.note = None

                clientObject.distances.member_result_intermediate_point_distances.append(mlvlp)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Member Result Intermediate Point to client model
        Model.clientModel.service.set_member_result_intermediate_point(clientObject)
