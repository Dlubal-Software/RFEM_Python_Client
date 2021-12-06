import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')

from RFEM.enums import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness


def test_init():

    Model(False)
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member(1, 1, 2, 0, 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_beam():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Beam(0, 1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [15], 1, 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_rigid():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Rigid(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_truss():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Truss(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_trussonlyn():
    
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.TrussOnlyN(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_tension():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Tension(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5
    
def test_compression():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Compression(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_buckling():

    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Buckling(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0]) 

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_cable():
    
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.Cable(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_resultbeam():
    
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.ResultBeam(0, 1, 1, 2, MemberSectionDistributionType.SECTION_DISTRIBUTION_TYPE_UNIFORM, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, MemberResultBeamIntegration.INTEGRATE_WITHIN_CUBOID_QUADRATIC, [0], 1, 1,  integration_parameters = [0.1])

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_definablestiffness():
    
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Section(1, 'IPE 300', 1)
    MemberDefinableStiffness(1)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.DefinableStiffness(0, 1, 1, 2, MemberRotationSpecificationType.COORDINATE_SYSTEM_ROTATION_VIA_ANGLE, [0], 1)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplingrigidrigid():
        
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingRigidRigid(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplingrigidhinge():
        
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingRigidHinge(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplinghingerigid():
        
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingHingeRigid(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5

def test_couplinghingehinge():
        
    Model.clientModel.service.reset()
    Model.clientModel.service.begin_modification()

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)

    Member.CouplingHingeHinge(0, 1, 1, 2)

    Model.clientModel.service.finish_modification()

    member = Model.clientModel.service.get_member(1)

    assert member.no == 1
    assert member.length == 5
