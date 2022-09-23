

To reset the API code run:

```
make setup
```

This removes the api code directory and copies it back from the git
repo - ../../app - which hopefully will have the latest version
of the code.

To run, first build the Docker image and then bring it up.

```
make build
make up
```

