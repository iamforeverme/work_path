def creat_linked_list_from_array(array):
    head=None
    tail=None
    for item in array:
        if not head:
            head=ListNode(item)
            tail=head
        else:
            tail.insert(ListNode(item))
            tail=tail.next
    return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def insert(self,node):
        self.next=node

class Solution(object):
    def show_list(self,head,tail=None):
        node=head
        sh_list=[]
        while node!=tail:
            sh_list.append(node.val)
            node=node.next
        print(sh_list)
    def length(self, head,tail=None):
        count=0
        node=head
        while node!=tail:
            node=node.next
            count=count+1
        return count

class Insert(Solution):
    def sort(self,head,tail):
        node=head
        prior_node=None
        while node!=tail:
            # insert node
            insert_node=head
            prior_insert_node=None
            # from start of a list to prior to current node 
            while insert_node != node:
                # insert current node to prior of sorted insert node
                if node.val<insert_node.val:
                    if prior_insert_node ==None:
                        if prior_node == None:
                            # link a node that is the head of a list
                            # no need to close the gap
                            pass
                        else:
                            # close the gap in the current list
                            prior_node.next=node.next
                        ### error start
                        # insert a node to the head of a list
                        node.next=head
                         ### error end
                        head=node
                    else:
                        # close gap in the current list
                        prior_node.next=node.next
                        # insert in the current location
                        ### error start
                        node.next=insert_node
                        ### error end
                        prior_insert_node.next=node
                        node=prior_node
                    # insert completed
                    break
                else:
                    pass

                prior_insert_node=insert_node
                insert_node=insert_node.next

            prior_node=node
            node=node.next
        return head


class Bubble(Solution):
    # switch value only
    def sort(self,head,tail):
        prior_node=None
        while prior_node!=head:
            node = head
            while node.next!=prior_node:
                if node.val > node.next.val:
                    temp=node.val
                    node.val=node.next.val
                    node.next.val=temp
                node=node.next
            prior_node=node
        return head


class Quick(Solution):
    # switch node
    # switch value mode: many items should move according to comparison, and an extra memory should be allocated to save stack
    def sort(self,head,tail):
        if head == tail:
            return head,tail
        head,tail,node=self.partition(head,tail)
        head,node=self.sort(head,node)
        node_next,tail=self.sort(node.next,tail)
        ### error start
        # the following content is very important:
        # Unlike array, linked list need extra efforts to link the gap items when applying the divide-and-conquer method
        node.next=node_next
        ### error end
        return head,tail

    def partition(self,head,tail):
        if head == tail or head.next==tail:
            return head, tail, head
        value=head.val
        node=head
        prior_node=None
        while node!=tail:
            if node.val < value:
                # insert in head
                if prior_node ==None:
                    # break the first node
                    pass
                else:
                    prior_node.next=node.next
                node_next=node.next
                ### error start
                node.next=head
                ### error end
                head=node
                prior_node=node
                node=node_next
            else:
                prior_node=node
                node=node.next
        node=head
        while node.val < value and node!=tail:
            node=node.next
        return head, tail, node

if __name__=="__main__":
    solution=Bubble()
    data=[3,7,6,4,2,1,-1,3]

    # head=ListNode(6)
    # head.next=ListNode(5)
    # head.next.next=ListNode(8)
    # head.next.next.next=ListNode(3)
    # head.next.next.next.next=ListNode(7)
    # head.next.next.next.next.next=ListNode(-1)
    head=creat_linked_list_from_array(data)
    solution.show_list(head,None)
    head=solution.sort(head,None)
    solution.show_list(head,None)