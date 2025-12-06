class Solution {

    private int convert(char x){
        switch(x){
           case 'I':
                    return 1;
                case 'V':
                    return 5;
                case 'X':
                    return 10;
                case 'L':
                    return 50;
                case 'C':
                    return 100;
                case 'D':
                    return 500;
                case 'M':
                    return 1000;
                default:
                    return 0;   
        }    
    }
    public int romanToInt(String s) {
        int total =0;
           int prev = convert(s.charAt(0));
           for(int i =1; i<s.length();i++){
               int next = convert(s.charAt(i));
               if(prev<next){
                   total -= prev;
               }else{
                   total+=prev;
               }
               prev = next;
           }
           total += prev;
           return total;
    }
}