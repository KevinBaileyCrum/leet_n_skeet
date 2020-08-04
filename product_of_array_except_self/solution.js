// Given an array nums of n integers where n > 1,
// return an array output such that output[i]
// is equal to the product of all the elements of
// nums except nums[i].

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
   let returnArray = []
   for (i=0; i<nums.length; i++) {
      let accum = 1  // accumulator for product
      for (j=0; j<nums.length; j++) {
         if (j === i) continue
         accum *= nums[j]
      }
      returnArray[i] = accum
   }
   return returnArray
}

console.log(productExceptSelf([1,2,3,4]))

