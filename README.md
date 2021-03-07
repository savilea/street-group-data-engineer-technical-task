# street-group-data-engineer-technical-task

Designed to be run on Google Cloud Dataflow. The task would be triggered by a google.storage.object.finalize occurring on the relevant Google Cloud Storage location.

Dataflow was chosen as the data pipeline as it is a managed service from Google cloud for executing a wide variety of data processing patterns and integrates nicely with apache beam.  Moreover it can be combined with other service offerings such as the operations suite for monitoring and error logging should it be required.  Moreover, the Dataflow service lends itself to distributed parallel processing and optimises many of these tasks automatically including;
-	Partitioning data & distributing worker code to Compute Engine instances for parallel processing.
-	Optimizes the dataflow execution graph for the most efficient performance and resource usage. 
-	Makes on-the-fly adjustments to resource allocation and data partitioning, such as Autoscaling and Dynamic Work Rebalancing. 

Each of these aids the Dataflow service in executing tasks as quickly and efficiently as possible.

Pricing is at per-second billing and if the task were run on a batch dataflow worker type would incur the below pricing; which would lead to the task costing a fraction of a dollar per month. 

Dataflow Worker Type	- Batch 

vCPU			- $0.0672000
(per hour)

Memory			- $0.0042684
(per GB per hour)

Data Processed 		- $0.01417

