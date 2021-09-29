
//Bitmasking techniques
//Counting number of bits
// Time which   is O(No of bits)
#include <bits/stdc++.h>
using namespace std;
int countBits(int n){
    int counts = 0;
    while(n > 0){
        counts += (n & 1);
        n = n >> 1;

    }
    return counts;
}
int countBitsFast(int n){
    int count = 0;
    while(n){
        count ++;
        n = n & (n  - 1);
    }
    return count;
}
int getIthBit(int n, int i){
    return n & (1 <<i) != 0?1:0;
}
//Change ith bit of no to 1
void setIthBit(int& n, int i){
    int mask = 1 << i;
    n = n | mask;
}
//Clear Ith bit
void clearBit(int& n, int i){
    int mask = ~(1 << i);
    n = n & mask;
}
//Generate all subsets using bitmask
void filterBits(char *a, int no){
        int i = 0;
        while(no > 0){
            (no&1)?cout << a[i] : cout << "";
            i ++;
            no = no >> 1;
        }
        cout << '\n';
}
void generateSubsets(char *a){
    //Generate a range of numbers  from 0 to 2 ^ n - 1
    int n = strlen(a);
    int range = (1 << n) - 1;
    for(int i = 1;i <= range;i ++){
        filterBits(a,i);
    }
}
void t_main(){
     int n, i;
  /*   cin >> n >> i;
     cout << countBits(n) << ' ' << countBitsFast(n) << ' ' << getIthBit(n, i);
     setIthBit(n, i);
     cout << '\n' << n;
     clearBit(n,i);
     cout << '\n' << n;
*/
     char a[100];
     cin >> a;
     generateSubsets(a);
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    //cin >> t;
    while(t--)t_main();
    return 0;
}


















/*
STL -> Functors
we are given some set of x and y coordinates, so we must find number of k nearest segment to (0,0) point;
*/

/*#include <bits/stdc++.h>
using namespace std;
class Car{
public:
    int x;
    int y;
    int id;
    Car(int id, int x, int y){
    this->id = id;
    this-> x = x;
    this->y = y;
    }
    void print(){
        cout << "ID: " << id << '\n';
        cout << "Location: " << x << ',' << y << '\n';
    }
    int dist(){
        return x * x + y * y;
    }

};
class CarCompare{
public:
    bool operator()(Car a, Car b) {
        return a.dist() > b.dist();
    }
};
void t_main(){
    /* stack<string>s;
     s.push("Apple");
     s.push("Mango");
     s.push("Guava");
     while(!s.empty()){
        cout << s.top();
        s.pop();
     }*/
     /*queue<int>q;
     for(int i = 0;i < 5;i ++){
        q.push(i);
     }
     while(!q.empty()){
        cout << q.front() << ' ';
        q.pop();
     }*/
     /*priority_queue<int>pq;
     int a[9] = {5,8,2,1,9,7,2,5,4};
     for(int i = 0;i < 9;i ++){
        pq.push(-a[i]);
     }
     while(!pq.empty()){
        cout << -pq.top() << ' ';
        pq.pop();
     }*/
     /*int poppings = 1, k;
     cin >> k;
    priority_queue<Car,vector<Car>, CarCompare>pq;
     int x[10] = {5, 6, 17, 18, 9, 11, 0, 3};
     int y[10] = {1, -2, 8, 9, 10, 91,1, 2};
     for(int i = 0;i < 8;i ++){
        Car c(i, x[i], y[i]);
        pq.push(c);
     }
     while(!pq.empty() && poppings <= k){
        Car p = pq.top();
        p.print();
        pq.pop();
        poppings ++;
     }

}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    //cin >> t;
    while(t--)t_main();
    return 0;
}
*/
/*#include <bits/stdc++.h>
using namespace std;
void t_main(){
     unordered_map<string, int> m;
     //Insert
     m["Mango"] = 100;
     m.insert(make_pair("Apple",120));

     //Search
     if(m.count("Apple") == 1){
        cout << "Price of Apples : " << m["Apple"] << '\n';
     }
     m["Guava"] = m["Apple"] + 90;
     if(m.count("Guava") == 0){
        cout << "Guava does not exists" << '\n';
     }
     else {
         cout << "Guava costs : " << m["Guava"] << '\n';
     }

     //

     //Iterators to search
     auto f = m.find("Mango");
     if(f != m.end()){
        cout << "Price of Mango : " << (f->second) << '\n';
     }
     else{
        cout << "Mango does not exist\n";
     }

     /*
     map<key_type, value_type>
     unordered_map<key_type, value_type>

     essential operands :

     1) insert(make_pair(key, value))
     2) count(k)
     3)[k]
     4) erase(k)
     */

/*}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    //cin >> t;
    while(t--)t_main();
    return 0;
}
*/
