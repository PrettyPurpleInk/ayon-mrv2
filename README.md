# MRV2 addon for AYON
This addon adds action plugins to other AYON addons to launch MrViewer 2. The addon does not contain MRV2 executables, only allows you to set them up in the addon settings. It is based on the DJV addon for AYON.

## Create package
To create addon package run `create_package.py` script in the root of repository.

```shell
python create_package.py
```

That will create `./package/mrv2-<version>.zip` file which can be uploaded to AYON server.
