class Solution {
    public int solution(int n, int[] tops) {
        int answer = 0;
        int mod = 10007;
        
        int[] rdig = new int[n + 1]; // 우측 아래로 뾰족한 마름모의 경우
        int[] rem = new int[n + 1]; // 나머지의 경우

        rdig[1] = 1;
        if (tops[0] == 1) rem[1] = 3;
        else rem[1] = 2;

        for (int i = 2; i <= n; i++) {
            rdig[i] = (rdig[i-1] + rem[i-1]) % mod;
            
            if (tops[i-1] == 1) rem[i] = (rdig[i-1] * 2 + rem[i-1] * 3) % mod;
            else rem[i] = (rdig[i-1] + rem[i-1] * 2) % mod;

        }
        answer =  (rdig[n] + rem[n]) % mod;
        
        return answer;
    }
}