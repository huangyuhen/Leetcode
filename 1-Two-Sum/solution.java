public class Solution {
    public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> array = new HashMap<Integer, Integer>();
	        int [] result = new int[2];
	        for (int i = 0; i < nums.length; i++){
	            int temp = target - nums[i];
	            if (array.containsKey(temp)){
	                result[0] = array.get(temp);
	                result[1] = i;
	                return result;
	            } 	
	            else	
	            	array.put(nums[i], i);
	        }
	        return result;
    }
}