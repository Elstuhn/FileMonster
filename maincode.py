from time import sleep
import pickle
import typing as t
import os
from collections import defaultdict

fileopened = {}
'''Notes:
    Saved files will automatically have a .fm behind indicating that it is a filemonster file
    When saving/loading files, filename need not have .fm behind (it'll be automatically added))'''
class SystemError(Exception):
    pass

def mergedict(storage1, storage2):
    keys = list(storage1.storage.keys())
    for i in storage2.storage:
        if i in keys:
            storage1.storage[i] = [storage1.storage[i], storage2.storage[i]]
            del storage2[i]

class FileMonster(defaultdict):
    
    def __init__(self, *args, **kwargs):
        super().__init__(list, *args, **kwargs)
        
    def create(self):
        return Storage()

    def save(self, storage):
        for i in fileopened:
            if fileopened[i] == hex(id(storage)):
                with open(i+".fm", "wb") as file:
                    pickle.dump(storage, file)
                return
        raise SystemError("Storage was not found.")

    def createsave(self, storage, filename : str, ask : bool = True):
        if ask:
            try:
                open(filename+".fm", "r")
                open(filename+".fm", "r").close()
                _ = input("It looks like you have a file with the same name. Would you like to overwrite it? (Y/N)\n")
            
                while _.lower() not in ["y", "n"]:
                    _ = input("It looks like you have a file with the same name. Would you like to overwrite it? (Y/N)\n")

                if _.lower() == "n":
                    print("Operation cancelled.")
                    return
                
            except:
                pass
        
        with open(filename+".fm", 'wb') as file:
            pickle.dump(storage, file)
            
        if ask:
            print("Saved file in", filename+".fm") 

    def load(self, filename : str):
        
        try:
            open(filename+".fm", "r")
            open(filename+".fm", "r").close()

        except:
            raise SystemError(f"Filename '{filename}' does not exist.")
        
        with open(filename+".fm", 'rb') as read:
            pickled = pickle.load(read)
            fileopened[filename] = hex(id(pickled))
            return pickled

    def showfiles(self):
        print("List of files:")
        files = [f for f in os.listdir() if all([os.path.isfile(f), ".fm" in f])]
        if not len(files):
            print("No FileMonster files found.")
        for i in files:
            print(i)

    def merge(self, *storages):
        if len(storages) == 1 or not len(storages):
            raise SystemError("Need 2 or more Storage objects to merge")
        newstorage = storages[0]
        #keys = list(newstorage.storage.keys())
        for i in storages[1:]:
            if not isinstance(i, Storage):
                raise SystemError("Arguments must all be Storage objects")
            
            #keysadd = list(i.storage.keys())
            #for labels in keys:
                #if labels in keysadd:
                    #mergedict(newstorage, i)
                    
            #newstorage.storage.update(i.storage)

            for k, v in i.storage.items():
                newstorage.storage[k].extend(v)
            
        return newstorage
            
        

class Storage():
    def __init__(self):
        self.storage = {}

    def __str__(self):
        return "f<Storage Object {self} at "+hex(id(self))+">"

    def __repr__(self):
        return self.storage
        
    def bulkadd(self, *objects):
        for i in objects:
            print(i)
            label = input("\nPlease enter the label you want for this object.\n")

            try:
                self.storage[label].append(i)
                        
            except:
                self.storage[label] = [i]

    def add(self, label : str, object_ : t.Any):

        try:
            self.storage[label].append(object_)
        except:
            self.storage[label] = [object_]
        
        return


    def remove_label(self, label : str):
        try:
            self.storage[label]
        except:
            raise SystemError(f"{label} was not found in data storage unit")

        del self.storage[label]

    def remove_elem(self, label : str, pos : int = 0):
        try:
            self.storage[label]
        except:
            raise SystemError(f"Label {label} was not found.")

        try:
            self.storage[label][pos]
        except:
            raise SystemError("Position is out of range.")

        del self.storage[label][pos]

    def bulkremove(self, *labels):
        if not len(labels):
            raise SystemError(f"Missing arguments.")
        
        invalid = 0
        valid = 0 
        for i in labels:
            
            try:
                self.storage[i]
                valid += 1
            except:
                invalid += 1
                continue
            
            del self.storage[i]

        if invalid:
            print(f"{invalid} invalid labels were detected.")
        print(f"{valid} valid labels and their corresponding data has been deleted.")

    def clear(self):
        self.storage = {}

    def showlabels(self):
        labels = []
        print("Labels:")
        for keys in self.storage:
            print(keys)
            labels.append(keys)
        return labels

    def showstorage(self):
        print(self.storage)

    def getstorage(self):
        return self.storage
    
    def chooseobj(self, label : str, pos : int = 0):
        try:
            self.storage[label]
        except:
            raise SystemError(f"Label {label} was not found.")

        try:
            self.storage[label][pos]
        except:
            raise SystemError("Position is out of range.")

        
        return self.storage[label][pos]

    def prettyshow(self):
        count = 1
        for i in self.storage:
            print(f"\nLabel {count} : {i}")
            sleep(0.5)
            print("Content:")
            sleep(1.2)
            for z in self.storage[i]:
                print(z)
            count += 1
            sleep(1.7)
