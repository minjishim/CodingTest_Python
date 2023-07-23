#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <cmath>
#include <vector>

#define MAX 1002
#define PI 3.141592

using namespace std;

typedef long long ll;

struct INFO {
    int x, y;
    int p, q;
    INFO(int x1 = 0, int y1 = 0) : x(x1), y(y1), p(1), q(0) {}
};

double distance(const INFO& A, const INFO& B) {
    double dist = sqrt(pow(A.x - B.x, 2) + pow(A.y - B.y, 2));

    return dist;
}
bool comp(const INFO& A, const INFO& B) {
    if (1LL * A.q * B.p != 1LL * A.p * B.q)
        return 1LL * A.q * B.p < 1LL * A.p * B.q;

    if (A.y != B.y)
        return A.y < B.y;

    return A.x < B.x;
}

ll ccw(const INFO& A, const INFO& B, const INFO& C) {
    return 1LL * (A.x * B.y + B.x * C.y + C.x * A.y - B.x * A.y - C.x * B.y - A.x * C.y);
}

INFO p[MAX];


int main() {
    //freopen_s(new FILE*, "input.txt", "r", stdin);
    int n, l;
    cin >> n >> l;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        p[i] = INFO(x, y);
    }

    // y좌표, x좌표가 작은 순으로 정렬
    sort(p, p + n, comp);

    // 기준점으로부터 상대 위치 계산
    for (int i = 1; i < n; i++) {
        p[i].p = p[i].x - p[0].x;
        p[i].q = p[i].y - p[0].y;
    }

    // 반시계 방향으로 정렬(기준점 제외)
    sort(p + 1, p + n, comp);

    stack<int> s;

    // 스택에 first, second를 넣어준다.
    s.push(0);
    s.push(1);

    int next = 2;

    while (next < n) {
        while (s.size() >= 2) {
            int first, second;
            second = s.top();
            s.pop();
            first = s.top();

            // first, second, next가 좌회전 ( > 0 )이라면 second push
            // 우회전( < 0 )이라면 위의 while문 계속 반복
            if (ccw(p[first], p[second], p[next]) > 0) {
                s.push(second);
                break;
            }
        }

        // next push
        s.push(next++);
    }

    vector<int> s1;
    int size = s.size();
    for (int i = 0; i < size; i++) {
        s1.push_back(s.top());
        s.pop();
    }

    double sum = 0;
    int ret = 0;
    for (int i = 0; i < size-1; i++) {
        sum += distance(p[s1[i]], p[s1[i+1]]);
    }
    sum += distance(p[s1[s1.size()-1]], p[s1[0]]);
    sum += 2 * PI * l;
    
    ret = round(sum);

    cout << ret;
    return 0;
}