__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class GCPBascule(node.MicmacNode):
    commandLine = 'mm3d GCPBascule {imagePatternValue} {orientationInValue} {orientationOutValue} {groundControlPointsFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPBascule'

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
            name='orientationIn',
            label='Input Orientation',
            description="Input Orientation.",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.File(
            name='groundControlPointsFile',
            label='GCP 3D Coordinates File',
            description="Ground Control Points File",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='GCP Image Coordinates File',
            description="Image Measurements File",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='L1',
            label='L1 Minimisation',
            description="L1 minimisation vs L2",
            uid=[0],
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='CPI',
            label='Calibration Per Image',
            description="when Calib Per Image has to be used",
            uid=[0],
            advanced=True,
            value=False,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show Unused Points',
            description="Show unused point",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ShowD',
            label='Show Details',
            description="Show details",
            uid=[0],
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='PatNLD',
            label='Pattern for Nonlinear Deformation',
            description="Pattern for Non linear deformation, with aerial like geometry",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='NLFR',
            label='Nonlinear deformation Force True Rot',
            description="Force Orthogonal Rotations",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='NLShow',
            label='Nonlinear deformation Details',
            description="Non Linear : Show Details",
            uid=[0],
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='Out',
            label='Output Name',
            description="Directory of Output Orientation",
            value="GCPBasc",
            group='',
            uid=[0],
        ),
      #  desc.StringParam(
      #      name='ForceSol',
      #      label='Force Sol',
      #      description="To Force Sol from existing solution (xml file)",
      #      uid=[0],
      #      value="",
      #      advanced=True,
      #  ),
    ]

    outputs = [
        desc.File(
		name='orientationOut',
		label='Output Orientation',
		description="Orientation out",
		group='',
		uid=[0],
		value="{OutValue}",
	),
    ]
