PI= 3.141592653589793238
def sin(x, term_count):
    if x<0:
        return -sin(-x,term_count)
    while x>= 2*PI:
        x-= 2*PI
    current_term=x
    estimated = current_term
    for n range(1, term_count):
        current_term *= -x*x / (2*n*(2*n+1))
        estimated += current_term
    return estimated
result = sin(PI, 15)
print(result)

def cos(x, term_count):
    if x<0:
        return cos(-x,term_count)
    while x>= 2*PI:
        x-= 2*PI
    current_term= 1
    estimated = current_term
    for n range(1, term_count):
        current_term *= -x*x / (2*n*(2*n-1))
        estimated += current_term
    return estimated
result = cos(PI, 15)
print(result)

def tan(x, term_count):
    return sin(x, term_count) / cos(x, term_count)

result = tan(PI/2, 15)
print(result)



#include <stdio.h>
#include <math.h>

#define TERMS 10


double factorial(int n) {
    if (n <= 1) return 1;
    else return n * factorial(n - 1);
}


double sin_taylor(double x) {
    double result = 0.0;
    int i;
    for (i = 0; i < TERMS; ++i) {
        int sign = (i % 2 == 0) ? 1 : -1; // 번갈아가며 부호 변경
        result += sign * pow(x, 2 * i + 1) / factorial(2 * i + 1);
    }
    return result;
}


double cos_taylor(double x) {
    double result = 0.0;
    int i;
    for (i = 0; i < TERMS; ++i) {
        int sign = (i % 2 == 0) ? 1 : -1; // 번갈아가며 부호 변경
        result += sign * pow(x, 2 * i) / factorial(2 * i);
    }
    return result;
}


double tan_taylor(double x) {
    return sin_taylor(x) / cos_taylor(x);
}

int main() {
    double angle_deg = 30.0; // 각도 (도 단위)
    double angle_rad = angle_deg * M_PI / 180.0; // 라디안으로 변환

    printf("sin(%.2f degrees) = %.4f (Taylor series approximation)\n", angle_deg, sin_taylor(angle_rad));
    printf("cos(%.2f degrees) = %.4f (Taylor series approximation)\n", angle_deg, cos_taylor(angle_rad));
    printf("tan(%.2f degrees) = %.4f (Taylor series approximation)\n", angle_deg, tan_taylor(angle_rad));

    return 0;
}
