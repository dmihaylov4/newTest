def closest_to_zero(nums):
    """
    Returns the number in the list `nums` that is closest to 0.
    
    If there are multiple numbers with the same distance from 0, 
    the function returns the largest of those numbers. If the list 
    is empty, the function returns None.
    
    Parameters:
    - nums: List of integers.
    
    Returns:
    - int or None: The number closest to 0 or None if the list is empty.
    """

    if not nums:
        return None
    smallest = float('inf')
    result = None
    for x in nums:
        if abs(x) < abs(smallest) or (abs(x) == abs(smallest) and x > smallest):
            smallest = x
            result = x
           
            

    return result
        

