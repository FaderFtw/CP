input/code.cpp: In function 'void solve(long long int, long long int)':
input/code.cpp:18:77: warning: suggest parentheses around '&&' within '||' [-Wparentheses]
   18 |     bool verif = v[r][c] || (c > 0 && c < 6 && !v[r][c + 1] && !v[r][c - 1] && ((r == 0 && v[r + 1][c]) || (r == 6 && v[r - 1][c])) ||
      |                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input/code.cpp:20:109: warning: suggest parentheses around '&&' within '||' [-Wparentheses]
   20 |                              r > 0 && r < 6 && c > 0 && c < 6 && v[r - 1][c] && v[r + 1][c] && !v[r][c - 1] && !v[r][c + 1] ||
      |                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
input/code.cpp:21:109: warning: suggest parentheses around '&&' within '||' [-Wparentheses]
   21 |                              r > 0 && r < 6 && c > 0 && c < 6 && v[r][c - 1] && v[r][c + 1] &&...