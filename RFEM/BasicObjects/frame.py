from RFEM.initModel import *

class Frame():
    def __init__(self,
                 no: int = 1,
                 member_type = MemberType.TYPE_BEAM,
                 start_node_no: int = 1,
                 end_node_no: int = 2,
                 rotation_angle: float = 0.0,
                 start_section_no: int = 1,
                 end_section_no: int = 1,
                 start_member_hinge_no: int = 0,
                 end_member_hinge_no: int = 0,
 
