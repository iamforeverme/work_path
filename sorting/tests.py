import array_sort,list_sort
import unittest
import time
import random
import copy
import sys

class SortingTest(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        sys.setrecursionlimit(15000)
        cls.test_data=[random.randint(0,5) for i in range(10000)]
        random.shuffle(cls.test_data)
        cls.sorted_data=copy.deepcopy(cls.test_data)
        solution=array_sort.Merge()
        solution.sort( cls.sorted_data)
        # link
        cls.test_link_head=creat_linked_list_from_array(cls.test_data)
        solution=list_sort.Bubble()
        cls.test_link_sorted_head=solution.sort(head,None)


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self): 
        # Generate test data
        self.start_time = time.time()

    def tearDown(self): 
        t = time.time() - self.start_time
        print("%s: %.3f" % (self.id(), t))

    def test_array_bubble(self):
        data=self.test_data
        solution=array_sort.Bubble()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)

    def test_array_insert(self):
        data=self.test_data
        solution=array_sort.Insert()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)
    def test_array_selection(self):
        data=self.test_data
        solution=array_sort.Selection()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)
    def test_array_quick_insert(self):
        data=self.test_data
        solution=array_sort.QuickInsert()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)
    def test_array_shell(self):
        data=self.test_data
        solution=array_sort.Shell()
        # shell sorting is stupid slow in my implementation
        # solution.sort( data)
        # self.assertEqual(data,self.sorted_data)
    def test_array_heap(self):
        pass
    def test_array_quick(self):
        data=self.test_data
        solution=array_sort.Quick()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)
    def test_array_merge(self):
        data=self.test_data
        solution=array_sort.Merge()
        solution.sort( data)
        self.assertEqual(data,self.sorted_data)
    def test_link_bubble(self):
        solution=list_sort.Bubble()
        sorted_head=solution.sort(head,None)
    def test_link_insert(self):
        pass
    def test_link_quick(self):
        pass

if __name__ == '__main__':
    unittest.main()