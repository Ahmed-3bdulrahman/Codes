#include <iostream>
#include <time.h>
using namespace std;

int main()
{
    srand(time(0));
    string pass;
    string data = "abcdefghijklmnopqrstuvwxyz"
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  "1234567890"
                  "¬!$%^&*()_+=-#~/?><.,[]{}";

    for (int i = 1; i <= 16; i++)
    {
        pass = pass + data[rand() % 93];
    }
    cout << "Your Password: " <<pass;
    return 0;
}