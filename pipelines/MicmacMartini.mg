{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "Martini": "1.1.1",
            "CameraInit": "9.0",
            "Tapas": "1.1.1",
            "TapiocaMulScale": "1.1.1",
            "AperiCloud": "1.1.1",
            "SetExif": "1.1.1",
            "MicMacProject": "1.0",
            "C3DC": "1.1.1"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                170,
                -88
            ],
            "inputs": {}
        },
        "MicMacProject_1": {
            "nodeType": "MicMacProject",
            "position": [
                167,
                37
            ],
            "inputs": {
                "input": "{CameraInit_1.output}"
            }
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                976,
                1
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                976,
                161
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}",
                "mode": "MicMac"
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                787,
                -3
            ],
            "inputs": {
                "projectDirectory": "{Martini_1.projectDirectory}",
                "imagePattern": "{Martini_1.imagePattern}",
                "calibrationModel": "FraserBasic",
                "InOri": "{Martini_1.orientationDirectory}",
                "SH": "{Martini_1.SH}",
                "Out": "Relative"
            }
        },
        "Martini_1": {
            "nodeType": "Martini",
            "position": [
                592,
                1
            ],
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "SH": "{TapiocaMulScale_1.PostFix}"
            }
        },
        "SetExif_1": {
            "nodeType": "SetExif",
            "position": [
                173,
                158
            ],
            "inputs": {
                "projectDirectory": "{MicMacProject_1.projectDirectory}",
                "imagePattern": ".*.(jpg|jpeg|JPG|JPEG|png|PNG|tif|tiff|TIF|TIFF)",
                "setF35": true
            },
            "internalInputs": {
                "comment": "Writes Exif metadata to images. \nRun separately before running the entire pipeline.",
                "color": "#5c3566"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                400,
                0
            ],
            "inputs": {
                "projectDirectory": "{SetExif_1.projectDirectory}",
                "imagePattern": "{SetExif_1.imagePattern}"
            }
        },
        "AperiCloud_2": {
            "nodeType": "AperiCloud",
            "position": [
                976,
                321
            ],
            "inputs": {
                "projectDirectory": "{Martini_1.projectDirectory}",
                "imagePattern": "{Martini_1.imagePattern}",
                "SH": "{Martini_1.SH}",
                "orientationDir": "{Martini_1.orientationDirectory}",
                "Out": "AperiCloud_martini.ply"
            }
        }
    }
}