# Searching Algorithms

## Linear search
Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. It is the simplest searching algorithm.
* Algorithm
  * Input: nums array, target
  * For each item at position i:
    * If nums[i] == target:
      * return i
  * Output: target index
  ```
  def linear_search(nums):
    '''
    T: O(n) and S: O(1)
    '''
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
  ```
* Complexity analysis
  * Time complexity: min number of search is 1 and max number of search is n. Therefore, average number of search is n/2.
    * T(n) = O(n/2) = O(n)
  * Space complexity: No additional space required, O(1)


## Binary search
Binary search is an efficient algorithm for finding an item from an ordered list of items. It works by repeatedly dividing in half the portion of the list, until narrowing down the possible locations to just one. The time complexity reduces from O(n) to O(logn).
* Algorithm
  * Input: nums array, target
  * Initialize left and right pointers
  * While left <= right:
    * Compute mid pointer
    * If mid item == target:
      * return mid
    * Else if target > mid item:
      * left = mid + 1
    * Else
      * right = mid - 1
  * Output: target index
  ```
  def binary_search(nums):
    '''
    T: O(log n) and S: O(1)
    '''
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
           return mid
        else if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
  ```
* Complexity analysis
  * Time complexity: At each iteration, the search array length becomes half. So, for at most `x` required searches, we say
    * 2^x = n or, x = log2 n, therefore
    * T(n) = O(log2 n) = O(log n)
  * Space complexity: No additional space required, O(1)

# Sorting Algorithms

## Insertion sort
It repeatedly take an element from the input data and inserts it into the position so that its value is between the previous and the next element.
* Algorithm
  * Input: nums array
  * For each item at position i:
    * While item at i-1 > item at i:
      * Swap items between i-1 and i
  * Output: nums array
  ```
  def insertionSort(nums):
    '''
    T: O(n^2) and S: O(1)
    '''
    i = 1
    while i < len(nums):
        j = i - 1
        while j >= 0:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
        i += 1
    return nums
  ```
* Complexity analysis
  * Time complexity: n-1 steps in the loop; maximum of n-1 compare and swap in each step. Therefore,
    * T(n) = T(n-1) * T(n-1) = O(n^2)
  * Space complexity: in-place. O(1)


## Bubble sort
It compares adjacent elements and swaps them if they are in the wrong order.
* Algorithm
  * Input: nums array
  * For each item:
    * Swap item with its next right until item > next right item
  * Output: nums array
  ```
  def bubbleSort(nums):
    '''
    T: O(n^2) and S: O(1)
    '''
    lastPosition = len(nums) - 1
    while True:
        countSwap = 0
        i = 1
        while i <= lastPosition:
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                countSwap += 1
            i += 1
        lastPosition -= 1
        if countSwap == 0: break
            
    return nums
  ```
* Complexity analysis
  * Time: O(n ^ 2) and space: O(1)


## Selection sort
It repeatedly finds the minimum element from unsorted part and puts it at the beginning.
* Algorithm
  ```
  def selectionSort(nums):
    '''
    Keep track of current position starting from the left and
    swap its element with the min from its right.
    T: O(n^2)
    S: O(1)
    '''
    curPosition = 0
    while curPosition < len(nums):
        unsortedPart = nums[curPosition:]
        minIndex = unsortedPart.index(min(unsortedPart)) + curPosition
        nums[curPosition], nums[minIndex] = nums[minIndex], nums[curPosition]
        curPosition += 1
        
    return nums
  ```
* Complexity analysis


## Merge Sort
It divides the array in half, sorts each of those halves, and then merges them together.
* Algorithm
  * Input: nums array
  * func mergeSort(nums):
    * left, right = divide(nums)
    * left = mergeSort(left)
    * right = mergeSort(right)
    * mergedSorted = merge(left, right)
  * Output: mergedSorted
  ```
  def mergeSort(nums):
    '''
    T: O(n log n) and S: O(n)
    '''
    if len(nums) <= 1: return nums
    
    def divide(nums):
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        return left, right
    
    def merge(left, right):
        nLeft, nRight = len(left), len(right)
        merged = []
        i, j = 0, 0
        while i < nLeft or j < nRight:
            vLeft = left[i] if i < nLeft else float('inf')
            vRight = right[j] if j < nRight else float('inf')
            if vLeft < vRight:
                merged.append(vLeft)
                i += 1
            else:
                merged.append(vRight)
                j += 1
        return merged
    
    left, right = divide(nums)
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)
  ```
  
  * Complexity analysis
  * Time complexity: Consider a tree with
    * T(n) = O(1) + 2T(n/2) * O(n), i.e. divide + merge sort + merge = O(n log n)
    * Explanation:
      * At level 0, total number of operations = n
      * At level 1, total number of operations = n/2 + n/2 = n
      * At level 2, total number of operations = n/4 + n/4 + n/4 + n/4 = n
      * ...
      * At final level, total number of operations = 1 + 1 + ... + 1 = n
      * Number of levels = height or depth of the tree = 1 + log n
      * Therefore, O( (1 + log n) * n ) = O(n log n)
  * Space complexity: Auxiliary space required for left and right arrays, so O(n).


