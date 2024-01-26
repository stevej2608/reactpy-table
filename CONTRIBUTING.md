## Building

    poetry install --no-root

### Debugging

Python VSCODE launch configurations are provided for each of the 
examples and for the pytest tests.


## Testing

    playwright install

*Then:*

    pytest [--headed]

## Publish 

    rm -rf dist && poetry build
    poetry publish

Or publish to local repo

    poetry publish -r pypicloud
