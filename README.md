# SD

This program runs a Writter that operate on a protocol, this protocol is created to ensure integrity of Objects in distributed systems with competion and parallelism.

- The object is represented by a Topic



---
## Writer

Run Writter
> python3 Writter.py |NumberOfThreads| |Repeats| |TimeOut| |NamePrefix| |Topic| |ServerIP| |ServerPort| |IdPartitionControl| |IdPartitionContent|  
- **Repeats**: Number of Object changes for Thread (int)
- **NumberOfThreads**: Number of threads executed by Writter (int)
- **TimeOut**: Time in seconds for shutdown request when writters hasn o response (int)
- **NamePrefix**: Prefix used to intentify the Writter in Kafka enviroment (str)
- **Topic**: Name of topic reserved for Object (str)
- **ServerIP**: Ip of Kafka server thats topic is storaged (str)
- **ServerPort**: Port of Kafka server thats topic is storaged (str)
- **IdPartitionControl**: Id of partition that's used for control of access (int)
- **IdPartitionContent**: Id of partition that's used for store the Object representation (int)


Example:
>  


---
## Rules
 - Topic thas represent the Object must have ate leats 2 partitions, one for control e one for Object representation
