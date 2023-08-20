class Solution {
    public int minNumberOfHours(
        int initialEnergy, int initialExperience, 
        int[] energy, int[] experience) {

        int answer = 1;
        for (var e: energy) {
            answer += e;
        }
        answer = answer > initialEnergy ? answer - initialEnergy : 0;

        int maxExperience = experience[0];
        energy[0] = 0;
        for(int i = 1; i < energy.length; i++) {
            energy[i] = energy[i-1] + experience[i-1];
            maxExperience = Math.max(maxExperience, experience[i] - energy[i]);
        }

        answer += maxExperience + 1 > initialExperience ? maxExperience + 1 - initialExperience : 0;

        return answer;
    }
}