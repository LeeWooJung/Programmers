class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int attack_index = 0;
        int fullCureTime = bandage[0];
        int curePerTime = bandage[1];
        int afterFullTimeCure = bandage[2];
        
        int currentHealth = health;
        
        int time = 0;
        int cureTime = 0;
        
        while(time < 1001 && currentHealth > 0) {
            
            int attackTime = attacks[attack_index][0];
            int damage = attacks[attack_index][1];
            
            if(time == attackTime) {
                currentHealth -= damage;
                cureTime = 0;
                attack_index++;
                time++;
                
                if(attack_index >= attacks.length) break;
                continue;
            }
            
            currentHealth = Math.min(health, currentHealth + curePerTime);
            cureTime++;
            if(cureTime >= fullCureTime) {
                currentHealth = Math.min(health, currentHealth + afterFullTimeCure);
                cureTime = 0;
            }
            
            time++;
        }
        
        if(currentHealth <= 0) {
            answer = -1;
        } else {
            answer = currentHealth;
        }
        
        
        return answer;
    }
}