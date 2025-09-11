// Last updated: 9/11/2025, 12:31:01 PM
class Solution {
    public int maximumWealth(int[][] accounts) {
        int highest = 0;
        int test=0;
        for(int i=0; i<accounts.length; i++){
            for(int j=0; j<accounts[i].length; j++){
                test+=accounts[i][j];
            }
                if(test>highest){
                    highest=test;
                }
            test=0;
        }
        return highest;
    }
}