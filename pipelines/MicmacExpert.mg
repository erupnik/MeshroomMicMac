{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "MicMacProject": "1.0",
            "GCPBascule": "1.1.1",
            "Campari": "0.0",
            "Tapas": "1.1.1",
            "CameraInit": "9.0",
            "TapiocaMulScale": "1.1.1",
            "AperiCloud": "1.1.1",
            "C3DC": "1.1.1"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                0,
                0
            ],
            "inputs": {}
        },
        "MicMacProject_1": {
            "nodeType": "MicMacProject",
            "position": [
                200,
                0
            ],
            "inputs": {
                "input": "{CameraInit_1.output}"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                400,
                0
            ],
            "inputs": {
                "projectDirectory": "{MicMacProject_1.projectDirectory}"
            }
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                1230,
                223
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}",
                "Out": "AperiCloud_rel.ply"
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                600,
                0
            ],
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "calibrationModel": "FraserBasic",
                "SH": "{TapiocaMulScale_1.PostFix}",
                "Out": "Relative"
            }
        },
        "GCPBascule_1": {
            "nodeType": "GCPBascule",
            "position": [
                812,
                -86
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "orientationIn": "{Tapas_1.orientationDirectory}",
                "groundControlPointsFile": "Saisie-S3D.xml",
                "imageMeasurementsFile": "Saisie-S2D.xml",
                "ShowU": false,
                "NLFR": false,
                "Out": "GCPBasc___"
            }
        },
        "AperiCloud_2": {
            "nodeType": "AperiCloud",
            "position": [
                1230,
                -29
            ],
            "inputs": {
                "projectDirectory": "{Campari_1.projectDirectory}",
                "imagePattern": "{Campari_1.imagePattern}",
                "SH": "{Campari_1.SH}",
                "orientationDir": "{Campari_1.orientationDirectory}",
                "Out": "AperiCloud_campari.ply"
            }
        },
        "Campari_1": {
            "nodeType": "Campari",
            "position": [
                1001,
                34
            ],
            "inputs": {
                "projectDirectory": "{GCPBascule_1.projectDirectory}",
                "imagePattern": "{GCPBascule_1.imagePattern}",
                "inputOrientation": "{GCPBascule_1.orientationOut}",
                "SH": "{Tapas_1.SH}",
                "SigmaTieP": 0.5,
                "FactElimTieP": 20.0,
                "ViscInterne": 0.0,
                "NbIterEnd": 0,
                "Out": "Campari1000"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                1231,
                100
            ],
            "inputs": {
                "projectDirectory": "{Campari_1.projectDirectory}",
                "imagePattern": "{Campari_1.imagePattern}",
                "SH": "{Campari_1.SH}",
                "orientationDir": "{Campari_1.orientationDirectory}",
                "OffsetPly": {
                    "x": 609600.0,
                    "y": 6382300.0,
                    "z": 0.0
                },
                "Out": "C3DC_ofsetted.ply"
            }
        }
    }
}