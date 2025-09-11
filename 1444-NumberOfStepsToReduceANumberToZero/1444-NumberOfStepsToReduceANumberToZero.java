// Last updated: 9/11/2025, 12:31:08 PM
class Solution {
    public int numberOfSteps(int num) {
        int n = 0;
        while(num>0){
            if(num%2==0){
            //even
            num/=2;
            n++;
            }

             else{
            //odd
            num--;
            n++;
            }
        }
        return n;
    }

}