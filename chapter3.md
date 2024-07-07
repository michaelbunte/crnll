# Chapter 3 - Storage and Retrieval
1. It's a good idea to understand what is happening under the hood!

## Data Structures That Power Your Database
2. Simplest Database: 
* Key value store that appends on writes, and greps on reads
* Good for writes, terrible for reads
3. Indexes are additional structures. They can slow down writes.

### Hash Indexes - Big idea of Bitcask
4. Useful to have a separate hash table data structure that maps keys with byte offsets
5. We currently only append to the file. Better to break the file into segments. We can sometimes perform compaction to get rid of old pairs. 
6. Each segment has a hash table. To find a value, we check the most recent hashmap, then the second most recent ...
7. file format - csv isn't great. easier to encode the the length, and then the raw string
8. To handle deletions, need some kind of "tombstone" flag
9. To handle crashes, need to record in memory hash tables on disk
10. Checksums to remove corrupted data
11. Only one writer thread to handle concurrency
12. Appending is faster than random writes. 
13. Immutability makes concurrency and crash recovery much easier
14. Merging old segments prevents file fragmentation
15. Limitations of hash tables
* Hash table must fit in memory. If too large, must go on disk, and is very very slow
* Range queries are not efficient - can't scan over keys in a range

### SSTables and LSM-Trees
16. Simple change to segment files - require that key value pairs are sorted by key 
* Format is called "Sorted String Table"
* Also require that each key only appears once in a merged segment file (which is already guaranteed by the compaction process)
17. Benefits of SSTables
* Merging tables is easy - use mergesort
* Don't need large hashmaps any more - can use in memory tables

#### Constructing SSTables
18. We can make our storage engine work by
* When writes come in, add it to a in memory balanced tree data structure (memtable)
* When it gets bigger than a threshold, write to an SSTable
* In order to serve a read request, try to find a key in a memtable, then the most recent on disk segment, then the next older segment
* Once in a while, run a merge and compaction algorithm

19. The issue with this is that if we crash, data in the memtable will be lost. Therefore, we will create a disk log of all of the writes

#### Performance Optimizations
20. Searches for keys that do not exist are slow - bloom filters can help with this 

### B-Trees

