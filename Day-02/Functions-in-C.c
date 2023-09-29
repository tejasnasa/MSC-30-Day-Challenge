int max(a,b){
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}

int max_of_four(int a, int b, int c, int d){
    int e = max(a, b);
    int f = max(c, d);
    int g = max(e, f);
    return g;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
