// Last updated: 9/11/2025, 12:32:13 PM
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    res = []

    for(let i = 0; i < nums.length; i++){
        j = i
        while(nums[j] + 1 == nums[j + 1]){
            j++;
        }
        if(nums[i] == nums[j]){
            res.push(nums[i] + "")
        }
        else{
            res.push(nums[i] + "->" + nums[j])
        }
        i = j
    }
    return res
};