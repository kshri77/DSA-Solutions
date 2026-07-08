class Solution {
    public boolean isValid(String s) {
        if(s.length()<=1){
            return false;
        }
        Stack<Character> st=new Stack();
        char[] sr = s.toCharArray();
        for (int i=0;i<s.length();i++){
            if(sr[i]=='[' || sr[i]=='{' || sr[i]=='('){
                st.push(sr[i]);
            }
            else{
                 if (st.isEmpty())
                    return false;

                char top = st.pop();

                if ((sr[i] == ')' && top != '(') ||
                    (sr[i] == ']' && top != '[') ||
                    (sr[i] == '}' && top != '{')) {
                    return false;
            }

        }

   
        }
     return st.isEmpty();
    }
}