## Quick sort
It partitions the array into two subarrays based on the pivot, move the larger ones to the right, and smaller ones to the left.  
* Algorithm
  ```
  def quickSort(nums):
    '''
    T: O(n log n) and S: O(1)
    '''
    def sort(nums, lo, hi):
        def partition(nums, lo, hi):
            i = lo - 1
            pivot = nums[hi]
            for j in range(lo, hi):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[hi] = nums[hi], nums[i+1]
            return i + 1

        if len(nums) <= 1: return nums
        if lo < hi:
            k = partition(nums, lo, hi)
            sort(nums, lo, k-1)
            sort(nums, k+1, hi)
        return nums
    
    lo = 0
    hi = len(nums) - 1
    return sort(nums, lo, hi)
  ```
* Complexity analysis

## Counting sort
* Algorithm
  * Input from a small range k integer, 0 to k-1
  * Loop through items, incrementing a counter (key = index, value = count)
  * Compute cumulative sum of the counter array
  * Loop through items in reverse order and:
    * Use item key to index the count array
    * Decrement that count array
    * Use decremented value as array index to copy item into sorted array
  ```
  def countingSort(nums):
    if len(nums) <= 1: return nums
    
    # Initialize the counter with all zeros
    minNum, maxNum = min(nums), max(nums)
    counter = {}
    for num in range(minNum, maxNum+1):
        counter[num] = 0
        
    # Count the numbers in nums
    for num in nums:
        counter[num] += 1
    
    # Computer cumulative sum of the counter
    # Key = number in nums; Value = index of the numbers in nums
    curCount = 0
    for num in counter:
        counter[num] += curCount
        curCount = counter[num]
    
    # Sort numbers in nums
    sortedNums = [0] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        index = counter[num] - 1
        sortedNums[index] = num
        counter[num] -= 1
    
    for i in range(len(sortedNums)):
        nums[i] = sortedNums[i]
    
    return nums
  ```
* Complexity analysis


## Radix sort
* Algorithm
  ```
  def radixSort(nums):
    '''
    T: O(n*d); n=#items in nums, d=#digt in max num
    S: O(n)
    '''
    def countingSort(nums, digitIndex):
        '''digitIndex: LSB-->0 and MSB-->n-1
        T: O(n) and S: O(n)'''
        n = len(nums)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (nums[i] // 10**digitIndex) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i-1]

        for i in range(n-1, -1, -1):
            index = (nums[i] // 10**digitIndex) % 10
            output[count[index] - 1] = nums[i]
            count[index] -= 1
        
        for i in range(n):
            nums[i] = output[i]
            
    # Apply counting sort for each digit from LSB to MSB
    if len(nums) <= 1: return nums
    maxDigitLen = len(str(max(nums)))
    for digitIndex in range(maxDigitLen):
        countingSort(nums, digitIndex)
    
    return nums
  ```
* Complexity analysis

## Bucket sort
* Algorithm
  ```
  def bucketSort(nums):
    '''
    T: O(n*d); n=#items in nums, d=#digt in max num
    S: O(n*d)
    '''
    if len(nums) <= 1: return nums
    # Get number of digits in max num and convert each number equal to that number of digits
    maxNum = max(nums)
    maxDigit = len(str(maxNum))
    nums = ['0'*(maxDigit-len(str(num)))+str(num) for num in nums]
    
    # Put the numbers into buckets according to its digit (least to most significant)
    for digit in range(maxDigit-1, -1, -1):
        # Init buckets and fill it
        buckets = {str(i): [] for i in range(10)}
        for num in nums:
            buckets[num[digit]].append(num)
        # Sorted nums based on curret digit
        nums = []
        for bucket in buckets:
            nums.extend(buckets[bucket])
    # Convert each number into int again
    nums = [int(num) for num in nums]
    
    return nums
  ```
* Complexity analysis


## Heap sort
* Algorithm
  ```
  import heapq
  def heapSort(nums):
    '''
    T: O(n log n) and S: O(n)
    '''
    copyNums = nums.copy()
    sortedNums = []
    
    while copyNums:
        heapq.heapify(copyNums)
        sortedNums.append(copyNums.pop(0))
        
    return sortedNums
  ```
* Complexity analysis


## Test sorting algorithms

```
import random
n, x = 50000, 30

nums = random.sample(range(n), x)
print('Insertion sort:', insertionSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Bubble sort:', bubbleSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Selection sort:', selectionSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Merge sort:', mergeSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Quick sort: ', quickSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Counting sort:', countingSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Radix sort:', radixSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Bucket sort:', bucketSort(nums)==sorted(nums))

nums = random.sample(range(n), x)
print('Heap sort:', heapSort(nums)==sorted(nums))
```
