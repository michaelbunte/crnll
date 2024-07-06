# Chapter 1 - Reliable, Scalable, and Maintainable Applications
1. Many apps today are data-intensive, not compute intensive
2. CPU not usually a limiting factor
3. Factor is often the amount and complexity of data, as well as the rate at which the data is changing at.

## Thinking About Data Systems
4. Combining tools to provide a service, API hides implementation details. You've created a new data system with smaller parts. "You are now a data system designer"

5. Three areas addressed in this book
* Reliability - System should still work when there are faults
* Scalability - As the system takes in more data, are there 'easy' ways to handle the growth
* Maintainability - Can developer work "productively" in the ecosystem

## Reliablility

6. Expectations for software include:
* Does what the user expects
* Can tolerate the user using the software strangely
* Performance is decent for the expected use case
* Prevents unauthorized access

7. Fault $\ne$ Failure
* Fault - a component behaves incorrectly
* Failure - System as a whole stops providing service to the user

### Hardware Faults
8. MTF (Mean time to failure) for disks is around 10 - 50 years
* With 10,000 disks, this means 1 fails a day

9. Historically, multi machine redundancy was rare, given that a backup could restore a system fairly quickly

10. However, large increase in multi machine computing => more hardware faults

11. Move towards systems that can tolerate the loss of entire machines 

### Software Errors
12. No quick solution - just careful thinking about assumptions and interactions in the system, as well as 
* Testing
* Process isolation
* Measuring
* Monitoring
* Constant checking of what it is supposed to guarantee 

### Human Errors
13. Configuration errors are the leading cause of outages
14. Systems use the following approaches to make their systems reliable, despite humans not being so reliabel
* Systems designed in a way that makes it hard for people to make errors. Such as apis that encourage doing things correctly, and make it harder to do things incorrectly. Balance between restrictivity and freedom!
* Try to decouple people from where they make mistakes from where they can cause failures. Such as creating sandbox environments
* Thorough automated testing 
* Fast rollback of changes, gradual deployment
* Tools for computing data
* Good management and practice


### How Important is Reliability
15. Tradoff between development cost and reliability. However, cutting corners is bad!!!

## Scalability
16. 'x scales' or 'y scales' is to simple of a description
* Better to say, "if a system grows in a certain manner, how do we cope with the growth?" or "How can we add resources to handle to load?"

### Describing Load
17. Load is described by **Load Parameters**

18. Twitter Example
* Twitter has around a 12k requests a second 
* Twitter needs to handle "posting tweets" and "home timeline reads"
* Approach one:
  * Posting a tweet goes into a huge table
  * Requesting to see your timeline requires a query to this table, that joins with who the user follows
* Approach two:
  * Each user has a cache of their own timeline.
  * Whenever anyone posts a tweet, they need to look up who's following them, and post in their caches
* Modern Twitter uses a hybrid approach. There are caches, but celebrities also have a global table to prevent huge amounts of writing upon their posts. 

### Describing Performance
19. Two methods of describing performance given a load:
* When you increase a load parameter and keep the resources the same, how is the performance of the system affected?
* When you increase a load parameter, how many resources do you need to keep the performance the same?

20. Latency vs Response Time
* Response time: What the client sees
  * Time to process the request
  * Network delays
  * Queuing Delays
* Duration that a request is waiting to be handled 

21. Best to describe performance in percentiles, mean/median leaves out a considerable amount of info.
22. **Tail Latencies** - High percentiles of response times
23. Amazon describes response times for internal services in terms of the 99.9th percentile. Those with the slowest requests usually have made the most purchases, important to keep them happy. However, optimizing 99.99th percentile was deemed to expensive. 
24. Percentiles are used in *Service Level Objectives* and *Service Level Agreements* 
25. **Tail latency amplification** - Several requests in parallel that require all requests to be made leads to a higher proportion of response times from the user perspective

### Approaches for Coping with Load
26. Historically, the advice was to build a system for a single node, and then scale horizontally once it is required.
27. No such thing as a one size fits all scaleable architecture. 
28. "An architecture that scales well is built using assumptions about which operations are common and which are rare"

## Maintainability
29. Three design principles for software systems:
* Operability - Make it easy for operations teams to keep the system up and running. 
* Simplicity - Remove complexity from the system so new engineers can understand the system
* Evolvability - Make it easy for engineers to make changes to the system 

### Operability: Making Life Easy for Operations 
30. Operation teams are responsible for:
* Monitoring the health of the system
* Restoring the health of the system
* Tracking down causes of problems
* Keeping software and platforms up to date 
* Monitor how systems affect each other. Can be used to proactively avoid problematic changes
* Establish tools for deployment, configuration management, etc
* Perform complex maintence tasks
* Maintain the security of the system as changes are made
* Define processes that make the operations perdictable
* Preserve knowledge about the system

31. In order to make routine things easy, data systems can:
* Provide visibility into the runtime behavior of the system (good monitoring)
* Support for automation and integration with tools
* Avoid dependency on a single machine
* Provide good documentation - operational models
* Default behavior, but also adminstrators can override defaults
* Self-healing behavior
* Exhibiting predictable behavior

### Simplicty: Managing Complexity
32. **Big Ball of Mud** - Name for a complex system
33. "One of the best tools we have for reducing complexity is **abstraction**" (yay abstraction) 

### Evolvability: Making Change Easy
34. **Agile** working patterns - framework for adapting to change
* tools and patterns that are useful for developing software in a changing environment

