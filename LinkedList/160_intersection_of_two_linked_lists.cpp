#include <iostream>
using namespace std;

class Solution {
  public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pa = headA, *pb = headB;
        while (pa != pb) {
            pa = pa ? pa -> next : headB;
            pb = pb ? pb -> next : headA;
        }
        return pa;
    }
};

// int main(){
//   return 0;
// }