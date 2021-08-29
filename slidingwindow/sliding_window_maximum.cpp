class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> monotonicDeque;
        for (int i = 0; i < k; i++) {//create the deque for the initial k-window
            while (monotonicDeque.size() > 0 && nums[i] >= nums[monotonicDeque.back()]) {
                monotonicDeque.pop_back();//remove any elements which are smaller than the new element
            }
            monotonicDeque.push_back(i);
        }
        vector<int> max;
        max.push_back(nums[monotonicDeque.front()]);//push the first max
        for (int i = k; i < nums.size(); i++) {//iterate over the remaining windows
            if (i - monotonicDeque.front() >= k) monotonicDeque.pop_front();//if largest element (at front of deque) is out of window, remove it
            while (monotonicDeque.size() > 0 && nums[i] >= nums[monotonicDeque.back()]) {
                monotonicDeque.pop_back();//remove any elements which are smaller than the new element
            }
            monotonicDeque.push_back(i);
            max.push_back(nums[monotonicDeque.front()]);//push the window max
        }
        return max;
    }
};
