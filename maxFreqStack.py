from collections import defaultdict

class FreqStack:
    """
    Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

    Implement the FreqStack class:

    FreqStack() constructs an empty frequency stack.
    void push(int val) pushes an integer val onto the top of the stack.
    int pop() removes and returns the most frequent element in the stack.
    If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
    

    Example:

    Input
    ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    Output
    [null, null, null, null, null, null, null, 5, 7, 5, 4]

    Explanation
    FreqStack freqStack = new FreqStack();
    freqStack.push(5); // The stack is [5]
    freqStack.push(7); // The stack is [5,7]
    freqStack.push(5); // The stack is [5,7,5]
    freqStack.push(7); // The stack is [5,7,5,7]
    freqStack.push(4); // The stack is [5,7,5,7,4]
    freqStack.push(5); // The stack is [5,7,5,7,4,5]
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

    """


    def __init__(self):
        # need to save freq of each element
        # we would also keep track of the max frequency
        # key is freq, val is a list of values with that freq to save the LIFO order in case of a tie
        self.freq_to_val = defaultdict(list)
        self.val_to_freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.val_to_freq:
            freq = self.val_to_freq[val]
            freq += 1
        else:
            freq = 1
            
        self.val_to_freq[val] = freq
        self.freq_to_val[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        
        if self.max_freq in self.freq_to_val and len(self.freq_to_val[self.max_freq]) > 0:
            val = self.freq_to_val[self.max_freq].pop()
            self.val_to_freq[val] -= 1 
            
            if len(self.freq_to_val[self.max_freq]) == 0:
                self.max_freq -= 1
            
            return val
            

#Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

my_stack = FreqStack()
tasks = ["push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
vals = [5, 7, 5, 7, 4, 5, 0, 0, 0, 0]
results = []
for task, val in zip(tasks, vals):
    if task == "push":
        results.append(my_stack.push(val))
    if task == "pop":
        results.append(my_stack.pop())

print(results)