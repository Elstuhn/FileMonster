# FileMonster
A module for mass saving and loading of objects in files.

initialize file manager(only need one) - variable = FileMonster()

### FileMonster methods
```
create() - creates a storage unit
e.g. storageunit = FileMonsterInstance.create()


save(storage) - saves a storage unit into a textfile
-storage parameter is a Storage instance
-storage parameter has to be loaded in before (save is only for saving opened storages, see next for saving new storages)


createsave(storage, filepath, ask = True) - creates new files for new storages
-parameter 'ask' is for if a file with the same name as the 'filename' parameter exists,
it will ask for confirmation to overwrite the file (True = ask, False = don't ask)
-if you want your saved file to be called "userinfo", filepath will have to include it
e.g C:\Users\user\Downloads\userinfo instead of just C:\Users\user\Downloads

load(filepath) - loads storage unit
-returns specified storage instance object if it exists


showfiles() - prints a column of FileMonster file names


merge(*storages) - merge all storage instances into one
-All storage instances' contents passed in gets merged into one storage unit and is returned
```
### Storage methods
```
bulkadd(*objects) - adds multiple objects to storage unit
-upon build adding objects, label for each object will be asked. If label is the same, object gets added to the list corresponding to label


add(label, object_) - adds an object into specified label


remove_label(label) - specified label and its contents go poof


remove_elem(label, pos = 0) - removes certain element from label(each label corresponds to a list which contains its objects)


bulkremove(*labels) - there was a bulkadd so why not a bulkremove?


clear() - I eat up all storage contents and now its empty


showlabels() - shows all storage unit labels


showstorage() - literally prints the raw storage out of dictionary type


getstorage() - returns raw storage


chooseobj(label, pos = 0) - returns an object from specified position from the specified label


prettyshow() - shows the storage in a beautiful way 
```

## Things to note
**⋅When importing this file, make sure to initiate all classes and functions that are included in the storages**

   -For example: if your storages includes an instance of class `Test`, initiate class `Test` before loading a storage that includes class `Test`
  
**⋅If you want to modify storages, it's better to use an interpreter**

   -You could do `storage.getstorage() = dictionary object` if you're too lazy to modify the storage bit by bit, just make sure that the dictionary object is in the same format as FileMonster's storages. `{'label' : [items]}` for example `{'label': ['hello', 123, ['poop', 'hehe']]}`
