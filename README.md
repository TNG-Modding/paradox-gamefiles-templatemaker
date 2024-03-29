# Intemplator

Generate hundreds of modding files effortlessly using Jinja2 templates and json. Need a common file, localisation file, and static modifier for every ethic, for every shipset, for every component? Child's play.

## Installation

- Install python.
- Checkout this repo.
- `cd` into the repo.
- `python setup.py install`

## Example of Creating a Faction for Every Ethic

- Define a template file (one for the faction file, one for static modifiers, one for localisation, etc) using Jinja2 python syntax, like so:

`"./intemplator/templates/faction/{{varname}}_faction.txt"`
```
##############################
# {{Faction}} Faction
##############################

{{varname}} = {
	election_header = "GFX_faction_header_yellow"
	{% if isMilitarist == 2 %}guiding_ethic = ethic_militarist
	{% elif isXenophobe == 2 %}guiding_ethic = ethic_xenophobe
	{% elif isEgalitarian == 2 %}guiding_ethic = ethic_egalitarian
	{% elif isMaterialist == 2 %}guiding_ethic = ethic_materialist
	{% elif isPacifist == 2 %}guiding_ethic = ethic_pacifist
	{% elif isXenophile == 2 %}guiding_ethic = ethic_xenophile
	{% elif isAuthoritarian == 2 %}guiding_ethic = ethic_authoritarian
	{% elif isSpiritualist == 2 %}guiding_ethic = ethic_spiritualist
	{% else %}guiding_ethic = ethic_militarist{% endif %}
    
    ...
```

- Define specs files that contain content that will populate your spec. The content must be an array of blobs. Each blob will get a piece of content per order. So far, we are creating a fanatic militarist xenophobe faction.

`./intemplator/specs/moderateFactions.json`
```
[
    {
        "varname": "fanatic_militarist_xenophobe_faction",
        "faction": "fanatic militarist xenophobe",
        "Faction": "Fanatic Militarist Xenophobe",
        "adjective": "fanatic militarist xenophobe",
        "Adjective": "Fanatic Militarist Xenophobe",
        "isMilitarist": 2,
        "isPacifist": 0,
        "isXenophobe": 1,
        "isXenophile": 0,
        "isEgalitarian": 0,
        "isAuthoritarian": 0,
        "isMaterialist": 0,
        "isSpiritualist": 0
    }
]

```



- Create a folder for our intemplator files in the root directory of your mod repo with an `orders.json` file in it.
- Create an order for every template+spec pair. For instance, this order create a `common/pop_faction_type`

`./intemplator/orders.json`
```
[
    {
        "name": "Moderate Faction Defines",
        "specFilePath": "./specs/moderateFactions.json",
        "templateDirectoryPath": "./templates/faction", # The folder that contains the template files
        "outputDirectoryPath": "../common/pop_faction_types", # Which folder to output to
        "disabled": false, # Whether this order is ignored
        "dumpContents": true, # Whether the template folder is copied into the output directory (false), or the contents are dumped into the output (true)
        "isBom": false # Take UTF-8 template files and create UTF-8-BOM files for localisation
    },
]

```

- Run `intemplator go` in the folder where the `orders.json` file is to generate files.
