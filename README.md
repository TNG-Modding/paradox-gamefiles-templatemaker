# Intemplator

Generate hundreds of Stellaris modding files effortlessly using Jinja2 templates and json. Need a common file, localisation file, and static modifier for every ethic, for every shipset, for every component? Child's play.

## Installation

- Install python.
- Checkout this repo.
- `cd` into the repo.
- `python setup.py install`

## Example of Creating a Faction for Every Ethic

- Define a template file (one for the faction file, one for static modifiers, one for localisation, etc) using Jinja2 python syntax, like so:

`"./templates/faction/{{varname}}_faction.txt"`
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

- Define specs files that contain content that will populate your spec. You must have "specs" defined. The content is otherwise arbitrary. For every item in the specs array, we will create a new file. The above template will create a fanatic militarist xenophobe faction.

`./specs/moderateFactions.json`
```
{
    
    "specs": [
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
}
```



- Create a folder called `intemplator` in the root directory of your mod repo.
- Create `./intemplator/intemplator.json`
- Create an order for every template+spec pair. For instance, this order create a `common/pop_faction_type`

```
{
    "orders": [
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
}
```

- Run `intemplator go` in the folder where the `intemplator.json` file is to generate files.
