# Linear Probe

Linear Probing is a form of open addressing, which is a method used to resolve collisions in a hash table.

## Alterations to the original hash table

### Add

### Search

### Delete

#### Rehashing

## Clustering in Linear Probe Table

A cluster is a sequential set of elements in a hash table.

Once a cluster forms, it tends to grow larger as more elements are inserted.

Clusters are bad for a Linear Probe Table because they increase the probe length, i.e. the number of spots that have to be probed for a certain element.

Adding an element with hash value $N$ can drastically increase the search time for other keys with the hash values other than $N$.

Clustering also causes deleting an element in the hash table to be slower as we have to rehash the entire cluster.

## Load Factor consideration in Linear Probe Table

In a linear probe table, the load factor must be kept under 1/2 or at least 2/3.

This is because for hash tables with load factor > 0.5, there is a higher tendency for clustering to occur.

One way to reduce the load factor is by resizing the whole hash table.