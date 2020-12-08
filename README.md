# FileMonster
A module for mass saving and loading of objects in files.

initialize file manager(only need one) - FileMonster()

### FileMonster methods
```
create() - creates a storage unit
e.g. storageunit = FileMonsterInstance.create()


save(storage) - saves a storage unit into a textfile
-storage parameter is a Storage instance
-storage parameter has to be loaded in before (save is only for saving opened storages, see next for saving new storages)


createsave(storage, filename, ask = True) - creates new files for new storages
-parameter 'ask' is for if a file with the same name as the 'filename' parameter exists,
it will ask for confirmation to overwrite the file (True = ask, False = don't ask)


load(filename) - loads storage unit
-returns specified storage instance object if it exists


showfiles() - prints a column of FileMonster file names


merge(*storages) - merge all storage instances into one
-All storage instances' contents passed in gets merged into one storage unit and is returned
```
### Storage methods
