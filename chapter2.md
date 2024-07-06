# Chapter 2 - Data Models and Query Language
1. Applications are usually built by representing one data model on top of another
* How is a model represented in the next lowest layer?

## Relational Model vs Document Model
2. Relational model was proposed by Edgar Codd in 1970.
* Data is organized into relations (tables)
* Each relation is a unordered collection of tuples (rows)
* Theoretical at first - to slow for older machines
* Success in the mid 1980's 

3. Relational origins in business data

4. **Network Model** and **heirarchial model** were alternatives, but lost out to relational model

### Birth of NoSQL
5. NoSQL is a bad name
6. Distributed, nonrelational database
7. Driving Forces:
* Need for greater scalability - very large datasets / high write throughput
* Certain queries not supported by relational model
* more dynamic model

### The Object-Relational Mismatch
8. Awkward translation layer between object oriented programming languages and SQL tuples 
* Also called **impedance mismatch**
9. Different ways of encoding information inside of SQL databases, some allow JSON/XML *with* quering 
10. NoSQL has better spacial locality than SQL. To represent something like a resume in a SQL database, you either need multiple queries, or a very messy multi table join. 
11. JSON style storage has an inherent One-To-Many tree like structure

### Many-To-One and Many-To-Many Relationships
12. Having several regions that users choose from is very easy with SQL - just have a regions table that we join with.
13. Limited join support with NoSQL. Data normalization means 'Many-to-one' relationships
14. **Many to one** relationships - 'many people live in one particular region'
15. With NoSQL, working with a join is something that is shifted to application code. 

### Are document Database repeating history?
16. Debate about how to represent join like relationships with NoSQL databases is very old - the earliest database systems had this problem as well.
17. IBM's *Information Management System*:
* Used a hierarchical model - in some ways similar to json
* Worked well for one to many relationships 
* Many-to-many difficult, no join support
* Developers had to choose whether they wanted to resolve references in application code, or duplicate data (normalization)
18. Prominent alternatives were the relational model (SQL), and the network model (obscure)

#### The network model
19. Network model standardized by the Conference on Data Systems Languages (CODASYL)
20. Network model - also known as the CODASYL Model
21. Generalization of the hierarchical model.
22. Records could have multiple parents, instead of just one. 
* ex: every user who lived in seattle could have it as a parent
23. Links more like pointers than foreign keys. 
24. Queries executed by following **access paths** (paths of links)
25. Problem - queries were very hard. If you didn't have a path, you were hosed.

#### The relational model
26. Much much simpler
27. A query optimizer is hidden from the user 
* Don't need to change your queries to handle a new index being added

### Relational vs Document Databases Today
28. Many differencces to consider, such as fault tolerance and concurency. 
29. Document model
* Schema flexibility
* Better spatial locality
30. Relational model
* Joins
* Many to many and many to one relationships

#### Which data model leads to simpler application code?
31. **Shredding** - Splitting a document like structure into multiple tables 
* Leads to very complex application code

32. Comes down to if we have a one to many relationship 

#### Schema Flexibility in the document model
33. Most document databases don't enforce a schema on documents
34. 'Schema on read' (document)  vs 'schema on write' (relational)
35. Document style is dynamically typed, relational is statically typed
36. The schema on read approach is beneficial when:
* Different kinds of objects, but it isn't practical to have each object have its own table
* External systems decide the structure of objects and they may change in the future

#### Data Locality for Queries
37. Documents are normally stored as strings, which encode the ifno for JSON, XML, etc. 
38. Locality advantage is only good when you use a large portion of the document. Generally, the database needs to load the entire document to look at a specific part of it. 
39. Document updates need to rewrite the entire thing.
40. Therefore, generally a good idea to keep the documents on the smaller side.

#### Convergence of Document and Relational Databases
41. Most modern relational databases allow for the storage and quering of XML files. (Including quering of items *inside* of XML files)
42. Support for JSON has been rapidly increasing as well

## Query Language for Data 
43. SQL is a **declarative** query language. IMS and CODASYL query **imparatively**
44. Imperative Langauges - tell the compter to perorm certain operations in a certain order
45. Declarative Langauges - Tell the computer what you want. You don't have to worry about implementation
46. Benefit of declarative languages is that database improvements don't break queries 


### Declarative Queriez on the Web
47. Javascript vs CSS updates to the DOM are an example of imperative vs declarative styling 

### MapReduce Querying 
48. **MapReduce** - programming model 
* used for processing large amounts of data in bulk across several machines
49. Found in several NoSQL databases, will discuss example in MongoDB
50. Neither declarative or fully imperative
* Code snippets define the logic of the query, which is called by the processing framework
51. Map and reduce functions must be pure
52. Recently added support for declarative query language: "aggregation pipeline"
* Philisophically similar to SQL

## Graph Like Data Models
53. Many-to-Many relationships can be handled by SQL databases, but there's a point where a more graph like approach is more natural 
54. Facebook - single graph
* vertices -  people, locations, events, checkins, and comments 
* edges - friends, who commented, locations between events                                                              

** Skipping the rest of the graph database stuff, for now **
