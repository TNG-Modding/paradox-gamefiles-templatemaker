subTypes = {
    "COMMON_RESOURCE": {
        "name": "Common Resource",
        "outputPath": "common/strategic_resources",
        "isDumpsContents": True,
        "isBom": False,
        "isTemplate": True,
        "files": [
            "resource/{{varname}}.txt"
        ]
    },
    "GFX_INTERFACE_ICONS_RESOURCES": {
        "name": "Gfx Interface Icons Resources",
        "outputPath": "gfx/interface/icons/resources",
        "isDumpsContents": True,
        "isBom": False,
        "isTemplate": False,
        "files": [
            "resource/{{varname}}_icon_gray.dds",
            "resource/{{varname}}_icon_large.dds",
            "resource/{{varname}}_icon.dds",
        ]
    },
    "INTERFACE_RESOURCE": {
        "name": "Interface Resource",
        "outputPath": "interface",
        "isDumpsContents": True,
        "isBom": False,
        "isTemplate": True,
        "files": [
            "resource/{{varname}}_interface.gfx"
        ]
    },
    "RESOURCE_LOCALIZATION": {
        "name": "Resource Localization",
        "outputPath": "localisation/english",
        "isDumpsContents": True,
        "isBom": True,
        "isTemplate": True,
        "files": [
            "resource/{{varname}}_l_english.yml"
        ]
    },
    "EVENT": {
        "name": "Events",
        "outputPath": "events",
        "isDumpsContents": True,
        "isBom": False,
        "isTemplate": True,
        "files": [
            "event/{{varname}}.txt"
        ]
    },
    "EVENT_LOCALIZATION": {
        "name": "Events Localization",
        "outputPath": "events",
        "isDumpsContents": True,
        "isBom": True,
        "isTemplate": True,
        "files": [
            "event/{{varname}}_l_english.yml"
        ]
    },
}