### Lab 2: Search and Optimization

#### Due: Tues, Sept 22, 11:59pm.

Grading Criteria:

Exemplary: All tasks completed with care. Code is well-structured and documented.

Satisfactory: major criteria satisfied, but missing some implicit or explicit components (for example, short/incomplete answers to questions, missing files, poorly formatted code, etc) 

Unsatisfactory: One or more major criteria missing.

#### 

In this lab, you'll do a combination of coding and non-coding exercises with the goal of 
exposing you to core search concepts and providing more Python experience. You should add
a PDF (please title it yourname_lab2.pdf) to your repo containing the answers to all of
the written questions. For the code, be sure to push and commit your changes. 

#### Part 1:  Problem setup

For each of the domains below, set them up as a classic search problem. To do so, you should identify:
- The state variables 
- The actions
- The goal test.

1. Romania. Our agent needs to travel from Arad to Bucharest.
2. 15-puzzle. The classic sliding-tile puzzle. https://en.wikipedia.org/wiki/15_puzzle
	The goal is to get all the tiles in ascending order.
3. Chess. Consider the standard 8x8 board setup. 
4. Block-stacking. Another classic AI domain. Assume that we 
have a table full of blocks and a gripper arm which can 
pick up and place blocks. Our goal is to place A on top of B on top of C.
5. Water Jug Problem. https://en.wikipedia.org/wiki/Water_pouring_puzzle. Assume that we have three water jugs, one holding 8 liters, 
one holding 5 liters, and one holding 3 liters. They are not marked.

The goal is to get 4 liters in the first pitcher, and 4 liters in the second pitcher.


### Part 2: Search tracing

For this part we'll use [this simulator](search-visualizer.html) which illustrates the performance of different search algorithms. It shows the number of states expanded and the maximum size of the frontier, and lets you get a visual sense of how each algorithm behaves.

To begin, choose a grid size and add some walls; enough that the problem is interesting. 
Run each of the six algorithms and report the number of nodes explored and the maximum queue size.

Now that you have a better feel for how each algorithm works, let's focus on BFS, DFS, Greedy, and A*.
For each of these problems, draw a set of walls that illustrates the strengths of the algorithm; that is, a 
configuration that the algorithm can solve easily. Then draw a set of walls that illustrates the algorithm's 
weaknesses, and shows it struggling to reach the goal. 

Take a screenshot of each configuration and include those in your PDF. 


Part 3: Mars Rover 

In this part, you'll get some more experience with Python, and with the
concept of search as problem-solving. 

Python features to look out for:

- List comprehensions
- functions as objects
- Polymorphism
- named and default parameters

You should complete this yourself, without AI assistance. 

One of the first applications of search was in robot planning. In this setting, we define a state, a goal, and a set 
of actions. Our actions transform the state, creating a search space. We can then apply our classic search
algorithms to this problem.

We'll start with a simple version of the Mars Rover problem. This can be found in mars_planner.py. 
I've also included some unit tests to help you get things working. In later assignments, I'll ask you to build 
your own unit tests.

There are three locations: the station, the sample site, and the charger.
Our rover should travel from the station to the sample,  pick the sample up,
bring the sample back to the station, and then go to the charger to recharge. 

It will do this by finding a series of *actions* to take. Those actions should lead us to a state that satisfies the *goal*.

In this case, our state has five variables, indicating robot location, sample location, whether we're holding the sample, and whether we're charged. 
(there's also a pointer to the previous state.)

We also have a set of actions. Each action is implemented as a function that can be applied to a state.
This approach allows us a great deal of flexibility to solve a variety of problems and easily add or change 
our actions without breaking our existing code.

The RoverState then has a *successor function* that applies possible actions to our current state
and returns a list of tuples, which are the adjacent states and the action needed to get there.

1. We need an __eq__ function in RoverState to detect repeated states. Implement this. 
Two states are equal if all of their instance variables are equal. I have provided a unit test that you can use to check this.


2. Now we need to create a *goal function*. This is a function that will return True if a state is the goal state,
and False otherwise. I've provided an example goal: a battery_goal test that returns True if we are at the battery and False otherwise. 

Create a mission_complete goal function that returns True if we are at the battery, charged, and the sample is at the station.


3. Run this with the included BFS and DFS implementations. Extend each of these to count the number of states generated. 
Print this out at the end. I have provided unit tests for BFS and DFS. 


4. Extend the depth_first_search function to implement *depth_limited_search* by using the optional *limit* parameter. 
When you are generating successors, only go to depth=limit in the search tree. You should extend the RoverState class 
by adding a depth variable to keep track of this. Add a unit test for DLS. 

 
5. Add an additional function for *iterative deepening search*. It should call depth-limited search. Count the total number of states generated. Add a unit test for this.


6. We found out that the rover cannot extract the sample on its own; it needs a tool. Extend the program as follows: 

Add a holding_tool instance variable to RoverState. Update your constructor and eq methods correctly.
add the following actions: 
- pick_up_tool 
- drop_tool 
- use_tool. 

Pick_up_tool should return a new state with the holding_tool 
variable set to True, drop_tool should return a new state with the holding_tool variable set to false, and use_tool should 
return a new state with the sample_extracted variable set to True, but only if we are holding the tool.

Run each of the four algorithms (breadth_first_search, depth_first_search, depth_limited_search, iterative deepening search) 
on this new problem and count the number of states generated. 

Please add to your written answers a table with the state data for each of the questions above.

### Part 4: OR-tools.

In this portion of the lab, you'll get familiar with OR-tools, which you'll use in Project 2.

OR-tools is a commercial package for doing optimization. It turns out that a lot 
of interesting problems can be framed this way. 

The great thing about OR tools is that the solvers are built in. That means 
that we can focus our energy on representing problems. This is our first 
introduction to knowledge-based programming. This is a style of program design 
where the focus is on representing complex problem knowledge (constraints in 
this case) and then handing that knowledge to an automated solver to find a 
solution.

To begin, get ortools installed and run the included code in nurse_scheduler.py. 

Read through it and see if you can understand what it does. Then follow the 
instructions below and add a section to your lab explaining what you learned.




Increase the number of nurses to 7, and add shift requests for them. Does this 
make the problem easier or harder? How can you tell?

Does this make the problem easier or harder? How can you tell?

Decrease the number of nurses to 3 and remove the extra shift requests. 
Does this make the problem easier or harder? How can you tell?

Return to five nurses, but increase the number of shifts to five, and 
update the shift requests. Does this make the problem easier or harder? 
How can you tell?

In this problem, we've separated the problem knowledge from the 
algorithmic knowledge. How does this help us in engineering a solution?