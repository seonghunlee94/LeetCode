class Solution {
    public int peakIndexInMountainArray(int[] arr) {

        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] < arr[mid + 1]) {
                // Peak은 오른쪽에 있음
                left = mid + 1;
            } else {
                // Peak은 왼쪽 or mid
                right = mid;
            }
        }

        return left;

    }
}