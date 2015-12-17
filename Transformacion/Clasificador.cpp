#include <bits/stdc++.h>
#define MAXN 100

using namespace std;

int dp[MAXN][MAXN];
int dir[MAXN][MAXN];
int l1, l2;

int msc(string a, string b) {
    //mset(M, -1, sizeof M);
    //memset(dir, 0, sizeof dir);

    l1 = a.size();
    l2 = b.size();

    for (int i = 0; i < l1; i++) {
        a[i] = tolower(a[i]);
        dp[i][l2] = 0;
    }

    for (int j = 0; j < l2; j++) {
        b[j] = tolower(b[j]);
        dp[l1][j] = 0;
    }

    for (int i = l1-1; i >= 0; i--) {
        for (int j = l2-1; j >= 0; j--) {
            if (dp[i+1][j] > dp[i][j+1]) {
                dp[i][j] = dp[i+1][j];
                dir[i][j] = -1;
            } else {
                dp[i][j] = dp[i][j+1];
                dir[i][j] = 1;
            }

            int cost = (a[i] == b[j]);
            if (cost + dp[i+1][j+1] >= dp[i][j]) {
                dp[i][j] = cost + dp[i+1][j+1];
                dir[i][j] = 0;
            }
        }
    }

    return dp[0][0];
}

int cnt_partes() {
    int ans = 0;
    int lim = dp[0][0];
    int i = 0, j = 0, ia = -1;
    while (lim > 0 && i < l1 && j < l2) {
        int d = dir[i][j];
        i += (d <= 0);
        j += (d >= 0);

        if (d == 0) {
            lim--;
            if (i - ia > 1) ans++;
            ia = i;
        }
    }

    return ans;
}


vector <string> make_split(string s, char c) {
    vector <string> ans;
    string ns = "";
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == c) {
            ans.push_back(ns);
            ns = "";
        } else {
            ns += s[i];
        }
    }
    return ans;
}

int main(int n, char *args[]) {
    if (n != 4) {
        cout << "Parametros incorrectos." << endl;
        
        return 0;
    }

    ifstream f1(args[1]), f2(args[2]);
    if (!f1.is_open() || !f2.is_open()) {
        cout << "Uno de los archivos no se puede abrir." << endl;
        
        if (f1.is_open()) {
            f1.close();
        }

        if (f2.is_open()) {
            f2.close();
        }

        return 0;
    }
    
    vector <pair<string, string> > tipos;
    string linea;
    while (getline (f2, linea)) {
        int pcoma = linea.find(';');
        tipos.push_back(make_pair(linea, linea.substr(pcoma + 1)));
    }

    f2.close();

    ofstream f3(args[3]);

    while (getline(f1, linea)) {
        vector <string> pls = make_split(linea, ',');

        double mx = -1.0;
        string op;
        for (int x= 0; x < tipos.size(); x++) {
            double nmx = msc(pls[2], tipos[x].second) / (tipos[x].second.size() + 0.0);
            nmx += 1.0 - cnt_partes()/(tipos[x].second.size() + 0.0);
            if (nmx >= mx) {
                mx = nmx;
                op = tipos[x].first;
            }
        }
        
        f3 << linea << "|" << op << endl;
    }

    f1.close();
    f3.close();

    return 0;
}
