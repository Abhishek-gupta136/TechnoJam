# TechnoJam Solutions

Contains all the solution of the questions. Here are the approaches : 

Question 1 : First for all we create a 2D list  then iterate the for loop in range of 2 to n+1. Initialize the list by [1,] 
and accsse the last index of value then again ietrate the for loop range of length of value -1 and add the jth and jth +1 value and append in list which is initialize. after the append 1 in last of list then initialize list append in 2D list.

Time complexity is O(n^2).
Space complexity is O(n^2)..



Question 2 : The function climb_stairs(n) calculates how many distinct ways there are to climb a staircase of n steps if you can either take 1 step or 2 steps at a time.
Base case when n = 0 and n = 1 then number of way is 1.
then initializethe step1 =1, step2 = 1, current = 0 ; and iterate the for loop in range of 2 to  n+1 and add step1 + step2 and store the value in current then swap the value of step1, step2 and current then print the value of current which is way of climbe.

Time complexity is O(n).
Space complexity is O(1).



Question 3 : Define the function and initialize the parameter with left and right then initialize the left value with 'ans' veriable and iterate the for loop in range (left+1 to right +1) then check 'ans' is 0 then break the loop after the ckeck use bitwise AND opration in loop then return the 'ans'.


Time complexity is O(right - left).
Space complexity is O(1).





Question 4 : This loop iterates over the chars list and counts the occurrences of each character using a dictionary (count).
If the character i is already in the count dictionary, it increments the count by 1.
If the character i is not in the dictionary, it adds it with a count of 1.
This loop goes over the dictionary count and processes each character i and its frequency.
For each character i, it appends the character to the list chars.
If the count of the character is greater than 1 and less than 10 (1 < count[i] < 10), it appends the count as a string directly to chars.
If the count is 10 or greater (count[i] >= 10), it converts the count to a string , and then appends each digit of the count separately to the list.
After rebuilding the chars list with the compressed version, the function returns the new length of the list.


Time complexity is O(n).
Space complexity is O(n).



