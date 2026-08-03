class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool repeat = false;
        int length = nums.size();
        for(int i = 0; i < length; i++){
            for(int j=i+1; j < length; j++){
                if(nums[i]==nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
};