## Building

    hatch build --clean

### Debugging

Python VSCODE launch configurations are provided for each of the 
examples and for the pytest tests.


## Testing

    playwright install

*Then:*

    hatch test [--headed]

## Publish 

    hatch build --clean
    hatch publish

Or publish to local repo

    hatch build --clean
    hatch publish -r pypicloud
