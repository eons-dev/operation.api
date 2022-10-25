# APIE Operation Endpoint

APIE Operations provide a consistent means of interacting with any resource in any way. This is a generalized system without many restrictions.

For more information on how operations can be used with apie, see [the apie Resource Paradigm](https://github.com/eons-dev/bin_apie/#resource-paradigm).

## What You Need to Know

There's only really one key setting for an operation: its name.  
The name of the operation determines what method is called when its `Call()`ed. The required method is "{name}_implementation". For example, the "list" operation would call "list_implementation()".

You are also provided `PreOperation()` and `PostOperation()` hooks, should you need them. 

All other settings can be found in [apie.Endpoint](https://github.com/eons-dev/bin_apie/#api-endpoints) and [eons.Functor](https://github.com/eons-dev/lib_eons/#functors).