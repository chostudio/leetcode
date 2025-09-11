// Last updated: 9/11/2025, 12:31:05 PM
class Solution {
    public int[] runningSum(int[] nums) {
        for(int i =1; i<nums.length;i++){
                nums[i]+=nums[i-1]; 
        }
        return nums;
    }
}