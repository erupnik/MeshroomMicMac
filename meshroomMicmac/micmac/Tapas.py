__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Tapas(node.MicmacNode):
    commandLine = 'mm3d Tapas {calibrationModelValue} {imagePatternValue} {allParams}'
    documentation = 'Tapas'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            uid=[0],
            value="",
        ),
        desc.ChoiceParam(
            name='calibrationModel',
            label='Calibration Model',
            description='Calibration model.',
            group='', # unnamed parameter
            value='RadialBasic',
            values=['RadialBasic', 'RadialExtended', 'Fraser', 'FishEyeEqui', 'AutoCal', 'Figee', 'HemiEqui', 'RadialStd', 'FraserBasic', 'FishEyeBasic', 'FE_EquiSolBasic', 'Four7x2', 'Four11x2', 'Four15x2', 'Four19x2', 'AddFour7x2', 'AddFour11x2', 'AddFour15x2', 'Four19x2', 'AddPolyDeg0', 'AddPolyDeg1', 'AddPolyDeg2', 'AddPolyDeg3', 'AddPolyDeg4', 'AddPolyDeg5', 'AddPolyDeg6', 'AddPolyDeg7', 'Ebner', 'Brown', 'FishEyeStereo'],
            exclusive=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description="Export in text format.",
            uid=[0],
            value=False,
        ),

    ]

    outputs = [
        desc.File(
            name='Out',
            label='Orientation Directory',
            description="Directory of Output Orientation",
            uid=[],
            value="Tapas",
        ),
    ]


