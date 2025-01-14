__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Campari(node.MicmacNode):
    commandLine = 'mm3d Campari {imagePatternValue} {inputOrientationValue} {OutValue} {allParams}'
    documentation = 'Campari'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description="Full Directory (Dir+Pattern)",
            uid=[0],
            group='unnamedParams',
            value="",
        ),
        desc.File(
            name='inputOrientation',
            label='Orientation Directory',
            description="Input Orientation",
            uid=[0],
            group='unnamedParams',
            value="",
        ),
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            uid=[0],
            value="",
        ),
        desc.GroupAttribute(
            name='GCP',
            label='Ground Control Points',
            description="Image and 3D coordinates of GCPs [GrMes.xml,GrUncertainty,ImMes.xml,ImUnc]",
            brackets='[]',
            joinChar=',', 
            advanced=True,
            groupDesc=[
            desc.StringParam(
                name="GrMes",
                label="Coordinates 3D",
                description="GrMes.xml",
                value="Saisie-S3D.xml", 
                uid=[0],
            ),
            desc.FloatParam(
                name="GrUncertainty",
                label="Uncertainty 3D",
                description="GrUncertainty",
                value=1.0, 
                range=(0.0, 100.0, 0.01),
                uid=[0], 
            ),
            desc.StringParam(
                name="ImMes",
                label="Image Coordinates",
                description="ImMes.xml",
                value="Saisie-S2D.xml", 
                uid=[0],
            ),
            desc.FloatParam(
                name="ImUnc",
                label="Image Uncertainty",
                description="ImUnc",
                value=1.0, 
                range=(0.0, 100.0, 0.1),
                uid=[0], 
            ),
        ]),
     	desc.BoolParam(
            name='enableGpsLa',
            label='Enable Lever Arm Estimation',
            description="Enable Lever Arm Estimation.",
            uid=[0],
            value=False,
            advanced=True,
            group=''
        ),
        desc.GroupAttribute(
            name='GpsLa',
            label='GPS Lever Arm Estimation',
            description="Gps Lever Arm, in combination with EmGPS",
            advanced=True,
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.enableGpsLa.value,
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(0.0, 100.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(0.0, 100.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(0.0, 100.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.GroupAttribute(
            name='IncLA',
            label='Initial Lever Arm Uncertainty',
            advanced=True,
            description="Initial Lever Arm Uncertainty (Def not used)",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.enableGpsLa.value,
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(0.0, 100.0, 0.5),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(0.0, 100.0, 0.5),
                uid=[0],
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(0.0, 100.0, 0.5),
                uid=[0],
            ),
        ]),
        desc.StringParam(
            name='PatGPS',
            label='Pat GPS',
            description="When EmGPS, filter images where GPS is used",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.FloatParam(
            name='SigmaTieP',
            label='Tie Points Weighting',
            description="Tie Points Weighting (Def=1)",
            uid=[0],
            value=1.0,
            range=(0.5, 10000.0, 0.5), 
        ),
        desc.FloatParam(
            name='FactElimTieP',
            label='Outlier Tie Points Reproj Error',
            description="Reprojection Error Eliminating Outlier Tie Points  (prop to SigmaTieP, Def=5)",
            uid=[0],
            value=5.0,
            range=(1.0, 10000.0, 1.0),
        ),
        desc.BoolParam(
            name='CPI1',
            label='Calibration Per Image 1',
            description="Calib Per Im, Firt time",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='CPI2',
            label='Calibration Per Image 2',
            description="Calib Per Im, After first time, reUsing Calib Per Im As input",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='AllFree',
            label='All Free',
            description="Refine all calibration parameters (Def=false)",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='AllFreePat',
            label='Free All Camera Parameters',
            description="Pattern of images that will be subject to AllFree (Def=.*)",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.StringParam(
            name='GradualRefineCal',
            label='Gradually Refine Camera Intrinsics',
            description="[Use With FishEye] Gradually Refine Camera Intrinsics",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.BoolParam(
            name='DetGCP',
            label='Show GCP Details',
            description="Show GCP Details (Def=false)",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='setVisc',
            label='Set Viscosity',
            description="Set Viscosity on Intrinsics and Extrinsics.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.FloatParam(
            name='Visc',
            label='Viscosity on Extrinsics',
            description="Viscosity on external orientation in Levenberg-Marquardt like resolution (Def=1.0)",
            uid=[0],
            enabled=lambda node: node.setVisc.value,
            value=1.0,
            advanced=True,
            range=(0.0, 10.0, 0.1),
        ),
        desc.BoolParam(
            name='AddViscInterne',
            label='Enable Viscosity on Intrinsics',
            description="Add Viscosity on calibration parameter (Def=false, exept for GradualRefineCal)",
            uid=[0],
            enabled=lambda node: node.setVisc.value,
            advanced=True,
            value=False,
        ),
        desc.FloatParam(
            name='ViscInterne',
            label='Viscosity on Intrinsics',
            description="Viscosity on calibration parameter (Def=0.1), use it with AddViscInterne=true",
            uid=[0],
            enabled=lambda node: node.setVisc.value,
            advanced=True,
            value=0.1,
            range=(0.0, 10.0, 0.1),
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description="Export in text format.)",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='PoseFigee',
            label='Fix Camera Poses',
            description="Does the external orientation of the cameras are frozen or free (Def=false, i.e. camera poses are free)",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.StringParam(
            name='FrozenPoses',
            label='Set Fixed Poses',
            description="List of fixed poses (pattern)",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.StringParam(
            name='FrozenCenters',
            label='Set Fixed Centers',
            description="List of fixed poses (pattern)",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.StringParam(
            name='FrozenOrients',
            label='Set fixed Ori',
            description="List of fixed poses (pattern)",
            uid=[0],
            advanced=True,
            value="",
        ),
        desc.BoolParam(
            name='AcceptGB',
            label='Accept Generic Bundle Camera',
            description="Accepte new Generik Bundle image (i.e., pushbroom), Def=true, set false for perfect backward compatibility",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.StringParam(
            name='NameRTA',
            label='Name RTA',
            description="Name for save results of Rolling Test Appuis , Def=SauvRTA.xml",
            uid=[0],
            advanced=True,
            value="",
        ), 
        desc.IntParam(
            name='NbIterEnd',
            label='Number of iterations',
            description="Number of iteration at end, Def = 4",
            uid=[0],
            value=4,
            range=(0, 10, 1),
        ),
        desc.BoolParam(
            name='FocFree',
            label='Foc Free',
            description="Foc Free (Def=true)",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='PPFree',
            label='PP Free',
            description="Principal Point Free (Def=true)",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='AffineFree',
            label='Affine Free',
            description="Affine Parameter (Def=true)",
            uid=[0],
            advanced=True,
            value=False,
        ),
      #  desc.IntParam(
      #      name='DegAdd',
      #      label='Deg Add',
      #      description="When specified, degree of additionnal parameter",
      #      uid=[0],
      #      value=0,
      #      advanced=True,
      #      range=(-sys.maxsize, sys.maxsize, 1),
      #  ),
      #  desc.IntParam(
      #      name='DegFree',
      #      label='Deg Free',
      #      description="When specified degree of freedom of parameters generiqs",
      #      uid=[0],
      #      value=0,
      #      advanced=True,
      #      range=(-sys.maxsize, sys.maxsize, 1),
      #  ),
        desc.BoolParam(
            name='setDRMax',
            label='Set DR Max',
            description="Set DR Max.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.IntParam(
            name='DRMax',
            label='DR Max',
            description="When specified degree of freedom of radial parameters",
            enabled=lambda node: node.setDRMax.value,
            uid=[0],
            value=0,
            range=(0, 9, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibCP',
            label='Set Lib CP',
            description="Set lib CP.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibCP',
            label='Lib CP',
            description="Free distorsion center, Def context dependant",
            enabled=lambda node: node.setLibCP.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibCD',
            label='Set Lib CD',
            description="Set lib CD.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibCD',
            label='Lib CD',
            description="Free distorsion center, Def context dependant. Principal Point should be also free if CD is free",
            enabled=lambda node: node.setLibCD.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='LibDec',
            label='Lib Dec',
            description="Free decentric parameter, Def context dependant",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.IntParam(
            name='SElimB',
            label='Bundle Elimination Stats',
            description="Print stat on reason for bundle elimination (0,1,2)",
            uid=[0],
            value=0,
            advanced=True,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='ExpMatMark',
            label='Export Cov Mat in Eigen',
            description="Export Cov Matrix to Matrix Market Format+Eigen/cmp",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.StringParam(
            name='SauvAutom',
            label='Save Ori Intermediary Iterations',
            description="Save intermediary results to, Set NONE if dont want any",
            uid=[0],
            advanced=True,
            value="",
        ), 
        desc.IntParam(
            name='NbLiais',
            label='Tie Points Relative Weight',
            description="Param for relative weighting for tie points",
            uid=[0],
            value=100,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.FloatParam(
            name='PdsGBRot',
            label='Weight rot constraint',
            description="[Applies to pushbroom] Weighting of the global rotation constraint (Generic bundle Def=0.002)",
            uid=[0],
            value=0.002,
            advanced=True,
            range=(0.0, 1.0, 0.001),
        ),
        desc.FloatParam(
            name='PdsGBId',
            label='Weight global deformation constraint',
            description="[Applies to pushbroom] Weighting of the global deformation constraint (Generic bundle Def=0.0)",
            uid=[0],
            value=0.0,
            advanced=True,
            range=(0.0, 1.0, 0.001),
        ),
        desc.FloatParam(
            name='PdsGBIter',
            label='Weight rot change constraint',
            description="[Applies to pushbroom] Weighting of the change of the global rotation constraint between iterations (Generic bundle Def=1e-6)",
            uid=[0],
            value=0.00001,
            advanced=True,
            range=(0.0, 0.1, 0.0001),
        ),
        desc.BoolParam(
            name='ExportSensib',
            label='Export Correlation/Covariances',
            advanced=True,
            description="Export sensiblity (accuracy) estimator : correlation , variance, inverse matrix variance ...",
            uid=[0],
            value=False,
        ),  
        desc.IntParam(
            name='NAWNF',
            label='NAWNF',
            description="Num Attribute for Weigthing in New Format",
            uid=[0],
            value=0,
            advanced=True,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),  
        desc.FloatParam(
            name='ExtIntZ',
            label='Ext Int Z',
            description="Extension of Z Interval for elimination",
            uid=[0],
            advanced=True,
            value=0.0,
            range=(-10000.0, 10000.0, 1.0),
        ),
        desc.StringParam(
            name='Out',
            label='Output Name',
            description="Directory of Output Orientation",
            value="Campari",
            group='',
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='orientationDirectory',
            label='Orientation Directory',
            description="Directory of Output Orientation",
            value="{OutValue}",
            group='', # not a command line parameter
            uid=[],
        ),
    ]
