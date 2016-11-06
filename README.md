# README


Download the script and put it anywhere.


Create a function like this in your bash_profile:

```
function createDirr() {
        wd="$(pwd)"
        python pathToMakeDirrFolder/makedirr.py -d $1 -w "${wd}"
}
```
Wherever your location is when you call createDirr(), the directory will be created in your working directory.


Call it like this: 
```
createDirr test
```

And a new folder will be created with the name test. 




