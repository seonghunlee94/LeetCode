class Solution {
    public boolean hasAllCodes(String s, int k) {
        int need = 1 << k;  // 2^k
        Set<String> seen = new HashSet<>();
        
        for (int i = 0; i <= s.length() - k; i++) {
            String sub = s.substring(i, i + k);
            if (!seen.contains(sub)) {
                seen.add(sub);
                if (seen.size() == need) {
                    return true;  // 모든 조합을 본 경우, 바로 true 반환
                }
            }
        }
        
        return false;
    }
}