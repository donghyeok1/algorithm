class Solution {
    public String[] solution(String my_str, int n) {
        int len = my_str.length() / n;
        int array_len = 0;
        if (my_str.length() % n == 0){
            array_len = my_str.length() / n;
        }
        else{
            array_len = my_str.length() / n + 1;
        }
        String[] answer = new String[array_len];
        int start = 0;
        int end = n;
        for (int i = 0; i < len; i++){
            answer[i] = my_str.substring(start, end);
            start += n;
            end += n;
        }
        if (my_str.length() % n != 0){
            answer[len] = my_str.substring(start);
        }
        return answer;
    }
}