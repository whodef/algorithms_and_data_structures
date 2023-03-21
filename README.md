# Algorithms and data structures
## 'Python Developer Plus' Course. Sprint 15, 16, 17

___
## Useful links
### [Playground](https://www.sololearn.com/compiler-playground/cEpZKIpYYm0o/) for unlimited mistakes :D

___

## What is an Algorithm?
The word Algorithm means ”A  set of rules to be followed in calculations or other problem-solving operations” Or ”A procedure for solving a mathematical problem in a finite number of steps that frequently by recursive operations“. 

Types of Algorithms:
There are several types of algorithms available. Some important algorithms are:

1. Brute Force Algorithm: It is the simplest approach for a problem. A brute force algorithm is the first approach that comes to finding when we see a problem.


2. Recursive Algorithm: A recursive algorithm is based on recursion. In this case, a problem is broken into several sub-parts and called the same function again and again.


3. Backtracking Algorithm: The backtracking algorithm basically builds the solution by searching among all possible solutions. Using this algorithm, we keep on building the solution following criteria. Whenever a solution fails we trace back to the failure point and build on the next solution and continue this process till we find the solution or all possible solutions are looked after.


4. Searching Algorithm: Searching algorithms are the ones that are used for searching elements or groups of elements from a particular data structure. They can be of different types based on their approach or the data structure in which the element should be found.


5. Sorting Algorithm: Sorting is arranging a group of data in a particular manner according to the requirement. The algorithms which help in performing this function are called sorting algorithms. Generally sorting algorithms are used to sort groups of data in an increasing or decreasing manner.


6. Hashing Algorithm: Hashing algorithms work similarly to the searching algorithm. But they contain an index with a key ID. In hashing, a key is assigned to specific data.


7. Divide and Conquer Algorithm: This algorithm breaks a problem into sub-problems, solves a single sub-problem and merges the solutions together to get the final solution. It consists of the following three steps:

   - Divide
   - Solve
   - Combine


8. Greedy Algorithm: In this type of algorithm the solution is built part by part. The solution of the next part is built based on the immediate benefit of the next part. The one solution giving the most benefit will be chosen as the solution for the next part.


9. Dynamic Programming Algorithm: This algorithm uses the concept of using the already found solution to avoid repetitive calculation of the same part of the problem. It divides the problem into smaller overlapping subproblems and solves them.


10. Randomized Algorithm: In the randomized algorithm we use a random number so it gives immediate benefit. The random number helps in deciding the expected outcome.


## What is Data Structure

>A data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.

A data structure is not only used for organizing the data. It is also used for processing, retrieving, and storing data. There are different basic and advanced types of data structures that are used in almost every program or software system that has been developed. So we must have good knowledge about data structures. 

### Classification of Data Structure:

![ClassificationofDataStructure-660x347](https://user-images.githubusercontent.com/7266512/221867187-ffc2297f-bb90-41f4-930d-3f28040bc4ed.jpg)


* __Linear data structure__: Data structure in which data elements are arranged sequentially or linearly, where each element is attached to its previous and next adjacent elements, is called a linear data structure. 
*Examples of linear data structures are array, stack, queue, linked list, etc.*
   * Static data structure: Static data structure has a fixed memory size. It is easier to access the elements in a static data structure. 
*An example of this data structure is an array.*
   * Dynamic data structure: In dynamic data structure, the size is not fixed. It can be randomly updated during the runtime which may be considered efficient concerning the memory (space) complexity of the code. 
*Examples of this data structure are queue, stack, etc.*
* __Non-linear data structure__: Data structures where data elements are not placed sequentially or linearly are called non-linear data structures. In a non-linear data structure, we can’t traverse all the elements in a single run only. 
*Examples of non-linear data structures are trees and graphs.*


For example, we can store a list of items having the same data-type using the array data structure.

![array-2](https://user-images.githubusercontent.com/7266512/221869287-0693c64e-8c52-4568-8c29-d9bf006f40f8.png)

[More...](https://www.geeksforgeeks.org/data-structures/)

___

## Semantic Commit Messages
See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

### Example:

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```


More Examples:

- `feat`: new feature for the user, not a new feature for build script
- `fix`: bug fix for the user, not a fix to a build script
- `docs`: changes to the documentation
- `style`: formatting, missing semi colons, etc; no production code change
- `refactor`: refactoring production code, eg. renaming a variable
- `test`: adding missing tests, refactoring tests; no production code change
- `chore`: updating grunt tasks etc; no production code change
- `perf`: a commit that improves performance, without functional changes
- or `build`, `ci`, `revert`, etc.

Less specific cases:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation

References:

1. https://www.conventionalcommits.org/
2. https://seesparkbox.com/foundry/semantic_commit_messages
3. http://karma-runner.github.io/1.0/dev/git-commit-msg.html
___
