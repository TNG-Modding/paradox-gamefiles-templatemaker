# Intemplator

Create bodies of code with templates and json data blobs. Templates are combined with specs to create 

## Requirements

- None.

## Directions

- Define orders as are collections of calls to Intemplator in the `intemplator.json` file of your current directory. You must have "orders" defined.

```
    {
        "orders": [
            {
                "name": "Order name",
                "specFilePath": "./path/to/specFile",           # Path to the desired
                "templateDirectoryPath": "./path/to/specFile",  # Path to the diretory of the template, even one file templates need directories
                "outputDirectoryPath": "./path/to/specFile",    # Where the folder goes
                "disabled": false,                              # Whether this is ignored
                "dumpContents": true                            # Whether the content arrives as a folder or as the folders contents
            }
        ]
    }
```

- Define specs files that contain content that will populate your spec. You must have "specs" defined. The content is otherwise arbitrary.

```
    {
        "specs": [
            {
                "name": "Auth Service",
                "desc": "The authentication service.",
                "endpoints": []
            }
        ]
    }
```

- Run `intemplator go` or `intemplator run --template rbx-service-template --input ./specs/dischargeSpec.json --output ~/robowar/ReplicatedStorage/Source`
