int minSubArrayLen(int target, int* nums, int numsSize) {
    int window_sum=0,left=0;
    int min_len=INT_MAX;
    for(int right=0;right<numsSize;right++){
        window_sum+=nums[right];
        while(window_sum>=target){
            min_len=min_len>right-left+1?right-left+1:min_len;
            window_sum-=nums[left];
            left++;
        }
    }
    return min_len==INT_MAX?0:min_len;

}