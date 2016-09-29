JSSP
===================

JSSP is a Job Shop Scheduling problem solver using a Genetic Algorithm implementation. Given a finite set of jobs, each consisting of a series of operations, with each operation being performed by a given machine in a set amount of time. It must also be taken into account that each operation can have other operations as dependencies and some operations can be performed in parallel. The goal of this program is to find an optimal arrangement of operations by minimizing the *makespan*. The makespan can be defined as the total time to perform all of the operations.

Jobs and Operations representation
-------------


Evolutionary aspect
-------------
Each series of operations is represented by a *genome*, which in JSSP is a list of Operation objects. In this genome, order of each element indicates which operation should be performed first.