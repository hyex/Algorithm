#include <iostream>

using namespace std;

int main() {
    char word[100];
    cin >> word;
    int alphabet[26];
    fill_n(alphabet, 26, -1);
    
    for(int i=0 ; i<100; i++){
        if (word[i] == '\0') break;
        int temp = word[i] - 'a';
        if (alphabet[temp] == -1) {
            alphabet[temp] = i;
        }
    }
    
    for(int i=0 ; i<26 ; i++){
        cout << alphabet[i] << " " ;
    }
    
}