# TODO: Add useful parameters
"""
        desc.File(
            name='InCal',
            label='In Cal',
            description="Directory of Input Internal Orientation (Calibration)",
            uid=[0],
            value="",
        ),
        desc.File(
            name='InOri',
            label='In Ori',
            description="Directory of Input External Orientation",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='DoC',
            label='Do C',
            description="Do Compensation",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='ForCalib',
            label='For Calib',
            description="Is for calibration (Change def value of LMV and prop diag)?",
            uid=[0],
            value=-1,
            range=(-1, 16000, 1),
        ),
        desc.GroupAttribute(
            name='Focs',
            label='Focs',
            description="Keep images with focal length inside range [A,B] (A,B in mm)",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(1.0, 10000.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=10000.0,
                range=(1.0, 10000.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.GroupAttribute(
            name='PPRel',
            label='P P Rel',
            description="Principal point shift",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=-1.0,
                range=(-5000.0, 5000.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=-1.0,
                range=(-5000.0, 5000.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.IntParam(
            name='Decentre',
            label='Decentre',
            description="Principal point is shifted",
            uid=[0],
            value=-1,
            range=(-1, 1, 1),
        ),
        desc.FloatParam(
            name='PropDiag',
            label='Prop Diag',
            description="Hemi-spherik fisheye diameter to diagonal ratio",
            uid=[0],
            value=-1.0,
            range=(-1.0, 10000.0, 0.01),
        ),
        desc.StringParam(
            name='ImInit',
            label='Im Init',
            description="Force first image",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='MOI',
            label='M O I',
            description="MOI",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='DBF',
            label='D B F',
            description="Debug (internal use : DebugPbCondFaisceau=true)",
            uid=[0],
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description="Partial file for debug",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='DegFree',
            label='Deg Free',
            description="When specified degree of freedom of parameters generiqs",
            uid=[0],
            value=100,
            range=(0, 360, 1),
        ),
        desc.IntParam(
            name='DegAdd',
            label='Deg Add',
            description="When specified, degree of additionnal parameter",
            uid=[0],
            value=0,
            range=(0, 360, 1),
        ),
        desc.IntParam(
            name='DegRadMax',
            label='Deg Rad Max',
            description="Max degree of radial, default model dependent",
            uid=[0],
            value=100,
            range=(0, 360, 1),
        ),
        desc.IntParam(
            name='DegGen',
            label='Deg Gen',
            description="Max degree of general polynome, default model dependent (generally 0 or 1)",
            uid=[0],
            value=100,
            range=(0, 360, 1),
        ),
        desc.BoolParam(
            name='LibAff',
            label='Lib Aff',
            description="Free affine parameter",
            uid=[0],
            value=True,
        ),
        desc.StringParam(
            name='RapTxt',
            label='Rap Txt',
            description="RapTxt",
            uid=[0],
            value="",
        ),
        desc.FloatParam(
            name='LinkPPaPPs',
            label='Link P Pa P Ps',
            description="Link PPa and PPs (double)",
            uid=[0],
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.StringParam(
            name='FrozenPoses',
            label='Frozen Poses',
            description="List of frozen poses (pattern)",
            uid=[0],
            value="",
        ),
        desc.StringParam(
            name='FrozenCenters',
            label='Frozen Centers',
            description="List of frozen centers of poses (pattern)",
            uid=[0],
            value="",
        ),
        desc.StringParam(
            name='FrozenOrients',
            label='Frozen Orients',
            description="List of frozen orients of poses (pattern)",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='FreeCalibInit',
            label='Free Calib Init',
            description="Free calibs as soon as created.",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='FrozenCalibs',
            label='Frozen Calibs',
            description="List of frozen calibration (pattern)",
            uid=[0],
            value="",
        ),
        desc.StringParam(
            name='FreeCalibs',
            label='Free Calibs',
            description="List of free calibration",
            uid=[0],
            value=".*",
        ),

        desc.BoolParam(
            name='RefineAll',
            label='Refine All',
            description="More refinement at all step, safer and more accurate, but slower",
            uid=[0],
            value=True,
        ),
        desc.FloatParam(
            name='EcMax',
            label='Ec Max',
            description="Final threshold for residual0",
            uid=[0],
            value=5.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.GroupAttribute(
            name='EcInit',
            label='Ec Init',
            description="Inital threshold for residual",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=100.0,
                range=(0.0, 10000.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=5.0,
                range=(0.0, 10000.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.FloatParam(
            name='CondMaxPano',
            label='Cond Max Pano',
            description="Precaution for conditionning with Panoramic images.",
            uid=[0],
            value=1e4,
            range=(0.0, 1.0, 0.000001),
        ),
        desc.IntParam(
            name='RankInitF',
            label='Rank Init F',
            description="Order of focal initialisation, ref id distotion =2",
            uid=[0],
            value=3,
            range=(0, 10, 1),
        ),
        desc.IntParam(
            name='RankInitPP',
            label='Rank Init P P',
            description="Order of Principal point initialisation, ref id distotion =2",
            uid=[0],
            value=4,
            range=(0, 10, 1),
        ),
        desc.FloatParam(
            name='MulLVM',
            label='Mul L V M',
            description="Multipier Levenberg Markard",
            uid=[0],
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='MultipleBlock',
            label='Multiple Block',
            description="Multiple block need special caution (only related to Levenberg Markard)",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='FocFree',
            label='Foc Free',
            description="Foc Free.",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='PPFree',
            label='P P Free',
            description="Principal Point Free.",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='AffineFree',
            label='Affine Free',
            description="Affine Parameter.",
            uid=[0],
            value=True,
        ),
        desc.IntParam(
            name='DRMax',
            label='D R Max',
            description="When specified degree of freedom of radial parameters",
            uid=[0],
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='LibPP',
            label='Lib P P',
            description="Free principal point",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='LibFoc',
            label='Lib Foc',
            description="Free focal",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='LibCP',
            label='Lib C P',
            description="Free distorsion center, Def context dependant",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='LibCD',
            label='Lib C D',
            description="Free distorsion center, Def context dependant. Principal Point should be also free if CD is free",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='LibDec',
            label='Lib Dec',
            description="Free decentric parameter, Def context dependant",
            uid=[0],
            value=True,
        ),
        desc.IntParam(
            name='SElimB',
            label='S Elim B',
            description="Print stat on reason for bundle elimination (0,1,2)",
            uid=[0],
            value=1,
            range=(0, 2, 1),
        ),
        desc.BoolParam(
            name='ExpMatMark',
            label='Exp Mat Mark',
            description="Export Cov Matrix to Matrix Market Format+Eigen/cmp",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='VitesseInit',
            label='Vitesse Init',
            description="VitesseInit.",
            uid=[0],
            value=2,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='UBR4I',
            label='UBR4I',
            description="UBR4I",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='SauvAutom',
            label='Sauv Autom',
            description="Save intermediary results to, Set NONE if dont want any.",
            uid=[0],
            value="",
        ),
        desc.FloatParam(
            name='RatioMaxDistCS',
            label='Ratio Max Dist C S',
            description="Ratio max of distance P-Center.",
            uid=[0],
            value=30.0,
            range=(0.0, 10000.0, 0.01),
        ),
"""