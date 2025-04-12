class MyHashMap {

    private final int[] map;

    public MyHashMap() {
        map = new int[1_000_001]; // key 범위에 맞게 배열 생성
        Arrays.fill(map, -1);     // 값이 없음을 나타내기 위해 초기값 -1로 채움
    }

    public void put(int key, int value) {
        map[key] = value;
    }

    public int get(int key) {
        return map[key];
    }

    public void remove(int key) {
        map[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */