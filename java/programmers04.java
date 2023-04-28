class Solution {
    public int solution(String A, String B) {
        int answer = 0;
        if (A.equals(B)){
            return 0;
        }
        else{
            int len = A.length();
            for (int i = 0; i < len; i++){
                B = B.substring(1, len) + B.substring(0, 1);
                if (A.equals(B)){
                    answer = i + 1;
                    return answer;
                }
            }
            return -1;
        }
    }
}