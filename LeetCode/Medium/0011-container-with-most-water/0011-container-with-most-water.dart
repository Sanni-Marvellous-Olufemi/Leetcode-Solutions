class Solution {
  int maxArea(List<int> height) {
    int curr, start = 0;
    int ans = 0;
    int end = height.length - 1;

    while (start < end) {
        curr = min(height[end], height[start]);
        ans = max(ans, curr * (end-start));
        
        if (height[end] > height[start]) {
            start += 1;
        }
        else {
            end -= 1;
        }
    }
    return ans;
  }
}