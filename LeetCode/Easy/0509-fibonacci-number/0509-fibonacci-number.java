class Solution {
    public int fib(int n) {
        int n_1 = 1;
        int n_2 = 0;
        int n_3 = 0;
        int num = 2;

        if (n < 2) {
            return n;
        }

        while (num <= n) {
            n_3 = n_1;
            n_1 += n_2;
            n_2 = n_3;
            num ++;
        }
        return n_1;
    }
}