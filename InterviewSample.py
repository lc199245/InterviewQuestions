import math;
# 1. Merge 2 arrays of integers into one
test_array_1 = [5,4,3,2,1];
test_array_2 = [4,5,6,7,8];

def merge_two_array(test_arr_1, test_arr_2):
    merge_result_list = test_arr_1 + test_arr_2;
    print 'Pure mege:';
    print merge_result_list;
    no_dup_list = list(set(merge_result_list));
    print 'Merge and remove duplicates:';
    print no_dup_list;
    reverse_order_list = sorted(no_dup_list, key=lambda x: (-x));
    print 'Reverse merge list:';
    print reverse_order_list;

merge_two_array(test_array_1, test_array_2);
    

#2. Write an algorithm to sort a string of numbers
test_string = "341341234127389461651341";
def sort_string_of_numbers(test_str):
    test_str_list = list(test_str);
    test_str_list = sorted(test_str_list, key=lambda x: (x));
    result_str = ''.join(test_str_list);
    return result_str;

print sort_string_of_numbers(test_string);


#3. Write an algo to reverse a string of numbers
test_string = "341341234127389461651341";
def reverse_string_of_numbers(test_str):
    test_str_list = list(test_str);
    result_str_list = [];
    for i in range(len(test_str_list)-1, -1, -1):
        result_str_list.append(test_str_list[i]);
    result_str = ''.join(result_str_list);
    return result_str;

print reverse_string_of_numbers(test_string);



#4.  Create a function that can pick out Fibonacci numbers and reject non-Fibonacci numbers.
test_number_list = range(0, 100);
def is_squared(number):
    temp_root = math.sqrt(number);
    temp_root = int(temp_root);
    return (temp_root * temp_root == number);

def check_all_fibo(test_number_list):
    result_fibo_list = [];
    for item in test_number_list:
        if item==0 or item == 1 or item == 2:
            result_fibo_list.append(item);
            continue;
        if is_squared(5 * item * item - 4) or is_squared(5 * item * item + 4):
            result_fibo_list.append(item);
    return result_fibo_list;

print check_all_fibo(test_number_list);


#5. Given a string, for example ABC, find the rank of the string among all its alphabetical permutations.
test_alph_string = 'DCBA';
def rank_of_string(test_alph_string):
    test_alph_list = list(test_alph_string);
    rank = 0;
    for i in range(0, len(test_alph_list)-1):
        x = 0;
        for j in range(i+1,len(test_alph_list)):
            if test_alph_list[j] < test_alph_list[i]:
                x= x + 1;
        rank = rank +x * math.factorial((len(test_alph_list) - i - 1));
    return rank;
print rank_of_string(test_alph_string);


#6. Define a binary tree using Python
class Node():
    def __init__(self, data=None, left_child = None, right_child=None):
        self.data = data;
        self.left_child = left_child;
        self.right_child = right_child;


 
class BinaryTree():
    def __init__(self):
        self.root = Node();

    def insert(self, data):
        node = Node(data);
        if self.root.data == None:
            self.root = node;
        else:
            current_layer = [];
            root_node = self.root;
            current_layer.append(root_node);
            while current_layer:
                root_node = current_layer.pop(0);
                if root_node.left_child == None:
                    root_node.left_child = node;
                    return;
                elif root_node.right_child == None:
                    root_node.right_child = node;
                    return;
                else:
                    current_layer.append(root_node.left_child);
                    current_layer.append(root_node.right_child);
    # ǰ������ ������
    def preorder_traversal_recur(self, root):
        if root == None:
            return;
        print root.data;
        self.preorder_traversal_recur(root.left_child);
        self.preorder_traversal_recur(root.right_child); 
    # �������� ������    
    def inorder_traversal_recur(self, root):
        if root == None:
            return;
        self.inorder_traversal_recur(root.left_child);
        print root.data;
        self.inorder_traversal_recur(root.right_child);
    # �������� ������
    def postorder_traversal_recur(self, root):
        if root==None:
            return;
        self.postorder_traversal_recur(root.left_child);
        self.postorder_traversal_recur(root.right_child);     
        print root.data;

    def preorder_traversal_stack(self, root):
        if root==None:
            return;
        current_stack = [];
        node = root;
        while node or current_stack:
            while node:
                print node.data;
                current_stack.append(node);
                node = node.left_child;
            node = current_stack.pop();
            node = node.right_child;

    def inorder_traversal_stack(self, root):
        if root==None:
            return;
        current_stack = [];
        node = root;
        while node or current_stack:
            while node:
                current_stack.append(node);
                node = node.left_child;
            node = current_stack.pop();
            print node.data;
            node = node.right_child;

    def postorder_traversal_stack(self, root):
        if root == None:
            return;
        current_stack_1 = [];
        current_stack_2 = [];
        node = root;
        current_stack_1.append(node);
        while current_stack_1:
            node = current_stack_1.pop();
            if node.left_child:
                current_stack_1.append(node.left_child);
            if node.right_child:
                current_stack_1.append(node.right_child);
            current_stack_2.append(node);
        while current_stack_2:
            print current_stack_2.pop().data;

    def layer_traversal(self, root):
        if root == None:
            return;
        current_layer = [];
        node = root;
        current_layer.append(node);
        while current_layer:
            node = current_layer.pop();
            print node.data;
            if node.left_child != None:
                current_layer.append(node.left_child);
            if node.right_child != None:
                current_layer.append(node.right_child);
            
                


if __name__ == '__main__':
    data_points = range(10);
    sample_bin_tree = BinaryTree();
    for item in data_points:
        sample_bin_tree.insert(item);
    
    print '---------------------------------------';
    sample_bin_tree.inorder_traversal_recur(sample_bin_tree.root);
    print '---------------------------------------';
    sample_bin_tree.inorder_traversal_stack(sample_bin_tree.root);
    print '---------------------------------------';
    sample_bin_tree.preorder_traversal_recur(sample_bin_tree.root);
    print '---------------------------------------';
    sample_bin_tree.preorder_traversal_stack(sample_bin_tree.root);
    print '---------------------------------------';
    sample_bin_tree.postorder_traversal_recur(sample_bin_tree.root);
    print '---------------------------------------';
    sample_bin_tree.postorder_traversal_stack(sample_bin_tree.root);
    print '---------------------------------------';    
    sample_bin_tree.layer_traversal(sample_bin_tree.root);        
            
            

    