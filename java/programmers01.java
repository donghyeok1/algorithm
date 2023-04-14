class Solution {
    public int solution(int[] common) {
        int answer = 0;
        int length = common.length;
        if (common[0] == 0 | common[1] == 0){
            answer = common[length - 1] + common[1] - common[0];
        }
        else {
            int sub_first = common[1] - common[0];
            int div_first = common[1] / common[0];
            int sub_second = common[2] - common[1];
            int div_second = common[2] / common[1];
            
            if (sub_second == sub_first){
                answer = common[length - 1] + sub_first;
            }
            else{
                answer = common[length - 1] * div_first;
            }
        }
        return answer;
    }
}
